import numpy as np
from scipy.stats import norm

def _d1_d2(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + 0.5 * sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    return d1, d2

def black_scholes_price(S, K, T, r, sigma, option_type='call'):
     """
    S: Spot Price
    K: Strike Price
    T: Time to Maturity (in years)
    r: Risk-free rate
    sigma: Volatility
    option_type: 'call' or 'put'
    """
    d1, d2 = _d1_d2(S, K, T, r, sigma)
    if option_type == 'call':
        return S*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)
    else:
        return K*np.exp(-r*T)*norm.cdf(-d2) - S*norm.cdf(-d1)


