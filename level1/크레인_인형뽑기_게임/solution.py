def solution(board, moves):
    basket = []  # 인형을 담을 바구니
    removed = 0  # 터트려진 인형 개수
    
    for move in moves:
        column = move - 1  # 인덱스는 0부터 시작하므로 1을 빼줌
        
        # 해당 열에서 가장 위에 있는 인형 찾기
        for row in range(len(board)):
            # 인형을 발견하면
            if board[row][column] != 0:
                doll = board[row][column]  # 인형 집기
                board[row][column] = 0  # 인형을 집었으므로 빈칸으로 만들기
                
                # 바구니에 같은 인형이 있는지 확인
                if basket and basket[-1] == doll:
                    basket.pop()  # 같은 인형이 있으면 제거
                    removed += 2  # 두 인형이 사라짐
                else:
                    basket.append(doll)  # 다른 인형이면 바구니에 추가
                
                break  # 인형을 찾았으므로 다음 move로 넘어감
    
    return removed