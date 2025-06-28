from itertools import permutations

def solution(numbers):
    
    def is_prime(n):
        if n < 2:
            return False
        
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
            
        return True
    
    answer = 0
    nums = set()
    
    # 1자리부터 전체 자리수까지 모든 순열 생성
    for length in range(1, len(numbers) + 1):
        for p in permutations(numbers, length):
            num_str = int(''.join(p))
            nums.add(num_str)
    
    # 소수인 것만 개수 세기
    for num in nums:
        if is_prime(num):
            answer += 1
            
    return answer