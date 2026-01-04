def solution(A, B):
    A.sort()  # A 배열을 오름차순 정렬
    B.sort(reverse=True)  # B 배열을 내림차순 정렬
    
    total = 0
    
    for i in range(len(A)):
        total += A[i] * B[i]  # 정렬된 두 배열의 같은 인덱스 원소를 곱하여 더함
    
    return total