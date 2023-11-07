# SPDX-License-Identifier: MIT
# Copyright 2023 by Andreas.Florath@telekom.de

def explicit_if(res_min, res_max):
    if res_max >= res_min:
        return (255, 0)
    else:
        return res_min, res_max
