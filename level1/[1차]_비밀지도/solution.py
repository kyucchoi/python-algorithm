def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        num = arr1[i] | arr2[i]
        
        binary = bin(num)[2:].zfill(n)
        
        row = binary.replace('1', '#').replace('0', ' ')
        
        answer.append(row)
    
    return answer