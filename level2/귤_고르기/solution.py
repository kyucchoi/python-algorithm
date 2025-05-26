# 방법 1
def solution(k, tangerine):
    # 수동으로 개수 세기
    count_dict = {}
    
    for size in tangerine:
        count_dict[size] = count_dict.get(size, 0) + 1
    
    # 개수를 기준으로 내림차순 정렬
    sorted_counts = sorted(count_dict.values(), reverse = True)
    
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
    
    # 각 크기별 개수 세기
    count = Counter(tangerine)
    
    # 개수를 기준으로 내림차순 정렬
    sorted_counts = sorted(count.values(), reverse = True)
    
    selected = 0  # 선택한 귤의 개수
    types = 0     # 사용한 크기 종류의 수
    
    for cnt in sorted_counts:
        selected += cnt
        types += 1
        
        # k개 이상 선택했으면 종료
        if selected >= k:
            break
    
    return types