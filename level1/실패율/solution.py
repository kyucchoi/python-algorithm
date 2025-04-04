def solution(N, stages):
    # 각 스테이지에 머물러 있는 사용자 수 계산
    stage_counts = [0] * (N + 2)  # 인덱스 1부터 N까지 사용, 0번과 N + 1번은 편의상 추가

    # 초기값 : stage_counts = [0, 0, 0, 0, 0, 0, 0]

    for stage in stages:
        stage_counts[stage] += 1

        # stages = [2, 1, 2, 6, 2, 4, 3, 3]을 처리하면
        # stage_counts[2] += 1 (3번 발생)
        # stage_counts[1] += 1 (1번 발생)
        # stage_counts[6] += 1 (1번 발생)
        # stage_counts[4] += 1 (1번 발생)
        # stage_counts[3] += 1 (2번 발생)
    
    # 각 스테이지에 도달한 사용자 수 계산
    reached_users = len(stages)

    # reached_users = 8
    
    # 각 스테이지의 실패율 계산
    failure_rates = []

    for i in range(1, N + 1):
        # 해당 스테이지에 도달한 사용자가 없는 경우 실패율은 0
        if reached_users == 0:
            failure_rate = 0
        else:
            failure_rate = stage_counts[i] / reached_users

            # i = 1 : failure_rate = 1 / 8 = 0.125 (8명이 도달하고 1명이 머물러 있음)
            # i = 2 : failure_rate = 3 / 7 = 0.429 (7명이 도달하고 3명이 머물러 있음)
            # i = 3 : failure_rate = 2 / 4 = 0.5 (4명이 도달하고 2명이 머물러 있음)
            # i = 4 : failure_rate = 1 / 2 = 0.5 (2명이 도달하고 1명이 머물러 있음)
            # i = 5 : failure_rate = 0 / 1 = 0 (1명이 도달하고 0명이 머물러 있음)
        
        failure_rates.append((i, failure_rate))

        # failure_rates = [(1, 0.125), (2, 0.429), (3, 0.5), (4, 0.5), (5, 0)]
        
        # 다음 스테이지 계산을 위해 현재 스테이지에 있는 사용자 수 빼기
        reached_users -= stage_counts[i]

        # i = 1 후 : reached_users = 8 - 1 = 7
        # i = 2 후 : reached_users = 7 - 3 = 4
        # i = 3 후 : reached_users = 4 - 2 = 2
        # i = 4 후 : reached_users = 2 - 1 = 1
        # i = 5 후 : reached_users = 1 - 0 = 1
    
    # 실패율에 따라 스테이지 번호 내림차순 정렬
    # 실패율이 같은 경우 스테이지 번호 오름차순으로 정렬
    failure_rates.sort(key = lambda x: (- x[1], x[0]))

    # 정렬 전 : [(1, 0.125), (2, 0.429), (3, 0.5), (4, 0.5), (5, 0)]
    # 정렬 후 : [(3, 0.5), (4, 0.5), (2, 0.429), (1, 0.125), (5, 0)]
    
    # 정렬된 스테이지 번호만 추출
    result = [stage for stage, _ in failure_rates]
    # result = []

    # for stage, _ in failure_rates:
        # result.append(stage)

    # result = [3, 4, 2, 1, 5]
    
    return result