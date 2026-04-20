n = int(input())
text = list(input())
words = []
i = 0
while i != n:
  if text[i] == "o":
    i += 1
  else:
    words += text[i:]
    break
print("".join(words))