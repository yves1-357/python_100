# For > prendre UN élément → l’utiliser → passer au suivant
# For ça lit, ça parcourt, ça execute 
import random
print("Welcome to the Password Generator!")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
letters_nr = int(input("How many letters would you like in your password : "))
symbols_nr = int(input("How many symbols :  "))
numbers_nr = int(input("How many numbers :"))
password = []
for i in range(0, letters_nr):
    password.append(random.choice(letters))
    print(password)
for i in range(0, symbols_nr):
    password.append(random.choice(symbols))
    print(password)
for i in range(0, numbers_nr):
    password.append(random.choice(numbers))
    print(password)
random.shuffle(password)
resultat = "".join(password)
print(f"Votre mot de passe est : {resultat}")

