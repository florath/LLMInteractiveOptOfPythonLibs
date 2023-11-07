# SPDX-License-Identifier: MIT
# Copyright 2023 by Andreas.Florath@telekom.de

import timeit
import io

from linebyline import linebyline
from tuple_impl import tuple_impl

from utils import print_bytecode_size

NUMBER=10000000
REPEAT=25

print_bytecode_size(tuple_impl)
print_bytecode_size(linebyline)

for i in range(5):
    res_tuple_all = timeit.repeat(stmt=tuple_impl, repeat=REPEAT, number=NUMBER)
    res_linebyline_all = timeit.repeat(stmt=linebyline, repeat=REPEAT, number=NUMBER)

    res_tuple_min = min(res_tuple_all)
    res_linebyline_min = min(res_linebyline_all)

    res_tuple_max = max(res_tuple_all)
    res_linebyline_max = max(res_linebyline_all)

    print(res_tuple_min, res_linebyline_min, "%5.3g" % (res_linebyline_min / res_tuple_min))
    print(res_tuple_max, res_linebyline_max, "%5.3g" % (res_linebyline_max / res_tuple_max))

    print(res_tuple_all)
    print(res_linebyline_all)
