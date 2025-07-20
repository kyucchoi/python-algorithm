def solution(s):
    # 각 문자의 등장 횟수 세기
    char_count = {}

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # 한 번만 등장하는 문자들 찾기
    unique_chars = []
    
    for char, count in char_count.items():
        if count == 1:
            unique_chars.append(char)
    
    # 사전순으로 정렬하여 문자열로 반환
    unique_chars.sort()

    return ''.join(unique_chars)