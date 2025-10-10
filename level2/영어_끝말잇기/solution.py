def solution(n, words):
    used_words = set()
    used_words.add(words[0])
    
    for i in range(1, len(words)):
        prev_word = words[i - 1]
        curr_word = words[i]
        
        # 1. 끝말잇기 규칙 위반
        if prev_word[-1] != curr_word[0]:
            person = (i % n) + 1
            turn = (i // n) + 1

            return [person, turn]
        
        # 2. 중복 단어 사용
        if curr_word in used_words:
            person = (i % n) + 1
            turn = (i // n) + 1
            
            return [person, turn]
        
        used_words.add(curr_word)
    
    return [0, 0]