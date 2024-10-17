#!/usr/bin/env python
  '''
    Basic usage is to create a bd object and make requests to get datasets and parameters.
    The BEA API method is to find your dataset, inspect the list of parameters, 
    find the parameter you like then get the parameter values, then use that to build
    a request to get data from the specific table values you need.
    Here is an example URL to retrieve JSON data from a dataset for all years: 

    'https://apps.bea.gov/api/data?&UserID=\
{self.bea_key}&method=GetData&datasetname=FixedAssets&TableName=FAAt105&year=x&ResultFormat=JSON'

    Basic Data Retrieval syntax examples for BEA API:
        - method = (GetParameterList, GetData, GetParameterValues)
        - dataset = 'FixedAssets'
        - ParameterName = TableName,
        - TableName = FAAt107
        - year = available or 'x' for all
    
    Its up to you to find the specific datasets needed.

    DatasetNames: ( see req_sets())
    NIPA
    NIUnderlyingDetail
    MNE
    FixedAssets
    ITA
    IIP
    InputOutput
    IntlServTrade
    IntlServSTA
    GDPbyIndustry
    Regional
    UnderlyingGDPbyIndustry
    APIDatasetMetaData
    '''
import requests
from key import BEA_Key
import json

class BeaData():
  

    def __init__(self):
        self.bea_key = self._bea_key()
        self.format = 'JSON'
        self.base = f'https://apps.bea.gov/api/data?&UserID={self.bea_key}&method='

    def __str__(self):
        return str(self.get_data())

    def _bea_key(self):
        bea_key = BEA_Key()
        return bea_key.key
    # urls
    def url_sets(self): # URL only request all the datasets
        bea_url = f'https://apps.bea.gov/api/data?&UserID=\
{self.bea_key}&method=GETDATASETLIST&ResultFormat=JSON'
        return bea_url 

    def url_param_list(self, dataset="ITA" ):
        method='GetParameterList'
        bea_url = f'https://apps.bea.gov/api/data?&UserID=\
{self.bea_key}&method={method}&datasetname={dataset}&ResultFormat=JSON'
        return bea_url 

    def get_param_vals(self, dataset="ITA", ):
        method='GetParameterValues'
        bea_url = f'https://apps.bea.gov/api/data?&UserID=\
{self.bea_key}&method={method}&datasetname={dataset}&ResultFormat=JSON'
        return bea_url 

# data request
    def req_dt(self, dataset='FixedAssets', table="FAAt105"):
        method = 'GetData'
        bea_url = f'https://apps.bea.gov/api/data?&UserID=\
{self.bea_key}&method={method}\
&datasetname={dataset}\
&TableName={table}&year=x&ResultFormat=JSON'
# split url for easier typing
        return bea_url #{self.bea_key}&method=GetData&datasetname=FixedAssets&TableName=FAAt105&year=x&ResultFormat=JSON'

# !raw request
    def req(self,url = None): # basic request to any url given
        try:
            if url != None:
                #print(f'\nRequesting URL: {url}\n')
                r = requests.get(url)
                data = json.dumps(r.json(), indent=1)
                return data
            else:
                print('You need to pass an URL')
                pass
        except Exception as e:
            print(f'Encountered an error: {e}')

# loop dataset names
    def req_sets(self):
        # returns a list of the dataset names
        url = self.url_sets()
        resp = json.loads(self.req(url))
        #print("Creating a list of the dataset names:")
        val = resp["BEAAPI"]["Results"]["Dataset"]
        n = len(val)
        i = 0
        da = []
        while i < n:
            da.append(val[i]["DatasetName"])
            #print(val[i]["DatasetName"])
            i+=1
        return da

    def find_all_params_all_sets(self):
        # returns all parameters available for all data sets
        sets = self.req_sets()
        n, i = len(sets), 0
        all_arr = []
        while i < n:
            resp = json.loads(self.req(self.url_param_list(sets[i])))
            all_arr.append(resp)
            i +=1
        #print(json.dumps(all_arr, indent=1))
        return all_arr

    def dict_set_params(self, all_arr=[]):
        n, i = len(all_arr), 0
        print(n)
        sets = []
        while i < n:
            j, k = 0, len(all_arr[i]["BEAAPI"]["Results"]["Parameter"])
            params = []
            
            i +=1
        return sets
            


# __ main
def main():
    bd = BeaData()
    #print(bd.req(bd.url_param_list("UnderlyingGDPbyIndustry")))
    
    print(bd.req('https://markets.newyorkfed.org//beta/api/ambs/all/results/details/last/1.json'))
    
   
if __name__ == "__main__":
    main()