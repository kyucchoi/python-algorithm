def solution(a, d, included):
    result = 0
    
    for i in range(len(included)):
        num = a + (d * i)
        
        if included[i]:
            result += num
            
    return result