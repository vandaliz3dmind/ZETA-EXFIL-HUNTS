from mpmath import mp, zetazero, li, log
mp.dps = 25
x = mp.mpf(1e9)
zeros = [zetazero(n) for n in range(1, 51)]
psi_approx = x
for rho in zeros:
    if abs(rho.imag) < 1000:
        psi_approx -= (x ** rho) / rho
psi_approx -= log(2 * mp.pi) / 2
pi_approx = li(x) + (psi_approx - x) / log(x)
print(float(pi_approx))
