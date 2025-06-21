def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    answer = 0
    
    def dfs(current_word, target_word):
        nonlocal answer
        
        # 현재 단어가 목표 단어와 같으면 찾았음
        if current_word == target_word:
            return True
        
        # 길이가 5가 되면 더 이상 진행하지 않음
        if len(current_word) == 5:
            return False
        
        # 각 모음을 추가해가며 DFS 탐색
        for vowel in vowels:
            answer += 1  # 사전 순서 증가
            
            # 다음 단어로 DFS 진행
            if dfs(current_word + vowel, target_word):
                return True
        
        return False
    
    # 빈 문자열부터 시작하여 DFS 탐색
    dfs('', word)

    return answer