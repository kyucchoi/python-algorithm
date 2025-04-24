def solution(survey, choices):
    # 성격 유형 점수를 저장할 딕셔너리 초기화
    scores = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    # 각 질문에 대한 응답을 처리
    for i in range(len(survey)):
        # 현재 질문의 성격 유형 쌍
        type_pair = survey[i]
        # 선택한 답변
        choice = choices[i]
        
        # 선택에 따른 점수 계산
        if choice < 4:  # 비동의 (1, 2, 3)
            scores[type_pair[0]] += 4 - choice  # 3, 2, 1점
        elif choice > 4:  # 동의 (5, 6, 7)
            scores[type_pair[1]] += choice - 4  # 1, 2, 3점
        # choice가 4인 경우 점수 변화 없음
    
    # 각 지표별로 성격 유형 결정
    result = ''
    
    # 1번 지표: R vs T
    if scores['R'] >= scores['T']:
        result += 'R'
    else:
        result += 'T'
    
    # 2번 지표: C vs F
    if scores['C'] >= scores['F']:
        result += 'C'
    else:
        result += 'F'
    
    # 3번 지표: J vs M
    if scores['J'] >= scores['M']:
        result += 'J'
    else:
        result += 'M'
    
    # 4번 지표: A vs N
    if scores['A'] >= scores['N']:
        result += 'A'
    else:
        result += 'N'
    
    return result