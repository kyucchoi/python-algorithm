def solution(board, moves):
    basket = []
    removed = 0
    
    for move in moves:
        column = move - 1
        
        for row in range(len(board)):
            if board[row][column] != 0:
                doll = board[row][column]
                board[row][column] = 0
                
                if basket and basket[-1] == doll:
                    basket.pop()
                    removed += 2
                else:
                    basket.append(doll)
                
                break
    
    return removed