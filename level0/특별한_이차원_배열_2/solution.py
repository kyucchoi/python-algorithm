def solution(arr):
    n = len(arr)  # 행렬의 크기
    
    # 모든 위치 쌍을 확인
    for i in range(n):
        for j in range(n):
            if arr[i][j] != arr[j][i]:
                return 0
                
    return 1