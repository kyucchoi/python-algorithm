def solution(num_list):
   total_count = 0
   
   for num in num_list:
       while num > 1:  # 1이 될 때까지 반복
           if num % 2 == 0:  # 짝수
               num //= 2
           else:  # 홀수
               num = (num - 1) // 2
           total_count += 1
           
   return total_count