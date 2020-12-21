class Solution:
    def change(self, amount, coins):
        return 0


def main():
    # input
    amount = 5
    coins = [1, 2, 5]
    # solution
    s = Solution()
    ret = s.change(amount, coins)
    # out
    print("ret:", ret)


if __name__ == "__main__":
    main()
