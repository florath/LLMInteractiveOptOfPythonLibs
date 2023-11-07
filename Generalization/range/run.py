# SPDX-License-Identifier: MIT
# Copyright 2023 by Andreas.Florath@telekom.de

import io
import timeit

from utils import get_bytecode_size, print_bytecode_size

from for_repeat import for_repeat
from while_impl import while_impl
from numpy_impl import numpy_impl
from fixedint_impl import fixedint_impl
from range_unroll import range_unroll
from itertools_impl import itertools_impl

NUMBER=10000
REPEAT=10

print_bytecode_size(for_repeat)
orig = min(timeit.repeat(stmt=for_repeat, repeat=REPEAT, number=NUMBER))

for impl in (while_impl, numpy_impl, fixedint_impl, range_unroll, itertools_impl):
    print(impl.__name__)
    print(impl.__name__, "Length", get_bytecode_size(impl))
    
    exec_time = timeit.repeat(stmt=impl, repeat=REPEAT, number=NUMBER)
    print(impl.__name__, "ExecTime", min(exec_time))

    print(impl.__name__, "RelTime %5.3g" % (min(exec_time) / orig))
