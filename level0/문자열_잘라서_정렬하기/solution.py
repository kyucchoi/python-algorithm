def solution(myString):
    # 1. 문자열을 'x'를 기준으로 나눔
    split_strings = myString.split('x')
    
    # 2. 빈 문자열을 제외하고 리스트 생성
    filtered_strings = []

    for s in split_strings:
        if s != '':          # 빈 문자열이 아닌 경우에만
            filtered_strings.append(s)  # 리스트에 추가
    
    # filtered_strings = [s for s in split_strings if s != '']
    
    # 3. 사전순으로 정렬
    return sorted(filtered_strings)