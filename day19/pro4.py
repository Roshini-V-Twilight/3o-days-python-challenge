import threading
import time

def task():
    time.sleep(2)


# Sequential execution
start = time.time()

task()
task()

end = time.time()

print("Sequential Time:", end - start, "seconds")


# Thread execution
start = time.time()

thread1 = threading.Thread(target=task)
thread2 = threading.Thread(target=task)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

end = time.time()

print("Thread Execution Time:", end - start, "seconds")