class1 = int(input("Enter the number of students in the 1st class: "))
class2 = int(input("Enter the number of students in the 2nd class: "))
class3 = int(input("Enter the number of students in the 3rd class: "))

total_students = class1 + class2 + class3

desks = (total_students + 1) // 2

print(f"You need to purchase {desks} desks.")
