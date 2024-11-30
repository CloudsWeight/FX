import numpy as np 
import pandas as pd 
import json
import random
import matplotlib as plt
from OandaFile import OandaApp as oa 

class Fx():

	def __init__(self):
		self.oa = oa()

	def get_rates(self, rate='eurusd', tf='M5', count=300):
		''' rates: eurusd, usdjpy, eurgbp, eurusd, chfjpy
			tf: M1, M5, M15, H1, H4, D, W, M
			count: 1 - 5000 
		'''
		return self.oa.get_rate(rate,tf,count)

	def df_rates(self, data=None):
		if data != None:
			candles = data['candles']
			df = pd.DataFrame([{
			    'time': candle['time'],
			    'open': float(candle['mid']['o']),
			    'high': float(candle['mid']['h']),
			    'low': float(candle['mid']['l']),
			    'close': float(candle['mid']['c']),
			    'volume': candle['volume']
			} for candle in candles])

		return df 

	def df_echarts(self, df=None):
		e_df = df[['time', 'open', 'close', 'low', 'high']].values.tolist()
		#print(e_df)
		return e_df
