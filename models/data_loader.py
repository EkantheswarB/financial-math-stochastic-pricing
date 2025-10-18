import datetime as dt
import yfinance as yf

def get_spx_options(nearest=True, expiry_index=0):
    ticker = yf.Ticker("^SPX")
    expirations = ticker.options
    if not expirations:
        raise ValueError("No option expirations available for ^SPX.")
    expiry = expirations[expiry_index] if not nearest else expirations[0]
    chain = ticker.option_chain(expiry)
    calls, puts = chain.calls.copy(), chain.puts.copy()
    calls["option_type"] = "call"
    puts["option_type"] = "put"
    calls["expiry"] = expiry
    puts["expiry"] = expiry
    return calls, puts

def get_spx_spot():
    # SPX spot via ^SPX (last close)
    spx = yf.Ticker("^SPX").history(period="1d")
    return float(spx["Close"].iloc[-1])

def get_risk_free_rate():
    """
    Simple proxy: 3-Month Treasury Bill ^IRX (annualized discount rate, approx).
    For cleaner control, hardcode a short-rate like 0.045 (4.5%).
    """
    try:
        t = yf.Ticker("^IRX").history(period="5d")
        rf_annual = float(t["Close"].dropna().iloc[-1]) / 100.0  # percent → decimal
        return rf_annual
    except Exception:
        return 0.045  # fallback 4.5%

