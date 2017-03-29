# run from command line: alaska_script.py ak_precincts.csv

from __future__ import division
import numpy as np
import pandas as pd
import sys
import re

file_name = sys.argv[1]

print("Reading file: " + file_name)

df = pd.read_csv(file_name)

# import states dict and convert to a dictionary
#df2 = pd.read_csv("States.csv")
#states = df2.set_index('StateAbbr').T.to_dict('list')


df["candidate"] = df["candidate"].str.lower()

# develop regex conditional statements to change values
# into standard naming convention
def format_values(str):
    johnson = '(johnson)'
    obama = '(obama)'
    romney = '(romney)'
    stein = '(stein)'

    if re.search(johnson, str):
        return "johnson"
    elif re.search(stein, str):
        return "stein"
    elif re.search(romney, str):
        return "romney"
    elif re.search(obama, str):
        return "obama"
    else:
        return "other"

# call conditional regex function to format the values for each candidate
df["candidate"] = df["candidate"].map(format_values)

# ensure votes is an integer and nulls are set to 0
df["votes"] = df["votes"].fillna(0.0).astype(int)

# pull out precinct numbers from precinct column (i.e. drop precinct names or separate into another column)
df["precno"], df["precname"] = df["precinct"].str.split(" ", 1).str

# pivot table so candidates are dimensions and fips/county are index
df = df.pivot_table(index=["precno","precname"],columns='candidate',values='votes')

# flatten column headers to index row - "level 0" the data
df = pd.DataFrame(df.to_records())

# existence check for files w/o particular candidates
if 'stein' not in df:
    df['stein'] = 0
if 'johnson' not in df:
    df['johnson'] = 0
if 'other' not in df:
    df['other'] = 0

# calc total votes
df["totalvotes"] = df["obama"] + df["stein"] + df["johnson"] + df["romney"] + df["other"]

# calculate other dimensions
df["dPct"] = df["obama"]/df["totalvotes"]
df["rPct"] = df["romney"]/df["totalvotes"]
df["otherPct"] = df["other"]/df["totalvotes"]
df["dDRPct"] = df["obama"]/(df["obama"]+df["romney"])
df["rDRPct"] = df["romney"]/(df["obama"]+df["romney"])
df["leanD"] = df["obama"]/df["romney"]
df["leanR"] = df["romney"]/df["obama"]

# match column naming structure
df.rename(columns={"precno": "Precinct", "precname":"PrecinctName"}, inplace=True)

# pull out the state abbreviation from the filename
stateAbbr = file_name[:2].upper()

# uppercase state abbreviation
df["StateAbbr"] =  stateAbbr

# get the matching value on StateAbbr join key
stateName = "AK"

# funky way to convert dict value to string
#stateNameStr = stateName

print("The State Name is " + stateName)

df["StateName"] = stateName

# define the out file name
file_name_out = stateAbbr + "_12.csv"

# explicit column positions
df = df[['Precinct','obama','romney','johnson', 'stein', 'other', 'totalvotes','PrecinctName', 'StateName', 'StateAbbr', 'dPct', 'rPct', 'leanD', 'leanR', 'otherPct', 'dDRPct', 'rDRPct']]

print("Writing to CSV...")

df.to_csv(file_name_out, index=False)

print("Script completed...")