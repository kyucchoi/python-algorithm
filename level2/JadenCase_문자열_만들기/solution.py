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
    words = s.split(' ')  # 공백을 기준으로 단어 분리
    capitalized_words = []
    
    for word in words:
        if word:  # 빈 문자열이 아닌 경우
            capitalized_words.append(word[0].upper() + word[1:].lower())
        else:  # 빈 문자열인 경우 (연속된 공백)
            capitalized_words.append('')
    
    return ' '.join(capitalized_words)