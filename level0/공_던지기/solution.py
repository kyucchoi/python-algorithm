def solution(numbers, k):
    current_index = 0
    
    # k번째까지 공을 던지기
    for i in range(k):
        if i == k - 1:
            return numbers[current_index]
        
        # 오른쪽으로 한 명 건너뛰고 다음 사람에게 (2칸 이동)
        current_index = (current_index + 2) % len(numbers)
    
    return numbers[current_index]