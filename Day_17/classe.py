class User: 
    def __init__(self, user_id, username):
        self.id = user_id   
        self.name = username
        self.follower = 0
        self.following = 0

    def follow(self, user):#method
        user.follower  += 1
        self.following += 1 

user_1 = User("001", "Cano") #user_1: object de user
user_2 = User("002", "Deani")
user_1.follow(user_2)
print(user_1.follower)
print(user_1.following)

print(user_2.follower)
print(user_2.following)




# user_1.id = "PP2" #user_1 : attributs de user_1 // variable associé a object
# user_1.username = "cano"
print(user_1.id)
print(user_1.name)


# constructor: