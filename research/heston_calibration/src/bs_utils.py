import numpy as np
from mpmath import findroot
from math import log, sqrt, exp
from scipy.stats import norm

def bs_price(S, K, T, r, sigma, call=True):
    if T <= 0 or sigma <= 0: 
        return max(0.0, (S - K) if call else (K - S))
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    if call:
        return S*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)
    else:
        return K*np.exp(-r*T)*norm.cdf(-d2) - S*norm.cdf(-d1)

def implied_vol(price, S, K, T, r, call=True, guess=0.2):
    # Brent would be more robust in practice; this is a placeholder.
    from scipy.optimize import brentq
    f = lambda sig: bs_price(S,K,T,r,sig,call) - price
    return brentq(f, 1e-6, 5.0)

