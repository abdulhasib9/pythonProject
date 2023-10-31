fruits =["mango","apple","banana"]
print(fruits)

print(fruits[0])

print(fruits[-1])
#fruits[3]="grapes" this is not valid
fruits.append("grapes")

print(fruits)

fruits.extend(["apricot","peach"])
print(fruits)

#nested lists
vegetables = ["lettuce","tomatos"]

food = [fruits,vegetables]

print(food)
print(food[0][0])