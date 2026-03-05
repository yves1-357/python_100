from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#objet instanciation

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

continue_game = True
while continue_game:
    user_input = str(input("What would you like : espresso/latte/cappuccino :  ")).lower()
    if user_input == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_input == "off":
        continue_game = False 

    else:
        drink = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
            
    
    





 