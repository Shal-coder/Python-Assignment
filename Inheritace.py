class Course:
    def __init__(self, course_name, instructor):
        self.course_name = course_name
        self.instructor = instructor
    def get_details(self):
        return f"Course: {self.course_name}, Instructor: {self.instructor}"
class WebDevClass(Course):
    def __init__(self, course_name, instructor, technologies):
        super().__init__(course_name, instructor)  
        self.technologies = technologies
    def get_details(self):
        base_details = super().get_details()  
        technology_string = ", ".join(self.technologies)  
        return f"{base_details}, Technologies: {technology_string}"
if __name__ == "__main__":
    general_course = Course("Introduction to Programming", "Jamal Akram")
    print(general_course.get_details())
    web_dev_course = WebDevClass("Web Development Fundamentals", "Abebe Alemu", ["HTML", "CSS" ,"JavaScript", "Python", "SQL"])
    print(web_dev_course.get_details())