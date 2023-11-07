# SPDX-License-Identifier: MIT
# Copyright 2023 by Andreas.Florath@telekom.de

import io
import timeit

from append import append
from generator import generator

from utils import print_bytecode_size

NUMBER=100000
REPEAT=10

print_bytecode_size(append)
print_bytecode_size(generator)


res_append_all = timeit.repeat(stmt=append, repeat=REPEAT, number=NUMBER)
res_generator_all = timeit.repeat(stmt=generator, repeat=REPEAT, number=NUMBER)

res_append_min = min(res_append_all)
res_generator_min = min(res_generator_all)

print(res_append_min, res_generator_min, "%5.3g" % (res_append_min / res_generator_min))
    
