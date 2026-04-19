N, M = map(int, input().split())
clothes = list(map(int, input().split()))
total_clothes = [i for i in range(1,M+1)]
quest1 = "Yes"
for i in range(N-1):
  for j in range(i+1,N):
    if clothes[i] == clothes[j]:
      quest1 = "No"
      break
print(quest1)
quest2 = "Yes"
for i in total_clothes:
  if i not in clothes:
    quest2 = "No"
    break
print(quest2)