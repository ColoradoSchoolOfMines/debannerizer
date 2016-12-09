from debannerizer import db
from sqlalchemy import Column, Integer, String, ForeignKey, Time, Date

class Meeting(db.Base):
    __tablename__ = 'meeting'

    id = Column(Integer, primary_key=True)
    crn = Column(String, ForeignKey("section.crn"), nullable=False)
    instructor_id = Column(Integer, ForeignKey("instructor.id"), nullable=False)
    begin_time = Column(Time)
    end_time = Column(Time)
    days = Column(String, nullable=False)
    begin_date = Column(Date)
    end_date = Column(Date)
    loc_building = Column(String, nullable=False)
    loc_room = Column(String, nullable=False)
    type = Column(String, nullable=False)
    schtype = Column(String, nullable=False)

    
    def __repr__(self):
        return "<meeting(id='%s', crn='%s', begin_time='%s', end_time='%s', days='%s', loc_building='%s',loc_room='%s')>"%(
        self.id, self.crn, self.begin_time, self.end_time, self.days, self.loc_building, self.loc_room)

Meeting.metadata.create_all(db.engine)
