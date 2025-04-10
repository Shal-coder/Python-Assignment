class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Course: {self.course}")

student = Student("yoye", 20, "Software Engineering")
student.display_info()