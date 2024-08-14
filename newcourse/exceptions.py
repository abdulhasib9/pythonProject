try:
    print (10/0)
except(ZeroDivisionError):
    print('Can not divide by zerro')
else:
    #this block will execute if no exception occure
    print('Code running successfully!!')
finally:
    print("this block will execute no matter what happens!!!")