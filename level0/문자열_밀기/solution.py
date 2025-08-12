def solution(A, B):
    # A와 B가 이미 같다면 0번
    if A == B:
        return 0
    
    # A를 오른쪽으로 밀면서 B와 비교
    current = A
    
    for i in range(1, len(A)):
        # 오른쪽으로 한 칸 밀기: 마지막 문자를 맨 앞으로
        current = current[-1] + current[:-1]
        
        # B와 같아졌다면 현재 밀기 횟수 반환
        if current == B:
            return i
    
    # A의 길이만큼 밀어도 B가 안 나오면 불가능
    return -1