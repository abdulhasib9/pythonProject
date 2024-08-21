import json

data = {
    'name':'abdul hasib',
    'lastname': 'yousufzai'
}

json_data = json.dumps(data)

print(json_data)

def user_data():
    user_list =[]
    
    while True:
        name = input('input name or enter quit to exit the program:')
        if name == quit:
            break
        email = input('please enter user email ')
        contact = input('please enter user contact ')
        
        #creating a dictionary for given data above 
        
        user ={
            'name':name,
            'email':email,
            'contact':contact
        }
       # print(user_data)
        user_list.append(user)
        print(user_list)
        with open('/Users/thebeast/Documents/pythonProject/newcourse/files/users.json','w') as file:
            json.dump(user_list,file)
        print('user data saved successfully!')
        
user_data()