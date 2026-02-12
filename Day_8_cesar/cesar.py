alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(text, shift, direction):
    if direction == "decoder":
        shift = shift * -1

    cipher_text = ""

    for letter in text:
        if letter in alphabet:
            position_actuelle = alphabet.index(letter)
            nouvelle_position = (position_actuelle + shift) % 26
            nouvelle_lettre = alphabet[nouvelle_position]
            cipher_text += nouvelle_lettre
        else:
            cipher_text += letter
    print(cipher_text)
continuer = True 
while continuer :  
    message = input("Quel message souhaitez vous stocker: ? ").lower()
    text = message
    decalage = int(input("Combien de lettres voulez vous decaler: "))
    shift = decalage
    encodage = input("Veut tu encoder ou decode : ")
    direction = encodage
    caesar(text=message, shift=decalage, direction=encodage)
    reprendre = input ("Veux tu reprendre ? ").lower()
    if reprendre == "non":
        continuer = False
        print("Au revoir ") 



