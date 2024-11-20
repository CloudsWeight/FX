
import requests
import json 
import csv
import argparse
from datetime import datetime 
import os
from dotenv import load_dotenv
load_dotenv()

SECRET = os.environ['SECRET']
ACCTS = os.environ["ACCTS"]

class OandaApp():
	def __init__(self, token=None, account=None):
		self.BASE_URL ='https://api-fxtrade.oanda.com'
		if account is not None:
			self.account = {
					'URL':f'{self.BASE_URL}/v3/accounts', # Accounts Endpoint
					'acctId': account,
					'current':f'{account}'
					}
		self.account = {
					'URL':f'{self.BASE_URL}/v3/accounts', # Accounts Endpoint
					'acctId': ACCTS,
					'current':f'{ACCTS[0]}'
						}
		#if token is None:
			#self.token = SECRET
		self.token = token
		self.HEADER = { # Headers and Auth
					'Authorization': 'Bearer {}'.format(f'{SECRET}'),
				} 
		self.ENDPOINT = { 
						'instruments':f'{self.BASE_URL}/v3/instruments/',
						'candles': f'{self.BASE_URL}/candles?',
						}
		self.instruments = {
					# CURRENCY PAIRS
					'URL':f'{self.BASE_URL}/v3/instruments/', 
					'current':'USD_JPY',
					'eurusd':'EUR_USD', 
					'usdjpy':'USD_JPY', 
					'usdchf':'USD_CHF', 
					}
		self.count = {
						'URL':'count=',
						'current':'3' # [default=500, maximum=5000] dont use with "FROM and TO"
						}
		self.candles = {'URL':'/candles?',
						'granularity':{
						'current':'&granularity=H4',
						'5s':'&granularity=S5',
						'5m':'&granularity=M5',
						'15m':'&granularity=M15',
						'1h':'&granularity=H1', 
						'4h':'&granularity=H4',
						'd':'&granularity=D',
						'w':'&granularity=W',
						'M':'&granularity=M',
						 },
					}
		self.current_url = (
			 f"{self.instruments['URL']}{self.instruments['current']}"
			 f"{self.candles['URL']}"
			 f"{self.count['URL']}{self.count['current']}"
			 f"{self.candles['granularity']['current']}"
			 				) # As Above So Below
	# Example:	https://api-fxtrade.oanda.com/v3/instruments/EUR_USD/candles?count=6&price=M&granularity=S5
	######################## methods, man
	def query_accounts(self, url=None, header=None):
		if header is None:
			header = self.HEADER
		if url is None:
			url = f"{self.account['URL']}"
		r = requests.get(url=url, headers=header)
		print(f"{r.status_code}, /n {r.content}")

	def query_account(self, url=None, header=None):
		if header is None:
			header = self.HEADER
		if url is None:
			url = f"{self.account['URL']}/{self.account['current']}"
			print(url)
		r = requests.get(url=url, headers=header)
		print(f"{r.status_code}")

	def query_rate(self, url=None, header=None):
		if header is None:
			header = self.HEADER
		if url is None:
			url = self.current_url
		#print(f"\nURL: {self.current_url}")
		r = requests.get(url=url, headers=header)
		#print(r.status_code)
		#print(r.content)
		json_content = r.content.decode('utf-8')
		return(json_content)

	def deserialize(self, bin_data=None):
		if json is None:
			print("must provide binary data")
		else:
			json_string = bin_data.decode('utf-8')
			json_data = json.loads(json_string)
			#print(json.dumps(json_data, indent=2))
		return json_data

	def update_current_url(self): # if you make changes then update with this method 
		self.current_url = (
					 f"{self.instruments['URL']}{self.instruments['current']}"
					 f"{self.candles['URL']}"
					 f"{self.count['URL']}{self.count['current']}"
					 f"{self.candles['granularity']['current']}"
					 )

	def set_rate(self, rate=None):
		if rate is None:
			print("No rate set no change made")
		rate = rate.lower()
		self.instruments['current'] = self.instruments[rate]
		print(f"new rate {self.instruments['current']}\n ")     
		self.update_current_url()

	def test_query(self):
		rates = self.query_rate()
		return rates

################## Enter the dragon
if __name__ == '__main__':
	#print("Null stuff")
	trade = OandaApp()
	try:
		rates = trade.test_query()
	except:
		pass
	print(rates)


	

