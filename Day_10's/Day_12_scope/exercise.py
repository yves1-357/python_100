import random
attempts_easy = 10
attempts_hard = 5
def guess_game():
    guess_computer = random.randint(1, 100)
    print(guess_computer)
    print("WELCOME TO THE NUMBER GUESSING GAME")
    print("I'm Thinking of number between 1 and 100")
    
    choice = input("Choose Difficulty. Type 'easy' or 'hard' : ").lower()
    if choice == 'easy':
        global attempts_easy
        while attempts_easy > 0:
            print(f"You have {attempts_easy} attempts remaining")
            guess = int(input("Make a guess : "))
            if guess > guess_computer:
                print("Too High")
                print("Guess Again")
                attempts_easy -= 1
            elif guess < guess_computer:
                print("Too Low")
                print("Guess Again")
                attempts_easy -= 1
            else:
                print("You won ")
                print(f"The Number was {guess_computer} ")
                break
            if attempts_easy == 0:
                print("You have no attempts left")
                print(f"The Number was {guess_computer}")

    else: 
        global attempts_hard 
        while attempts_hard > 0:
            print(f"You have {attempts_hard} attempts remaining")
            guess = int(input("Make a guess : "))
            if guess > guess_computer:
                print("Too High")
                print("Guess Again")
                attempts_hard -= 1
            elif guess < guess_computer:
                print("Too Low")
                print("Guess Again")
                attempts_hard -= 1
            else:
                print("You won ")
                print(f"The Number was {guess_computer} ")
                break
            if attempts_hard == 0:
                print("You have no attempts left")
                print(f"The Number was {guess_computer}")
      
guess_game()
while input("Do you want to re-do the game Type y/n: ").lower() == "y":
    print("\n" * 20)
    guess_game()