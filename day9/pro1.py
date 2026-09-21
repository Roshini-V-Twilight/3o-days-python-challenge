class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name:", self.name)


class Student(Person):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department

    def display_details(self):
        self.display_name()
        print("Department:", self.department)


student = Student("Roshini", "AI & Data Science")
student.display_details()