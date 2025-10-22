def solution(my_string, indices):
    string_list = list(my_string)
    
    # indices의 위치에 있는 문자들을 빈 문자로 변경
    for index in indices:
        string_list[index] = ''
    
    # 리스트를 다시 문자열로 합치기
    return ''.join(string_list)