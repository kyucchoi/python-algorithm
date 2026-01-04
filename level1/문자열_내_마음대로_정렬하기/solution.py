# 방법 1
def solution(strings, n):
    # n번째 문자를 기준으로 정렬하고, 같은 경우 문자열 전체를 기준으로 정렬
    return sorted(strings, key=lambda x: (x[n], x))

# 방법 2
def solution(strings, n):
    modified_strings = []

    for string in strings:
        modified_strings.append(string[n] + string)
    
    modified_strings.sort()
    
    result = []
    
    for string in modified_strings:
        result.append(string[1:])
    
    return result