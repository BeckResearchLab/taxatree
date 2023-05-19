#!/usr/bin/env python3
"""
Read a predefined file (taxa.csv), parse it and do some type revision.
Write out a FASTA file for down stream processing.
"""

import numpy as np
import pandas as pd


# the input csv has column 0 as a numbered index, we want taxonid
# use the rest of the colums
csv = pd.read_csv("taxa.csv", usecols=range(1,11))
csv.set_index("taxid", inplace=True)

print(csv.head(2))

seqfield = "16s_seq"
# note: use the trailing underscore below for parsing downstream
# files with sed or other string matching to prevent partial 
# matches from replacing, e.g. 1234 matching 12345
# useful for subbing in full tax or other info
for index, row in csv.iterrows():
    print(f">taxid_{index}_\n{row[seqfield]}")
