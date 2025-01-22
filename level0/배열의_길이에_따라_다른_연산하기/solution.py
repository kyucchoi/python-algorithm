def solution(arr, n):
   # arr의 길이가 홀수인 경우, 짝수 인덱스에 n 더하기
   if len(arr) % 2 == 1:
       for i in range(0, len(arr), 2):
           arr[i] += n
           
   # arr의 길이가 짝수인 경우, 홀수 인덱스에 n 더하기
   else:
       for i in range(1, len(arr), 2):
           arr[i] += n
           
   return arr