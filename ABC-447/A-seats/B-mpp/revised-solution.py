text = input()
count_words = {word: text.count(word) for word in text}
M = max(count_words.values())
print("".join(word for word in text if count_words[word] != M))