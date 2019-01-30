from flaskexample import app
from flask import request 
from flask import render_template
import pandas as pd
#from flaskexample.a_Model import ModelIt
from bs4 import BeautifulSoup
import requests
from gensim.models.doc2vec import Doc2Vec
from nltk.tokenize import word_tokenize
import pickle


@app.route('/')
#@app.route('/index')
#def index():
#	return "Hello, World!"

@app.route('/input')
def input():
	return render_template('input.html')

@app.route('/output', methods=['POST'])
def output():

	df1 = pd.read_pickle('df.pkl')
	results = []
	url = request.form.get('url')
	link = requests.get(url)

	soup = BeautifulSoup(link.text, 'lxml')
	news_text = soup.findAll('p')[1].text + soup.findAll('p')[3].text + soup.findAll('p')[5].text + soup.findAll('p')[7].text + soup.findAll('p')[11].text + soup.findAll('p')[20].text + \
			soup.findAll('p')[16].text
	news_text = news_text.lower()
	news_text = news_text.replace('.', '')
	news_text = news_text.replace(',', '')
	news_text = news_text.replace('\'', '')
	news_text = news_text.replace('\t', '')
	news_text = news_text.replace('"', '')
	news_text = news_text.replace('(', '')
	news_text = news_text.replace(')', '')
	news_text = news_text.replace(';', '')
	news_text = news_text.replace(':', '')
	news_text = news_text.replace('\n', '')
	news_text = news_text.replace('  ', '')

	model= Doc2Vec.load('d2v.model')
	test_data = word_tokenize(news_text)
	v1 = model.infer_vector(test_data)
	similar_doc = model.docvecs.most_similar([v1])


	for i in range(10):
		results.append(df1['Title'][int(similar_doc[i][0])])
#		result[df1['Title'][int(similar_doc[i][0])]] = 	df1['Description'][int(similar_doc[i][0])]
#	print(result)
	return render_template('output.html', results = results)
	












