# Python 3.7
import math

def isodd(num):
    return int(math.sqrt(num) + 0.5) ** 2 == num


def test():
    print(isodd(4))
    print(isodd(5))

if __name__ == '__main__':
    test()

