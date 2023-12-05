import yfinance as yf
import mplfinance as mpf


ticker_symbol = input("Input ticker symbol : ").upper()

ticker = yf.Ticker(ticker_symbol)

data = ticker.history(period="3y", interval="1wk")

ema_short_period = 10
ema_medium_period = 30
ema_long_period = 50

data["EMA_short"] = data["Close"].ewm(span=ema_short_period, adjust=True).mean()
data["EMA_medium"] = data["Close"].ewm(span=ema_medium_period, adjust=True).mean()
data["EMA_long"] = data["Close"].ewm(span=ema_long_period, adjust=True).mean()

apds = [
    mpf.make_addplot(data["EMA_short"], color="green", label="EMA 10"),
    mpf.make_addplot(data["EMA_medium"], color="blue", label="EMA 30"),
    mpf.make_addplot(data["EMA_long"], color="red", label="EMA 50"),
]

mpf.plot(
    data,
    type="candle",
    figscale=1.75,    
    addplot=apds,
    style="yahoo",
    volume=True,
    title=f"{ticker_symbol} Weekly Chart", 
    panel_ratios=(4,1),
)
