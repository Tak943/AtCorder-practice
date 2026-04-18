def query1(W, R):
  return R*W

def query2(H, C):
  return C*H 
  
H, W, Q = map(int, input().split())
choco = []
for i in range(Q):
  q, RC = map(int, input().split())
  if q == 1:
    choco.append(query1(W, RC))
    H -= RC
  elif q == 2:
    choco.append(query2(H, RC))
    W -= RC
for i in range(Q):
  print(choco[i])