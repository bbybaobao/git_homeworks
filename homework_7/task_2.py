sentence = input("Enter a sentence: ")

words = sentence.split(" ")

words = [word for word in words if word.strip() != ""]

words.sort()

print("Index\tWord")
for index, word in enumerate(words):
    print(f"{index}\t{word}")

print(f"Word count: {len(words)}")
