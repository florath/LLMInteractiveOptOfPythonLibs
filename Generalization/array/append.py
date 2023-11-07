# SPDX-License-Identifier: MIT
# Copyright 2023 by Andreas.Florath@telekom.de

def append():

    def some_data(i):
        return (i, i+1)

    v = []
    for i in range(0, 100):
        v.append(some_data(i))
    return v
