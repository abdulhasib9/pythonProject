def gen ():
    counter =0
    while counter <10:
        yield counter
        counter = counter+1
        
print(list(gen()))

#generating even number using genrator function 

def even(x):
 
    for i in range(x):
        if i%2==0:
            yield i
            
print(list(even(10)))