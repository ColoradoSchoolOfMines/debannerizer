from debannerizer import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Course(db.Base):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    # name cannot be unique, several of the following in data
    # (GRADUATE THESIS / DISSERTATION RESEARCH CREDIT)
    department = Column(String, nullable=False)
    title = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    number = Column(String, nullable=False)

    def __repr__(self):
        return "<course(id='%s', name='%s', department='%s', number='%s', credits='%s')>"%(
        self.id, self.name, self.department, self.number, self.credits)

    sections = relationship('Section', back_populates='course')

Course.metadata.create_all(db.engine)
