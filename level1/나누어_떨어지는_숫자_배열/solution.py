# 방법 1
def solution(arr, divisor):
    result = []
    
    for num in arr:
        if num % divisor == 0:
            result.append(num)
    
    if not result:
        return [-1]
    
    return sorted(result)

# 방법 2
def solution(arr, divisor):
    answer = []

    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])

    return sorted(answer) if answer else [-1]