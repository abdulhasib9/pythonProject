def decorator (fun):
    def wrapper():
        print('decorations begin')
        fun()
        print('decorations ends')
    return wrapper
@decorator    
def simple3():
    print('this is a simple function')
    
simple3()

@decorator
def cake():
    print('decorating cake')
    
cake()