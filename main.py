import requests
import datetime
import os

os.chdir(r'Some DIR')

share=requests.get('https://www.dividends.sg/prices.json')
raw_msg=share.json()
watch_list={
    'ES3':'STI SPDR',
    'G3B':'NIKKO AM',
    'AJBU':'KEPPEL DC REIT',
    'C38U':'Capitaland Mall Trust',
    'J69U':'Frasers Centrepoint Trust',
    'G13':'Genting Singapore PLC',
    'Z74':'Singtel'
    }
result=[]
for item in raw_msg:
    if item['ticker'] in watch_list.keys():
        result.append(str(item)+'-'+str(watch_list[item['ticker']]))

with open('tracker.txt',mode='a') as f:
    f.write(str(datetime.datetime.now())+'\n')
    for item in result:
        f.write(str(item)+'\n')     
