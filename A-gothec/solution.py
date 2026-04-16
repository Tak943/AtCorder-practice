days = [(1,7), (3,3), (7,7), (5,5), (9,9)]
m, d = map(int, input().split())
if ((m,d) in days):
  print("Yes")
else:
  print("No")