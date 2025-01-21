def solution(my_string, m, c):
   result = ''
   
   # m개씩 나누었을 때 c번째 문자들 추출
   for i in range(c - 1, len(my_string), m):
       result += my_string[i]
       
   return result