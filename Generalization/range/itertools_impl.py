# SPDX-License-Identifier: MIT
# Copyright 2023 by Andreas.Florath@telekom.de

import itertools

def itertools_impl():
    c = itertools.count(0)
    while next(c) < 10000:
        pass
