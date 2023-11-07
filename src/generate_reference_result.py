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

IMAGENET_DIR="/llm-opt/devel/imagenet-1k/data"
IMAGENET_FILES=[
    "test_images.tar.gz",
    "train_images_0.tar.gz",
    "train_images_1.tar.gz",
    "train_images_2.tar.gz",
    "train_images_3.tar.gz",
    "train_images_4.tar.gz",
    "val_images.tar.gz",
]

def write_extrema(bname, res_extrema):
    with open(f"{bname}-orig_extrema.json", "w") as oejfd:
        json.dump(res_extrema, oejfd)

def main():
    res_extrema = {}
    cnt = 0

    bname = sys.argv[1]

    if os.path.exists(f"{bname}-orig_extrema.json"):
        print("Reading existing file")
        with open(f"{bname}-orig_extrema.json", "r") as oejfd:
            res_extrema = json.load(oejfd)
        print("Read existing file with [%d] entries" % len(res_extrema))

    IMAGENET_FILES = [ sys.argv[1], ]
    
    for tfname in IMAGENET_FILES:
        with tarfile.open(os.path.join(IMAGENET_DIR, tfname),
                          "r", bufsize=1024*1024*1024) as tf: # r:gz
            print("Call getmembers for [%s]" % tfname)
            tfmembers = tf.getmembers()
            print("  Member count[%s]" % len(tfmembers))
            for tfinfo in tfmembers:
                cnt += 1
                if tfinfo.name in res_extrema:
                    print("  %08d" % cnt, "Skipping [%s]" % tfinfo.name)
                    continue
                tfcontent = tf.extractfile(tfinfo)
                img = Image.open(tfcontent)
                stat = ImageStat.Stat(img)
                res = stat._getextrema()
                res_extrema[tfinfo.name] = res
                print("  %08d" % cnt, tfname, tfinfo, res)

                if cnt % 1000 == 0:
                    write_extrema(bname, res_extrema)

    write_extrema(bname, res_extrema)

if __name__ == '__main__':
    main()
