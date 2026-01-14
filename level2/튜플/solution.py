def solution(s):
    s = s[2:-2]
    
    sets = s.split('},{')
    
    sets = [set(map(int, s.split(','))) for s in sets]
    
    sets.sort(key=len)
    
    answer = []
    for s in sets:
        for num in s:
            if num not in answer:
                answer.append(num)
                break
    
    return answer