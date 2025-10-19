# Heston Calibration on SPX (Single Maturity)

**Goal.** Calibrate Heston stochastic volatility parameters \(\kappa, \theta, \sigma, \rho, v_0\) to a *single* SPX option maturity by minimizing the squared error between market implied volatilities and Heston-implied volatilities. Output: side-by-side **volatility smile** (Market vs Heston) and a brief error report.

**Why this matters.** Black–Scholes assumes constant volatility and cannot reproduce the smile/skew observed in index options. Heston allows **stochastic variance** with mean-reversion and correlation with price, capturing leverage and skew effects—this is the canonical next step for a PhD-track research agenda.

## Scope (Phase II of the project)
- Single-maturity slice (near-month expiry)
- Calls (or puts via parity)
- Mid quotes → compute market IVs (already available in Phase I)
- Least-squares calibration on IVs

## Inputs
- Underlying index level \(S_0\)
- Risk-free rate \(r\), dividend yield \(q\) (or futures-based \(F_0\))
- Maturity \(T\) (in years)
- Strikes \(K_i\), market IVs \(\sigma^{mkt}_i\)

## Outputs
- Calibrated parameters \((\kappa,\theta,\sigma,\rho,v_0)\)
- Plot: Market vs Heston **implied volatility by strike**
- Error metrics: RMSE (vol points), MAE

## Quickstart (Colab)
1. Upload this folder to your repo.
2. Open `notebooks/01_heston_single_maturity.ipynb` (create from Colab).
3. Run:
   - `data_loader.py` → get a clean single-maturity slice
   - `calibration.py` → `fit_heston_iv(...)`
   - `plot_smile.py` → `plot_iv_smile(...)`

## Deliverables (for paper/SOP)
- Figure: Market vs Heston IV smile
- Table: Calibrated params + errors
- Short note: “Heston reproduces skew better than BS” (qualitative)

