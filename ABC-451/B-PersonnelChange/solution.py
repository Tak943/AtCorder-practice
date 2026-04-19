N, M = map(int, input().split())
last_sem = [0] * M
this_sem = [0] * M
for _ in range(N): # for _ で繰り返し処理だけをやらせて、回数は関係ない
  i, j = map(int, input().split())
  last_sem[i-1] += 1
  this_sem[j-1] += 1
for i in range(M):
  print(this_sem[i] - last_sem[i])