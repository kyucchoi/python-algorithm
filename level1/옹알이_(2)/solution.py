def solution(babbling):
    count = 0
    pronounceable = ['aya', 'ye', 'woo', 'ma']
    
    for word in babbling:
        for p in pronounceable:
            if p * 2 in word:  # "aya" * 2 = "ayaaya"
                break
        else:
            temp_word = word

            for p in pronounceable:
                temp_word = temp_word.replace(p, ' ')
            
            if temp_word.strip() == '':
                count += 1
    
    return count