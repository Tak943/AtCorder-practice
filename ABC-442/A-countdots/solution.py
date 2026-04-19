ij = ["i", "j"]
n = 0
text = input()
text_words = list(text)
for i in range(len(text_words)):
  if text_words[i] in ij:
    n += 1
print(n)