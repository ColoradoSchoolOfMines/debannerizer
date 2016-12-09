from debannerizer import db
from debannerizer.model.course import Course
from debannerizer.model.section import Section
from debannerizer.model.meeting import Meeting
from debannerizer.model.instructor import Instructor

__all__ = ["create_metadata", "Course", "Section", "Meeting", "Instructor"]

def create_metadata():
    for m in (Course, Section, Meeting, Instructor):
        m.metadata.drop_all(db.engine)
        m.metadata.create_all(db.engine)
