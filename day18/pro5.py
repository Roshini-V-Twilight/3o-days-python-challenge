class UpperCaseMeta(type):
    def __new__(cls, name, bases, attributes):

        new_attributes = {}

        for key, value in attributes.items():
            if not key.startswith("__"):
                key = key.upper()

            new_attributes[key] = value

        return super().__new__(cls, name, bases, new_attributes)


class Student(metaclass=UpperCaseMeta):
    name = "Roshini"
    department = "AI & DS"


print(Student.NAME)
print(Student.DEPARTMENT)