from collections import Counter

def solution(N, stages):
    stage_count = Counter(stages)
    
    total_players = len(stages)
    failure_rates = []
    
    for stage in range(1, N + 1):
        if total_players == 0:
            failure_rate = 0
        else:
            stuck = stage_count.get(stage, 0)
            failure_rate = stuck / total_players
            total_players -= stuck
        
        failure_rates.append((failure_rate, stage))
    
    failure_rates.sort(key=lambda x: (-x[0], x[1]))
    
    return [stage for _, stage in failure_rates]