def solution(arr, intervals):
   result = []
   
   # 첫 번째 구간 추가
   a1, b1 = intervals[0]
   result.extend(arr[a1:b1+1])
   
   # 두 번째 구간 추가
   a2, b2 = intervals[1]
   result.extend(arr[a2:b2+1])
   
   return result