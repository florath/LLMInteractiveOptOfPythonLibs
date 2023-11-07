# SPDX-License-Identifier: MIT
# Copyright 2023 by Andreas.Florath@telekom.de

import timeit
import functools

from utils import print_bytecode_size

from check_with_else import check_with_else
from check_without_else import check_without_else

NUMBER = 10000000
REPEAT = 100

print_bytecode_size(check_with_else)
print_bytecode_size(check_without_else)

for i in [777, 1012]:
    res_with = timeit.repeat(functools.partial(check_with_else, i), number=NUMBER, repeat=REPEAT)
    res_without = timeit.repeat(functools.partial(check_without_else, i), number=NUMBER, repeat=REPEAT)

    res_with_min = min(res_with)
    res_without_min = min(res_without)

    print(i, res_with_min, res_without_min, res_with_min / res_without_min)
