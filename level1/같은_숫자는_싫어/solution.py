# 방법 1
def solution(arr):
   result = []  # 결과를 저장할 리스트
   
   for num in arr:
       # result가 비어있거나, 마지막 숫자와 현재 숫자가 다르면
       if not result or result[-1] != num:
           result.append(num)
           
   return result

# 방법 2
def solution(arr):
    answer = []
    
    # 첫 번째 원소는 항상 결과 배열에 추가
    answer.append(arr[0])
    
    # 두 번째 원소부터 비교하여 이전 원소와 다른 경우에만 추가
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:  # 현재 원소가 이전 원소와 다르면
            answer.append(arr[i])  # 결과 배열에 추가
    
    return answer