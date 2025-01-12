def solution(arr, query):
   # query의 각 인덱스에 대해 처리
   for i in range(len(query)):
       if i % 2 == 0:  # 짝수 인덱스
           # query[i] + 1까지 남기고 뒷부분 자르기
           arr = arr[:query[i] + 1]
       else:  # 홀수 인덱스
           # query[i]부터 끝까지 남기기
           arr = arr[query[i]:]
   
   return arr