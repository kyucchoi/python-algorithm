def solution(spell, dic):
    # spell의 알파벳들을 정렬
    spell_sorted = sorted(spell)
    
    # dic의 각 단어를 확인
    for word in dic:
        # 단어의 길이가 spell과 같은지 확인
        if len(word) == len(spell):
            # 단어를 구성하는 알파벳들을 정렬
            word_sorted = sorted(word)
            
            # spell과 단어의 구성 알파벳이 같은지 비교
            if spell_sorted == word_sorted:
                return 1
    
    # 일치하는 단어를 찾지 못한 경우
    return 2