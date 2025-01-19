def solution(str1, str2):
    # str2의 모든 가능한 부분 문자열 확인
    for i in range(len(str2) - len(str1) + 1):
        if str2[i : i + len(str1)] == str1:
            return 1
    return 0