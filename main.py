import pandas as pd
from pycoingecko import CoinGeckoAPI
import matplotlib.pyplot as plt


cg = CoinGeckoAPI()
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='USD', days=30)

# Pretvori u DataFrame
dt = pd.DataFrame(bitcoin_data['prices'], columns=['TimeStamp', 'Price'])

# Pretvori timestamp iz milisekundi u stvarno vrijeme
dt['Time'] = pd.to_datetime(dt['TimeStamp'], unit='ms')

# (Opcionalno) postavi vrijeme kao indeks
dt.set_index('Time', inplace=True)

print(dt.head())


# Crtanje grafa
plt.figure(figsize=(10,5))
plt.plot(dt.index, dt['Price'], label='Bitcoin (USD)', color='orange')
plt.title('Bitcoin cijena - zadnjih 30 dana')
plt.xlabel('Vrijeme')
plt.ylabel('Cijena (USD)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()