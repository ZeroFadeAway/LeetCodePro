# -*- coding: utf-8 -*-


class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        return max(self.help(nums[1:]),self.help(nums[:-1]))

    def help(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        opt = [0 for i in range(n)]
        opt[0] = nums[0]
        opt[1] = max(nums[0], nums[1])
        for i in range(2, n):
            opt[i] = max(opt[i-1], opt[i-2]+nums[i])
        return opt[-1]


def main():
    # input
    nums = [2,7,9,3,1]
    # solution
    s = Solution()
    ret = s.rob(nums)
    # out
    print("ret:", ret)


if __name__ == "__main__":
    main()
