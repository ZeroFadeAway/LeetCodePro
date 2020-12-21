class Solution:
    def carFleet(self, target, position, speed):
        if target == 0:
            return 0
        if not position or not speed:
            return 0
        cars = [[position[i], speed[i]] for i in range(len(position))]
        cars.sort(key=lambda x: x[0], reverse=True)
        n = len(position)
        ret = n
        for i in range(n - 1):
            for j in range(i + 1, n):
                if meet(cars[i], cars[j]):
                    ret -= 1
        return ret


def meet(a, b):
    return True


def main():
    # input
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    # solution
    s = Solution()
    ret = s.carFleet(target, position, speed)
    # out
    print("ret:", ret)


if __name__ == "__main__":
    main()
