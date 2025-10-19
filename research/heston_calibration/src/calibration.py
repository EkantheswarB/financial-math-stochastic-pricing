import numpy as np
from scipy.optimize import least_squares
from .bs_utils import implied_vol
from .heston_pricer import heston_call_price

def objective(theta, market, S, T, r, strikes, prices):
    kappa, bigtheta, xi, rho, v0 = theta
    # price model → implied vol → residual vs market iv
    iv_model = []
    for K, p_mkt in zip(strikes, prices):
        p_mod = heston_call_price(S, K, T, r, kappa, bigtheta, xi, rho, v0)
        try:
            ivm = implied_vol(p_mod, S, K, T, r, call=True)
            iv_model.append(ivm)
        except:
            iv_model.append(np.nan)
    iv_model = np.array(iv_model)
    mask = np.isfinite(iv_model) & np.isfinite(market)
    return (iv_model[mask] - market[mask])

def calibrate(market_iv, S, T, r, strikes, prices, x0=None):
    if x0 is None:
        atm_iv = float(market_iv[np.argmin(np.abs(strikes - S))])
        x0 = np.array([1.5, atm_iv**2, 0.5, -0.5, atm_iv**2])  # kappa, theta, xi, rho, v0
    bounds = ([0.01, 1e-5, 0.05, -0.99, 1e-6], [8.0, 0.6, 2.0, -0.01, 1.0])
    res = least_squares(objective, x0, bounds=bounds,
                        args=(market_iv, S, T, r, strikes, prices),
                        loss='soft_l1', f_scale=0.05, max_nfev=200)
    return res.x, res.cost

