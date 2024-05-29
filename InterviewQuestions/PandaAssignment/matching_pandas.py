import os
import pandas as pd


def analyze(factbook_pop, factbook_obesity):

	# read csv files as we need
	population = pd.read_csv(factbook_pop, usecols=[1,2], header=0, names=['Country', 'Population'])
	obesity = pd.read_csv(factbook_obesity, usecols=[1,2], header=0, names=['Country', 'Obesity Rate'])
	
	# merging two dataset into one by column Country
	data = pd.merge(population, obesity, on='Country')

	# filter data by Population and Obesity Rate
	data = data[data['Population'] > 10**7]
	data = data[data['Obesity Rate'] > 20]

	# sort data  by Obesity Rate and select top 10
	data = data.sort_values('Obesity Rate', ascending=False).iloc[:10]
	
	# set indexes from 1 to 10
	data.index = list(range(1,11))

	return data

path = os.path.join(os.path.dirname(__file__), 'data')
factbook_pop_path = os.path.join(path, 'c2119.csv')
factbook_obesity_path = os.path.join(path, 'c2228.csv')
print(path, factbook_pop_path, factbook_obesity_path)
print(analyze(factbook_pop_path, factbook_obesity_path))