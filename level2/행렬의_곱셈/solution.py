def solution(arr1, arr2):
    # arr1의 크기: m x n, arr2의 크기: n x p
    # 결과 행렬의 크기: m x p
    m = len(arr1)      # arr1의 행 개수
    n = len(arr1[0])   # arr1의 열 개수 (= arr2의 행 개수)
    p = len(arr2[0])   # arr2의 열 개수
    
    # 결과 행렬 초기화
    result = [[0] * p for _ in range(m)]
    
    # 행렬 곱셈 수행
    for i in range(m):        # 결과 행렬의 행
        for j in range(p):    # 결과 행렬의 열
            for k in range(n):  # 내적 계산
                result[i][j] += arr1[i][k] * arr2[k][j]
    
    return result