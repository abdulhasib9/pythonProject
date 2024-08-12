# shopping_list =[]
# items_number  = int(input("please enter the number of items you want to add: "))

# for x in range(items_number):
#     item =input(f'please enter the item number {x} ')
#     shopping_list.append(item)
    
# print(shopping_list)

def remove_duplicate(list):
    new_list = []
    for x in list:
        if x not in new_list:
            new_list.append(x)
    return new_list
    #return list(set(list))


list = [23,44,55,44,33,44,22,34]
print(remove_duplicate(list))

def return_multiple(x,y):
    return x,y

x,y = return_multiple(23,44)
print(f"{x}   {y}")