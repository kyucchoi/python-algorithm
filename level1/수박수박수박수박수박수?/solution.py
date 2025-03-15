# 방법 1
def solution(n):
    # 결과 문자열을 저장할 변수
    result = ""
    
    # n번 반복하면서 패턴 생성
    for i in range(n):
        # 짝수 인덱스(0, 2, 4, ...)에는 "수" 추가
        if i % 2 == 0:
            result += "수"
        # 홀수 인덱스(1, 3, 5, ...)에는 "박" 추가
        else:
            result += "박"
            
    return result

# 방법 2
def solution(n):
    # "수박" 패턴을 만들고 n 길이만큼 잘라내기
    return ("수박" * n)[:n]

# 내 방법
def solution(n):
    answer = ''
    
    if n % 2 == 0:
        answer += '수박' * (n // 2)
    else:
        answer += '수박' * (n // 2) + '수'
        
    return answer