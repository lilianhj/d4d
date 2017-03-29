from __future__ import division
import numpy as np
import pandas as pd
import sys
import re

df = pd.read_csv("AK_12_countiesgrouped2.csv")
df["dPct"] = df["obama"]/df["totalvotes"]
df["rPct"] = df["romney"]/df["totalvotes"]
df["otherPct"] = df["other"]/df["totalvotes"]
df["dDRPct"] = df["obama"]/(df["obama"]+df["romney"])
df["rDRPct"] = df["romney"]/(df["obama"]+df["romney"])
df["leanD"] = df["obama"]/df["romney"]
df["leanR"] = df["romney"]/df["obama"]
df["CountyName"] = "None"
df["StateName"] = "Alaska"
df["StateAbbr"] = "AK"
df = df[['County','obama','romney','johnson', 'stein', 'other', 'totalvotes','CountyName', 'StateName', 'StateAbbr', 'dPct', 'rPct', 'leanD', 'leanR', 'otherPct', 'dDRPct', 'rDRPct']]

print("Writing to CSV...")

df.to_csv("AK_12_done.csv", index=False)

print("Script completed...")