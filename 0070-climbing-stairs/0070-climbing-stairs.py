class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 1] # dp[0] and dp[1] are base cases
        for i in range(2, n + 1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n]

# test
s = Solution()
print(s.climbStairs(2)) # 2
print(s.climbStairs(6)) # 13
