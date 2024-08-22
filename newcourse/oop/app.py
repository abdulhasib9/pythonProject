from typing import Any


class Person:
    age =24
    
james = Person()

print(james.age)

class Animal:
    
    def __init__(self,type ='Unknown',age=0):
        self.type = type
        self.age = age
        
cat = Animal('cat',2)
print(cat.type)
print(cat.age)

Dog = Animal()
print(Dog.age)


class Product:
    
    def __init__(self,name,price) -> None:
        
        self.price = price
        self.name=name
        
    def discount(self):
        self.price = self.price /2
        return self.price
    

laptop = Product('laptop',4000)

print(laptop.name + str(laptop.price))

print(laptop.discount())