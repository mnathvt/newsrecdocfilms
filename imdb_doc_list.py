#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 14:04:58 2019

@author: madhurima
"""

## this file produces the plot for the number of documentaries on IMDB as a function of year

#import the libraries
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
    
#reads the .tsv file downloaded from IMDB
f = pd.read_table('title.basics.tsv')

#f[['tconst', 'genres']].groupby('genres')

# lists the type of genres in the IMDB dataset
ftype = f['genres']

# extract a dataframe which says genre as documentary
df = f.loc[ftype.str.contains('Documentary', na=False)]

#retain only three columns - IMDB ID, title, startyear
df = df[['tconst', 'primaryTitle', 'startYear']]
df = df.reset_index(drop = True)


## check if the titles have english letters, drop those which do not have english letters in their titles
idx = []

for i in range(len(df)):
    if isEnglish(df['primaryTitle'][i]) == True:
        idx.append(i)
        
df = df.iloc[idx, :].reset_index(drop = True)

# to check if there are null values in the start year, if so, drop those
print(len(df[pd.to_numeric(df['startYear'], errors='coerce').isnull()]))
df['startYear'] = pd.to_numeric(df['startYear'], errors='coerce')
#print(len(df))

if len(df[df['startYear'].isnull()].index.tolist()) != 0:
    df.dropna(inplace=True)
#print(df[df['startYear'].isnull()].index.tolist())
#print(len(df))

#print(len(df[df['startYear'] < 1970]))


## retain movie titles from 1970-2018 only
df = df[(df['startYear'] >= 1970) & (df['startYear'] < 2019)]
df = df.reset_index(drop = True)
#print(len(df))
#df.head()

df['startYear'] = df['startYear'].astype(int)

## group by the year
#df1 = df[df['startYear'] >= 2000]
dfyr = df[['tconst', 'startYear']].groupby('startYear')
#dfyr = df1[['tconst', 'startYear']].groupby('startYear')


## finally plot the number of titles as a function of time
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


