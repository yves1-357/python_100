# Unlimited arguments

# def add(*args): #arguments / *:accepts any number of arguments, tuple form
#     for n in args:
#         print(n)


#kwargs : many : keyword arguments 

def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3, 5, 12))

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)
def test(*args):
    print(args)
 
test(1,2,3,5)