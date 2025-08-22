def solution(n):
    prev, curr = 0, 1

    for _ in range(2, n + 1):
        prev, curr = curr, (prev + curr) % 1234567

    return curr