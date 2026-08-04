# Exercise 35: Check if a list can be partitioned into two sublists with equal sum

def can_partition_dp(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    
    for num in nums:
        for i in range(target, num - 1, -1):
            if dp[i - num]:
                dp[i] = True
    
    return dp[target]

def can_partition_bruteforce(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    
    def dfs(index, current_sum):
        if current_sum == target:
            return True
        if index >= len(nums) or current_sum > target:
            return False
        return dfs(index + 1, current_sum + nums[index]) or dfs(index + 1, current_sum)
    
    return dfs(0, 0)

# Example
test1 = [1, 5, 11, 5]
test2 = [1, 2, 3, 5]
print(f"[1, 5, 11, 5] -> {can_partition_dp(test1)}")
print(f"[1, 2, 3, 5] -> {can_partition_bruteforce(test2)}")