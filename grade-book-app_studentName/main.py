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


