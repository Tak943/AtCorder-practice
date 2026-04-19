p, q = map(int, input().split())
x, y = map(int, input().split())
if p <= x and x <= p+99:
  if q <= y and y <= q+99:
    print("Yes")
  else: 
    print("No")
else:
  print("No")