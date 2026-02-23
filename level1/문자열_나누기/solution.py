def solution(s):
    answer = 0
    
    while s:
        x = s[0]
        x_count = 0
        other_count = 0
        
        for i in range(len(s)):
            if s[i] == x:
                x_count += 1
            else:
                other_count += 1
            
            if x_count == other_count:
                break
        
        s = s[i + 1:]
        answer += 1
    
    return answer