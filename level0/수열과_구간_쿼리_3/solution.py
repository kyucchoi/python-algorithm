def solution(arr, queries):
    for i, j in queries:
        # arr[i]와 arr[j]의 값을 교환
        arr[i], arr[j] = arr[j], arr[i]
    
    return arr