def solution(food):
    # 결과 문자열 초기화
    result = ''
    
    # 1번 음식부터 차례대로 배치
    for i in range(1, len(food)):
        # 각 음식은 두 명이 나눠 먹어야 하므로 2로 나눈 몫만큼만 사용
        count = food[i] // 2
        # 해당 음식의 번호를 개수만큼 결과 문자열에 추가
        result += str(i) * count
    
    # 중앙에 물(0) 배치하고, 왼쪽 배치의 역순을 오른쪽에 추가
    # [::-1]은 문자열을 뒤집는 파이썬 슬라이싱
    return result + '0' + result[::-1]