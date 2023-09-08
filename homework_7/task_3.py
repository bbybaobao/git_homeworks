list1 = [1, 2, 5, 7, 9, 99, 87, 200, 39, 2]
list2 = [5, 42, 29, 345, 50, 33, 7, 0, 201, 9, 2, 132, 45, 23, 934]

count1 = {}
count2 = {}

for number in list1:
    if number in count1:
        count1[number] += 1
    else:
        count1[number] = 1

for number in list2:
    if number in count2:
        count2[number] += 1
    else:
        count2[number] = 1

print("{:<10} {:<10} {:<10}".format("Numbers", "List 1", "List 2"))
for number in count1.keys():
    print("{:<10} {:<10} {:<10}".format(number, count1.get(number, 0), count2.get(number, 0)))
