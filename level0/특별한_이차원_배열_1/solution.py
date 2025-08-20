def solution(n):
    # n x n 크기의 0으로 채워진 2차원 배열 생성
    arr = [[0] * n for _ in range(n)]
    
    # 대각선(i == j)에 1 넣기
    for i in range(n):
        arr[i][i] = 1
        
    return arr