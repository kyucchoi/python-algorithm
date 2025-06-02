def solution(elements):
    n = len(elements)
    sums = set()  # 중복 제거를 위한 집합
    
    # 길이별로 연속 부분 수열 생성
    for length in range(1, n + 1):  # 길이 1부터 n까지
        for start in range(n):  # 시작 위치
            current_sum = 0
            
            # length만큼 원형으로 더하기
            for i in range(length):
                index = (start + i) % n  # 원형 인덱스
                current_sum += elements[index]
            
            sums.add(current_sum)
    
    return len(sums)