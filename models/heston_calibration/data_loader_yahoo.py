import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from scipy.stats import norm

# --- Black–Scholes call for implied vol extraction ---
def bs_price_call(S, K, T, r, q, sigma):
    if T <= 0 or sigma <= 0:
        return max(S*np.exp(-q*T) - K*np.exp(-r*T), 0.0)
    d1 = (np.log(S/K) + (r - q + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    return S*np.exp(-q*T)*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)

def implied_vol_call_bisect(S, K, T, r, q, price, lo=1e-6, hi=5.0, tol=1e-6, max_iter=100):
    if T <= 0 or price <= 0: return np.nan
    plo = bs_price_call(S, K, T, r, q, lo)
    phi = bs_price_call(S, K, T, r, q, hi)
    if price < plo or price > phi: return np.nan
    for _ in range(max_iter):
        mid = 0.5*(lo+hi)
        pm = bs_price_call(S, K, T, r, q, mid)
        if abs(pm - price) < tol: return mid
        if pm > price: hi = mid
        else: lo = mid
    return 0.5*(lo+hi)

# --- Main Loader ---
def load_spx_option_slice(target_window=(20, 45), r=0.00, q=0.015, min_quotes=12):
    """
    Fetch SPX options from Yahoo Finance, pick one maturity (20–45 days), compute mid-price & IVs.
    Returns: df_slice, S0, r, q, T
    """
    print("Fetching SPX data from Yahoo Finance ...")
    ticker = yf.Ticker("^SPX")
    S0 = ticker.history(period="1d")["Close"].iloc[-1]
    expirations = ticker.options

    # pick one expiry 20–45 days ahead
    today = datetime.utcnow().date()
    valid = []
    for e in expirations:
