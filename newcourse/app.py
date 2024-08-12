# list_of_people = ['raqib','hasib','mumtaz']
# print(list_of_people)
items = [2,3,55,6,43]
# # print(items.index(5))
# if 5 in items:
#     print('True')
# else: 
#     print('sorry 5 is not in list')
items.sort()
print(items)
items.reverse()
print(items)

new_items = items.copy()
print(new_items)

list = [i for i in range (10)]
print(list)
list_of_lists = [23,45,[23,45],[434,55],[4,2]]
#flattening list of lists 
# flatten = [ele for row in list_of_lists for ele in row]
# print(flatten)
# list_of_lists.sort()
# print(list_of_lists)

#creating custom function for sorting lists with different data types 
different =[2,44,5,'b','a',[23,44],[1,4]]

def custom_sort(item):
    if isinstance (item,int):
        return(0,item)
    elif isinstance (item,str):
        return(1,str)
    elif isinstance (item, list):
        return (2,len(list),list)
    else:
        return (3,item)
        
sorted_different = sorted(different,key=custom_sort)
print(sorted_different)