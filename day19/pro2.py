import multiprocessing

def print_numbers(name):
    for i in range(1, 6):
        print(name, ":", i)

if __name__ == "__main__":
    process1 = multiprocessing.Process(
        target=print_numbers,
        args=("Process 1",)
    )

    process2 = multiprocessing.Process(
        target=print_numbers,
        args=("Process 2",)
    )

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("Both processes completed.")