stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = r'''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
import random
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

#verification d'abbord 
    if guess in liste_des_mots:
        print(f"Vous avez déjà proposées cette lettre: {guess}")
    else: 
        liste_des_mots.append(guess)

#Verifie erreur    
    if guess not in choosen_word:
        life -= 1
        print(f"Raté ! '{guess}' n'est pas dans le mot.")
        print(stages[life])
        print(f"Il vous reste :  {life} vies")

#Mise a jour affichage
    display = ""
    for letter in choosen_word:
        if letter in liste_des_mots:
            display += letter
        else:
            display += "_"
    print(display)   

#Verification victoire
    if "_" not in display:
        print(f"Vous avez Gagné, Le mot etait {choosen_word}")
        break 
    if life == 0:
        print(f"Vous avez raté, le mot etait {choosen_word}")
