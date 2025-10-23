import pandas as pd
from pycoingecko import CoinGeckoAPI
import matplotlib.pyplot as plt
import plotly.graph_objects as go


cg = CoinGeckoAPI()
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='USD', days=30)

# Pretvori u DataFrame
data = pd.DataFrame(bitcoin_data['prices'], columns=['TimeStamp', 'Price'])

# Pretvori timestamp iz milisekundi u stvarno vrijeme
data['Date'] = pd.to_datetime(data['TimeStamp'], unit='ms')

# (Opcionalno) postavi vrijeme kao indeks
#data.set_index('Date', inplace=True)

candlestick_data = data.groupby(data.Date.dt.date).agg({'Price':['min','max','first','last']})


print(candlestick_data)


# Crtanje grafa
plt.figure(figsize=(10,5))
plt.plot(data.index, data['Price'], label='Bitcoin (USD)', color='red')
plt.title('Bitcoin cijena - zadnjih 30 dana')
plt.xlabel('Vrijeme')
plt.ylabel('Cijena (USD)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()



fig = go.Figure(data=[
    go.Candlestick(
        x=candlestick_data.index,
        open=candlestick_data['Price']['first'],
        high=candlestick_data['Price']['max'],
        low=candlestick_data['Price']['min'],
        close=candlestick_data['Price']['last']
    )
])

fig.update_layout(
    xaxis_rangeslider_visible=False,
    xaxis_title='Date',
    yaxis_title='Price (USD $)',
    title='Bitcoin Candlestick Chart Over Past 30 Days'
)

fig.show()