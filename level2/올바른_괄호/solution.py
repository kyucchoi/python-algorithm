def solution(s):
   count = 0  # 여는 괄호의 개수를 세는 변수
   
   for char in s:
       if char == '(':
           count += 1
       else:  # char == ')'
           count -= 1
       
       if count < 0:  # 닫는 괄호가 더 많은 경우
           return False
           
   return count == 0  # 모든 괄호가 짝이 맞으면 count는 0