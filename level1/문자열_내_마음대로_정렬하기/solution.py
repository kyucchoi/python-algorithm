def solution(strings, n):
    # n번째 문자를 기준으로 정렬하고, 같은 경우 문자열 전체를 기준으로 정렬
    return sorted(strings, key=lambda x: (x[n], x))