N = int(input("How many students: "))
K = int(input("Apple quantity: "))

apples_per_student = K // N
apples_left = K % N

print(f"Each student got an apple: {apples_per_student}")
print(f"Apples left in the basket: {apples_left}")
