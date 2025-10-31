from itertools import permutations

def solution(k, dungeons):
    max_count = 0
    
    for perm in permutations(dungeons):
        current_k = k
        count = 0
        
        for min_required, cost in perm:
            if current_k >= min_required:
                current_k -= cost
                count += 1
        
        max_count = max(max_count, count)
    
    return max_count