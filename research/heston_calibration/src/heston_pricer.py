import numpy as np

def heston_char_cf(u, T, kappa, theta, xi, rho, v0, r=0.0):
    i = 1j
    d = np.sqrt((rho*xi*i*u - kappa)**2 + (u**2 + i*u)*xi**2)
    g = (kappa - rho*xi*i*u - d) / (kappa - rho*xi*i*u + d)
    C = i*u*r*T + (kappa*theta/xi**2)*((kappa - rho*xi*i*u - d)*T - 2.0*np.log((1 - g*np.exp(-d*T))/(1-g)))
    D = ((kappa - rho*xi*i*u - d)/xi**2)*((1 - np.exp(-d*T))/(1 - g*np.exp(-d*T)))
    return np.exp(C + D*v0)

def heston_call_price(S, K, T, r, kappa, theta, xi, rho, v0):
    # Heston closed-form via P1/P2 integrals (Lewis 2000 form)
    from numpy import real
    i = 1j
    def integrand(u, j):
        if j == 1:
            phi = heston_char_cf(u - i, T, kappa, theta, xi, rho, v0, r)
            numer = np.exp(-i*u*np.log(K)) * phi
            denom = i*u*S*np.exp(r*T)
        else:
            phi = heston_char_cf(u, T, kappa, theta, xi, rho, v0, r)
            numer = np.exp(-i*u*np.log(K)) * phi
            denom = i*u
        return (numer/denom)

    # Numerical integration (Gauss-Laguerre or Simpson). Simpson coarse:
    umax, N = 200.0, 2000
    u = np.linspace(1e-5, umax, N)
    du = u[1]-u[0]
    P1 = 0.5 + (1/np.pi)*np.sum(np.real(integrand(u,1)))*du
    P2 = 0.5 + (1/np.pi)*np.sum(np.real(integrand(u,2)))*du
    return S*P1 - K*np.exp(-r*T)*P2

