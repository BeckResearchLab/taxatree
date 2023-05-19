#!/usr/bin/env python3
"""
Read a predefined file (taxa.csv), parse it and do some type revision.
Write out a FASTA file for down stream processing.
"""

import numpy as np
import pandas as pd


# the input csv has column 0 as a numbered index, we want taxonid
# use the rest of the colums and force types back to int for ids
csv = pd.read_csv("taxa.csv", index_col=1, usecols=range(2,11), 
                dtype={
                    "superkingdom": np.int32,
                    "phylum": np.int32,
                    "class": np.int32,
                    "order": np.int32,
                    "family": np.int32,
                    "genus": int
                }
            )


print(csv.head())
