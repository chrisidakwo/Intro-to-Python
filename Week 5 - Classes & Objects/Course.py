# coding: utf-8
"""Working with classes and objects"""
import datetime


class Course:
    """Course"""
    def __init__(self, coursecode, coursename):
        self._course_code = coursecode
        self._course_name = coursename
        self._course_tutor = ""
        self._course_desc = ""
        self._course_start_date = datetime.date.today()
        self._course_end_date = datetime.date.today()
        self._students = []

    def __unicode__(self):
        """Returns a human-readable representation of a Course for < Python 3"""
        result = "{0} - {1}".format(self._course_code, self._course_name)
        return result

    def __str__(self):
        """Returns a human-readable representation of a Course for > Python 2"""
        result = "{0} - {1}".format(self._course_code, self._course_name)
        return result

    def get_course_code(self):
        """Get the course of the course"""
        return self._course_code

    def get_course_name(self):
        """Get the name of the course"""
        return self._course_name

    def set_course_name(self, coursename):
        """Set the name of the course"""
        self._course_name = coursename

    def get_students(self):
        """Get a list of students"""
        return self._students

    def add_student(self, student):
        """Add an individual student"""
        self._students.append(student)

    def add_students(self, students):
        """Add multiple students"""
        if len(students) != 0:
            self._students.extend(students)
        else:
            return "List contains {0} element".format(len(students))

    def get_number_of_students(self):
        """Get number of students in a course"""
        return len(self._students)
    

New_Course_1 = Course("EX02934", "Psychology & Counselling Skills")
print(New_Course_1)
print(type(New_Course_1))
