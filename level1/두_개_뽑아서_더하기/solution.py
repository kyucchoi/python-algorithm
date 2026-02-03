# 방법 1
def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            sum_value = numbers[i] + numbers[j]

            if sum_value not in answer:
                answer.append(sum_value)
    
    return sorted(answer)

# 방법 2
def solution(numbers):
    answer = set()
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.add(numbers[i] + numbers[j])
    
    return sorted(list(answer))

# 내 방법
def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    
    return sorted(list(answer))