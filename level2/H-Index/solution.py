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

        if citations[i] >= i + 1:
            h_index = i + 1
        else:
            break
    
    return h_index