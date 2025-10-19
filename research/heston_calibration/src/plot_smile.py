import numpy as np
import matplotlib.pyplot as plt

def plot_iv_smile(strikes, iv_mkt, iv_model, title="Implied Volatility Smile (Market vs Heston)"):
    fig = plt.figure(figsize=(7,4.5))
    plt.plot(strikes, iv_mkt, marker='o', linestyle='-', label='Market IV')
    plt.plot(strikes, iv_model, marker=None, linestyle='--', label='Heston IV')
    plt.xlabel("Strike")
    plt.ylabel("Implied Volatility")
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    return fig
