class University():

    def __init__(self, name, url, address):
        self.name = name.title()
        self.url = url
        self.address = address.title()
        self.schedule = []

    def add_schedule(self, schedule):
        self.schedule.append(schedule)

    def university_info(self):
        print('\nName: ' + str(self.name))
        print('Url: ' + str(self.url))
        print('Address: ' + str(self.address))
        for schedule in self.schedule:
            prof = schedule.professor
            print('\nProfessor: ' + prof.name)
            course = schedule.course
            print('Course: ' + course.name)
            day = schedule.day
            print('Day: ' + day)
            time = schedule.time
            print('Time: ' + time)


uom = University('University of Minnesota', 'www.twin-cities.umn.edu', 'Minneapolis, MN 55455')


class Professors():

    def __init__(self, name, ssn, degree):
        self.name = name.title()
        self.ssn = ssn
        self.degree = degree.title()

    def professor_info(self):
        print('\nName: ' + str(self.name))
        print('Ssn: ' + str(self.ssn))
        print('Degree: ' + str(self.degree))


class Courses():

    def __init__(self, name):

        self.name = name.title()

    def course_name(self):
        print('\nCourse: ' + self.name)


class Schedule():

    def __init__(self, professor, course, day, time):
        self.professor = professor
        self.course = course
        self.day = day
        self.time = time


Uday = Professors('Uday', '013748273', 'masters')
Anika = Professors('Anika', '278163943', 'masters')
Vedant = Professors('Vedant', '863836374', 'masters')

Course1 = Courses('Calculus BC')
Course2 = Courses('bio chemistry')
Course3 = Courses('English honors')

Sched1 = Schedule(Uday, Course1, 'Monday', '11:00 AM')
Sched2 = Schedule(Anika, Course2, 'Tuesday', '12:00 PM')
Sched3 = Schedule(Vedant, Course3, 'Wednesday', '1:30 PM')

uom.add_schedule(Sched1)
uom.add_schedule(Sched2)
uom.add_schedule(Sched3)
uom.university_info()
