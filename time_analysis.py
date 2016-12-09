# this just goes to show how cool our data set can be
# this is to analyse the growth in pecentage of CS courses over time

from debannerizer.importer import import_term

def term_range(start, stop):
    t = start
    while t != stop:
        yield t
        if t.endswith('10'):
            t = t[:4] + '80'
        elif t.endswith('80'):
            t = str(int(t[:4]) + 1) + '10'
    yield t
