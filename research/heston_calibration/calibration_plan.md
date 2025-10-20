# Calibration Plan (Least Squares on Implied Vols)

## Steps
1) **Data slice**: pick nearest liquid maturity (e.g., 15–45 days). Keep strikes with decent volume / positive mid.
2) **Market IVs**: ensure each quote has a valid implied vol (fallback to bid/ask midpoint).
3) **Model IVs**: for each strike, price with Heston (Fourier integral) → invert to IV via Black–Scholes.
4) **Objective**: SSE/weighted-SSE between market IV and model IV across strikes.
5) **Optimizer**: `scipy.optimize.least_squares` with bounds and good initial guess.
6) **Report**: parameters, RMSE (vol points), figure of smile.

## Initial guess (reasonable defaults)
- \(\kappa=1.0,\ \theta=0.04,\ \sigma=0.5,\ \rho=-0.5,\ v_0=0.04\)

## Bounds (soft)
- \(\kappa \in [1e{-3}, 5.0]\)
- \(\theta \in [1e{-5}, 0.5]\)
- \(\sigma \in [1e{-3}, 3.0]\)
- \(\rho \in [-0.999, 0.0]\)
- \(v_0 \in [1e{-5}, 0.5]\)

## Deliverables
- `calibration_report.json` (params + RMSE)
- `iv_smile_market_vs_heston.png`
- `notebooks/01_heston_single_maturity.ipynb` with all steps

