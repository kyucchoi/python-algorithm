def solution(array):
    frequency = {}

    for num in array:
        frequency[num] = frequency.get(num, 0) + 1
    
    max_count = max(frequency.values())
    
    mode_candidates = []
    
    for num, count in frequency.items():
        if count == max_count:
            mode_candidates.append(num)
    
    if len(mode_candidates) == 1:
        return mode_candidates[0]
    else:
        return -1