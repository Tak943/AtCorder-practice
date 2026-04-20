text = input()
text_words = set(text)
list_text = list(text)
dict = {}
max_count = 0
for i in text_words:
  dict[i] = text.count(i)
  max_count = max(max_count, dict[i])
for k, v in dict.items():
  if v == max_count:
    for i in range(len(list_text)):
      if list_text[i] == k:
        list_text[i] = ""
print("".join(list_text))