def solution(my_string):
    # 알파벳 개수를 저장할 리스트 (A-Z, a-z 순서)
    result = [0] * 52
    
    for char in my_string:
        # 대문자인 경우 (A=65 ~ Z=90)
        if char.isupper():
            result[ord(char) - ord('A')] += 1
        # 소문자인 경우 (a=97 ~ z=122)
        else:
            result[ord(char) - ord('a') + 26] += 1
            
    return result