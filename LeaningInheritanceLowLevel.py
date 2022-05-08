class Person:
    def __init__(person, fname, lname):
        person.firstname = fname
        person.lastname = lname

    def printName(person):
        print(person.firstname, person.lastname)

# Child Class
class Student(Person):
    def __init__(student, fname, lname, year):
        # the supper call inherits everything form the current calss's
        # parent class
        super().__init__(fname, lname)
        student.graduationyear = year
    def welcome(student):
        print("Welcom", student.firstname, student.lastname, "to the class of", student.graduationyear)

x = Person("John", "Doe")
x.printName()

y = Student("Mike", "Olsen", 2019)
y.printName()
y.welcome()
