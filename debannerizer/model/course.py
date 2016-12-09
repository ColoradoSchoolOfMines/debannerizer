from debannerizer import db
from sqlalchemy import Column, Integer, String

class Course(db.Base):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    # name cannot be unique, several of the following in data
    # (GRADUATE THESIS / DISSERTATION RESEARCH CREDIT)
    department = Column(String, nullable=False)
    number = Column(String, nullable=False)
    credits = Column(String)

    def __repr__(self):
        return "<course(id='%s', name='%s', department='%s', number='%s', credits='%s')>"%(
        self.id, self.name, self.department, self.number, self.credits)

Course.metadata.create_all(db.engine)
