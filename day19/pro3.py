import threading

lock = threading.Lock()
balance = 0

def deposit():
    global balance

    for i in range(100000):
        with lock:
            balance += 1

thread1 = threading.Thread(target=deposit)
thread2 = threading.Thread(target=deposit)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Final Balance:", balance)