def solution(clothes):
    clothes_type = {}
    
    for cloth, type in clothes:
        if type in clothes_type:
            clothes_type[type] += 1
        else:
            clothes_type[type] = 1
    
    answer = 1
    
    for count in clothes_type.values():
        answer *= (count + 1)
        
    return answer - 1