#local scope 

def game():
    potion_one = 2
    print(potion_one)

game()

#Global scope 

potion_three = 12

def game_2():
    global potion_three #Ici on modifie la variable du scope avec global
    potion_three += 24
    print(potion_three)

game_2()

#No block scope in python

def is_prime(num):
    print(num)
    if num < 2:
        return False

    for i in range( 2, num):
        if num % i == 0:
            return False
    
    return True
print(is_prime(73))