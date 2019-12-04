class A:

    def __init__(self,name):
        self.name = name

    def see(self):
        print('see in A called')

    def __hide(self):
        print('i am hide. find me if you can')

    def __repr__(self):
        return str(dict([('name',self.name)]))

class B(A):
    pass

a = A('A is for Amir')
b = B('B is for BOY')

print(a)
print(b)



# a._A__hide()  not truly hidden from global scope.  but mangled way to access the var.
# a.__hide()  #generates an error. A object has no attribute __hide












# class Human:
#     species = "homo-sapien"

#     def __init__(self, first,last,age):
#         self.first = first
#         self.last = last
#         self.age = age
    
#     def speak(self, speech):
#         print(f"{self.first} says {speech}!")

#     def __str__(self):
#         return str(dict([('first name',self.first), ('last name', self.last), ('age', self.age)]))

#     def __repr__(self):
#         return str(dict([('first name',self.first), ('last name', self.last), ('age', self.age)]))

# man = Human('amir','yunas', 37)
# woman = Human('juliet', 'jones', 18)

# print(man)




# print(man.first)
# print(man.age)
# print(man.species)

# man.speak('howdy partner')

# class Muslim(Human):
#     def religion(self):



        









# class Comedian:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

#     def __str__(self):
#         return f"{self.first_name} {self.last_name} is {self.age}."

#     def __repr__(self):
#         return f"{self.first_name} {self.last_name} is {self.age}. Surprise!"

# new_comedian = Comedian('Amir', 'Yunas', '37')

# print(f"{new_comedian!r}")

# person = {
#     "name" : "Amir",
#     "age" : 27,
#     "height" : 6,
#     "weight" : 210
# }

# name,age,height,weight = person
# print(name,age,height,weight)

# print(person)

# print(f"{person['name']} is {person['age']} years old")

# print(f"{name} is {age} years old.  He is {height} feet tall, weighing in at {weight} lbs.  ")

# message = (
#     f"This is {name}. "
#     f"He is {age} years old. "
#     f"He is {height} feet tall. "
#     f"He is {weight} lbs."
# )

# print(message)
