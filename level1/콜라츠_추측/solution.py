# 방법 1
def solution(num):
    if num == 1:
        return 0
    
    count = 0
    
    while num != 1:
        if count >= 500:
            return -1
        
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
            
        count += 1
    
    return count

# 방법 2
def solution(num):
    for count in range(500):
        if num == 1:
            return count
        
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
    
    return -1