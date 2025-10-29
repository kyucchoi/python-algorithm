# 방법 1
def solution(progresses, speeds):
    days = []
    
    # 1. 각 기능별 필요한 일수 계산
    for p, s in zip(progresses, speeds):
        day = (100 - p + s - 1) // s  # 올림 계산
        days.append(day)
    
    # 2. 배포 가능한 기능 개수 계산
    answer = []
    count = 1
    max_day = days[0]
    
    for i in range(1, len(days)):
        if days[i] <= max_day:
            count += 1
        else:
            answer.append(count)
            count = 1
            max_day = days[i]
    
    answer.append(count)  # 마지막 그룹 추가

    return answer

# 방법 2
import math

def solution(progresses, speeds):
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    
    answer = []
    current_max = days[0]
    count = 1
    
    for i in range(1, len(days)):
        if days[i] <= current_max:
            count += 1
        else:
            answer.append(count)
            count = 1
            current_max = days[i]
    
    answer.append(count)
    
    return answer