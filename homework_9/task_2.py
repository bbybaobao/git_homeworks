import random

random_dict = {f'k{i}': random.randint(1, 100) for i in range(20)}

print("Generated dictionary:")
print(random_dict)

product = 1
for value in random_dict.values():
    product *= value

print(f"The result of multiplying all numbers: {product}")
