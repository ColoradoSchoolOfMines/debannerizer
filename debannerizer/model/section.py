from debannerizer import db
from debannerizer.model.meeting import Meeting
from debannerizer.model.course import Course
from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from decimal import Decimal

class Section(db.Base):
    __tablename__ = 'section'
    crn = Column(String, primary_key=True)
    course_id = Column(Integer, ForeignKey('course.id'), nullable=False)
    section_letter = Column(String)
    min_credits = Column(Numeric(precision=5, scale=3))
    max_credits = Column(Numeric(precision=5, scale=3))

    course = relationship('Course', back_populates='sections')
    meetings = relationship('Meeting', back_populates='section')

    def __repr__(self):
        return "<section(crn='%s',section='%s')>"%(
        self.crn, self.section)

    @staticmethod
    def add_from_bsection(bsection):
        if ' TO ' in bsection.credits:
            min_credits, _, max_credits = bsection.credits.partition(' TO ')
        else:
            min_credits, max_credits = [bsection.credits] * 2

        crse = db.session.query(Course)\
                .filter(Course.subject == bsection.subject)\
                .filter(Course.number == bsection.number).first()
        if not crse:
            crse = Course(
                    title=bsection.title,
                    subject=bsection.subject,
                    number=bsection.number)
            db.session.add(crse)
            db.session.flush()

        db.session.add(Section(
                crn=bsection.crn,
                course_id=crse.id,
                section_letter=bsection.letter,
                min_credits=min_credits,
                max_credits=max_credits
            ))

        for m in bsection.meetings:
            Meeting.add_from_bmeeting(crn=bsection.crn, bmeeting=m)
