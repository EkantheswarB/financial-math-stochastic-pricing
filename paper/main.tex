\documentclass[12pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath, amssymb}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{setspace}
\onehalfspacing

\title{\textbf{A Computational Study of Derivative Pricing under Stochastic Volatility Using the Black--Scholes Framework}}
\author{\textbf{Ekantheswar Bandarupalli}\\
\small Working Paper --- Computational Finance Research\\
\small \texttt{study.ekantheswar@gmail.com}}
\date{\today}

\begin{document}
\maketitle
\thispagestyle{empty}
\vspace{1em}
\noindent\textbf{Abstract. }
The intersection of financial markets and mathematical modeling has long fascinated both practitioners and academics.
While algorithmic trading first sparked my interest in finance, it was the underlying question of how risk and price evolve
that drew me toward stochastic calculus and derivative pricing. This study presents a computational approach to pricing European options
using the Black--Scholes model and compares theoretical values with real S\&P 500 (SPX) market data. We highlight model fit, limitations,
and directions toward stochastic volatility models.

\newpage
\setcounter{page}{1}
\section{Introduction}
My initial interest in financial markets began through trading, where market behavior seemed both systematic and unpredictable.
What began as an exploration of trading strategies evolved into a deeper curiosity about the mathematics governing price movements,
volatility, and risk. I soon realized that true insight lies not in execution alone, but in the stochastic models that shape financial dynamics.
The objective of this work is to bridge theoretical finance with computational implementation.
By applying the Black--Scholes model to real SPX option data, this paper evaluates accuracy, limitations, and potential extensions
toward stochastic volatility (e.g., Heston).

\section{Methodology}
We consider the standard Black--Scholes setting with underlying price $(S_t)_{t\ge 0}$ following geometric Brownian motion under the risk--neutral measure:
\begin{equation}
dS_t = r S_t\,dt + \sigma S_t\, dW_t,
\end{equation}
where $r$ is the constant risk--free rate, $\sigma$ the (assumed constant) volatility, and $(W_t)$ a standard Brownian motion.
For a European call with strike $K$ and maturity $T$, the no--arbitrage price at $t=0$ is
\begin{equation}
C = S_0 \Phi(d_1) - K e^{-rT} \Phi(d_2), \quad
d_{1,2} = \frac{\ln(S_0/K) + (r \pm \tfrac{1}{2}\sigma^2)T}{\sigma\sqrt{T}},
\end{equation}
and for a put
\begin{equation}
P = K e^{-rT} \Phi(-d_2) - S_0 \Phi(-d_1),
\end{equation}
where $\Phi$ denotes the standard normal CDF.

We compute the \emph{Greeks} to assess sensitivities: Delta ($\partial C/\partial S$), Gamma ($\partial^2 C/\partial S^2$),
Vega ($\partial C/\partial \sigma$), Theta ($\partial C/\partial T$), and Rho ($\partial C/\partial r$), using closed--form expressions.
Empirically, we retrieve SPX option chains via public data and form the time--to--maturity $T$ and strike grids around the at--the--money region.
We compare market mid quotes with the Black--Scholes price computed using market implied volatilities and report pricing errors by strike.

\paragraph{Limitations.} The constant volatility assumption leads to systematic mispricing patterns (e.g., volatility smile/smirk).
In subsequent work we outline a stochastic volatility extension (Heston) where $d\nu_t = \kappa(\theta-\nu_t)dt + \xi \sqrt{\nu_t}\, dZ_t$
and price via Fourier methods or simulation.

\section{Results}
We report (i) price deviations by strike near ATM, and (ii) example Greek curves (Delta, Gamma, Vega) for short maturities.
Figures are produced directly from the accompanying Python notebook.

\section{Conclusion}
Black--Scholes provides a transparent baseline and a reproducible pipeline from data to price and sensitivities.
Observed deviations highlight the need for richer dynamics; future work will implement and compare a Heston specification.

\bibliographystyle{plain}
\bibliography{references}
\end{document}
