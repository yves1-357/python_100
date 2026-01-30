print("Welcome to the tip calcultor")
bill = float(input("What as the total bill : "))
tip = int(input("How much tip would you like to give between (10, 12, 15): "))
split = int(input("How many people split the bill: "))

pay = bill * (1 + tip/100)
pay_person = pay / split
print(f"Each person should pay : {round(pay_person)}")