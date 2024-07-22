#!/usr/bin/python3

#Define the 'Student' class
class Student:
    def __init__(self, email,names):
        self.email = email
        self.names = names
        self.courses_registered = {}
        self.GPA = 0.0


    def calculate_GPA(self,total_points, total_possible_points):
        if total_possible_points == 0: 
            return 0 
        percentage = (total_points / total_possible_points) * 100
        gpa = percentage / 20
        print(f"The GPA is :{gpa:.2f}")
        return gpa
   
#Define the 'Course' class
class Course:
    def __init__(self, name,trimester,credits):
        self.name = name
        self.trimester = trimester
        self.credits =credits


#Define the 'GradeBook' class
class GradeBook
    def __init__(self)
        self.student_list = [] #list to store all the students
        self.course_list = [] #List to store all courses

    def add_student(self, email, names):
        student = Student(email, names)
        self.student_list.append(student) #adds the studemt to student list
        return student 

    def add_course(self, name, trimester, credits):
        course = Course(name, trimester, credits)
        self.course_list.append(course) #adds the course to the course list

