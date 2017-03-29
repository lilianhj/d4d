# run from command line: python county_merge.py AK_12.csv AlaskaPrecinctBoroughMapping.csv

from __future__ import division
import numpy as np
import pandas as pd
import sys
import re

#file_name1 = sys.argv[1]
#file_name2 = sys.argv[2]

ak = pd.read_csv("AK_12.csv")
df = pd.read_csv("AlaskaPrecinctBoroughMapping.csv")

dfdrop = df[df['Year'] == 2012]
dfsort = dfdrop.sort_values(by='County')
print(dfsort)
joined = pd.merge(ak, dfsort, how='left', on='Precinct')
joined = joined[['County','Precinct','obama','romney','johnson', 'stein', 'other', 'totalvotes','PrecinctName', 'StateName', 'StateAbbr', 'dPct', 'rPct', 'leanD', 'leanR', 'otherPct', 'dDRPct', 'rDRPct']]
#joined = pd.merge(df, df1, on="Precinct", how="outer")
joined = joined.sort_values(by='County')
print("Writing to CSV...")

joined.to_csv("AK_12_withcounty.csv", index=False)

print("Script completed...")