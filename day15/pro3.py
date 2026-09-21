def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper


@uppercase_decorator
def message():
    return "hello python"


print(message())