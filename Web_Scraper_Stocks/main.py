import datetime
import pandas as pd

stockcode='SPY'

ts1= str(int(datetime.datetime(2023,1,15).timestamp()))
ts2= str(int(datetime.datetime(2023,1,25).timestamp()))

interval='1d'
# interval='1wk'
# interval='1mo'

event= 'history'
# events= 'div'
# events= 'splits'

url ='https://query1.finance.yahoo.com/v7/finance/download/'\
     + stockcode + '?period1=' + ts1 + '&period2=' +ts2+ '&interval='\
     + interval+ '&events=' +event+ '&includeAdjustedClose=true'

print(url)
print(ts1)
print(ts2)

stockdata = pd.read_csv(url)
stockdata