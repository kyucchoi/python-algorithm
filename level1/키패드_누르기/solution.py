def solution(numbers, hand):
    # 키패드 좌표 설정 (0부터 9까지, *, #)
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
    
    # 초기 손 위치
    left_pos = keypad['*']
    right_pos = keypad['#']
    
    # 주손 설정
    main_hand = 'R' if hand == 'right' else 'L'
    
    result = ''
    
    for number in numbers:
        # 왼쪽 열의 숫자는 왼손
        if number in [1, 4, 7]:
            result += 'L'
            left_pos = keypad[number]
        # 오른쪽 열의 숫자는 오른손
        elif number in [3, 6, 9]:
            result += 'R'
            right_pos = keypad[number]
        # 가운데 열의 숫자는 더 가까운 손
        else:
            target = keypad[number]
            
            # 두 손과의 거리 계산 (맨해튼 거리)
            left_dist = abs(left_pos[0] - target[0]) + abs(left_pos[1] - target[1])
            right_dist = abs(right_pos[0] - target[0]) + abs(right_pos[1] - target[1])
            
            # 더 가까운 손 선택 (거리가 같으면 주손)
            if left_dist < right_dist:
                result += 'L'
                left_pos = target
            elif right_dist < left_dist:
                result += 'R'
                right_pos = target
            else:
                result += main_hand
                
                if main_hand == 'L':
                    left_pos = target
                else:
                    right_pos = target
    
    return result