def longest_words(file):
    max_length = 0
    longest_w = []

    with open(file, 'r') as f:
        for line in f:
            for word in line.split():
                word = ''.join(filter(str.isalpha, word))
                length = len(word)
                if length > max_length:
                    max_length = length
                    longest_w = [word]
                elif length == max_length:
                    longest_w.append(word)

    return longest_w


file_path = 'article.txt'
longest_words_list = longest_words(file_path)
print('Longest words:', longest_words_list)
