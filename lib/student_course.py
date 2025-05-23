from datetime import datetime

class Course:
    all = []

    def __init__(self, name):
        self.name = name
        Course.all.append(self)


class Enrollment:
    all = []

    def __init__(self, student, course, enrollment_date):
        self.student = student
        self.course = course
        self._enrollment_date = enrollment_date  # should be a datetime object
        Enrollment.all.append(self)

    def get_enrollment_date(self):
        return self._enrollment_date

    @classmethod
    def aggregate_enrollments_per_day(cls):
        enrollment_count = {}
        for enrollment in cls.all:
            date = enrollment.get_enrollment_date().date()
            enrollment_count[date] = enrollment_count.get(date, 0) + 1
        return enrollment_count


class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []
        self._grades = {}

    def enroll(self, course, enrollment_date=None):
        if not enrollment_date:
            enrollment_date = datetime.now()
        enrollment = Enrollment(self, course, enrollment_date)
        self._enrollments.append(enrollment)
        return enrollment

    def course_count(self):
        return len(self._enrollments)

    def set_grade(self, enrollment, grade):
        self._grades[enrollment] = grade

    def aggregate_average_grade(self):
        if not self._grades:
            return 0
        total_grades = sum(self._grades.values())
        num_courses = len(self._grades)
        average_grade = total_grades / num_courses
        return average_grade
