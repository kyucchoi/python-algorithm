def solution(spell, dic):
    spell_sorted = sorted(spell)
    
    for word in dic:
        if len(word) == len(spell):
            word_sorted = sorted(word)
            
            if spell_sorted == word_sorted:
                return 1
    
    return 2