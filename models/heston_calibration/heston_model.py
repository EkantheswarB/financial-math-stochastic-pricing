import numpy as np
from numpy import exp, log, sqrt
from numpy.complex128 import complex128

def _phi(u, params, S0, r, q, T, j):
    # Heston characteristic function (Lewis/Heston form)
    kappa, theta, sigma, rho, v0 = params
    u = np.asarray(u, dtype=complex128)
    i = 1j

    if j == 1:
        b = kappa - rho*sigma
        u_shift = u - i
    else:  # j == 2
        b = kappa
        u_shift = u

    d = np.sqrt((rho*sigma*u_shift*i - b)**2 - (sigma**2)*( -u_shift*u_shift - i*u_shift))
    g = (b - rho*sigma*u_shift*i - d) / (b - rho*sigma*u_shift*i + d)
    # Avoid numerical issues
    g = np.where(np.abs(g) < 1-1e-12, g, (1-1e-12)*g/np.abs(g))

    C = (r - q)*u*i*T + (kappa*theta/(sigma**2)) * ( (b - rho*sigma*u_shift*i - d)*T - 2.0*np.log((1 - g*exp(-d*T))/(1 - g)) )
    D = ((b - rho*sigma*u_shift*i - d) / (sigma**2)) * ( (1 - exp(-d*T))/(1 - g*exp(-d*T)) )

    return exp(C + D*v0 + i*u*log(S0*exp((r-q)*T)))

def heston_call_price(S0, K, T, r, q, params, n=1600, umax=100.0):
    # Numerical integration for P1, P2 (Carr-Madan style integrals)
    u = np.linspace(1e-8, umax, n)
    du = u[1]-u[0]
    i = 1j

    phi1 = _phi(u - 1j, params, S0, r, q, T, j=1)
    phi2 = _phi(u,        params, S0, r, q, T, j=2)

    # Integrals for probabilities
    # Pj = 1/2 + 1/pi * ∫ Re( e^{-i u ln K} φ_j(u) / (i u) ) du
    lnK = np.log(K)
    integrand1 = np.real(np.exp(-i*u*lnK) * phi1 / (i*u))
    integrand2 = np.real(np.exp(-i*u*lnK) * phi2 / (i*u))
    P1 = 0.5 + (1/np.pi) * np.trapz(integrand1, dx=du)
    P2 = 0.5 + (1/np.pi) * np.trapz(integrand2, dx=du)

    return S0*np.exp(-q*T)*P1 - K*np.exp(-r*T)*P2
