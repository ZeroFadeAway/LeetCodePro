class Solution:
    def decode(self, encoded, first):
        n = len(encoded)
        arr = [0 for i in range(n + 1)]
        arr[0] = first
        for i in range(n):
            arr[i + 1] = arr[i] ^ encoded[i]

        return arr


def main():
    # input
    encoded = [1, 2, 3]
    first = 1

    # solution
    s = Solution()
    ret = s.decode(encoded, first)

    # result
    print("ret:", ret)


if __name__ == "__main__":
    main()
