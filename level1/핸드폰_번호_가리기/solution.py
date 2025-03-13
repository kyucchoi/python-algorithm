def solution(phone_number):
    # 전화번호의 길이 구하기
    length = len(phone_number)
    
    # 뒷 4자리를 제외한 나머지 부분을 '*'로 변환
    masked_part = '*' * (length - 4)
    
    # 뒷 4자리 추출
    last_four = phone_number[-4:]
    
    # 마스킹된 부분과 뒷 4자리 합치기
    return masked_part + last_four