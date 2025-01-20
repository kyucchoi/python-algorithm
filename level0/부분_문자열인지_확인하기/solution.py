def solution(my_string, target):
    target_len = len(target)
    
    # my_string의 모든 가능한 부분 문자열 확인
    for i in range(len(my_string) - target_len + 1):
        # 현재 위치에서 target 길이만큼의 부분 문자열 추출
        if my_string[i : i + target_len] == target:
            return 1
            
    return 0