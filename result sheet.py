name = input("Enter your name:")
print(name)
id = input("Enter your student ID:")
print(id)
skill = int(input("Enter the marks:"))
print(skill)
programming = int(input("Enter the marks:"))
print(programming)
operating = int(input("Enter the marks:"))
print(operating)
pen = int(input("Enter the marks:"))
print(pen)
res=(skill+programming+operating+pen)/4
if skill>40 and programming>40 and operating>40 and pen>40:
    if res >=70 :
        print("Frist class")
    elif res >=50 and res <70 :
        print("upper class")
    elif res >=40 and res <50 :
        print("lower class")
    elif res<40 :
        print("fail")
else:
    print("fail")
    
    

