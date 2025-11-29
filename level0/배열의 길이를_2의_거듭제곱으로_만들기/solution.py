def solution(arr):
    length = len(arr)
    
    target_length = 1
    
    while target_length < length:
        target_length *= 2
    
    return arr + [0] * (target_length - length)