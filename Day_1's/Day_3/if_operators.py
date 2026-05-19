condition = 1
if condition:
    print("do this")
else:
    print("do this")

not 5 == 5

print("Welcome to python pizza deliveries")
size = input("What size pizza do you want ? S,M,L : ")
if size == "s":
    pepperoni = input("Do you want pepperoni on your pizza? type: Y/n : ")
    price = 15
    if pepperoni == "y":
        price += 2
    extra_cheese = input("Do you want extra cheese on your pizza? type: Y/n : ")
    if extra_cheese == "y":
        price += 1
    print(f"your total bill is : {price}")
elif size == "m":
    pepperoni = input("Do you want pepperoni on your pizza? type: Y/n : ")
    price = 20
    if pepperoni == "y":
        price += 3
    extra_cheese = input("Do you want extra cheese on your pizza? type: Y/n : ")
    if extra_cheese == "y":
        price += 1
    print(f"your total bill is : {price}")  
elif size == "l":
    pepperoni = input("Do you want pepperoni on your pizza? type: Y/n : ")
    price = 25
    if pepperoni == "y":
        price += 3
    extra_cheese = input("Do you want extra cheese on your pizza? type: Y/n : ")
    if extra_cheese == "y":
        price += 1
    print(f"your total bill is : {price}") 
else:
    print("You typed a wrong letter")

print("Welcome roller coaster")
height = int(input("Enter your height : "))
if height >= 120:
    print("Can ride")
    age = int(input("Enter your Age : "))
    price = 5
    if age <= 12:
        price = 5
        print(f"You have to pay {price}$")
    elif age >= 12 and age <= 18:
        price += 2
        print(f"You have to pay {price}$")
    elif age >= 45 and age <= 55:
        price = 0
        print("Your ride is free ")
    else:
        price += 7
        print(f"You have to pay {price}$")
    pictures = str(input("You want any pictures : Yes/No :  "))
    if pictures == "Yes" :
        print("3$ will be added to your total bill")
        price += 3
    print(f"Your total bill is {price}")

else:
    print("can't ride")

print("Welcome to the modulo")
number = int(input("Ecrivez un nombre pour verification : "))
if number % 2 == 0:
    print("Pair")
else:
    print("impair")
