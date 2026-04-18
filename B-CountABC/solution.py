N = int(input())
text = input()
n = 0
for i in range(N-1):
  if text[i:i+3] == "ABC":
    n += 1
print(n)