class User:
    #pass
    def __init__(self,id,username):
        self.user_id = id
        self.username= username
        print("Created New Object")
    # def __init__(self,id):
    #     print(f"user with id{id}")
    
user_1 = User("001","Abdul hasib Yousufzai")
print(user_1.user_id)
print(user_1.username)

