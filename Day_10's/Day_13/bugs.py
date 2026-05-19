def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it ")

my_function()

try:
    age = int(input("How old r u "))

except ValueError:
    print("You have typed a invalid number")
    age = int(input("How old r u "))
if age > 18:
    print(f"You can drive at age {age}")