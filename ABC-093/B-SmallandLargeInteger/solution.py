A, B, K = map(int, input().split())
ans = set()
for i in range(A, min(A+K, B+1)):
  ans.add(i)
for i in range(max(B-K+1, A), B+1):
  ans.add(i)
for x in ans:
  print(x)