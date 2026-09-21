class MyMeta(type):
    def __new__(cls, name, bases, attributes):
        print(f"Creating class: {name}")
        return super().__new__(cls, name, bases, attributes)


class Student(metaclass=MyMeta):
    pass


student = Student()