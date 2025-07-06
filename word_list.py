word_list = []

with open("valid-wordle-words.txt", "r") as file:
    for line in file:
        word = line.strip().lower()
        if len(word) == 5:
            word_list.append(word)