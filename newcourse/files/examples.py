#generating initails from first and lastname 

print("*************** Generating Initials from a Full Name")
names = ['abdul yousufzai','sahar yousufzai','noman yousufzai']

for name in names:
    print(f"{name.split()[0][0].capitalize()}{name.split()[1][0].capitalize()}")
    
#generating initials using map and lambda funcionts
print("*************** Generating Initials from a Full Name using map and lambda functions ***************")

initails = list(map(lambda name: "".join([n[0] for n in name.split()]),names))
cap_init = list(map(str.upper,initails))
print(initails)
print(cap_init)

[print(x) for x in cap_init]

#revesing a string 
name = 'abdulhasib'
print(name[::-1])


