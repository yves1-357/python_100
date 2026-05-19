import random
#rock wins against scissors
#scissors win against paper
#paper wins against rock
print("Welcome to rock paper scissors game")
choice = ["Rock", "Paper", "Scissors"]
gamer = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 Scissors : "))
computer_choice = random.choice(choice)
if gamer == 0:
    print(f" You chose : {choice[gamer]}")
    if computer_choice == "Scissors":
        print(f"Computer chose : {computer_choice}")
        print("You win")
    elif computer_choice == "Rock":
        print(f"Computer chose : {computer_choice}")
        print("It's a Draw ")
    else:
        print(f"Computer chose : {computer_choice}")
        print("Computer Won ")
elif gamer == 1:
    print(f" You chose : {choice[gamer]}")
    if computer_choice == "Rock":
        print("You Win")
    elif computer_choice == "Paper":
        print(f"Computer chose : {computer_choice}")
        print("It's a Draw ")
    else:
        print(f"Computer chose : {computer_choice}")
        print("Computer Won ")
elif gamer == 2:
    print(f" You chose : {choice[gamer]}")
    if computer_choice == "Paper":
        print("You Win")
    elif computer_choice == "Scissors":
        print(f"Computer chose : {computer_choice}")
        print("It's a Draw ")
    else :
        computer_choice == "Rock"
        print("Computer Won ")
else:
    print("You Typed Invalid Number")
    


