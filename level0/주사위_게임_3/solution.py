def solution(a, b, c, d):
    # 각 숫자의 등장 횟수를 저장하는 딕셔너리
    counts = {}
    for num in [a, b, c, d]:
        counts[num] = counts.get(num, 0) + 1
    
    # 등장 횟수별로 케이스 구분
    if len(counts) == 1:
        # 모든 주사위가 같은 경우
        p = a  # 아무 숫자나 선택 가능
        return 1111 * p
    
    elif len(counts) == 2:
        # 3개가 같은 경우 또는 2개씩 같은 경우
        nums = list(counts.items())  # (숫자, 횟수) 쌍의 리스트
        if 3 in counts.values():
            # 3개가 같은 경우
            p = [k for k, v in counts.items() if v == 3][0]
            q = [k for k, v in counts.items() if v == 1][0]
            return (10 * p + q) ** 2
        else:
            # 2개씩 같은 경우
            p, q = nums[0][0], nums[1][0]
            return (p + q) * abs(p - q)
    
    elif len(counts) == 3:
        # 2개가 같고 나머지가 다른 경우
        p = [k for k, v in counts.items() if v == 2][0]
        q, r = [k for k, v in counts.items() if v == 1]
        return q * r
    
    else:
        # 모두 다른 경우
        return min(counts.keys())