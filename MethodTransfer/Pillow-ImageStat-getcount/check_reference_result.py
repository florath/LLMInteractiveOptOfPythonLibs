#!/usr/bin/env python
#
# Be sure to use the venv-patched environment
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
    "test_images.tar",
    "train_images_0.tar",
    "train_images_1.tar",
    "train_images_2.tar",
    "train_images_3.tar",
    "train_images_4.tar",
    "val_images.tar",
]

def check_same(la, lb):
    assert len(la) == len(lb)
    for i in range(len(la)):
        assert la[i][0] == lb[i][0]
        assert la[i][1] == lb[i][1]
    return True

def main():
    res_extrema = {}
    cnt = 0

    for tfname in IMAGENET_FILES:
        print("Reading existing file")
        with open(f"{tfname}-orig_extrema.json", "r") as oejfd:
            res_extrema = json.load(oejfd)
        print("Read existing file with [%d] entries" % len(res_extrema))
        
        with tarfile.open(os.path.join(IMAGENET_DIR, tfname),
                          "r", bufsize=1024*1024*1024) as tf: # r:gz
            print("Call getmembers for [%s]" % tfname)
            tfmembers = tf.getmembers()
            print("  Member count[%s]" % len(tfmembers))
            for tfinfo in tfmembers:
                cnt += 1

                if tfinfo.name not in res_extrema:
                    print("Name [%s] not in result" % tfinfo.name)
                    assert False
                tfcontent = tf.extractfile(tfinfo)
                img = Image.open(tfcontent)
                stat = ImageStat.Stat(img)
                res = stat._getcount()

                assert res == res_extrema[tfinfo.name]

                # check_same(res, res_extrema[tfinfo.name])
                print("  %08d" % cnt, tfname, tfinfo, res, res_extrema[tfinfo.name])

if __name__ == '__main__':
    main()
