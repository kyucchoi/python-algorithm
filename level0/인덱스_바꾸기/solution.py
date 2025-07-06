def solution(my_string, num1, num2):
    # 문자열을 리스트로 변환 (문자열은 변경 불가능하므로)
    char_list = list(my_string)
    
    # 두 인덱스의 문자를 서로 바꾸기
    char_list[num1], char_list[num2] = char_list[num2], char_list[num1]
    
    # 리스트를 다시 문자열로 변환하여 반환
    return ''.join(char_list)