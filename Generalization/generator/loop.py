# SPDX-License-Identifier: MIT
# Copyright 2023 by Andreas.Florath@telekom.de

def loop(h):
    for i in range(256):
        if h[i]:
            return i
