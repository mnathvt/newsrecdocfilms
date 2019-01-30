import pandas as pd
import pickle
import numpy as np
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize

df = pd.read_csv('doc_list/list_all.csv')
df1 = df.drop_duplicates('Title', keep = False)
if df1.isnull().values.any() == True:
	df1.dropna(inplace=True)

df1 = df1.sample(frac=1).reset_index(drop=True)

df1.to_pickle('df.pkl')

with open('brendan/news_2k_filt.pkl', 'rb') as infile:
	facts = pd.DataFrame.from_dict(pickle.load(infile))
with open('brendan/op_2k_filt.pkl', 'rb') as infile:
	op = pd.DataFrame.from_dict(pickle.load(infile))

news_df = pd.concat([op, facts])
news_df['body'] = news_df['body'].str.lower()
news_df['body'] = news_df['body'].str.replace('\n', '')
news_df['body'] = news_df['body'].str.replace('{', '')
news_df['body'] = news_df['body'].str.replace('[', '')
news_df['body'] = news_df['body'].str.replace('}', '')
news_df['body'] = news_df['body'].str.replace('(', '')
news_df['body'] = news_df['body'].str.replace(')', '')
news_df['body'] = news_df['body'].str.replace(']', '')
news_df['body'] = news_df['body'].str.replace('_', '')
news_df['body'] = news_df['body'].str.replace('-', '')
news_df['body'] = news_df['body'].str.replace('>', '')
news_df['body'] = news_df['body'].str.replace(';', '')
news_df['body'] = news_df['body'].str.replace('?', '')
news_df['body'] = news_df['body'].str.replace('!', '')
news_df['body'] = news_df['body'].str.replace(':', '')
news_df['body'] = news_df['body'].str.replace('\t', ' ')
news_df['body'] = news_df['body'].str.replace('\'', ' ')

#print(news_df['body'][:10])
news_df = news_df[['author', 'body', 'source']].copy()
news_df = news_df.sample(frac = 1).reset_index(drop = True)


#model = Doc2Vec(vector_size=20, min_count=0, alpha=0.025, min_alpha=0.0025)
tagged_data = [TaggedDocument(words=word_tokenize(_d), tags=[str(i)]) for i, _d in enumerate(df1['Description'].tolist())]

max_epochs = 50
vec_size = 20
alpha = 0.025

model = Doc2Vec(vector_size=vec_size, alpha=alpha, in_alpha=0.0025, min_count=1, dm =1)

model.build_vocab(tagged_data)

for epoch in range(max_epochs):
    #print('iteration {0}'.format(epoch))
    model.train(tagged_data,
                total_examples=model.corpus_count,
                epochs=model.iter)
    # decrease the learning rate
    model.alpha -= 0.0002
    # fix the learning rate, no decay
    model.min_alpha = model.alpha

model.save("d2v.model")
print("Model Saved")








