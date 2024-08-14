def decorator (fun):
    def wrapper():
        print('decorations begin')
        fun()
        print('decorations ends')
    return wrapper

def decorator_with_argument(func):
    def wrapper(*args,**kwargs):
        print('******************** Designing *************************')
        func(*args,**kwargs)
        print('******************** Designing Ends ***********************')
    return wrapper
@decorator    
def simple3():
    print('this is a simple function')
    
simple3()

@decorator
def cake():
    print('decorating cake')
    
cake()

@decorator_with_argument
def apple_cake(name):
    print(f'preparing {name} cake!!!! ')
    
apple_cake('apple')


def discount(func):
    def wrapper(price):
        func(price)
        return func(price/2)
    return wrapper

@discount

def sale(price):
    return price

print(sale(2000))