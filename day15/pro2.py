import time

def execution_time(func):
    def wrapper():
        start_time = time.time()

        func()

        end_time = time.time()

        print("Execution Time:", end_time - start_time, "seconds")

    return wrapper


@execution_time
def program():
    for i in range(1000000):
        pass


program()