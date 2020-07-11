import os
import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import logging
import itertools
# Logging -----------------------------------------------------


def get_logger(logger_name):
    root = logging.getLogger(logger_name)
    root.setLevel(logging.DEBUG)

    out_handler = logging.StreamHandler(stream=sys.stdout)
    out_handler.setLevel(logging.DEBUG)
    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    out_handler.setFormatter(logging.Formatter(fmt=fmt,  datefmt="%H:%M:%S"))
    root.addHandler(out_handler)
    return root


logger = get_logger(__name__)

# IO files -----------------------------------------------------

dirname, filename = os.path.split(os.path.abspath(__file__))
DATA_PATH = os.path.join(dirname, '../data/')
PROCESSED_PATH = os.path.join(DATA_PATH, 'processed/')
RAW_PATH = os.path.join(DATA_PATH, 'raw/')


def load_raw(filename):
    logger.info(f"Loading {filename}")
    path = os.path.join(RAW_PATH, filename)
    return pd.read_csv(path)


def save_processed(df, filename):
    logger.info(f"Saving {filename}")
    if not os.path.exists(PROCESSED_PATH):
        os.makedirs(PROCESSED_PATH)
    path = os.path.join(PROCESSED_PATH, filename)
    return df.to_csv(path)
