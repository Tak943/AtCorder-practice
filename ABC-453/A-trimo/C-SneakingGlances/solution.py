N = int(input())
L = list(map(int, input().split()))
ans = 0
count0 = 0
for i in range(1 << N): # 2^N通りのパターンを全て試す
  # 各パターンについてシミュレーション
  pos = 1 # 位置を整数にして小数の誤差によるエラーを防ぐ
  count0 = 0 # このパターンで何回0をまたいだか
  for j in range(N):
    next_pos = pos
    move = L[j] * 2 # 移動も2倍
    if (i >> j) & 1:
      next_pos += move
    else:
      next_pos -= move
    if (next_pos < 0 and pos > 0) or (next_pos > 0 and pos < 0):
      count0 += 1
    pos = next_pos
  ans = max(ans, count0)
print(ans)