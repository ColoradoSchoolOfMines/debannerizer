from debannerizer import db
from sqlalchemy import Column, Integer, String, ForeignKey, Time, Date
from sqlalchemy.orm import relationship
from debannerizer.model.instructor import Instructor

class Meeting(db.Base):
    __tablename__ = 'meeting'

    id = Column(Integer, primary_key=True)
    crn = Column(String, ForeignKey("section.crn"), nullable=False)
    begin_time = Column(Time)
    end_time = Column(Time)
    days = Column(String)
    begin_date = Column(Date)
    end_date = Column(Date)
    loc_building = Column(String)
    loc_room = Column(String)

    
    def __repr__(self):
        return "<meeting(id='%s', crn='%s', begin_time='%s', end_time='%s', days='%s', loc_building='%s',loc_room='%s')>"%(
        self.id, self.crn, self.begin_time, self.end_time, self.days, self.loc_building, self.loc_room)

    instructors = relationship('Instructor', back_populates='meeting')
    section = relationship('Section', back_populates='meetings')

    @staticmethod
    def add_from_bmeeting(bmeeting, crn):
        mtg = Meeting(
                crn=crn,
                begin_time=bmeeting.timerange[0],
                end_time=bmeeting.timerange[1],
                days=bmeeting.days,
                begin_date=bmeeting.daterange[0],
                end_date=bmeeting.daterange[1],
                loc_building=bmeeting.building,
                loc_room=bmeeting.room,
            )
        db.session.add(mtg)
        db.session.flush()
        db.session.add_all([Instructor(meeting_id=mtg.id, name=p) for p in bmeeting.instructors])
