num1 = int(input("Enter the number:"))
num2 = int(input("Enter the number:"))
num3 = int(input("Enter the number:"))

if num1>num2 and num1>num3:
    print("First num is largest", num1)
elif num2>num1 and num2>num3:
    print("Second num is largest", num2)
else:
    print("Third num is largest", num3)
