from debannerizer import db
from debannerizer.stripper import banner_reader
from debannerizer.model import create_metadata, Section

def import_term(term):
    create_metadata()
    for bsection in banner_reader(term):
        Section.add_from_bsection(bsection)
    db.session.commit()
