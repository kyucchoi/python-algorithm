def solution(numbers):
    numbers = list(map(str, numbers))
    
    # 정렬: x * 3과 y * 3을 비교 (최대 1000이므로 3자리 × 3 = 9자리면 충분)
    numbers.sort(key=lambda x: x * 3, reverse = True)
    
    answer = ''.join(numbers)
    
    return str(int(answer))