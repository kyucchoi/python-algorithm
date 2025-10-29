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
    
    for num in arr:
        if not answer:
            answer.append(num)
        elif num != answer[-1]:
            answer.append(num)
    
    return answer