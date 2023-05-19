#!/usr/bin/env python3
"""
Read a predefined file (taxa.csv), parse it and do some type revision.
Write out a FASTA file for down stream processing.
"""

import numpy as np
import pandas as pd


# the input csv has column 0 as a numbered index, we want taxonid
# use the rest of the colums and force types back to int for ids
csv = pd.read_csv("taxa.csv", index_col=1, usecols=range(2,11))
csv["superkingdom"] = csv["superkingdom"].astype(np.int32)
csv["phylum"] = csv["phylum"].astype(np.int32)
csv["class"] = csv["class"].astype(np.int32)
csv["order"] = csv["order"].astype(np.int32)
csv["family"] = csv["family"].astype(np.int32)
csv["genus"] = csv["genus"].astype(np.int32) 

print(csv.head())
