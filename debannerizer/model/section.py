from debannerizer import db
from sqlalchemy import Column, Integer, String

class Section(db.Base):
    __tablename__ = 'section'
    # CRN is guaranteed to be unique, don't need ID
    crn = Column(String, primary_key=True)
    section = Column(String, nullable = False)
    
    def __repr__(self):
        return "<section(crn='%s',section='%s')>"%(
        self.crn, self.section)

Section.metadata.create_all(db.engine)
