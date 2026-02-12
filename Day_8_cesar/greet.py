# def greet():
#     print("hello")
#     print("sara")
#     print("love")
# greet()

# def greet_with(name, location ):
#     print(f"hello {name}")
#     print(f"what is your {location}")

# greet_with("Sara", "switzerland")

def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()
    
    mots1 = "true".lower()
    mot2 = "love".lower()
    score_true = 0
    score_love = 0
    for letter in combined_names:
        if letter in mots1:
            score_true += 1
        if letter in mot2:
            score_love += 1
   
    total_final_true = str(score_true) + str(score_love)
    print(total_final_true)
calculate_love_score("Yu", "Jack Bauer")



