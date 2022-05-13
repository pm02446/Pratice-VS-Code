mytuple= ("apple", "banana","cherry")
#Lists, tupels, dictionaries, and sets are
# all iterable objects, you can just use iter()
myit = iter(mytuple)

mystr = "four"
myit = iter(mystr)

#print(next(myit))
#print(next(myit))

#for x in mystr:
#    print(x)

# creating an iterator 
""" class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x
myclass = MyNumbers()
myiter = iter(myclass)

#print(next(myiter))
print(next(myiter)) """

# Stopping iterations with StopIteration
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)