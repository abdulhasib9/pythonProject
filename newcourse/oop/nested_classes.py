class Zoo:
    
    def __init__(self,animals =[]) -> None:
        self.animals = []
        
    def add_animal(self,type,name):
        animal = self.Animal(type,name)
        self.animals.append(animal)
        
        
    class Animal:
        def __init__(self,type,name) -> None:
            self.type = type
            self.name = name
        @staticmethod
        def display_animal(self):
            print(f"{self.type} name is {self.name}")
        

# sea_zoo = Zoo()
# sea_zoo.add_animal('cat','kitty')


class Parent:
    
    def __init__(self) -> None:
        self.parent_amount = 500000
        print(self.amount)
        
class Child(Parent):
    def __init__(self) -> None:
        self.amount = 70000
        super().__init__()
        print(self.amount)
        print(self.parent_amount)

ch = Child()