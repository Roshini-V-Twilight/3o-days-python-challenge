def greet(self):
    print("Hello! Welcome to Python.")

Person = type(
    "Person",
    (),
    {
        "greet": greet
    }
)

person = Person()

person.greet()