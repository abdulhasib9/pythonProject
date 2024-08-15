

try:
    file = open('/Users/thebeast/Documents/pythonProject/newcourse/files/data.txt','r')
    content = file.read()

    print(f'text in the file {content}') 
    
except (FileNotFoundError):
    print('File does not Exits!')
else: 
    print('File Exists')
finally:
    print('the code made it thru the end')
    
try: 
    with open('/Users/thebeast/Documents/pythonProject/newcourse/files/data.txt','a') as file:
        #print(file.read())
        file.write('\n new line of text added !!!')
except (FileNotFoundError):
    print('file not found')