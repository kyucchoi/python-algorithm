def solution(myString):
    # 문자열을 'x'를 기준으로 나눔
    split_strings = myString.split('x')
    
    # 각 문자열의 길이를 구해서 리스트로 반환
    return [len(s) for s in split_strings]