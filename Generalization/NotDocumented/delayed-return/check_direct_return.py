# SPDX-License-Identifier: MIT
# Copyright 2023 by Andreas.Florath@telekom.de

def check_direct_return(i):
    res = None
    if i < 1000:
        res = i
    else:
        res = 3
    return res
