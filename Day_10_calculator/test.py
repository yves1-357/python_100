def format_name(f_name , l_name ):
    print(f_name.title())
    print(l_name.title())

format_name("Sara", "sara")


def is_leap_year(year):
    if year % 400 == 0:
        print(f"{year}")
        return True 
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        print(f"{year}")
        return True
    else :
        return False

is_leap_year(1989)
print(is_leap_year(1989))
