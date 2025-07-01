
def solution(array):
    # 각 숫자의 출현 횟수를 세기
    count_dict = {}
    
    for num in array:
        count_dict[num] = count_dict.get(num, 0) + 1
    
    # 최대 출현 횟수 찾기
    max_count = max(count_dict.values())
    
    # 최대 출현 횟수를 가진 숫자들 찾기
    modes = [num for num, count in count_dict.items() if count == max_count]
    
    # 최빈값이 여러 개면 -1, 하나면 그 값 반환
    return -1 if len(modes) > 1 else modes[0]