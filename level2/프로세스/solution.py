from collections import deque

def solution(priorities, location):    
    # 큐에 (우선순위, 원래 인덱스) 저장
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    execution_order = 0
    
    while queue:
        current_priority, current_index = queue.popleft()
        
        # 더 높은 우선순위가 있는지 확인
        if any(p > current_priority for p, _ in queue):
            # 다시 큐 뒤에 넣기
            queue.append((current_priority, current_index))
        else:
            # 실행!
            execution_order += 1
            
            if current_index == location:
                return execution_order
    
    return -1