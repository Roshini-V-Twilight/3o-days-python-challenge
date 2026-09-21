try:
    number = int(input("Enter an integer: "))
    print("You entered:", number)

except ValueError:
    print("Invalid input! Please enter a valid integer.")