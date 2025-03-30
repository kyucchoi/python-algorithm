def solution(answers):
    # 각 수포자의 찍는 패턴
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 각 수포자가 맞힌 문제 수
    score = [0, 0, 0]
    
    # 각 문제마다 수포자들의 답안과 실제 정답 비교
    for i, answer in enumerate(answers):
        if answer == pattern1[i % len(pattern1)]:
            score[0] += 1
        if answer == pattern2[i % len(pattern2)]:
            score[1] += 1
        if answer == pattern3[i % len(pattern3)]:
            score[2] += 1
    
    # 가장 높은 점수 찾기
    max_score = max(score)
    
    # 가장 높은 점수를 받은 사람들 찾기
    # result = [i + 1 for i in range(len(score)) if score[i] == max_score]
    result = []  # 결과를 저장할 빈 리스트 생성

    # score 리스트의 인덱스를 하나씩 확인
    for i in range(len(score)):
        # 현재 인덱스의 점수가 최고 점수와 같은지 확인
        if score[i] == max_score:
            # 인덱스는 0부터 시작하지만, 수포자 번호는 1부터 시작하므로 +1
            result.append(i + 1)
    
    return result