# SPDX-License-Identifier: MIT
# Copyright 2023 by Andreas.Florath@telekom.de

def generator():

    def some_data(i):
        return (i, i+1)

    return [some_data(i) for i in range(0, 100)]
