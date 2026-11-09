def solution(x):
    digit_num = sum(map(int, str(x)))
    
    return x % digit_num == 0