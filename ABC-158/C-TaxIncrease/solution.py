A, B = map(int, input().split())
ans = -1
for i in range(10000):
  a = i * 8 // 100
  b = i * 10 // 100
  if a == A and b == B:
    ans = i
    break
print(ans)