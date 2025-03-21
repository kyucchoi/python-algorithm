def solution(s):
    answer = []
    char_positions = {}  # 각 문자의 마지막 위치를 저장할 딕셔너리
    
    for i, char in enumerate(s):
        # 이전에 같은 문자가 있었는지 확인
        if char in char_positions:
            # 현재 위치 - 이전 위치 = 거리
            answer.append(i - char_positions[char])
        else:
            # 처음 나오는 문자라면 -1
            answer.append(-1)
        
        # 현재 문자의 위치 업데이트
        char_positions[char] = i
    
    return answer