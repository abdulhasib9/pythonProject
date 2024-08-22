class Food:
    greetings = "hello Good Morning!"
    
    def __init__(self,type) -> None:
        self.type=type
        self.g = Food.greetings
    
    @classmethod
    def greet(cls):
        print(cls.greetings)
    def add(a,b):
        return a+b
        
        
apple = Food("Apple")
apple.greet()

print(apple.g)
print(apple.add(23,44))

print(Food.add(23,44))