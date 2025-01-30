def solution(a, b):
   # 두 수가 모두 홀수인 경우
   if a % 2 == 1 and b % 2 == 1:
       return a**2 + b**2
       
   # 하나만 홀수인 경우
   elif a % 2 == 1 or b % 2 == 1:
       return 2 * (a + b)
       
   # 둘 다 짝수인 경우
   else:
       return abs(a - b)