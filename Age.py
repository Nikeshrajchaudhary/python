'''age = int(input("Enter the age:"))
if age<=10:
    print("Children")
elif age>10 and age<=20:   
    print("Teen")
elif age>20 and age<=50:
    print("Adult")
else:
    print("Old")
'''

age = int(input("Enter the age:"))
if age in range(1,11):
    print("Children")
elif age in range(11,21):
    print("Teen")
elif age in range(21,50):
    print("Adult")
else:
    print("Old")