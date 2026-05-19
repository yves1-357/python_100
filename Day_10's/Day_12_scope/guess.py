# logo = """
#    _____                        _____                      
#   / ____|                      / ____|                     
#  | |  __ _   _  ___  ___ ___  | |  __  __ _ _ __ ___   ___ 
#  | | |_ | | | |/ _ \/ __/ __| | | |_ |/ _` | '_ ` _ \ / _ \
#  | |__| | |_| |  __/\__ \__ \ | |__| | (_| | | | | | |  __/
#   \_____|\__,_|\___||___/___/  \_____|\__,_|_| |_| |_|\___|
                                                           
#                                                            """
import random
from art import logo
def guess_game():
    guess_computer = random.randint(1, 100)
    print(logo)
    print("WELCOME TO THE NUMBER GUESSING GAME")
    print("I'm Thinking of number between 1 and 100")
    
    choice = input("Choose Difficulty. Type 'easy' or 'hard' : ").lower()
    if choice == 'easy':
        attempts = 10
    else:
        attempts = 5
    
    while attempts > 0:
        print(f"You have {attempts} attempts remaining")
        guess = int(input("Make a guess : "))
        if guess > guess_computer:
            print("Too High")
            print("Guess Again")
            attempts -= 1
        elif guess < guess_computer:
            print("Too Low")
            print("Guess Again")
            attempts -= 1
        else:
            print("You won ")
            print(f"The Number was {guess_computer} ")
            break
        if attempts == 0:
            print("You have no attempts left")
            print(f"The Number was {guess_computer}")

      
guess_game()
while input("Do you want to re-do the game Type y/n: ").lower() == "y":
    print("\n" * 20)
    guess_game()