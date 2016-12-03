import requests
from bs4 import BeautifulSoup

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

