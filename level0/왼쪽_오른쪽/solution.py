def solution(str_list):
    for i in range(len(str_list)):
        if str_list[i] == 'l':
            return str_list[:i]  # l 왼쪽 부분 반환
        elif str_list[i] == 'r':
            return str_list[i + 1:]  # r 오른쪽 부분 반환
            
    return []