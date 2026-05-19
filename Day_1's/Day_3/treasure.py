print("Welcome to treasure island")
print("Your mission is to find the treasure")
choice = input("You're at cross road. Where do  you want to go ? Left/ Right : ").lower()
if choice == "Right":
    print("Game Over")
elif choice == "left":
    swim = input("Do you want to swim or wait: Type swim/wait : ").lower()
    if swim == "swim":
         print("Game over")
    elif swim == "wait":
        door = input("Which door do you want to go too : Red/blue/Yellow : ").lower()
        if door == "blue" or door == "Red":
              print("Game over")
        else:
             print("Congrats, You win ")
else:
     print("You typed the worng letter")