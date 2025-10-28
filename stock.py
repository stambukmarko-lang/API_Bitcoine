import yfinance as yf
# Download historical data for a stock
msft = yf.Ticker("AMD")
# prikaz za period - 7d = 7 dana  / 1mo = 1 mjesec  / 1y = 1 godina / max = maksimalno 
msft_data = msft.history(period="7d")
# Display the downloaded data
print(msft_data.head())
print()