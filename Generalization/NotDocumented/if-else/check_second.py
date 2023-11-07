# SPDX-License-Identifier: MIT
# Copyright 2023 by Andreas.Florath@telekom.de

def check_second(i):
    if i >= 1000:
        i += 2
    else:
        i += 3
    return i + 1
