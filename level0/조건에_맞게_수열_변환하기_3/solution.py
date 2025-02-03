def solution(arr, k):
    result = []
    
    # k가 홀수인 경우
    if k % 2 == 1:
        for x in arr:
            result.append(x * k)

    # k가 짝수인 경우
    else:
        for x in arr:
            result.append(x + k)

    return result