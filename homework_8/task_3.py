import random

random_numbers = [random.randint(1, 100) for _ in range(15)]

sum_odd = sum(x for x in random_numbers if x % 2 != 0)
sum_even = sum(x for x in random_numbers if x % 2 == 0)

print("List of random numbers:", random_numbers)

if sum_odd > sum_even:
    print("Yes")
else:
    print("No")
