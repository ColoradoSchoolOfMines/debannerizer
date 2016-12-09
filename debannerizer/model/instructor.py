from debannerizer import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Instructor(db.Base):
    __tablename__ = 'instructor'

    meeting_id = Column(Integer, ForeignKey('meeting.id'), primary_key=True)
    name = Column(String, primary_key=True)

    meeting = relationship('Meeting', back_populates='instructors')

Instructor.metadata.create_all(db.engine)
