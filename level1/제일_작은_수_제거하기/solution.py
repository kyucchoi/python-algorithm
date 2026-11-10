# remove 함수 사용
def solution(arr):
    if len(arr) == 1:
        return [-1]

    arr.remove(min(arr))

    return arr

# 리스트 컴프리헨션 방법
def solution(arr):
    if len(arr) == 1:
        return [-1]

    min_value = min(arr)
    answer = []

    for num in arr:
        if num != min_value:
            answer.append(num)

    return answer