# 방법 1
def solution(s):
    result = []
    is_first_char = True  # 단어의 첫 문자인지 추적
    
    for char in s:
        if char == ' ':
            result.append(char)
            is_first_char = True  # 다음 문자는 새 단어의 시작
        elif is_first_char:
            result.append(char.upper())  # 첫 문자는 대문자
            is_first_char = False
        else:
            result.append(char.lower())  # 나머지는 소문자
    
    return ''.join(result)

# 방법 2
def solution(s):
    words = s.split(' ')
    answer = []

    for word in words:
        answer.append(word[:1].upper() + word[1:].lower())
        
    return ' '.join(answer)