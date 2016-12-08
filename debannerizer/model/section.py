from debannerizer import db
from sqlalchemy import Column, Integer, String

class Section(db.Base):
    __tablename__ = 'section'

    crn = Column(String, primary_key=True)
    section = Column(String, nullable = False)
    type = Column(String, nullable=False)
    section_type = Column(String, nullable=False)
    
    def __repr__(self):
        return "<section(id='%s', crn='%s', type='%s', section_type='%s')>"%(
        self.id, self.crn, self.type, self.section_type)

Section.metadata.create_all(db.engine)
