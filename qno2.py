while True:
    print("Choose an option:")
    print("1. Find maximum and minimum between two numbers")
    print("2. Find maximum and minimum among three numbers")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if num1 > num2:
            max_num = num1
            min_num = num2
        else:
            max_num = num2
            min_num = num1

        print(f"The maximum number is {max_num}")
        print(f"The minimum number is {min_num}")

    elif choice == '2':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))

        max_num = max(num1, num2, num3)
        min_num = min(num1, num2, num3)

        print(f"The maximum number is {max_num}")
        print(f"The minimum number is {min_num}")

    elif choice == '3':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")