def solution(my_string, overwrite_string, s):
    # 앞부분 + 교체할 문자열 + 뒷부분
    return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]