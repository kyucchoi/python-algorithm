def solution(common):
    diff1 = common[1] - common[0]
    diff2 = common[2] - common[1]

    if diff1 == diff2:
        return common[-1] + diff1
    else:
        ratio = common[1] // common[0]

        return common[-1] * ratio