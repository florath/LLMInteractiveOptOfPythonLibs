# SPDX-License-Identifier: MIT
# Copyright 2023 by Andreas.Florath@telekom.de

def ternary(res_min, res_max):
    return res_min, res_max if res_max >= res_min else (255, 0)
