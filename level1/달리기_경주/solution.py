def solution(players, callings):
    # 각 선수의 현재 등수를 저장하는 딕셔너리
    # rank_dict = {player: i for i, player in enumerate(players)}

    # 빈 딕셔너리 생성
    rank_dict = {}

    # enumerate를 사용하여 players 배열을 순회
    for i, player in enumerate(players):
        # 각 선수 이름을 키로, 인덱스(등수)를 값으로 딕셔너리에 저장
        rank_dict[player] = i
    
    # 각 호출에 대해 등수 변경 처리
    for call in callings:
        # 호출된 선수의 현재 등수
        current_rank = rank_dict[call]
        
        # 바로 앞선 선수
        front_player = players[current_rank - 1]
        
        # 등수 교환 (리스트에서)
        players[current_rank - 1], players[current_rank] = players[current_rank], players[current_rank - 1]
        
        # 등수 교환 (딕셔너리에서)
        rank_dict[call] = current_rank - 1
        rank_dict[front_player] = current_rank
    
    return players