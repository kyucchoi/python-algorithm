def solution(n):
    # 2부터 n까지의 모든 숫자를 소수 후보로 집합에 저장
    prime_candidates = set(range(2, n + 1))
    
    # 2부터 n의 제곱근까지만 확인하면 충분합니다
    for current_number in range(2, int(n ** 0.5) + 1):
        # 현재 숫자가 아직 소수 후보 집합에 있다면 (즉, 소수라면)
        if current_number in prime_candidates:
            # 현재 소수의 제곱부터 시작하여 모든 배수를 후보 집합에서 제거
            multiples_to_remove = set(range(current_number * current_number, n + 1, current_number))
            prime_candidates -= multiples_to_remove
    
    # 남은 숫자들이 모두 소수이므로 그 개수를 반환
    return len(prime_candidates)