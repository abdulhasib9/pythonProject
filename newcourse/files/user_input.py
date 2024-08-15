while True: 
    with open('/Users/thebeast/Documents/pythonProject/newcourse/files/user.txt','a') as file:
        user_input = input("please enter the user name: ")
        file.write(user_input)
        choice = input('do you want to add another user? (Y/N)')
        choice.lower()
        if choice == 'n':
            break
