# SPDX-License-Identifier: MIT
# Copyright 2023 by Andreas.Florath@telekom.de

from utils import print_bytecode_size



def _getextrema_optimized(h):
    def minmax(h):
        res_min, res_max = 255, 0
        for i in range(256):
            if h[i]:
                res_min = i
                break
        for i in range(255, -1, -1):
            if h[i]:
                res_max = i
                break
        if res_max >= res_min:
            return res_min, res_max
        else:
            return (255, 0)

    v = []
    for i in range(0, len(h), 256):
        v.append(minmax(h[i:i+256]))
    return v


def _getextrema_orig(self):
    """Get min/max values for each band in the image"""

    def minmax(histogram):
        n = 255
        x = 0
        for i in range(256):
            if histogram[i]:
                n = min(n, i)
                x = max(x, i)
        return n, x  # returns (255, 0) if there's no data in the histogram

    v = []
    for i in range(0, len(self.h), 256):
        v.append(minmax(self.h[i:]))
    return v


print_bytecode_size(_getextrema_optimized)
print_bytecode_size(_getextrema_orig)
