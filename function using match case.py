a=5
b=4
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def divided(a,b):
    return a/b

ch=int(input("Enter your choice "))
match ch:
    case 1:print(add(a,b))
    case 2:print(sub(a,b))
    case 3:print(multiplication(a,b))
    case 4:print(divided(a,b))
    case _:exit()