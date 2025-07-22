def solution(emergency):
    # 응급도를 내림차순으로 정렬 (높은 순서)
    sorted_emergency = sorted(emergency, reverse = True)
    
    # 각 응급도의 순위를 매핑
    rank_map = {}

    for i, value in enumerate(sorted_emergency):
        rank_map[value] = i + 1  # 순위는 1부터 시작
    
    # 원래 배열의 각 원소에 해당하는 순위 반환
    result = []

    for value in emergency:
        result.append(rank_map[value])
    
    return result