def solution(num, total):
    # 연속된 num개 수의 합 공식: num * a + num * (num - 1) / 2 = total
    # 따라서 a = (total - num * (num - 1) / 2) / num
    first_num = (total - num * (num - 1) // 2) // num

    result = [first_num + i for i in range(num)]

    return result