import yfinance as yf

def get_spx_options():
    ticker = yf.Ticker("^SPX")
    expirations = ticker.options  # List of expiries
    opt = ticker.option_chain(expirations[0])  # Use nearest expiry
    calls = opt.calls
    puts = opt.puts
    return calls, puts
