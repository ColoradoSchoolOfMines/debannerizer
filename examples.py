from debannerizer import db
from debannerizer.model import *

print("All the courses that CPW teaches...")
for instructor in db.session.query(Instructor)\
        .filter(Instructor.name == 'Christopher Robert Painter-Wakefield')\
        .all():
    course = instructor.meeting.section.course
    print("{}-{}: {}".format(course.subject, course.number, course.title))

# TODO: More examples?
