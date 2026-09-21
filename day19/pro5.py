import threading
import time

def download_file(file_name):
    print(file_name, "download started...")

    time.sleep(2)

    print(file_name, "download completed!")


files = ["File1.pdf", "File2.pdf", "File3.pdf"]

threads = []

for file in files:
    thread = threading.Thread(target=download_file, args=(file,))
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()


print("All files downloaded successfully.")