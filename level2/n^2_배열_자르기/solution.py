def solution(n, left, right):
    answer = []
    
    for i in range(left, right + 1):
        # index = row * i + col
        # 2차원 → 1차원: 각 행을 차례대로 이어붙임
        row = i // n
        col = i % n
        
        value = max(row, col) + 1
        answer.append(value)

    return answer