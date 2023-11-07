# SPDX-License-Identifier: MIT
# Copyright 2023 by Andreas.Florath@telekom.de

from itertools import islice

def generator(h):
    return next((i for i, x in islice(enumerate(h), 256) if x), None)
