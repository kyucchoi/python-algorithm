def solution(name, yearning, photo):
    # 이름과 그리움 점수를 매핑하는 딕셔너리 생성
    score_dict = dict(zip(name, yearning))
    
    result = []
    
    # 각 사진에 대한 추억 점수 계산
    for people in photo:
        total_score = 0

        for person in people:
            # 해당 인물의 그리움 점수가 있으면 더함, 없으면 0
            total_score += score_dict.get(person, 0)
            
        result.append(total_score)
    
    return result