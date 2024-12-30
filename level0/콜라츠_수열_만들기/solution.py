def solution(n):
   answer = [n]  # 시작 숫자를 먼저 리스트에 추가
   
   while n != 1:  # n이 1이 될 때까지 반복
       if n % 2 == 0:  # 짝수일 때
           n = n // 2
       else:  # 홀수일 때
           n = 3 * n + 1
       answer.append(n)  # 계산된 숫자를 리스트에 추가
       
   return answer