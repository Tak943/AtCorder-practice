N = int(input())
if N < 1 or N > 9:
  print("input number 1 to 9")
else:
    while N != 1:
      print(N, end=",")
      N -= 1
    print(N)