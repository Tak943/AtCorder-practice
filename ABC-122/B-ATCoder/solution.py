text = input()
acgt = ["A", "C", "G", "T"]
ans = 0
cnt = 0
for i in text:
  if i in acgt:
    cnt += 1
    ans = max(ans, cnt)
  else:
    cnt = 0
print(ans)