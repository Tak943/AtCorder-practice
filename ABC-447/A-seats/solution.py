N, M = map(int, input().split())
seats = [0] * N
seats = [0] + seats + [0]
for i in range(1, N+1):
  if seats[i-1] == 0 and seats[i+1] == 0:
    seats[i] = 1
    M -= 1
if M <= 0:
  print("Yes")
else:
  print("No")