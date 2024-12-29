def solution(a, d, included):
   result = 0
   
   for i in range(len(included)):
       # i번째 항 계산 (첫 항 a에서 공차 d를 i번 더함)
       num = a + (d * i)
       
       # included[i]가 True인 경우에만 더하기
       if included[i]:
           result += num
           
   return result