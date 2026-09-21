name = input("Enter student name: ")
age = input("Enter age: ")
department = input("Enter department: ")

with open("student.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Age: " + age + "\n")
    file.write("Department: " + department + "\n")

print("Student details saved successfully.")