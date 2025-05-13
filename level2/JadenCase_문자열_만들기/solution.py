def solution(s):
    words = s.split(' ')  # 공백을 기준으로 단어 분리
    capitalized_words = []
    
    for word in words:
        if word:  # 빈 문자열이 아닌 경우
            capitalized_words.append(word[0].upper() + word[1:].lower())
        else:  # 빈 문자열인 경우 (연속된 공백)
            capitalized_words.append('')
    
    return ' '.join(capitalized_words)