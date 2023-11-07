#!/usr/bin/env python3

import timeit
import dis
import functools

from utils import print_bytecode_size

from check_first import check_first
from check_second import check_second

NUMBER = 10000000
REPEAT = 100

print_bytecode_size(check_first)
print_bytecode_size(check_second)

i = 777

res_first = timeit.repeat(functools.partial(check_first, i), number=NUMBER, repeat=REPEAT)
res_second = timeit.repeat(functools.partial(check_second, i), number=NUMBER, repeat=REPEAT)

res_first_min = min(res_first)
res_second_min = min(res_second)

print(i, res_first_min, res_second_min, res_first_min / res_second_min)
