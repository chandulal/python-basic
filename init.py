class Person:
 def __init__(self, name, age):
  self.name = name
  self.age = age
 
 def printname(self):
   print("Hello, my name is " + self.name)

p1 = Person("Bob", 20)
print(p1.name)
print(p1.age)
p1.printname()
