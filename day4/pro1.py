inventory = {
    "Pen": 50,
    "Pencil": 30,
    "Notebook": 20
}

print("Inventory Items:")
for item, quantity in inventory.items():
    print(item, ":", quantity)

# Adding a new item
inventory["Eraser"] = 15

print("\nUpdated Inventory:")
for item, quantity in inventory.items():
    print(item, ":", quantity)