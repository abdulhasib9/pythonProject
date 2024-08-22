class Product:
    
    def __init__(self,name='',price=0) -> None:
        self.name = name
        self.price = price
        
    def put_data(self):
        print(f'{self.name} is ${self.price}')
        
    def __str__(self) -> str:
        return f"{self.name}"
        
        
laptop = Product('Dell XPS','400')

laptop.put_data()
print(laptop)

class Digital_Product(Product):
    pass

digital = Digital_Product('HP',500)

digital.put_data()