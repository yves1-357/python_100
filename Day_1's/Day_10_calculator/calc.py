logo = """
 _____________________
|  _________________  |
| | Python Calc    | |
| |_________________| |
...
"""
def calculator():
    print(logo)
    def add(n1, n2):
        return n1 + n2
    
    def subtract(n1, n2):
        return n1 - n2
    
    def multiply(n1, n2):
        return n1 * n2
    
    def divide(n1, n2):
        return n1 / n2
    operations = {
        "+" : add,
        "-" : subtract,
        "*" : multiply,
        "/" : divide,
        }
    user = int(input("Type first number : "))
    symbol = input("Choose an  opération (+, -, *, /) : ")
    user_1 = int(input("Type second number : "))
    calcul_function = operations[symbol]
    result = calcul_function(user, user_1)
    print(f"{user} {symbol} {user_1} = {result}")
    continue_1 = True

    while continue_1:
        user_3 = input("Do you want to continue with previous result : Type Y or N : ").lower()
        if user_3 == "y":
            symbol = input("Choose an  opération (+, -, *, /) : ")
            user_4 = int(input("Type second number : "))
            calcul_function = operations[symbol]
            result_2 = calcul_function(result, user_4)
            print(f"{result} {symbol} {user_4} = {result_2}")
            result = result_2
        else:
            continue_1 = False
            calculator()
calculator()

