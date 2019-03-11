#!/usr/bin/env python3
import tensorflow as tf
import urllib.request
import sys


def retrain():
    file = urllib.request\
        .urlopen('https://raw.githubusercontent.com/tensorflow/hub/master/examples/image_retraining/retrain.py')\
        .read()
    sys.argv = ['--image_dir', 'trainingdata']
    exec(file)


if __name__ == "__main__":
    print(tf.__version__)

    # retrain()
