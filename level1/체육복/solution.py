def solution(n, lost, reserve):
    lost_only = set(lost) - set(reserve)
    reserve_only = set(reserve) - set(lost)
    
    answer = n - len(lost_only)
    
    lost_only = sorted(lost_only)
    
    for student in lost_only:
        if student - 1 in reserve_only:
            reserve_only.remove(student - 1)
            answer += 1
        elif student + 1 in reserve_only:
            reserve_only.remove(student + 1)
            answer += 1
    
    return answer