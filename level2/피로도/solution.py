from itertools import permutations

def solution(k, dungeons):
    
    max_count = 0
    
    # 모든 가능한 던전 순서를 생성
    for perm in permutations(dungeons):
        current_fatigue = k  # 현재 피로도 초기화
        count = 0           # 탐험한 던전 수
        
        # 이 순서로 던전을 하나씩 탐험해보기
        for min_required, consume in perm:
            if current_fatigue >= min_required:  # 탐험 가능?
                current_fatigue -= consume       # 피로도 소모
                count += 1                      # 탐험 수 증가
            else:
                break  # 더 이상 탐험 불가능하면 중단
        
        # 최대 탐험 수 업데이트
        max_count = max(max_count, count)
    
    return max_count