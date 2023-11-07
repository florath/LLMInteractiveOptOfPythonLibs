# SPDX-License-Identifier: MIT
# Copyright 2023 by Andreas.Florath@telekom.de

import numpy as np

def numpy_impl():
    i = np.ushort(0)
    while i < 10000:
        i += 1
    
