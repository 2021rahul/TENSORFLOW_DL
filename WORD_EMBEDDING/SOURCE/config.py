#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 17:51:32 2018

@author: rahul
"""

import os

# DIRECTORY INFORMATION
ROOT_DIR = os.path.abspath('..')
DATA_DIR = os.path.join(ROOT_DIR, 'DATASET')
OUT_DIR = os.path.join(ROOT_DIR, 'RESULT')
MODEL_DIR = os.path.join(ROOT_DIR, 'MODEL')

# DATA INFORMATION
TRAIN_FILENAME = 'text8.zip'
OUT_FILENAME = 'text8_plot.png'
EXPECTED_BYTES = 31344016
VOCABULARY_SIZE = 50000
BATCH_SIZE = 128

# MODEL INFORMATION
EMBEDDING_SIZE = 128
SKIP_WINDOW = 1
NUM_SKIP = 2
NUM_SAMPLED = 64
VALID_SIZE = 16
VALID_WINDOW = 100

assert BATCH_SIZE % NUM_SKIP == 0
assert NUM_SKIP <= 2 * SKIP_WINDOW

# RANDOM NUMBER GENERATOR INFORMATION
SEED = 128

# TRAINING INFORMATION
NUM_STEPS = 200001
