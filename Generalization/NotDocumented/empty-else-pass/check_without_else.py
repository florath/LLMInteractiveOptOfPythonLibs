# SPDX-License-Identifier: MIT
# Copyright 2023 by Andreas.Florath@telekom.de

# Defining the optimized function without "else: pass"
def check_without_else(i):
    if i < 1000:
        i *= 2
    return i + 1
