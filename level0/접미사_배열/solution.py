def solution(my_string):
    result = []
    
    # 모든 가능한 접미사 만들기
    for i in range(len(my_string)):
        result.append(my_string[i:])
        
    # 사전순 정렬
    result.sort()
    
    return result