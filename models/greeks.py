import numpy as np
from scipy.stats import norm

def _d1_d2(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + 0.5 * sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    return d1, d2

def delta(S, K, T, r, sigma, option_type='call'):
    d1, _ = _d1_d2(S, K, T, r, sigma)
    if option_type == 'call':
        return norm.cdf(d1)
    else:
        return norm.cdf(d1) - 1

def gamma(S, K, T, r, sigma):
    d1, _ = _d1_d2(S, K, T, r, sigma)
    return norm.pdf(d1) / (S * sigma * np.sqrt(T))

def vega(S, K, T, r, sigma):
    d1, _ = _d1_d2(S, K, T, r, sigma)
    # Return vega in price units (per 1.0 volatility, not 1%)
    return S * norm.pdf(d1) * np.sqrt(T)

def theta(S, K, T, r, sigma, option_type='call'):
    d1, d2 = _d1_d2(S, K, T, r, sigma)
    term1 = - (S * norm.pdf(d1) * sigma) / (2*np.sqrt(T))
    if option_type == 'call':
        term2 = - r * K * np.exp(-r*T) * norm.cdf(d2)
        return term1 + term2
    else:
        term2 = + r * K * np.exp(-r*T) * norm.cdf(-d2)
        return term1 + term2

def rho(S, K, T, r, sigma, option_type='call'):
    _, d2 = _d1_d2(S, K, T, r, sigma)
    if option_type == 'call':
        return K * T * np.exp(-r*T) * norm.cdf(d2)
    else:
        return -K * T * np.exp(-r*T) * norm.cdf(-d2)
