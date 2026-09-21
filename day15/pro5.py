def decorator_one(func):
    def wrapper():
        print("Decorator One - Before")
        func()
        print("Decorator One - After")
    return wrapper


def decorator_two(func):
    def wrapper():
        print("Decorator Two - Before")
        func()
        print("Decorator Two - After")
    return wrapper


@decorator_one
@decorator_two
def display():
    print("Hello, Python!")


display()