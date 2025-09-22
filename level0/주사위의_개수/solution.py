# 방법 1
def solution(box, n):
    result = 1
    
    for length in box:
        result *= length // n
    
    return result

# 방법 2
def solution(box, n):
    x, y, z = box
    
    return (x // n) * (y // n) * (z // n)