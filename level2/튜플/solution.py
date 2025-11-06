def solution(s):
    # 1. 문자열 파싱
    s = s[2:-2]
    sets = s.split('},{')
    
    # 2. 각 집합을 숫자 리스트로 변환
    sets = [list(map(int, s.split(','))) for s in sets]
    
    # 3. 길이순 정렬
    sets.sort(key = len)
    
    # 4. 새로운 원소만 순서대로 추가
    answer = []

    for s in sets:
        for num in s:
            if num not in answer:
                answer.append(num)
                break
    
    return answer