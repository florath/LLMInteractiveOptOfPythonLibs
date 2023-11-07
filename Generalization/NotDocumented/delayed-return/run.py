# SPDX-License-Identifier: MIT
# Copyright 2023 by Andreas.Florath@telekom.de

import timeit
import functools

from utils import print_bytecode_size

from check_delayed_return import check_delayed_return
from check_direct_return import check_direct_return

NUMBER = 10000000
REPEAT = 100

print_bytecode_size(check_delayed_return)
print_bytecode_size(check_direct_return)

for i in [777, 1012]:
    res_delayed = timeit.repeat(functools.partial(check_direct_return, i), number=NUMBER, repeat=REPEAT)
    res_direct = timeit.repeat(functools.partial(check_delayed_return, i), number=NUMBER, repeat=REPEAT)

    res_delayed_min = min(res_delayed)
    res_direct_min = min(res_direct)

    print(i, res_delayed_min, res_direct_min, res_delayed_min / res_direct_min)
