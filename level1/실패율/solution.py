def solution(N, stages):
    # 1. 각 스테이지별 인원 수 세기
    from collections import Counter
    stage_count = Counter(stages)
    
    # 2. 실패율 계산
    total_players = len(stages)
    failure_rates = []
    
    for stage in range(1, N + 1):
        if total_players == 0:  # 도달한 사람이 없으면
            failure_rate = 0
        else:
            stuck = stage_count.get(stage, 0)
            failure_rate = stuck / total_players
            total_players -= stuck
        
        failure_rates.append((failure_rate, stage))
    
    # 3. 정렬 (실패율 내림차순, 같으면 스테이지 오름차순)
    failure_rates.sort(key=lambda x: (-x[0], x[1]))
    
    # 4. 스테이지 번호만 추출
    return [stage for _, stage in failure_rates]