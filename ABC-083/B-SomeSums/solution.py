# 整数の各桁の和を求める関数
def calc_sum_digits(n):
  sum_digit = 0
  while n > 0:
    sum_digit += n % 10
    n //= 10
  return sum_digit

N, A, B = map(int, input().split())
ans = 0
for i in range(1, N+1):
  if A <= calc_sum_digits(i) <= B: 
    ans += i
print(ans)