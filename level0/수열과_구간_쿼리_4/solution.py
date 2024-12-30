def solution(arr, queries):
   for s, e, k in queries:
       # s부터 e까지 반복
       for i in range(s, e + 1):
           # i가 k의 배수인 경우 (k가 0이 아닐 때)
           if k != 0 and i % k == 0:
               arr[i] += 1
   
   return arr