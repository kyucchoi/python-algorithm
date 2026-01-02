def solution(operations):
    queue = []
    
    for op in operations:
        cmd, num = op.split()
        num = int(num)
        
        if cmd == 'I':
            queue.append(num)
        
        elif cmd == 'D':
            if not queue:
                continue
            
            if num == 1:
                queue.remove(max(queue))
            elif num == -1:
                queue.remove(min(queue))
    
    if not queue:
        return [0, 0]
    else:
        return [max(queue), min(queue)]