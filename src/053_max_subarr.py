class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        dp = [0 for i in range(n)]
        dp[0] = nums[0]
        res = dp[0]
        for i in range(1, n):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
            res = max(res, dp[i])

        return res


def main():
    # input
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # solution
    s = Solution()
    ret = s.maxSubArray(nums)
    # out
    print("ret:", ret)


if __name__ == "__main__":
    main()
