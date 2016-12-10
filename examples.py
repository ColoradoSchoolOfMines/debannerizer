from debannerizer import db
from debannerizer.model import *

print("All the courses that CPW teaches...")
for instructor in db.session.query(Instructor)\
        .filter(Instructor.name == 'Christopher Robert Painter-Wakefield')\
        .all():
    course = instructor.meeting.section.course
    print("{}-{}: {}".format(course.subject, course.number, course.title))

print("All the courses that TBA teaches...")
for instructor in db.session.query(Instructor)\
        .filter(Instructor.name == 'TBA')\
        .all():
    course = instructor.meeting.section.course
    print("{}-{}: {}".format(course.subject, course.number, course.title))

print("The number of sections taught in each room of Brown Building on MWF")
brown_rooms = {}
for meeting in db.session.query(Meeting)\
        .filter(Meeting.loc_building == 'Brown Building')\
        .filter(Meeting.days == 'MWF')\
        .all():
    if meeting.loc_room in brown_rooms:
        brown_rooms[meeting.loc_room] += 1
    else:
        brown_rooms[meeting.loc_room] = 1

for key, val in sorted(brown_rooms.items(),
                       key=lambda item: item[1],
                       reverse=True):
    print('{}: {}'.format(key, val))

print("The number of sections taught by each department")
num_sections_taught = {}
for section in db.session.query(Section).all():
    if section.course.subject in num_sections_taught:
        num_sections_taught[section.course.subject] += 1
    else:
        num_sections_taught[section.course.subject] = 1

for key, val in sorted(num_sections_taught.items(),
                       key=lambda item: item[1],
                       reverse=True):
    print('{}: {}'.format(key, val))

print('All CSCI Instructors')
instructors = set()
for course in db.session.query(Course)\
        .filter(Course.subject == 'CSCI')\
        .all():
    for section in course.sections:
        for meeting in section.meetings:
            for instructor in meeting.instructors:
                instructors.add(instructor.name)
print(instructors)

