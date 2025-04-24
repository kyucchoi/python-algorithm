def solution(cards1, cards2, goal):
    # 각 카드 뭉치의 현재 인덱스
    idx1 = 0
    idx2 = 0
    
    for word in goal:
        # 첫 번째 카드 뭉치에서 현재 단어를 찾을 수 있는 경우
        if idx1 < len(cards1) and word == cards1[idx1]:
            idx1 += 1
        # 두 번째 카드 뭉치에서 현재 단어를 찾을 수 있는 경우
        elif idx2 < len(cards2) and word == cards2[idx2]:
            idx2 += 1
        # 두 카드 뭉치 모두에서 현재 단어를 찾을 수 없는 경우
        else:
            return 'No'
    
    # 모든 단어를 성공적으로 찾은 경우
    return 'Yes'