mark = float(input("Enter your mark: "))

if mark >= 90:
    grade = "A+"
elif mark >= 80:
    grade = "A"
elif mark >= 70:
    grade = "B"
elif mark >= 60:
    grade = "C"
elif mark >= 50:
    grade = "D"
else:
    grade = "F"

print("Your Grade is:", grade)