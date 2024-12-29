def solution(array, commands):
   answer = []
   
   for i, j, k in commands:
       # 배열 자르기 (i-1부터 j까지)
       sliced = array[i - 1 : j]
       # 정렬
       sliced.sort()
       # k번째 수 추가
       answer.append(sliced[k - 1])
       
   return answer