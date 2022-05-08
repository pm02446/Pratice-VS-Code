class Person:
    # this is called automatically when you call the class
    def __init__(self, name, age):
        # the self parameter reference the current instance of the class
        # you can name it what ever you want
        self.name = name
        self.age = age
    # this is a method
    def greatings(self):
        print("Hello my name is " + self.name)
    # if you need to create an empyt class use this call
    pass

# this is you creating the object
p1 = Person("John", 36)

print(p1.name)
print(p1.age)
p1.greatings()

#modifing objects
p1.age = 40
print(p1.age)
#you can delete objects
#del
