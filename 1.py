# WAP to enter your name,age,gender,address,contact and email address in the file "info.txt" and display only name and email address.

name = input("Enter your name: ")
age = input("Enter your age: ")
gender = input("Enter your gender: ")
address = input("Enter your address: ")
contact = input("Enter your contact number: ")
email = input("Enter your email address: ")


with open("info.txt", "w") as file:
    file.write(f"Name: {name}\nAge: {age}\nGender: {gender}\nAddress: {address}\nContact: {contact}\nEmail: {email}")


with open("info.txt", "r") as file:
    for line in file:
        if line.startswith("Name") or line.startswith("Email"):
            print(line.strip())