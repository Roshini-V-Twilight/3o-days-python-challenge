with open("source.txt", "r") as source, open("destination.txt", "w") as destination:
    
    data = source.read()
    
    destination.write(data)

print("File copied successfully.")