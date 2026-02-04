def solution(lottos, win_nums):
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    
    match_count = 0
    zero_count = 0
    
    for num in lottos:
        if num == 0:
            zero_count += 1
        elif num in win_nums:
            match_count += 1
    
    max_match = match_count + zero_count
    
    min_match = match_count
    
    return [rank[max_match], rank[min_match]]