numbers = [1,3,4,32,44]

def square(x):
    return x*x

print(list(map(square,numbers)))

#more map examples
string_numbers =['1','2','23','23']
print(string_numbers)
converted_to_numbers = list(map(int,string_numbers))
print(converted_to_numbers)

#applying mathematical operation using lambda functions

list1 =[2,3,4,5]

sq = list(map(lambda x: x**x ,list1))
print(sq)

names= ['noman','sahar','hasib']
cap = list(map(str.capitalize,names))
print(cap)