# SPDX-License-Identifier: MIT
# Copyright 2023 by Andreas.Florath@telekom.de

import fixedint

def fixedint_impl():
    i = fixedint.UInt16(0)
    while i < 10000:
        i += 1
    
