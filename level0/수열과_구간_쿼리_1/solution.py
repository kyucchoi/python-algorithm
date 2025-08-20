def solution(arr, queries):
    # 각 쿼리 처리
    for s, e in queries:
        # s부터 e까지의 인덱스에 대해
        for i in range(s, e + 1):
            arr[i] += 1
            
    return arr