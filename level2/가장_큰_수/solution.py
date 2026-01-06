# 방법 1
def solution(numbers):
    numbers = list(map(str, numbers))
    
    # 정렬: x * 3과 y * 3을 비교 (최대 1000이므로 3자리 × 3 = 9자리면 충분)
    numbers.sort(key=lambda x: x * 3, reverse=True)
    
    answer = ''.join(numbers)
    
    return str(int(answer))

# 방법 2
from functools import cmp_to_key

def solution(numbers):
    numbers = list(map(str, numbers))
    
    def compare(x, y):
        if x + y > y + x:
            return -1  # x를 앞에
        elif x + y < y + x:
            return 1   # y를 앞에
        else:
            return 0   # 같음
    
    numbers.sort(key=cmp_to_key(compare))
    
    answer = ''.join(numbers)
    
    return '0' if answer[0] == '0' else answer