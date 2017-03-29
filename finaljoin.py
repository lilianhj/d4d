from __future__ import division
import numpy as np
import pandas as pd
import sys
import re

ak = pd.read_csv("AK_12_done.csv")
pres = pd.read_csv("PresidentialElectionResults2012.csv")

final = pd.concat([ak, pres])

print("Writing to CSV...")

final.to_csv("PresidentialElectionResults2012_Final.csv", index=False)

print("Script completed...")