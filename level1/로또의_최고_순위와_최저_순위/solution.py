def solution(lottos, win_nums):
    # 순위 매핑 (맞힌 갯수 -> 순위)
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    
    # 당첨 번호와 일치하는 번호 개수 계산
    match_count = 0
    zero_count = 0
    
    for num in lottos:
        if num == 0:
            zero_count += 1  # 알아볼 수 없는 번호 개수
        elif num in win_nums:
            match_count += 1  # 당첨 번호와 일치하는 번호 개수
    
    # 최고 순위: 모든 0이 당첨 번호와 일치한다고 가정
    max_match = match_count + zero_count
    
    # 최저 순위: 모든 0이 당첨 번호와 일치하지 않는다고 가정
    min_match = match_count
    
    # 순위 반환
    return [rank[max_match], rank[min_match]]