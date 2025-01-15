def solution(arr):
   count = 0
   
   while True:
       # 현재 배열을 복사해서 저장
       prev = arr.copy()
       
       # 각 원소를 조건에 따라 변환
       for i in range(len(arr)):
           if arr[i] >= 50 and arr[i] % 2 == 0:  # 50 이상 짝수
               arr[i] //= 2
           elif arr[i] < 50 and arr[i] % 2 == 1:  # 50 미만 홀수
               arr[i] = arr[i] * 2 + 1
       
       # 이전 배열과 현재 배열이 같으면 종료
       if prev == arr:
           return count
           
       count += 1