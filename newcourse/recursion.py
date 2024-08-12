def factorial(number):

    if number == 1: 
        return 1
    else:
        return number * factorial(number-1)


# def fun2():
#     print('1')
#     fun2()

# fun2()

name = 'something'
print(id(name))