# 방법 1
def solution(babbling):
    count = 0
    pronounceable = ['aya', 'ye', 'woo', 'ma']
    
    for word in babbling:
        # 연속된 같은 발음이 있는지 확인
        for p in pronounceable:
            if p * 2 in word:  # 예: "ayaaya"
                break
        else:
            # 발음 가능한 단어를 특수 문자로 치환
            temp_word = word

            for p in pronounceable:
                temp_word = temp_word.replace(p, ' ')
            
            # 모든 발음을 제거한 후 공백만 남으면 발음 가능
            if temp_word.strip() == '':
                count += 1
    
    return count

# 방법 2
def solution(babbling):
    count = 0
    pronounceable = ['aya', 'ye', 'woo', 'ma']
    
    for word in babbling:
        # 단어가 발음 가능한지 확인
        if is_pronounceable(word, pronounceable):
            count += 1
    
    return count

def is_pronounceable(word, pronounceable):
    i = 0
    last_pronunciation = ''
    
    while i < len(word):
        found = False
        
        for pronunciation in pronounceable:
            # 현재 위치에서 발음이 시작되는지 확인
            if word[i:].startswith(pronunciation):
                # 연속된 같은 발음인지 확인
                if pronunciation == last_pronunciation:
                    return False
                
                # 발음을 찾았으면 인덱스 이동 및 마지막 발음 업데이트
                i += len(pronunciation)

                last_pronunciation = pronunciation

                found = True

                break
        
        # 발음을 찾지 못했으면 발음 불가능
        if not found:
            return False
    
    # 단어의 끝까지 발음 가능하면 True 반환
    return True