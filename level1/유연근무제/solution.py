def solution(schedules, timelogs, startday):
    # 상품을 받을 직원 수
    reward_count = 0
    
    # 각 직원별로 검사
    for i in range(len(schedules)):
        # 출근 희망 시각과 출근 인정 시각 계산
        desired_time = schedules[i]
        allowed_time = desired_time + 10
        
        if allowed_time % 100 >= 60:  # 분이 60분 이상이면 시간 조정
            allowed_time = (allowed_time // 100 + 1) * 100 + (allowed_time % 100 - 60)
        
        # 이 직원이 상품을 받을 수 있는지 여부
        is_eligible = True
        
        # 일주일 간의 출근 기록 확인
        for j in range(7):
            # 현재 요일 계산 (1:월, 2:화, 3:수, 4:목, 5:금, 6:토, 7:일)
            current_day = (startday + j - 1) % 7 + 1
            
            # 주말(토, 일)이면 건너뜀
            if current_day == 6 or current_day == 7:
                continue
            
            # 평일에 출근 시간이 늦었는지 확인
            if timelogs[i][j] > allowed_time:
                is_eligible = False
                break
        
        # 모든 평일에 늦지 않았으면 상품 받을 수 있음
        if is_eligible:
            reward_count += 1
    
    return reward_count