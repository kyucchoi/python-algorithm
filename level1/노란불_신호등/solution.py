def solution(signals):
    from math import lcm
    from functools import reduce
    
    cycles = [sum(s) for s in signals]
    total_lcm = reduce(lcm, cycles)
    
    yellow_sets = []

    for g, y, r in signals:
        cycle = g + y + r
        yellow = set()
        
        for t in range(1, total_lcm + 1):
            pos = (t - 1) % cycle

            if g <= pos < g + y:
                yellow.add(t)

        yellow_sets.append(yellow)
    
    common = yellow_sets[0]
    
    for s in yellow_sets[1:]:
        common = common & s
    
    return min(common) if common else -1