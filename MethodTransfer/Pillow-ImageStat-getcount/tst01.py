#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright 2023 by Andreas.Florath@telekom.de

import functools
import operator
import random
import timeit

class PerfOpt:

    def __init__(self, h):
        self.h = h

    def _getcount(self):
        """Get total number of pixels in each layer"""

        v = []
        for i in range(0, len(self.h), 256):
            v.append(functools.reduce(operator.add, self.h[i : i + 256]))
        return v

    def _getcount_optimized(self):
        """Get total number of pixels in each layer"""
        return [sum(self.h[i: i + 256]) for i in range(0, len(self.h), 256)]

test_data = [
    [0] * 512,
    [x for x in range(0, 345)],
    [random.randint(0, 255) for _ in range(256)],
    [random.randint(0, 255) for _ in range(1024)]
]
REPEAT=25
NUMBER=100000

def func_tests():
    for td in test_data:
        po = PerfOpt(td)
        assert po._getcount() == po._getcount_optimized()

def perf_tests():
    for td in test_data:
        po = PerfOpt(td)
        nres = timeit.repeat(po._getcount, repeat=REPEAT, number=NUMBER)
        ores = timeit.repeat(po._getcount_optimized, repeat=REPEAT, number=NUMBER)

        min_nres = min(nres)
        min_ores = min(ores)

        print(min_nres, min_ores, min_nres / min_ores)


def main():
    func_tests()
    perf_tests()


if __name__ == '__main__':
    main()
