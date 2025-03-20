def solution(s):
    words = s.split(' ')  # 공백을 기준으로 단어 분리
    result = []
    
    for word in words:
        new_word = ''
        
        for i in range(len(word)):
            if i % 2 == 0:  # 짝수 인덱스 (0, 2, 4, ...)
                new_word += word[i].upper()
            else:  # 홀수 인덱스 (1, 3, 5, ...)
                new_word += word[i].lower()

        result.append(new_word)
    
    return ' '.join(result)  # 공백으로 단어들 연결