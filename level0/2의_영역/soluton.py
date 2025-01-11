def solution(arr):
   # 2가 없는 경우
   if 2 not in arr:
       return [-1]
   
   # 처음과 마지막 2의 위치 찾기
   first = arr.index(2)  # 첫 번째 2의 위치
   last = len(arr) - arr[::-1].index(2) - 1  # 마지막 2의 위치
   
   # first부터 last까지의 부분 배열 반환
   return arr[first:last+1]