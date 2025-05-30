# 방법 1
def solution(n, words):
    # 이미 사용된 단어들을 저장할 집합
    used_words = set()
    
    for i, word in enumerate(words):
        # 현재 누구 차례인지 계산
        current_player = i % n + 1  # 1번부터 시작
        current_turn = i // n + 1   # 1번째 차례부터 시작
        
        # 탈락 조건 1: 이미 사용된 단어
        if word in used_words:
            return [current_player, current_turn]
        
        # 탈락 조건 2: 끝말잇기 규칙 위반 (첫 번째 단어가 아닌 경우)
        if i > 0:  # 첫 번째 단어가 아니라면
            prev_word = words[i - 1]
            if prev_word[-1] != word[0]:  # 이전 단어의 마지막 글자 != 현재 단어의 첫 글자
                return [current_player, current_turn]
        
        # 단어를 사용된 단어 집합에 추가
        used_words.add(word)
    
    # 탈락자가 없는 경우
    return [0, 0]

# 방법 2
def solution_alternative(n, words):
    # 사용된 단어를 추적하는 리스트 방식
    used_words = []
    
    for i in range(len(words)):
        word = words[i]
        
        # 중복 단어 체크
        if word in used_words:
            player = i % n + 1
            turn = i // n + 1

            return [player, turn]
        
        # 끝말잇기 규칙 체크 (첫 번째 단어 제외)
        if i > 0 and words[i-1][-1] != word[0]:
            player = i % n + 1
            turn = i // n + 1
            
            return [player, turn]
        
        used_words.append(word)
    
    return [0, 0]