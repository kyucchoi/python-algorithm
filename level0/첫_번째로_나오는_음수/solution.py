def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i] < 0:    # 음수인지 확인
            return i
        
    return -1      # 음수가 없는 경우