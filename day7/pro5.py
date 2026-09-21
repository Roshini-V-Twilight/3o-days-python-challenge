file = open("student.txt", "r")

content = file.read()

words = content.split()

print("Number of words:", len(words))

file.close()