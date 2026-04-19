T, X = map(int, input().split())
values = list(map(int, input().split()))
sensored_elements = {}
for t in range(T+1):
  if t == 0:
    sensored_elements["0"] = values[0]
    standard = values[0]
  else:
    if (standard + X) <= values[t] or values[t] <= (standard - X):
      sensored_elements[str(t)] = values[t]
      standard = values[t]
for key, value in sensored_elements.items():
  print(key, value)