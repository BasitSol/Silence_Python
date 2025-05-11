from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, _id):
        self.name = name  
        self.age = age
        self._id = _id   #Protected 

    @abstractmethod
    def get_details(self):
        pass


class Student(Person):
    def __init__(self, name, age, _id, major, grades = {"Maths":"A", "Physics":"B","chemistry":"C"}):
       super().__init__(name,age,_id)
       self.major = major
       self.grades = grades
    
    def calculate_gpa(self):
        grade_scale = {
            'A+': 4.0, 'A': 4.0, 'A-': 3.7,
            'B+': 3.3, 'B': 3.0, 'B-': 2.7,
            'C+': 2.3, 'C': 2.0, 'C-': 1.7,
            'D+': 1.3, 'D': 1.0, 'F': 0.0
        }

        total_points = 0
        total_courses = 0

        for course, grade in self.grades.items():
            if grade in grade_scale:
                total_points += grade_scale[grade]
                total_courses += 1
            else:
                print(f"Invalid grade '{grade}' for {course}")

        if total_courses == 0:
            return 0.0
        
        gpa = total_points / total_courses
        return round(gpa, 2)


    def get_details(self):
        return f"Student Name: {self.name}, Age: {self.age}, Major: {self.major}, GPA: {self.calculate_gpa()}"



class Professor(Person):
    def __init__(self,name, age, _id, dep, courses_taught):
        super().__init__(name, age, _id)
        self.dep = dep
        self.__courses_taught = courses_taught ## private
    
   
    
    def assign_courses(self, course_name):
        self.course_name = course_name
    
    def get_details(self):
        return f"Professor Department is {self.dep} his assigned course was {self.course_name }and he taught {self.__courses_taught}"



s1 = Student("Basit", 23 ,"F22ba", "Computer Science")
s2 = Student("Ali", 28 ,"F22tr", "IT")
print(s1.get_details())
print(s2.get_details())

p = Professor("FAisal", 45, "tyri", "Dep Of CS", "DSA")
p.assign_courses("ISP")

merge_student = s1 + s2
print(merge_student.get_details())
print(p.get_details())
p.get_details()

    

