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
list_of_lists = [[23,45],[434,55],[4,2]]
#flattening list of lists 
flatten = [ele for row in list_of_lists for ele in row]
print(flatten)