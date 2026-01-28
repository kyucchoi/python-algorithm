# 방법 1
def solution(arr):
    result = []
    
    for num in arr:
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