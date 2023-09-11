import string

text = """
Любіть Україну, як сонце любіть,
як вітер, і трави, і води...
В годину щасливу і в радості мить,
любіть у годину негоди.
Любіть Україну у сні й наяву,
вишневу свою Україну,
красу її, вічно живу і нову,
і мову її солов'їну.
Без неї — ніщо ми, як порох і дим,
розвіяний в полі вітрами...
Любіть Україну всім серцем своїм
і всіми своїми ділами.
"""

translator = str.maketrans('', '', string.punctuation)
text = text.lower().translate(translator)

words = text.split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

most_common_word = max(word_count, key=word_count.get)
most_common_count = word_count[most_common_word]

least_common_word = min(word_count, key=word_count.get)
least_common_count = word_count[least_common_word]

print(f"The word that appears most often: '{most_common_word}' ({most_common_count} time)")
print(f"The word '{least_common_word}' appears {least_common_count} time (least of all).")