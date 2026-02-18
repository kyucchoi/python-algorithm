from itertools import combinations

def solution(nums):
    count = 0
    
    # 모든 가능한 3개 숫자의 조합 찾기
    for combo in combinations(nums, 3):
        total = sum(combo)
        
        if is_prime(total):
            count += 1
    
    return count

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True