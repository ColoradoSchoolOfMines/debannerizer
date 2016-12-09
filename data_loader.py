from debannerizer.stripper import banner_reader

# Load Data from Banner
spring2017_sections = banner_reader('201510')

from debannerizer.model.course import Course
from debannerizer.model.instructor import Instructor
from debannerizer.model.meeting import Meeting
from debannerizer.model.section import Section

# Load instructors into Instructor objects
instructor_strs = set()
meetings = set()
sections = set()
courses = set()

for section in spring2017_sections:
    # Load sections
    sections.add(Section(crn=section.crn,
                        section=section.section
                        ))

    # Load courses
    courses.add(Course(name=section.title,
                       department=section.subject,
                       number=section.number,
                       credits=section.credits
                       ))

    for meeting in section.meetings:
        # Load instructors
        instructor_strs.update({instructor.strip() for instructor in meeting.instructors
                            if instructor not in instructor_strs})

        # Load meetings
        # I'm sure there's a more Pythonic way to do this, but eh
        # TODO: Handle No rooom
        location = meeting.location.split()
        building = location[:-1]
        room = location[-1]

        meetings.add(Meeting(crn=section.crn,
                             instructor_id=1, # TODO
                             begin_time=meeting.timerange[0],
                             end_time=meeting.timerange[1],
                             days=meeting.days,
                             begin_date=meeting.daterange[0],
                             end_date=meeting.daterange[1],
                             loc_building=building,
                             loc_room=room,
                             type=meeting.type,
                             schtype=meeting.schtype
                             ))

instructors = {Instructor(name=instructor) for instructor in instructor_strs}

import debannerizer.db as db
db.session.add_all(instructors)
db.session.commit()
db.session.add_all(courses)
db.session.commit()
db.session.add_all(sections)
db.session.commit()
db.session.add_all(meetings)
db.session.commit()
