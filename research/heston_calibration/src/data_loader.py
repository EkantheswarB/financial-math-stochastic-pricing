import pandas as pd
import numpy as np

def load_single_maturity_slice(df_chain, target_maturity_days=(20,45), min_quotes=12):
    """
    df_chain columns expected: ['strike','mid','type','expiration','dte','bid','ask','volume', ...]
    Returns a cleaned single-maturity CALL slice with strikes & mid prices.
    """
    # pick nearest maturity within window
    dte_mask = (df_chain['dte']>=target_maturity_days[0]) & (df_chain['dte']<=target_maturity_days[1])
    sub = df_chain.loc[dte_mask & (df_chain['type']=='call')].copy()
    if sub.empty:
        raise ValueError("No maturity slice in requested DTE window.")
    # choose the most liquid expiration (max non-null mid)
    counts = sub.groupby('expiration')['mid'].apply(lambda s: s.notna().sum())
    expiry = counts.idxmax()
    sl = sub[sub['expiration']==expiry].dropna(subset=['mid','strike'])
    sl = sl.sort_values('strike')
    if sl.shape[0] < min_quotes:
        raise ValueError("Not enough quotes for a robust smile.")
    return sl, expiry
