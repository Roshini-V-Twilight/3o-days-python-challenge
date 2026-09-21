def start_decorator(func):
    def wrapper():
        print("Program Started")
        func()
    return wrapper


@start_decorator
def display():
    print("Hello, World!")


display()