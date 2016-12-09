from debannerizer import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Course(db.Base):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    number = Column(String, nullable=False)

    sections = relationship('Section', back_populates='course')
