def solution(my_string):
    result = ''
    seen = set()
    
    for char in my_string:
        if char not in seen:
            result += char
            seen.add(char)
    
    return result