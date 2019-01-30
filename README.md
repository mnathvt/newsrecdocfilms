Insight project files

The IMDB list is obtained from https://www.imdb.com/interfaces/
I used the title.basics.tsv file as my data.
Total number of entries in this file: 5570541
Total number of documentary entries: 95532
That is, 1.715% of this movie list is documentaries (titles in both English and other languages).

For this work, selected only those titles which are written in English and in the year range 1970-present (2019), last ~50 years.
Considered only the start year of the films.
The file imdb_doc_list.csv contains imdb_id, titles, year for documentary films. There are ~52,000+ titles.


Dropped those titles for which the plot summary does not exist on IMDB. This further reduces the number of films in the list.
The final version of the dataset contains ~23,000+ titles with description with start year in 1970s onwards. This list is
saved as imdb_desc.csv.


Used Google pre-trained word2vec model (available https://code.google.com/archive/p/word2vec/).

The plots show the increase of number of documentary films over the years, there is a steep increase since 2010.
The plot goes down to 0 for 2020, because of no records! 


