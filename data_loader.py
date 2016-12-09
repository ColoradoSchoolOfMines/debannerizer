import debannerizer.stripper

# Load Data from Banner
#spring2017_sections = stripper.banner_reader('201510')

# Load instructors into Instructor objects
from debannerizer.model import *
instructors = set()
for section in spring2017_sections:
    for meeting in section.meetings:
        instructors.update({Instructor(name=instructor)
                            for instructor in meeting.instructors})

# Load meetings into Meeting objects
meetings = set()
for section in spring2017_sections:
    for meeting in meetings:
        # I'm sure there's a more Pythonic way to do this, but eh
        # TODO: Handle No rooom
        location = meeting.location.split()
        building = location[:-1]
        room = location[-1]

        meetings.add(Meeting(crn=section.crn,
                             instructor_id=0, # TODO
                             begin_time=meeting.timerange[0],
                             end_time=meeting.timerange[1],
                             days=meeting.days,
                             begin_date=meeting.daterange[0],
                             end_date=meeting.daterange[1],
                             loc_building=building,
                             loc_room=room
                             )
                     )

# Load Sections
sections = set()
for section in spring2017_sections:
    section.add(Section(crn=section.crn,
                        section=section.section,
                        type=





