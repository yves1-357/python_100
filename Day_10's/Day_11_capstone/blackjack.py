import random


def blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    your_cards = random.sample(cards, 2)
    print(f"Your cards are :  {your_cards}")
    somme = sum(your_cards)
    print(f"Current score = {somme}")

    computer = [random.choice(cards)]
    print(f"Computer choose : {computer}")
    result_computer = computer

    continue_1 = True
    while continue_1:
        user = input("Type 'y' to get another card, type 'n' to pass : ").lower()
        if user == "y":
            nouvelle_carte = random.choice(cards)
            your_cards.append(nouvelle_carte)
            print(f"Your new cards are :  {your_cards}")
            somme = sum(your_cards)
            print(f"Current score = {somme}")
            print(f"Computer first card : {result_computer }")

            if somme > 21 and 11 in your_cards:
                your_cards.remove(11)
                your_cards.append(1)
                somme = sum(your_cards)
                print(f"Points adjusted! New score : {somme}")

            if somme > 21:
                print("You went over. You lose! ")
                continue_1 = False

        elif user == "n":
            while sum(computer) < 17:
                computer.append(random.choice(cards))

            print(f"Current score = {somme}")
            somme_computer = sum(result_computer)

            print(f"Computer Final score = {somme_computer}")

            if somme_computer > 21:
                print("You Won, Computer Lost ")

            elif somme > somme_computer:
                print("You Win! User")
            elif somme_computer > somme:
                print("You Lost! Computer Won")
            else:
                print("It's a draw!")

            continue_1 = False

        else:

            continue_1 = False
            print("Game over")


blackjack()

while input("Do you want to re-do the game Type y/n: ").lower() == "y":
    print("\n" * 20)
    blackjack()
