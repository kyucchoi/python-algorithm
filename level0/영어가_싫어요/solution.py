def solution(numbers):
    # 영어 숫자와 실제 숫자의 매핑
    word_to_digit = {
        'zero': '0',
        'one': '1', 
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    
    # 각 단어를 숫자로 치환
    for word, digit in word_to_digit.items():
        numbers = numbers.replace(word, digit)
    
    # 문자열을 정수로 변환하여 반환
    return int(numbers)