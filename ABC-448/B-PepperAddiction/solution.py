N, M = map(int, input().split())
shop_pep = list(map(int, input().split()))
item_pep = [0]*M
for i in range(N):
  a, b = map(int, input().split())
  item_pep[a-1] += b
max = 0
for i in range(M):
  if shop_pep[i] < item_pep[i]:
    max += shop_pep[i]
  else:
    max += item_pep[i]
print(max)