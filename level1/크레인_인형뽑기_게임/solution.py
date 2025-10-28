def solution(board, moves):
    basket = []
    removed = 0
    
    for move in moves:
        column = move - 1  # 인덱스는 0부터 시작하므로 1을 빼줌
        
        for row in range(len(board)):
            if board[row][column] != 0:
                doll = board[row][column]  # 인형 집기
                board[row][column] = 0  # 인형을 집었으므로 빈칸으로 만들기
                
                if basket and basket[-1] == doll:
                    basket.pop()  # 같은 인형이 있으면 제거
                    removed += 2
                else:
                    basket.append(doll)
                
                break
    
    return removed