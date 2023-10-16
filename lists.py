demo_list =["naem",3,True,5.44]

for items in demo_list:
    print(items)

r = range(1,11)
list(r)
for items in list(r):
    print(f"{items}")
    
# print("hello world") 

#checking a value in list 
name_check="naem" in demo_list
print(name_check)

#iterating through the list using while loop 
print("***********************************-----Iterating Using While Loop----************************************")
numbers = range(1,11)
numbers = list(numbers)
i =0
while i < len(numbers):
    print(numbers[i])
    i+=1