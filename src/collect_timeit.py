#!/usr/bin/env python
#
# SPDX-License-Identifier: MIT
# Copyright 2023 by Andreas.Florath@telekom.de

from PIL import Image, ImageStat
import json
import os
import tarfile
import time
import sys
import csv
import timeit

IMAGENET_DIR="/llm-opt/devel/imagenet-1k/data"
IMAGENET_FILES=[
    "test_images.tar",
    "train_images_0.tar",
    "train_images_1.tar",
    "train_images_2.tar",
    "train_images_3.tar",
    "train_images_4.tar",
    "val_images.tar",
]

NUMBER=100
REPEAT=10

def main():
    res_extrema = {}
    cnt = 0

    typename = sys.argv[1]

    with open(f'timeit-{typename}.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',', dialect='unix',
                                quotechar='\\', quoting=csv.QUOTE_MINIMAL)

        for tfname in IMAGENET_FILES:
            with tarfile.open(os.path.join(IMAGENET_DIR, tfname),
                              "r", bufsize=1024*1024*1024) as tf: # r:gz
                print("Call getmembers for [%s]" % tfname)
                tfmembers = tf.getmembers()
                print("  Member count[%s]" % len(tfmembers))
                for tfinfo in tfmembers:
                    cnt += 1
                    tfcontent = tf.extractfile(tfinfo)
                    img = Image.open(tfcontent)
                    stat = ImageStat.Stat(img)
                    res = stat._getextrema()

                    exec_times = timeit.repeat(stmt=stat._getextrema, repeat=REPEAT, number=NUMBER)
                    exec_times_ms = map(lambda x: int(x * 1000000), exec_times)

                    csv_writer.writerow([tfname, tfinfo.name, img.mode, img.width, img.height, len(res)] + list(exec_times_ms))
                    print(tfname, tfinfo.name, img.mode, img.width, img.height)


if __name__ == '__main__':
    main()
