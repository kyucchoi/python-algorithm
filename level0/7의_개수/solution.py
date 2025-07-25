def solution(array):
    count = 0
    
    for num in array:
        # 각 숫자를 문자열로 변환하여 '7'의 개수 세기
        count += str(num).count('7')
    
    return count