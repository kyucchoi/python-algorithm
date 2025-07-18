def solution(i, j, k):
    count = 0
    k_str = str(k)  # 비교할 숫자를 문자열로 변환
    
    # i부터 j까지 모든 숫자 확인
    for num in range(i, j + 1):
        num_str = str(num)  # 각 숫자를 문자열로 변환
        count += num_str.count(k_str)  # 해당 숫자가 몇 번 나오는지 세기
    
    return count