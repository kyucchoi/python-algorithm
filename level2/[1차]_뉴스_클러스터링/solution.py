from collections import Counter

def solution(str1, str2):
    # 다중집합 만들기
    def make_multiset(s):
        s = s.upper()
        multiset = []
        
        for i in range(len(s) - 1):
            pair = s[i:i + 2]

            if pair.isalpha():
                multiset.append(pair)
        
        return multiset
    
    set1 = make_multiset(str1)
    set2 = make_multiset(str2)
    
    # 둘 다 공집합
    if not set1 and not set2:
        return 65536
    
    counter1 = Counter(set1)
    counter2 = Counter(set2)
    
    # 교집합: 각 원소의 최솟값
    intersection = counter1 & counter2
    
    # 합집합: 각 원소의 최댓값
    union = counter1 | counter2
    
    # 자카드 유사도
    jaccard = sum(intersection.values()) / sum(union.values())
    
    return int(jaccard * 65536)