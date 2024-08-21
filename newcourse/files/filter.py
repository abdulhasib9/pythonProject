num=[12,3,2,11,33,44,21]

def odd(x):
    if x%2  ==1:
        return x
    
odd_numbers  = list(filter(odd,num))
print(odd_numbers)

#solving above problem using lambda and filter

lambda_odd_numbers = list(filter(lambda x: x%2==1,num))
print(f"this result use lambda to filter the odd numbers from the given list {lambda_odd_numbers}")