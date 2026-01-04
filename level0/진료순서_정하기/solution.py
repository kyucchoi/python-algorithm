def solution(emergency):
    sorted_emergency = sorted(emergency, reverse=True)
    
    rank_map = {}

    for i, value in enumerate(sorted_emergency):
        rank_map[value] = i + 1
    
    result = []

    for value in emergency:
        result.append(rank_map[value])
    
    return result