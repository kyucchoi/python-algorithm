def solution(q, r, code):
    result = ''
    
    # 각 인덱스를 확인
    for i in range(len(code)):
        # 인덱스를 q로 나눈 나머지가 r과 같으면
        if i % q == r:
            result += code[i]
            
    return result