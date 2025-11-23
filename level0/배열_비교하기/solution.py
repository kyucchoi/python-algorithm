# ?? 1
def solution(arr1, arr2):
    if len(arr1) < len(arr2):
        return -1
    elif len(arr1) > len(arr2):
        return 1
    
    sum_arr1 = sum(arr1)
    sum_arr2 = sum(arr2)
    
    if sum_arr1 > sum_arr2:
        return 1
    elif sum_arr1 < sum_arr2:
        return -1
    elif sum_arr1 == sum_arr2:
        return 0
    
# ?? 2
def solution(arr1, arr2):
    if len(arr1) != len(arr2):
        return 1 if len(arr1) > len(arr2) else -1
    
    sum1, sum2 = sum(arr1), sum(arr2)

    if sum1 > sum2:
        return 1
    elif sum1 < sum2:
        return -1
    elif sum1 == sum2:
        return 0