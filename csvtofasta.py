#!/usr/bin/env python3
"""
Read a predefined file (taxa.csv), parse it and do some type revision.
Write out a FASTA file for down stream processing.
"""

import numpy as np
import pandas as pd


# the input csv has column 0 as a numbered index, we want taxonid
# use the rest of the colums
csv = pd.read_csv("taxa.csv", index_col=1, usecols=range(2,11))

print(csv.head())
