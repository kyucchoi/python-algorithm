def solution(myString):
    result = ''
    
    for c in myString:
        if c.lower() == 'a':
            result += 'A'
        else:
            result += c.lower()
            
    return result