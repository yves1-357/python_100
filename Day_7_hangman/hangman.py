import random

#ToDO 1
#Choose a word from word_list and assign to variable

print("Welcome to the Hangman Game")

word_list = ["python","hangman","computer","programming","developer","algorithm","function","variable","keyboard","monitor","software",]
choosen_word = random.choice(word_list)
print(choosen_word)

placeholer = ""
longueur_mot = len(choosen_word) # longueur mot choisie
for position in range(longueur_mot):
    placeholer += "_"
print(placeholer)

life = 6
liste_des_mots = []
while life > 0:
    guess = str(input("Guess a letter : ").lower())
    if guess not in liste_des_mots:
        liste_des_mots.append(guess) 

    display = ""
    for letter in choosen_word:
        if letter in liste_des_mots:
            display += letter
        else:
            display += "_"
    print(display)   

    if "_" not in display:
        print(f"Vous avez Gagné, Le mot etait {choosen_word}")
        break 

    if guess not in choosen_word:
        life -= 1
        print(f"Vous avez {life} vies restants")
    if  life == 0:
        print(f"Vous avez raté, le mot etait {choosen_word}")






# for letter in word:
#     display_word.append("_")
# life = 6
# indices = []
# user = str(input("Guess a letter : "))

# for i in range(len(word[i])):
#     if user == word: 
#         indices.append(i)
#         display_word[indices] = user







