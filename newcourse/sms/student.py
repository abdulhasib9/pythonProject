class Student:
    def  __init__(self,name,age,roll_number) -> None:
        self.name = name
        self.age = age
        self.roll_number = roll_number
        
    def __str__(self) -> str:
        return f"{self.name} {self.age} {self.roll_number}"
    
