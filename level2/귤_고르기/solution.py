def solution(k, tangerine):
    # 수동으로 개수 세기
    count_dict = {}
    
    for size in tangerine:
        count_dict[size] = count_dict.get(size, 0) + 1
    
    # 개수를 기준으로 내림차순 정렬
    sorted_counts = sorted(count_dict.values(), reverse=True)
    
    selected = 0
    types = 0
    
    for cnt in sorted_counts:
        selected += cnt
        types += 1
        
        if selected >= k:
            break
    
    return types