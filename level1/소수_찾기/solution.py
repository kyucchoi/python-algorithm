# 방법 1
def solution(n):
    # 2부터 n까지의 모든 숫자를 소수 후보로 집합에 저장
    prime_candidates = set(range(2, n + 1))
    
    # 2부터 n의 제곱근까지만 확인하면 충분합니다
    for current_number in range(2, int(n**0.5) + 1):
        # 현재 숫자가 아직 소수 후보 집합에 있다면 (즉, 소수라면)
        if current_number in prime_candidates:
            # 현재 소수의 제곱부터 시작하여 모든 배수를 후보 집합에서 제거
            multiples_to_remove = set(range(current_number * current_number, n + 1, current_number))
            prime_candidates -= multiples_to_remove
    
    # 남은 숫자들이 모두 소수이므로 그 개수를 반환
    return len(prime_candidates)

# 방법 2
from itertools import permutations

def solution(numbers):
    # 1. 소수 판별 함수
    def is_prime(n):
        if n < 2:
            return False
        
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
                
        return True
    
    # 2. 만들 수 있는 모든 숫자 조합
    all_numbers = set()
    
    # 1자리부터 전체 길이까지
    for length in range(1, len(numbers) + 1):
        # 순열 생성
        for perm in permutations(numbers, length):
            # 문자열 → 정수 변환
            num = int(''.join(perm))
            all_numbers.add(num)
    
    # 3. 소수 개수 세기
    count = 0
    
    for num in all_numbers:
        if is_prime(num):
            count += 1
    
    return count