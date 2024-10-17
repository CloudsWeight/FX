#!/usr/bin/env python
''' Fed API tools
'''
import requests
import json
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

class Fed:

	def __init__(self): 
		self.api = 'https://markets.newyorkfed.org'

	def __str__(self):
		return 'Fed API tools see fed -h'

	def get(self, url=None, H = None):
		if url != None:
			r = requests.get(url, headers=H)
			if r.status_code == 200:
				self.status_code = 200
				data = json.dumps(r.json(), indent=1)
				return data
			elif r.status_code != 200:
				try:
					data = json.dumps(r.json(), indent=1)
					return data
				except Exception as e:
					return f'Check status code: {r.status_code}\nEncountered error: {e}'
		else:
			return 'Needs a proper URL.'
			

	def fxs(self, date_type='trade', start='2010-01-10', end='2024-10-10', country='japan'):
		data = self.get(f'{self.api}\
/api/fxs/all/search.json?startDate={start}&endDate={end}\
&dateType={date_type}&counterparties={country}', {"Accept":"application/json"})
		#print(len(data))
		return json.loads(data) 

	def plot(self, x=None, y=None, country=None):
		plt.plot(x, y)
		plt.xticks(rotation=38)
		if country != None:
			plt.title(f'{country} Fed Swap Rates')
		else:
			plt.title('Swap Rates and Amount')
		n = len(x) // 13
		plt.ylabel('Interest Rates')
		plt.xlabel('Dates')
		ax = plt.gca()
		ax.xaxis.set_major_locator(MultipleLocator(n))
		plt.show()

	def lists(self, data = None):
		if data == None:
			return 'Needs fxs json'
		elif data != None:
			try:
				interest_rate, trade_date, amount = [], [], []
				counterparty = data['fxSwaps']['operations'][1]['counterparty']
				i = 0
				n = len(data['fxSwaps']['operations'])
				while i < n:
					interest_rate.append(data['fxSwaps']['operations'][i]['interestRate'])
					trade_date.append(data['fxSwaps']['operations'][i]['tradeDate'])
					i += 1
				return trade_date, interest_rate, counterparty
			except Exception as e:
				return e
				pass

	def fxs_counterparties(self): # returns list of swap country counter parties
		data = json.loads(self.get(f'{self.api}/api/fxs/list/counterparties.json'))
		country_list = []
		for i in data['fxSwaps']['counterparties']:
			country_list.append(i)
		return country_list

if __name__ == "__main__":
	fed = Fed()
	data = fed.fxs('trade', '2014-01-01', '2024-10-10', 'europe')

	x, y, counterparty = fed.lists(data)
	fed.plot(x, y, counterparty)