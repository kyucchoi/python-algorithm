def solution(s):
    # 영단어와 숫자 매핑
    word_to_num = {
        'zero' : '0',
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9'
    }
    
    # 모든 영단어를 숫자로 변환
    result = s
    
    for word, num in word_to_num.items():
        result = result.replace(word, num)
    
    # 문자열을 정수로 변환하여 반환
    return int(result)