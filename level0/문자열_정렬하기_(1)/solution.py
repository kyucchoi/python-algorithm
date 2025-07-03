
def solution(my_string):
    # 숫자만 골라내기
    numbers = []
    
    for char in my_string:
        if char.isdigit():
            numbers.append(int(char))
    
    # 오름차순 정렬
    numbers.sort()
    
    return numbers