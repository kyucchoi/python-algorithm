from collections import Counter

def solution(str1, str2):
    def make_multiset(s):
        s = s.lower()
        multiset = []
        
        for i in range(len(s) - 1):
            pair = s[i:i + 2]

            if pair.isalpha():
                multiset.append(pair)
        
        return multiset
    
    set1 = make_multiset(str1)
    set2 = make_multiset(str2)
    
    if not set1 and not set2:
        return 65536
    
    counter1 = Counter(set1)
    counter2 = Counter(set2)
    
    intersection = sum((counter1 & counter2).values())
    
    union = sum((counter1 | counter2).values())
    
    jaccard = intersection / union
    
    return int(jaccard * 65536)