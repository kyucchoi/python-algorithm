def solution(s, skip, index):
    result = ''
    
    # 알파벳 중 skip에 포함되지 않는 문자들만 모은 리스트
    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1) if chr(i) not in skip]
    
    for char in s:
        # 현재 문자의 알파벳 리스트 내 인덱스
        char_index = alphabet.index(char)
        # index만큼 뒤로 이동한 새 인덱스 (원형 리스트처럼 처리)
        new_index = (char_index + index) % len(alphabet)
        # 변환된 문자 추가
        result += alphabet[new_index]
    
    return result