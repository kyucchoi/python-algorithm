from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)  # 다리 초기화
    trucks = deque(truck_weights)  # 대기 트럭
    current_weight = 0  # 다리 위 무게
    
    while trucks or current_weight > 0:
        time += 1
        
        # 1. 다리 맨 앞 트럭 내보내기
        out = bridge.popleft()
        current_weight -= out
        
        # 2. 새 트럭 올리기
        if trucks:
            if current_weight + trucks[0] <= weight:
                truck = trucks.popleft()
                bridge.append(truck)
                current_weight += truck
            else:
                bridge.append(0)
    
    return time