from http.client import GONE
import plotly.graph_objs as go
from chart_studio import plotly
from matplotlib.pyplot import *
from pycoingecko import CoinGeckoAPI
import pandas as pd
cg = CoinGeckoAPI()
bitcoin_data = cg.get_coin_market_chart_by_id(
    id='bitcoin', vs_currency='usd', days=30)
data = pd.DataFrame(bitcoin_data, columns=['TimeStamp', 'Price'])
data['Date'] = pd.to_datetime(data['TimeStamp'], unit='ms')
candlestick_data = data.groupby(data.Date.dt.date).agg(
    {'Price': ['max', 'min', 'first', 'last']})
fig = go.Figure(data=[go.Candlestick(x=candlestick_data.index, open=candlestick_data['Price']['first'],
                                     high=candlestick_data['Price']['max'],
                                     low=candlestick_data['Price']['min'],
                                     close=candlestick_data['Price']['last'])])
print(bitcoin_data)
fig.update_layout(xaxis_rangeslider_visible=True, xaxis_title='date', yaxis_title='price',
                  title='Bitcoin Price over the 30 days')
plot(fig, filename='BitcoinPrice.html')
