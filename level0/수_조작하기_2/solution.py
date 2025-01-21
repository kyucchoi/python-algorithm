def solution(numLog):
   result = ''
   
   for i in range(1, len(numLog)):
       # 현재 값과 이전 값의 차이를 계산
       diff = numLog[i] - numLog[i - 1]
       
       # 차이에 따라 해당하는 문자 추가
       if diff == 1:
           result += 'w'
       elif diff == -1:
           result += 's'
       elif diff == 10:
           result += 'd'
       else:  # diff == -10
           result += 'a'
           
   return result