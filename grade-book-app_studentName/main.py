#!/usr/bin/python3

# Define the 'Student' class
class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = {}
        self.GPA = 0.0

    def calculate_GPA(self):
        total_points = sum(self.courses_registered.values())
        total_possible_points = len(self.courses_registered) * 100  # Assuming 100 is the max grade for each course
        if total_possible_points == 0:
            self.GPA = 0
        else:
            percentage = (total_points / total_possible_points) * 100
            self.GPA = percentage / 20  # GPA out of 5
        print(f"The GPA is: {self.GPA:.2f}")
        return self.GPA

    def register_for_course(self, course, grade):
        self.courses_registered[course] = grade


# Define the 'Course' class
class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits


# Define the 'GradeBook' class
class GradeBook:
    def __init__(self):
        self.student_list = []  # List to store all the students
        self.course_list = []  # List to store all courses

    def add_student(self, email, names):
        student = Student(email, names)
        self.student_list.append(student)  # Adds the student to student list
        return student

    def add_course(self, name, trimester, credits):
        course = Course(name, trimester, credits)
        self.course_list.append(course)  # Adds the course to the course list

    def register_student_for_course(self, student_email, course_name, grade):
        student = next((s for s in self.student_list if s.email == student_email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)
        if student and course:
            student.register_for_course(course, grade)  # Register the student for the course
            student.calculate_GPA()  # Calculate the student's GPA
            return True
        return False

    def calculate_ranking(self):
        ranked_students = sorted(self.student_list, key=lambda s: s.GPA, reverse=True)
        return ranked_students

    def search_by_grade(self, grade):
        result = []
        for student in self.student_list:
            for course, student_grade in student.courses_registered.items():
                if student_grade == grade:
                    result.append((student, course))
        return result

    def generate_transcript(self, student_email):
        student = next((s for s in self.student_list if s.email == student_email), None)
        if student:
            transcript = f"Transcript for {student.names} ({student_email}):\n"
            transcript += "Course\tGrade\n"
            for course, grade in student.courses_registered.items():
                transcript += f"{course.name}\t{grade}\n"
            transcript += f"GPA: {student.GPA:.2f}"
            return transcript
        return "Student not found."


def main():
    gradebook = GradeBook()

    while True:
        print("GradeBook:")
        print("1. Add student")
        print("2. Add course")
        print("3. Register student for course")
        print("4. Calculate ranking")
        print("5. Search by Grade")
        print("6. Generate Transcript")
        print("7. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            email = input("Enter student email: ")
            names = input("Enter student name: ")
            gradebook.add_student(email, names)
        elif choice == '2':
            name = input("Enter course name: ")
            trimester = input("Enter course trimester: ")
            credits = int(input("Enter course credits: "))
            gradebook.add_course(name, trimester, credits)
        elif choice == '3':
            email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade: "))
            if gradebook.register_student_for_course(email, course_name, grade):
                print("Student registered for course successfully.")
            else:
                print("Unable to register student for course.")
        elif choice == '4':
            ranked_students = gradebook.calculate_ranking()
            print("Student Ranking by GPA:")
            for rank, student in enumerate(ranked_students, start=1):
                print(f"{rank}. {student.names} ({student.email}) - GPA: {student.GPA:.2f}")
        elif choice == '5':
            grade = float(input("Enter grade to search for: "))
            results = gradebook.search_by_grade(grade)
            for student, course in results:
                print(f"{student.names} ({student.email}) - {course.name}: {grade}")
        elif choice == '6':
            email = input("Enter student email: ")
            transcript = gradebook.generate_transcript(email)
            print(transcript)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
