def solution(keymap, targets):
    answer = []
    # 각 문자에 대한 최소 키 입력 횟수를 저장할 딕셔너리
    char_presses = {}
    
    # 각 키맵을 순회하며 문자별 최소 입력 횟수 계산
    for i, key in enumerate(keymap):
        for j, char in enumerate(key):
            # 처음 보는 문자이거나, 더 적은 횟수로 입력 가능한 경우 업데이트
            if char not in char_presses or j + 1 < char_presses[char]:
                char_presses[char] = j + 1
    
    # 각 target 문자열에 대해 필요한 총 키 입력 횟수 계산
    for target in targets:
        total_presses = 0
        impossible = False
        
        for char in target:
            # 입력할 수 없는 문자가 있으면 불가능
            if char not in char_presses:
                impossible = True
                break
            total_presses += char_presses[char]
        
        # 불가능하면 -1, 아니면 총 입력 횟수 추가
        if impossible:
            answer.append(-1)
        else:
            answer.append(total_presses)
    
    return answer