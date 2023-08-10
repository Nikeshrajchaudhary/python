# WAP to enter name, occupation and address for 10 employees and display all the records.
 
employee_records = []
for i in range(2):
    name = input("Enter your name of employee{}: ".format(i+1))
    occupation = input("Enter your occupation employee{}: ".format(i+1))
    address = input("Enter your address employee{}: ".format(i+1))
    employee = {'name': name, 'occupation': occupation, 'address': address}
    employee_records.append(employee)

print("\nEmployee Records:")
for employee in employee_records: 
    for i in range(2):
        print("Name of employee {}: ".format(i+1), employee['name'])
        print("Occupation of employee {}: ".format(i+1), employee['occupation'])
        print("Address of employee {}: ".format(i+1), employee['address'])
        print()