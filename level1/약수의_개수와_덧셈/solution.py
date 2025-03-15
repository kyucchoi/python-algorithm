def solution(left, right):
    result = 0
    
    for num in range(left, right + 1):
        # 약수의 개수 계산
        divisor_count = 0
        
        for i in range(1, num + 1):
            if num % i == 0:
                divisor_count += 1
        
        # 약수의 개수가 짝수면 더하고, 홀수면 뺌
        if divisor_count % 2 == 0:
            result += num
        else:
            result -= num
    
    return result