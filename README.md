Insight project files

The IMDB list is obtained from https://www.imdb.com/interfaces/
I used the title.basics.tsv file as my data.
Total number of entries in this file: 5570541
Total number of documentary entries: 95532
That is, 1.715% of this movie list is documentaries (titles in both English and other languages).

For this work, selected only those titles which are written in English and in the year range 1950-present (2019).
The file imdb_doc_list.csv contains imdb_id, titles, year for documentary films.


Used Google pre-trained word2vec model (available https://code.google.com/archive/p/word2vec/).

The plots show the increase of number of documentary films over the years, there is a steep increase since 2010.
The plot goes down to 0 for 2020, because of no records! 
