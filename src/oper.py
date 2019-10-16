#!bin/bash

import math


class Operations:
    @staticmethod
    def sum(a, b):
        return a+b

    @staticmethod
    def sub(a, b):
        return a-b

    @staticmethod
    def div(a, b):
        return a/b

    @staticmethod
    def mul(a, b):
        return a*b

    @staticmethod
    def square(a):
        return math.sqrt(a)


if __name__ == '__main__':
    op = Operations()

    print("sum(1+2): ", op.sum(1, 2))
    print("sub(2-1): ", op.sub(2, 1))
    print("mul(1*2): ", op.mul(1, 2))
    print("div(2%1): ", op.div(2, 1))
    print("square(4): ", op.square(4))
