#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 14:04:58 2019

@author: madhurima
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#check if the string is in English
def isEnglish(s):
    try:
        s.encode('ascii')
    except UnicodeEncodeError:
        return False
    else:
        return True
    
#reads the     
f = pd.read_table('title.basics.tsv')

f[['tconst', 'genres']].groupby('genres')


ftype = f['genres'][0]

df = f.loc[f['genres'] == ftype]
df = df[['tconst', 'primaryTitle', 'startYear']]

df = df.reset_index(drop = True)
#this resultant dataframe contains only the 3 columns - title, year and imdb ID


idx = []

for i in range(len(df)):
    if isEnglish(df['primaryTitle'][i]) == True:
        idx.append(i)
        
df = df.iloc[idx, :].reset_index(drop = True)
    
print(len(df[pd.to_numeric(df['startYear'], errors='coerce').isnull()]))
df['startYear'] = pd.to_numeric(df['startYear'], errors='coerce')
print(len(df))

if len(df[df['startYear'].isnull()].index.tolist()) != 0:
    df.dropna(inplace=True)
print(df[df['startYear'].isnull()].index.tolist())
print(len(df))

print(len(df[df['startYear'] < 1950]))

df = df[df['startYear'] >= 1950]
df = df.reset_index(drop = True)
print(len(df))
df.head()

df['startYear'] = df['startYear'].astype(int)

df.to_csv('imdb_doc_list.csv', index = False, header = True)

df1 = df[df['startYear'] >= 2000]
#dfyr = df[['tconst', 'startYear']].groupby('startYear')
dfyr = df1[['tconst', 'startYear']].groupby('startYear')

plt.figure(figsize=(8,8))
plt.plot(dfyr.startYear.first(), dfyr.tconst.nunique(), '.-',
         linewidth = 2.5, markersize = 10)

axis_font = {'size':'20', 'color':'black'}
axis_tick_font = {'size':'12', 'color':'black'}

plt.xlabel('year', **axis_font)
plt.ylabel('# of films', **axis_font)
plt.xticks(**axis_tick_font)
plt.yticks(**axis_tick_font)
plt.xticks(np.arange(2000, 2021, 2))
plt.savefig('film_freq.pdf')
plt.savefig('film_freq1.pdf')


