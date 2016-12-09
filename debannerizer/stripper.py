import requests
import re
import datetime
from itertools import islice
from bs4 import BeautifulSoup
from collections import namedtuple

__all__ = ['listing_url', 'listing_post', 'BannerSection', 'banner_reader']

listing_url = "https://banner.mines.edu/prod/owa/bwckschd.p_get_crse_unsec"
listing_post = {
    "begin_ap": "a",
    "begin_hh": "0",
    "begin_mi": "0",
    "end_ap": "a",
    "end_hh": "0",
    "end_mi": "0",
    "sel_attr": "dummy",
    "sel_camp": "dummy",
    "sel_crse": "",
    "sel_day": "dummy",
    "sel_from_cred": "",
    "sel_insm": "dummy",
    "sel_instr": ["dummy", "%"],
    "sel_levl": ["dummy", "%"],
    "sel_ptrm": ["dummy", "%"],
    "sel_schd": ["dummy", "%"],
    "sel_sess": "dummy",
    "sel_subj": ["dummy", "AFGN", "CSM", "CBEN", "CHGN", "CHGC", "CEEN", "LICM", "CSCI",
                 "EPIC", "EBGN", "EENG", "ENGY", "EGGN", "LIFL", "GEGX", "GEGN", "GEOL",
                 "GPGN", "HNRS", "LAIS", "MLGN", "MATH", "MEGN", "MTGN", "MSGN", "MNGN",
                 "LIMU", "NUGN", "PEGN", "PAGN", "PHGN", "SYGN"],
    "sel_title": "",
    "sel_to_cred": "",
    "term_in": "201710"
}

despacify = re.compile(r' +')

BannerSection = namedtuple(
    "BannerSection",
    ["crn", "title", "subject", "number", "letter", "credits", "meetings"]
)

class BannerMeeting:
    columns = ["type", "timerange", "days", "location", "daterange", "schtype", "instructors"]
    def __init__(self, row):
        for attr, td in zip(BannerMeeting.columns, row.find_all('td')):
            setattr(self, attr, td.get_text())

    def __repr__(self):
        return "BannerMeeting({})".format(
                ', '.join("{}={}".format(c, repr(getattr(self, c))) for c in BannerMeeting.columns)
            )

    @property
    def instructors(self):
        return self._instructors

    @instructors.setter
    def instructors(self, value):
        if isinstance(value, str):
            self._instructors = despacify.sub(' ', value).replace(' (P)', '').split(', ')
        else:
            self._instructors = value

    @property
    def location(self):
        return self.building + " " + self.room

    @location.setter
    def location(self, value):
        self.building, _, self.room = value.rpartition(" ")

    @property
    def timerange(self):
        return (self.start_time, self.end_time)

    @timerange.setter
    def timerange(self, value):
        if value == 'TBA':
            self.start_time, self.end_time = None, None
            return
        if isinstance(value, str):
            self.start_time, self.end_time = (
                    datetime.datetime.strptime(t, "%I:%M %p").time()
                    for t in value.split(" - ")
            )
        else:
            self.start_time, self.end_time = value

    @property
    def daterange(self):
        return (self.start_date, self.end_date)

    @daterange.setter
    def daterange(self, value):
        if value == 'TBA':
            self.start_date, self.end_date = None, None
            return
        if isinstance(value, str):
            self.start_date, self.end_date = (
                    datetime.datetime.strptime(d, "%b %d, %Y").date()
                    for d in value.split(" - ")
            )
        else:
            self.start_date, self.end_date = value

def banner_reader(term):
    listing_post["term_in"] = term
    r = requests.post(listing_url, params=listing_post)
    if not r.ok:
        raise RuntimeError("Unable to download page from banner")
    soup = BeautifulSoup(r.text, "lxml")
    titles = soup(class_='ddtitle')
    rows = islice(soup.find(class_='pagebodydiv').table('tr', recursive=False), 1, None, 2)
    flat_title_p = re.compile(r'^(.+) - (\d+) - ([A-Z]{3,4}) (\d{3}[A-Z]?) - ([A-Z0-9]+)$')
    credits_p = re.compile(r'((?:\d+\.\d+ TO +)?\d+\.\d+) Credits')
    for t, row in zip(titles, rows):
        flat_title = t.contents[0].contents[0].replace('\r', '')
        m = flat_title_p.match(flat_title)
        if not m:
            continue
        title, crn, subject, number, letter = m.groups()
        m = credits_p.search(str(row.td))
        credits = despacify.sub(' ', m.group(1)) if m else ''
        if row.td.table:
            meetings = [BannerMeeting(mtgrow) for mtgrow in islice(row.td.table('tr'), 1, None)]
        else:
            meetings = []
        yield BannerSection(crn, title, subject, number, letter, credits, meetings)
