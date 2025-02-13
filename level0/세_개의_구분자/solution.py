import re

def solution(myStr):
    # a, b, c를 기준으로 문자열을 분할하고 빈 문자열 제거
    result = [x for x in re.split('[abc]', myStr) if x]
    
    # 결과가 비어있으면 ["EMPTY"] 반환
    return result if result else ["EMPTY"]