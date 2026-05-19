MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

monnaies = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01
}
def proceess_coins():
    dime_quartes = float(input("Insert quarters only above 0.25 :  "))
    dime_dimes = float(input("Insert dimes only above 0.10 :  "))
    nickels_dimes = float(input("Insert nickels only above 0.05 :  "))
    pennies_dimes = float(input("Insert pennies only above 0.01 :  "))
    Total = dime_quartes * monnaies["quarters"] + dime_dimes * monnaies["dimes"]  + nickels_dimes * monnaies["nickels"] + pennies_dimes * monnaies["pennies"]
   
    return Total


def coffee_machine():
    continue_game = True

    while continue_game:
        user_input = str(input("What would you like : espresso/latte/cappuccino :  ")).lower()
        if user_input == "espresso":
            if resources["water"] >= 50 and resources["coffee"] >= 18:
                print("Please insert your dimes")
                argent_insere = proceess_coins()

                cost = 1.5
                if argent_insere >= cost:
                    change = round(argent_insere - cost, 2)
                    print(f"Here is ${change} in change.")
                    resources["water"] -= 50
                    resources["coffee"] -= 18
                    print("Here it is your espresso ")
                else:
                   print("Sorry that's not enough money. Money refunded.")
        
            else: 
              print("Sorry, there is not enough water or ingredients.")
        


        elif user_input == "latte":
            if resources["water"] >= 200 and resources["coffee"] >= 24 and resources["milk"] >= 150:
                    print("Please insert your dimes")
                    argent_insere = proceess_coins()

                    cost = 2.5
                    if argent_insere >= cost:
                       change = round(argent_insere - cost, 2)
                       print(f"Here is ${change} in change.")
                       resources["water"] -= 200
                       resources["coffee"] -= 24
                       resources["milk"] -= 150
                    
                       print("Here it is your Latte ")
                    else:
                      print("Sorry that's not enough money. Money refunded.")
            else: 
                print("Sorry, there is not enough water or ingredients.") 


        elif user_input == "capuccino":
            if resources["water"] >= 250 and resources["coffee"] >= 24 and resources["milk"] >= 100:
                    print("Please insert your dimes")
                    argent_insere = proceess_coins()

                    cost = 3
                    if argent_insere >= 3:
                       change = round(argent_insere - cost, 2)
                       print(f"Here is ${change} in change.")
                       resources["water"] -= 250
                       resources["coffee"] -= 24
                       resources["milk"] -= 100
                       print("Here it is your Capucinno ")
                    else:
                       print("Sorry that's not enough money. Money refunded.")
            else: 
                print("Sorry, there is not enough water or ingredients.")

        elif user_input == "report":
            print(f"Here are the remaining ressources. : {resources}")

        else : 
            continue_game = False
            if user_input == "off":
                break
                   
coffee_machine()
# while input("Would you like another coffee y/n: ").lower() == "y":
#     print("\n" * 20)
#     coffee_machine()


