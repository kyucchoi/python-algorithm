def solution(a, b, c):
   # 세 숫자가 모두 같은 경우
   if a == b == c:
       return (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
   
   # 두 숫자만 같은 경우
   elif a == b or b == c or a == c:
       return (a + b + c) * (a**2 + b**2 + c**2)
   
   # 세 숫자가 모두 다른 경우
   else:
       return a + b + c