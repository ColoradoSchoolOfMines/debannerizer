from debannerizer import db
from sqlalchemy import Column, Integer, String

class Instructor(db.Base):
    __tablename__ = 'instructor'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    
def __repr__(self):
    return "<section(id='%s', name='%s')>"%(
        self.id, self.name)

Instructor.metadata.create_all(db.engine)
