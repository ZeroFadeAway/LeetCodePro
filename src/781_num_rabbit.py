from collections import Counter
import math


class Solution:
    def numRabbits(self, answers):
        n = len(answers)
        if n == 0:
            return 0
        rabbit_map = Counter(answers)
        res = 0
        for rabbit in rabbit_map.keys():
            temp = num_of_rabbit(rabbit, rabbit_map[rabbit])
            res += temp

        return res


def num_of_rabbit(key, value):
    rabbit = key + 1
    n = math.ceil(value / rabbit)
    return n * rabbit


def main():
    # input
    answers = [1, 1, 2]
    s = Solution()
    ret = s.numRabbits(answers)

    # result
    print("ret:", ret)


if __name__ == "__main__":
    main()
