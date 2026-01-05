def solution(n, costs):
    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
            
        return parent[x]
    
    def union(parent, rank, a, b):
        a = find(parent, a)
        b = find(parent, b)
        
        if a == b:
            return False
        
        if rank[a] < rank[b]:
            parent[a] = b
        elif rank[a] > rank[b]:
            parent[b] = a
        else:
            parent[b] = a
            rank[a] += 1
        
        return True
    
    costs.sort(key=lambda x: x[2])
    
    parent = list(range(n))
    rank = [0] * n
    
    total_cost = 0
    edges = 0
    
    for a, b, cost in costs:
        if union(parent, rank, a, b):
            total_cost += cost
            edges += 1
            
            if edges == n - 1:
                break
    
    return total_cost