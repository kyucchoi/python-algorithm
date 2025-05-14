def solution(s):
    transform_count = 0  # 이진 변환 횟수
    zero_count = 0       # 제거한 0의 개수
    
    while s != '1':      # s가 '1'이 될 때까지 반복
        # 0의 개수 세기
        zeros = s.count('0')
        zero_count += zeros
        
        # 0 제거 후 길이 계산
        length_without_zeros = len(s) - zeros
        
        # 길이를 이진법으로 변환
        s = bin(length_without_zeros)[2:]  # bin() 결과에서 '0b' 접두사 제거
        
        transform_count += 1
    
    return [transform_count, zero_count]