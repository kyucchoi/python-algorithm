def solution(bin1, bin2):
    # 이진수 문자열을 십진수로 변환
    decimal1 = int(bin1, 2)
    decimal2 = int(bin2, 2)
    
    # 십진수로 덧셈 수행
    sum_decimal = decimal1 + decimal2
    
    # 결과를 다시 이진수 문자열로 변환
    return bin(sum_decimal)[2:]