def solution(score):
    # 각 학생의 평균 점수 계산
    averages = [(eng + math) / 2 for eng, math in score]
    
    # 평균 점수를 내림차순으로 정렬 (중복 제거)
    sorted_averages = sorted(set(averages), reverse=True)
    
    # 각 평균 점수에 대한 등수 매핑
    rank_map = {}
    current_rank = 1
    
    for avg in sorted_averages:
        rank_map[avg] = current_rank
        # 해당 평균을 가진 학생 수만큼 다음 등수 증가
        count = averages.count(avg)
        current_rank += count
    
    # 각 학생의 등수 반환
    return [rank_map[avg] for avg in averages]