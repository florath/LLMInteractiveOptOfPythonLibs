#!/usr/bin/env python3
#
# Merges the two CSV files into one.
# It's done line by line with some additional checks.
# The runtime is computed: from both input files the min() is used and placed in the new file.
#
# SPDX-License-Identifier: MIT
# Copyright 2023 by Andreas.Florath@telekom.de

import csv

def main():

    count=0

    res = [0] * 10000
    
    with open('timeit-original.csv', newline='') as csvorig:
        reader_orig = csv.reader(csvorig, delimiter=',', quotechar='\\', dialect="unix")
        with open('timeit-optimized.csv', newline='') as csvopt:
            reader_opt = csv.reader(csvopt, delimiter=',', quotechar='\\', dialect="unix")
            # For further analysis
            with open(f'timeit-merged.csv', 'w', newline='') as csvmerge:
                writer_merge = csv.writer(csvmerge, delimiter=',', dialect='unix',
                                          quotechar='\\', quoting=csv.QUOTE_MINIMAL)
                while True:
                    try:
                        row_orig = next(reader_orig)
                        if row_orig is None:
                            break
                    except StopIteration:
                        break

                    row_opt = next(reader_opt)

                    # print("R ORIG", row_orig)
                    # print("R OPT", row_opt)

                    for i in range(6):
                        # print("DIFF", row_orig[i], "=?=", row_opt[i])
                        assert row_orig[i] == row_opt[i]

                    min_orig = min(row_orig[6:])
                    min_opt = min(row_opt[6:])

                    speedup = int(float(min_orig) / float(min_opt))
                    print(row_orig[0], row_orig[1], min_orig, min_opt, speedup)

                    assert speedup < 10000
                    res[speedup] += 1

                    writer_merge.writerow(row_orig[:6] + [min_orig, min_opt, speedup])

                    count += 1

    # Find max entry
    max_idx = 0
    for idx in range(10000):
        if res[idx] != 0:
            max_idx = idx

    for idx, ae in enumerate(res):
        print(f"({idx},{ae}) ", end="")
        if idx > max_idx:
            break
    print()

                    
if __name__ == '__main__':
    main()
