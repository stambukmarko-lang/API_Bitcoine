import requests
import pandas as pd

url = "https://sekom-apps.com"
html = requests.get(url).text

tables = pd.read_html(html)
df = tables[0]
print(df.head())
