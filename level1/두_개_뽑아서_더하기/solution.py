# 방법 1
def solution(numbers):
    answer = []
    
    # 모든 가능한 인덱스 조합 검사
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):  # i + 1부터 시작하여 중복 방지
            sum_value = numbers[i] + numbers[j]
            # 중복 제거
            if sum_value not in answer:
                answer.append(sum_value)
    
    # 오름차순 정렬
    return sorted(answer)

# 방법 2
def solution(numbers):
    answer = set()  # 중복 자동 제거를 위한 set 사용
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.add(numbers[i] + numbers[j])
    
    return sorted(list(answer))  # set을 리스트로 변환 후 정렬

# 내 방법
def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    
    return sorted(list(answer))