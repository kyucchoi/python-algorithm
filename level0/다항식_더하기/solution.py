def solution(polynomial):
    terms = polynomial.split(' + ')
    
    x_coeff = 0
    const_sum = 0
    
    for term in terms:
        if 'x' in term:
            if term == 'x':
                x_coeff += 1
            else:
                coeff = int(term.replace('x', ''))
                x_coeff += coeff
                
        else:
            const_sum += int(term)
            
    result = ''
    
    if x_coeff > 0:
        if x_coeff == 1:
            result += 'x'
        else:
            result += str(x_coeff) + 'x'
        
        if const_sum > 0:
            result += ' + ' + str(const_sum)
            
    elif const_sum > 0:
        result += str(const_sum)
    
    return result