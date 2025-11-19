def solution(babbling):
    count = 0
    pronounceable = ['aya', 'ye', 'woo', 'ma']
    
    for word in babbling:
        has_consecutive = False
        
        for p in pronounceable:
            if p * 2 in word:
                has_consecutive = True
                break
        
        if has_consecutive:
            continue
        
        temp_word = word
        
        for p in pronounceable:
            temp_word = temp_word.replace(p, ' ')
        
        if temp_word.strip() == '':
            count += 1
    
    return count