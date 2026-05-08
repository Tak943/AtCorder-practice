N = int(input())
d = list(map(int, input().split()))
d.sort(reverse = True)
i = N // 2
if d[i-1] == d[i]:
  ans = 0
else:
  ans = d[i-1] - d[i]
print(ans)