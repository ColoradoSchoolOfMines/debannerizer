from debannerizer import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Course(db.Base):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True, autoincrement=True)
<<<<<<< HEAD
    name = Column(String, nullable=False)
    # name cannot be unique, several of the following in data
    # (GRADUATE THESIS / DISSERTATION RESEARCH CREDIT)
    department = Column(String, nullable=False)
=======
    title = Column(String, nullable=False)
    subject = Column(String, nullable=False)
>>>>>>> 2a0a1dcb593c6380db9210b0329445a433fc0bd3
    number = Column(String, nullable=False)

<<<<<<< HEAD
    def __repr__(self):
        return "<course(id='%s', name='%s', department='%s', number='%s', credits='%s')>"%(
        self.id, self.name, self.department, self.number, self.credits)

Course.metadata.create_all(db.engine)
=======
    sections = relationship('Section', back_populates='course')
>>>>>>> 2a0a1dcb593c6380db9210b0329445a433fc0bd3
