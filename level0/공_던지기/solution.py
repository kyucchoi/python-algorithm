def solution(numbers, k):
    # 현재 공을 가진 사람의 인덱스 (1번부터 시작하므로 인덱스 0)
    current_index = 0
    
    # k번째까지 공을 던지기
    for i in range(k):
        # k번째에 도달하면 현재 사람이 답
        if i == k - 1:
            return numbers[current_index]
        
        # 오른쪽으로 한 명 건너뛰고 다음 사람에게 (2칸 이동)
        current_index = (current_index + 2) % len(numbers)
    
    return numbers[current_index]