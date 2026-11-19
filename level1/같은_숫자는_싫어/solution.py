# 방법 1
def solution(arr):
    answer = []

    for num in arr:
        if not answer or answer[-1] != num:
            answer.append(num)

    return answer

# 방법 2
def solution(arr):
    answer = [arr[0]]

    for num in arr[1:]:
        if answer[-1] != num:
            answer.append(num)
            
    return answer