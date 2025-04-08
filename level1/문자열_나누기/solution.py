def solution(s):
    answer = 0
    
    while s:  # 문자열이 남아있는 동안 반복
        x = s[0]  # 첫 글자를 x로 지정
        x_count = 0  # x의 등장 횟수
        other_count = 0  # x가 아닌 글자의 등장 횟수
        
        for i in range(len(s)):
            if s[i] == x:
                x_count += 1
            else:
                other_count += 1
            
            # x와 x가 아닌 글자의 등장 횟수가 같아지면
            if x_count == other_count:
                break
        
        # 현재까지 읽은 부분 분리
        s = s[i + 1:]
        answer += 1
    
    return answer