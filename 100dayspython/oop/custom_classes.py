class User:
    #pass
    # user_id=0
    # username =""
    def __init__(self,id,username):
        self.user_id = id
        self.username= username
        self.followers=0
        print("Created New Object")
    # def __init__(self,id):
    #     print(f"user with id{id}")
    def print_full_name(self):
        print(f"{self.user_id} {self.username} Total Followers {self.followers}")
    def add_follower(self):
        self.followers +=1
    
user_1 = User("001","Abdul hasib Yousufzai")
print(user_1.user_id)
print(user_1.username)
user_1.print_full_name()
user_1.add_follower()
print(user_1.followers)
user_1.print_full_name()

