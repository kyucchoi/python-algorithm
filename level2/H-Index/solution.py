# 방법 1
def solution(citations):
    citations.sort(reverse=True)

    for i in range(len(citations)):
        if i >= citations[i]:
            return i
        
    return len(citations)

# 방법 2
def solution(citations):
    citations.sort(reverse=True)
    
    h_index = 0
    
    for i in range(len(citations)):

        # h = min(논문 수, 인용 횟수)
        h = min(i + 1, citations[i])
        
        h_index = max(h_index, h)
    
    return h_index