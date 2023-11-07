# SPDX-License-Identifier: MIT
# Copyright 2023 by Andreas.Florath@telekom.de

import io
import timeit
import functools

from loop import loop
from generator import generator

from utils import print_bytecode_size

NUMBER=100000
REPEAT=10

# dis.dis(generator)

print_bytecode_size(loop)
print_bytecode_size(generator)

for i in (0, 15, 127, 239, 255):
    h = [0] * 512
    h[i] = 1

    res_loop = min(timeit.repeat(stmt=functools.partial(loop, h), repeat=REPEAT, number=NUMBER))
    res_generator = min(timeit.repeat(stmt=functools.partial(generator, h), repeat=REPEAT, number=NUMBER))

    print(i, res_loop, res_generator, "%5.3g" % (res_generator / res_loop))
