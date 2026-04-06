def solution(picture, k):
    result = []
    
    for row in picture:
        scaled_row = ''.join(pixel * k for pixel in row)
        
        for _ in range(k):
            result.append(scaled_row)
    
    return result