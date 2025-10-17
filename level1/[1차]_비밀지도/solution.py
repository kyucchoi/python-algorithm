def solution(n, arr1, arr2):
    result = []
    
    for i in range(n):
        # 두 배열의 해당 위치 값을 이진수로 변환 후 OR 연산
        binary = bin(arr1[i] | arr2[i])[2:]  # bin() 결과는 '0b'로 시작하므로 [2:]로 제거
        
        # n 길이에 맞게 앞에 0 채우기
        binary = binary.zfill(n)
        
        row = binary.replace('1', '#').replace('0', ' ')
        
        result.append(row)
    
    return result