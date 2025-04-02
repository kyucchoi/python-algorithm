from itertools import combinations

def solution(nums):
    count = 0
    
    # 모든 가능한 3개 숫자의 조합 찾기
    for combo in combinations(nums, 3):
        # 3개 숫자의 합
        total = sum(combo)
        
        # 합이 소수인지 확인
        if is_prime(total):
            count += 1
    
    return count

def is_prime(n):
    # 2보다 작으면 소수가 아님
    if n < 2:
        return False
    
    # 2부터 제곱근까지의 모든 수로 나눠보기
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    # 나누어 떨어지는 수가 없으면 소수
    return True