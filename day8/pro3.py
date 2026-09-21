class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

employee1 = Employee("John", 50000)

print("Employee Name:", employee1.name)
print("Salary:", employee1.salary)