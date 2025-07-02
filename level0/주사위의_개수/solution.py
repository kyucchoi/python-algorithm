def solution(box, n):
    result = 1
    
    for length in box:
        result *= length // n
    
    return result