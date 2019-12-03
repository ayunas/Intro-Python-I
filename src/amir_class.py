class Comedian:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age}."

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age}. Surprise!"

new_comedian = Comedian('Amir', 'Yunas', '37')

# print(f"{new_comedian!r}")

person = {
    "name" : "Amir",
    "age" : 27,
    "height" : 6,
    "weight" : 210
}

name,age,height,weight = person
print(name,age,height,weight)

# print(person)

# print(f"{person['name']} is {person['age']} years old")

# print(f"{name} is {age} years old.  He is {height} feet tall, weighing in at {weight} lbs.  ")

message = (
    f"This is {name}. "
    f"He is {age} years old. "
    f"He is {height} feet tall. "
    f"He is {weight} lbs."
)

print(message)
