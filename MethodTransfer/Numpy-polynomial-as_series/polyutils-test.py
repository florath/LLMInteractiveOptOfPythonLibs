#!/usr/bin/env python3
#
# SPDX-License-Identifier: MIT
# Copyright 2023 by Andreas.Florath@telekom.de

import numpy as np
from numpy.polynomial import polyutils as pu

from numpy.testing import (
    assert_raises, assert_equal, assert_,
)

import functools
import timeit

def func_tests_docu(testf):
    '''Functional tests from the documentation'''
    
    a = np.arange(4)
    assert_equal(testf(a), [np.array([0.]), np.array([1.]), np.array([2.]), np.array([3.])])

    b = np.arange(6).reshape((2,3))
    assert_equal(testf(b), [np.array([0., 1., 2.]), np.array([3., 4., 5.])])
    
    assert_equal(testf((1, np.arange(3), np.arange(2, dtype=np.float16))),
                 [np.array([1.]), np.array([0., 1., 2.]), np.array([0., 1.])])

    assert_equal(testf([2, [1.1, 0.]]),
                 [np.array([2.]), np.array([1.1])])

    assert_equal(testf([2, [1.1, 0.]], trim=False),
                 [np.array([2.]), np.array([1.1, 0. ])])


def func_test_unit(testf):
    '''Functional tests from the unit tests wich come with numpy'''

    # check exceptions
    assert_raises(ValueError, testf, [[]])
    assert_raises(ValueError, testf, [[[1, 2]]])
    assert_raises(ValueError, testf, [[1], ['a']])
    # check common types
    types = ['i', 'd', 'O']
    for i in range(len(types)):
        for j in range(i):
            ci = np.ones(1, types[i])
            cj = np.ones(1, types[j])
            [resi, resj] = testf([ci, cj])
            assert_(resi.dtype.char == resj.dtype.char)
            assert_(resj.dtype.char == types[i])


def exec_time(testf):
    tdata = [
        np.arange(4),
        np.arange(6).reshape((2,3)),
        (1, np.arange(3), np.arange(2, dtype=np.float16)),
        [2, [1.1, 0.]]
    ]

    res_times = []
    
    for td in tdata:
        res = timeit.repeat(functools.partial(testf, td), repeat=100, number=100000)
        res_times.append(min(res))

    return res_times

def test_wrapper(testf, td):
    try:
        testf(td)
        assert False
    except ValueError:
        pass
        #assert False


def exec_time_exceptions(testf):
    tdata = [
        [[]],
        [[[1, 2]]],
        [[1], ['a']],
        [[1], [], [2], [3]],
        [[1], [], [2], [3]] + [ [7] * 100 ],
    ]

    res_times = []
    
    for td in tdata:
        res = timeit.repeat(functools.partial(test_wrapper, testf, td), repeat=100, number=1000)
        res_times.append(min(res))

    return res_times


def main():
    func_tests_docu(pu.as_series)
    func_test_unit(pu.as_series)
    func_tests_docu(pu.as_series_opt)
    func_test_unit(pu.as_series_opt)
    res_orig = exec_time(pu.as_series)
    print("Orig exec time", res_orig)
    res_opt = exec_time(pu.as_series_opt)
    print("Opt exec time", res_opt)

    diff = []
    for i in range(len(res_orig)):
        diff.append("%5.3f" % (res_orig[i] / res_opt[i]))
    print(diff)
    
    res_orig_ex = exec_time_exceptions(pu.as_series)
    print("Orig exption exec time", res_orig_ex)
    res_opt_ex = exec_time_exceptions(pu.as_series_opt)
    print("OPT exption exec time", res_opt_ex)

    diff = []
    for i in range(len(res_orig_ex)):
        diff.append("%5.3f" % (res_orig_ex[i] / res_opt_ex[i]))
    print(diff)
        

if __name__ == '__main__':
    main()
