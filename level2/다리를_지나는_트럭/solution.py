from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 대기 트럭을 큐로 변환
    waiting_trucks = deque(truck_weights)
    
    # 다리 상태를 나타내는 큐 (0은 빈 공간, 숫자는 트럭 무게)
    bridge = deque([0] * bridge_length)
    
    current_weight = 0
    time = 0
    
    # 모든 트럭이 다리를 건널 때까지 반복
    while waiting_trucks or current_weight > 0:
        time += 1
        
        # 1. 다리 맨 앞의 트럭이 다리를 완전히 건넜는지 확인
        exiting_truck = bridge.popleft()
        current_weight -= exiting_truck
        
        # 2. 대기 중인 트럭이 있고, 다리에 올라갈 수 있는지 확인
        if waiting_trucks:
            next_truck = waiting_trucks[0]
            
            # 무게 제한 체크 (다리 길이 제한은 큐 크기로 자동 체크됨)
            if current_weight + next_truck <= weight:
                # 트럭을 다리에 올림
                truck = waiting_trucks.popleft()
                bridge.append(truck)
                current_weight += truck
            else:
                # 올라갈 수 없으면 빈 공간 추가
                bridge.append(0)
        else:
            # 대기 트럭이 없으면 빈 공간 추가
            bridge.append(0)
    
    return time