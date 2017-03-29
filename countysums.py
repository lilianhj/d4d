from __future__ import division
import numpy as np
import pandas as pd
import sys
import re

df = pd.read_csv("AK_12_withcounty.csv")
df['groupby_obama'] = df.groupby(by=['County'], as_index=False)['obama'].transform('sum')
df['groupby_romney'] = df.groupby(by=['County'], as_index=False)['romney'].transform('sum')
df['groupby_johnson'] = df.groupby(by=['County'], as_index=False)['johnson'].transform('sum')
df['groupby_stein'] = df.groupby(by=['County'], as_index=False)['stein'].transform('sum')
df['groupby_other'] = df.groupby(by=['County'], as_index=False)['other'].transform('sum')
df['groupby_total'] = df.groupby(by=['County'], as_index=False)['totalvotes'].transform('sum')
newdf = df[['County','groupby_obama','groupby_romney','groupby_johnson', 'groupby_stein', 'groupby_other', 'groupby_total']]
newdf = newdf.drop_duplicates(['County'])
newdf.rename(columns={"groupby_obama": "obama", "groupby_romney": "romney", "groupby_johnson": "johnson", "groupby_stein": "stein", "groupby_other": "other", "groupby_total": "totalvotes"}, inplace=True)
newdf["dPct"] = newdf["obama"]/newdf["totalvotes"]
newdf["rPct"] = newdf["romney"]/newdf["totalvotes"]
newdf["otherPct"] = newdf["other"]/newdf["totalvotes"]
newdf["dDRPct"] = newdf["obama"]/(newdf["obama"]+newdf["romney"])
newdf["rDRPct"] = newdf["romney"]/(newdf["obama"]+newdf["romney"])
newdf["leanD"] = newdf["obama"]/newdf["romney"]
newdf["leanR"] = newdf["romney"]/newdf["obama"]
#newdf["CountyName"] =  "None"
#newdf["StateName"] =  "Alaska"
#newdf["StateAbbr"] =  "AK"
newdf = df[['County','obama','romney','johnson', 'stein', 'other', 'totalvotes','dPct', 'rPct', 'leanD', 'leanR', 'otherPct', 'dDRPct', 'rDRPct']]
print("Writing to CSV...")

newdf.to_csv("AK_12_sumsdone.csv", index=False)

print("Script completed...")