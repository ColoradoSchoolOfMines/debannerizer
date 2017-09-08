# this just goes to show how cool our data set can be
# this is to analyse the growth in pecentage of CS courses over time

import sys
from collections import defaultdict
from debannerizer import db
from debannerizer.importer import import_term
from debannerizer.model import Section

def term_range(start, stop):
    t = start
    while t != stop:
        yield t
        if t.endswith('10'):
            t = t[:4] + '80'
        elif t.endswith('80'):
            t = str(int(t[:4]) + 1) + '10'
    yield t

def frequency_analysis(subject):
    counts = defaultdict(int)
    for section in db.session.query(Section).all():
        if int(section.course.number[0]) < 5:
            counts[section.course.subject] += 1
    return counts[subject] / sum(counts.values())

if __name__ == '__main__':
    for term in term_range(*sys.argv[1:]):
        import_term(term)
        db.session.commit()
        print("{},{}".format(term, frequency_analysis("CSCI")))
