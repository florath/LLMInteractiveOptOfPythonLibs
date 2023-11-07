# SPDX-License-Identifier: MIT
# Copyright 2023 by Andreas.Florath@telekom.de

import dis
import io
import timeit
import functools

from ternary import ternary
from explicit_if import explicit_if

from utils import print_bytecode_size

NUMBER=1000000
REPEAT=10

print_bytecode_size(ternary)
print_bytecode_size(explicit_if)

for tup in ((100, 7), (7, 100)):
    res_ternary_all = timeit.repeat(stmt=functools.partial(ternary, tup[0], tup[1]), repeat=REPEAT, number=NUMBER)
    res_explicit_if_all = timeit.repeat(stmt=functools.partial(explicit_if, tup[0], tup[1]), repeat=REPEAT, number=NUMBER)

    res_ternary_min = min(res_ternary_all)
    res_explicit_if_min = min(res_explicit_if_all)

    print(tup, res_ternary_min, res_explicit_if_min, "%5.3g" % (res_ternary_min / res_explicit_if_min))
    
