def solution(progresses, speeds):
    answer = []
    days = []  # 각 기능의 완료까지 필요한 일수
    
    # 1. 각 기능별 필요한 일수 계산
    for p, s in zip(progresses, speeds):
        day = (100 - p + s - 1) // s  # 올림 계산
        days.append(day)
    
    # 2. 배포 가능한 기능 개수 계산
    count = 1
    max_day = days[0]
    
    for i in range(1, len(days)):
        if days[i] <= max_day:  # 이전 기능보다 일찍/같이 끝나는 경우
            count += 1
        else:  # 더 늦게 끝나는 경우
            answer.append(count)
            count = 1
            max_day = days[i]
    
    answer.append(count)  # 마지막 그룹 추가
    return answer