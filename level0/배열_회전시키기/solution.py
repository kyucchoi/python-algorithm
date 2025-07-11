def solution(numbers, direction):
    if direction == 'right':
        # 오른쪽 회전: 마지막 원소를 맨 앞으로
        return [numbers[-1]] + numbers[:-1]
    else:  # direction == 'left'
        # 왼쪽 회전: 첫 번째 원소를 맨 뒤로
        return numbers[1:] + [numbers[0]]