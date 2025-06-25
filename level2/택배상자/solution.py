def solution(order):
    answer = 0      # 트럭에 실은 상자 개수
    belt = []       # 보조 벨트 (스택)
    idx = 0         # order에서 현재 실어야 할 상자의 인덱스
    
    # 메인 벨트에서 1번부터 n번까지 순서대로 상자 처리
    for box in range(1, len(order) + 1):
        # 1. 현재 상자를 보조 벨트에 추가
        belt.append(box)
        
        # 2. 보조 벨트 맨 위 상자가 현재 실어야 할 상자와 일치하는 동안 반복
        while (belt) and (belt[-1] == order[idx]):
            answer += 1     # 트럭에 실은 상자 수 증가
            idx += 1        # 다음에 실어야 할 상자로 이동
            belt.pop()      # 보조 벨트에서 상자 제거
    
    return answer