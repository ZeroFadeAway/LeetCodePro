class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n
        opt = [0 for i in range(n+1)]
        opt[0] = 0
        opt[1] = 1
        opt[2] = 2
        for i in range(3,n+1):
            opt[i] = opt[i-1] + opt[i-2]
        print(opt)
        return opt[-1]





def main():
    # input
    n = 10
    # solution
    s = Solution()
    ret = s.climbStairs(n)
    # out
    print("ret:", ret)


if __name__ == "__main__":
    main()