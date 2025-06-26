def solution(x, y, n):
    steps = 0
    current = set([x])
    
    while current:
        if y in current:
            return steps
        
        next_level = set()

        for num in current:
            if num + n <= y:
                next_level.add(num + n)

            if num * 2 <= y:
                next_level.add(num * 2)
                
            if num * 3 <= y:
                next_level.add(num * 3)
        
        current = next_level
        steps += 1
    
    return -1