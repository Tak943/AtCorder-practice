import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
  a, b = map(int, input().split())
  g[a-1] += [b-1]
q = deque()# 訪問した頂点を保存queue
d = [False for _ in range(n)]# 訪問済みかどうか
q.append(0)
d[0] = True # 頂点1すなわちindex 0 をqに入れて訪問済みにする
while q:# qがなくなるまで繰り返し
  x = q.popleft()# qから取り出し訪問
  for i in g[x]:
    if d[i]:
      continue # 訪問済みならスルー
    d[i] = True
    q.append(i)# 未訪問なら訪問済みにしてqueueに保存
print(sum(d))