def solution(number, limit, power):
    total_weight = 0
    
    for knight in range(1, number + 1):
        # 약수의 개수 계산
        divisor_count = count_divisors(knight)
        
        # 제한 수치를 초과하면 power로 대체
        if divisor_count > limit:
            total_weight += power
        else:
            total_weight += divisor_count
    
    return total_weight

def count_divisors(n):
    count = 0
    # 제곱근까지만 확인하면 됨
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            # i가 약수라면 n//i도 약수
            if i == n // i:  # 제곱근인 경우 한 번만 카운트
                count += 1
            else:
                count += 2  # i와 n//i 두 개의 약수를 카운트
    return count