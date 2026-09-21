Person = type(
    "Person",
    (),
    {
        "name": "Roshini",
        "age": 20
    }
)

person = Person()

print("Name:", person.name)
print("Age:", person.age)