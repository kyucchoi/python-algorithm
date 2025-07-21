def solution(my_string):
    total = 0
    current_number = ''
    
    for char in my_string:
        if char.isdigit():
            # 숫자인 경우 현재 숫자에 추가
            current_number += char
        else:
            # 문자인 경우, 지금까지의 숫자를 합에 추가
            if current_number:
                total += int(current_number)
                current_number = ''
    
    # 문자열 끝에 숫자가 있는 경우 처리
    if current_number:
        total += int(current_number)
    
    return total