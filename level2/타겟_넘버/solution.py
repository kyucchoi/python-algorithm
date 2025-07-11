def solution_dfs(numbers, target):
    def dfs(index, current_sum):
        # 모든 숫자를 다 사용했을 때
        if index == len(numbers):
            return 1 if current_sum == target else 0
        
        # 현재 숫자를 더하거나 빼는 경우
        count = 0
        count += dfs(index + 1, current_sum + numbers[index])  # +
        count += dfs(index + 1, current_sum - numbers[index])  # -
        
        return count
    
    return dfs(0, 0)