#!/usr/bin/env python3
"""
Read a predefined file (taxa.csv), parse it and do some type revision.
Write out a FASTA file for down stream processing.
"""

import click
import numpy as np
import pandas as pd


@click.command()
@click.option('--input', '-i', 'input_',
              required=True, type=str, default="taxa.csv")
@click.option('--output', '-o', 'output_',
              required=True, type=str, default="16s_seq.fna")
def csvtofasta(input_, output_):
    """
    Read a predefined file (taxa.csv), parse it and do some type revision.
    Write out a FASTA file for down stream processing.
    """

    # the input csv has column 0 as a numbered index, we want taxonid
    # use the rest of the colums
    print(f"reading from {input_}")
    csv = pd.read_csv(input_, usecols=range(1,11))
    csv.set_index("taxid", inplace=True)

    seqfield = "16s_seq"
    # note: use the trailing underscore below for parsing downstream
    # files with sed or other string matching to prevent partial 
    # matches from replacing, e.g. 1234 matching 12345
    # useful for subbing in full tax or other info
    print(f"saving to {output_}")
    with open(output_, "w") as outf:
        for index, row in csv.iterrows():
            outf.write(f">taxid_{index}_\n{row[seqfield]}")

if __name__ == '__main__':
    csvtofasta()
