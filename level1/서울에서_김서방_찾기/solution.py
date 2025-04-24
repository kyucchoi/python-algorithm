# index() 방법
def solution(seoul):
    # 'Kim'의 인덱스를 찾습니다
    kim_index = seoul.index('Kim')
    
    # 결과 문자열을 만들어 반환합니다
    return f'김서방은 {kim_index}에 있다'

# 방법 2
def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            return f'김서방은 {i}에 있다'