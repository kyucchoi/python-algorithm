def solution(dartResult):
    scores = []  # 각 기회마다의 점수를 저장할 리스트
    num = ''     # 점수를 임시로 저장할 변수
    
    for char in dartResult:
        if char.isdigit():  # 숫자인 경우 (0-10점)
            num += char
        elif char in ['S', 'D', 'T']:  # 보너스 영역인 경우
            score = int(num)

            if char == 'D':
                score **= 2  # 더블(D): 2제곱
            elif char == 'T':
                score **= 3  # 트리플(T): 3제곱

            scores.append(score)

            num = ''  # 점수 초기화
        else:  # 옵션인 경우 (*, #)
            if char == '*':  # 스타상: 현재 점수와 이전 점수 2배
                scores[-1] *= 2

                if len(scores) > 1:  # 첫 번째 기회가 아닌 경우에만
                    scores[-2] *= 2
            elif char == '#':  # 아차상: 해당 점수 마이너스
                scores[-1] *= -1
    
    return sum(scores)  # 3번의 기회에서 얻은 점수 합계 반환