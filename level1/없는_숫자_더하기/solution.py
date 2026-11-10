# 방법 1
def solution(numbers):
    # 0부터 9까지의 모든 숫자의 합
    total_sum = sum(range(10))  # 0 + 1 + 2 + ... + 9 = 45
    
    # 배열에 있는 숫자들의 합
    numbers_sum = sum(numbers)
    
    # 없는 숫자들의 합 = 모든 숫자의 합 - 배열에 있는 숫자들의 합
    return total_sum - numbers_sum

# 전체 합에서 빼기
def solution(numbers):
    return 45 - sum(numbers)

# 방법 3
def solution(numbers):
    answer = 0
    
    for num in range(10):
        if num not in numbers:
            answer += num
            
    return answer