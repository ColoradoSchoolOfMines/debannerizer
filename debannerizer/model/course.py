from debannerizer import db
from sqlalchemy import Column, Integer, String

class Course(db.Base):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    department = Column(String, nullable=False)
    number = Column(String, nullable=False)
    credits = Column(String)

Course.metadata.create_all(db.engine)
