# 방법 1
from collections import deque

def solution(priorities, location):
    # (인덱스, 우선순위) 형태로 큐 생성
    queue = deque([(i, p) for i, p in enumerate(priorities)])

    answer = 0
    
    while queue:
        current = queue.popleft()

        if any(current[1] < q[1] for q in queue):
            queue.append(current)
        else:
            answer += 1

            if current[0] == location:
                return answer
    
    return answer

# 방법 2
from collections import deque

def solution(priorities, location):
    queue = deque()
    
    for i, p in enumerate(priorities):
        queue.append((i, p))
        
    answer = 0
    
    while queue:
        current = queue.popleft()
        
        found_higher = False
        
        for q in queue:
            if current[1] < q[1]:
                found_higher = True
                break
                
        if found_higher:
            queue.append(current)
        else:
            answer += 1
            
            if current[0] == location:
                return answer
            
    return answer