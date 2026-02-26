# 방법 1
def solution(k, tangerine):
    count_dict = {}
    
    for size in tangerine:
        count_dict[size] = count_dict.get(size, 0) + 1
    
    sorted_counts = sorted(count_dict.values(), reverse=True)
    
    selected = 0
    types = 0
    
    for cnt in sorted_counts:
        selected += cnt
        types += 1
        
        if selected >= k:
            break
    
    return types

# 방법 2
def solution(k, tangerine):
    from collections import Counter
    
    count = Counter(tangerine)
    
    sorted_counts = sorted(count.values(), reverse=True)
    
    selected = 0
    types = 0
    
    for cnt in sorted_counts:
        selected += cnt
        types += 1
        
        if selected >= k:
            break
    
    return types