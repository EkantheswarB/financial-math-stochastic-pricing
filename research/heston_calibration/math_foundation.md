# Mathematical Foundation (Heston)

## Dynamics
\[
\begin{aligned}
dS_t &= (\mu - q) S_t\, dt + \sqrt{v_t}\, S_t\, dW_t^{(1)}, \\
dv_t &= \kappa(\theta - v_t)\, dt + \sigma \sqrt{v_t}\, dW_t^{(2)}, \\
\mathrm{corr}(dW_t^{(1)}, dW_t^{(2)}) &= \rho,
\end{aligned}
\]
where \(v_t\) is instantaneous variance, \(\kappa>0\) mean-reversion speed, \(\theta>0\) long-run variance, \(\sigma>0\) vol-of-vol, \(\rho \in (-1,1)\) correlation, and \(v_0>0\) initial variance.

Under risk-neutral measure:
\[
dS_t = (r - q) S_t\, dt + \sqrt{v_t}\, S_t\, dW_t^{(1)}.
\]

## European call pricing (Heston 1993)
Closed-form via characteristic functions:
\[
C(S_0, K, T) = S_0 e^{-qT} P_1 - K e^{-rT} P_2,
\]
where \(P_j = \mathbb{Q}(S_T > K)\) under two characteristic functions \(\phi_j(u)\) (different drifts). Numerically:
\[
P_j = \frac{1}{2} + \frac{1}{\pi}\int_0^\infty \Re\left(\frac{e^{-i u \ln K}\, \phi_j(u)}{i u}\right) du.
\]

We compute \(C\), then back out model-implied volatility \(\sigma^{hes}\) by inverting Black–Scholes.

## Calibration objective
Given market IVs \(\sigma^{mkt}_i\) at strikes \(K_i\), maturity \(T\):
\[
\min_{\kappa,\theta,\sigma,\rho,v_0}\ \sum_i \left[\sigma^{mkt}_i - \sigma^{hes}(K_i; \kappa,\theta,\sigma,\rho,v_0)\right]^2.
\]
Optionally weight by vega or quote quality (liquidity).

## Practical notes
- Enforce **Feller condition** \(2\kappa\theta \ge \sigma^2\) softly via bounds/penalty.
- Typical bounds: \(\kappa \in [0.01,10]\), \(\theta \in [1e{-6},1]\), \(\sigma \in [1e{-4},3]\), \(\rho \in [-0.999,0.0]\), \(v_0 \in [1e{-6},1]\).
- Use robust IV inversion with bracketing for stability.

