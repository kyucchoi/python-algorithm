# index() 방법
def solution(seoul):
    kim_index = seoul.index('Kim')
    
    return f'김서방은 {kim_index}에 있다'

# 방법 2
def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            return f'김서방은 {i}에 있다'