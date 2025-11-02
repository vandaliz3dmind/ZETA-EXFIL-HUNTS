# sacred_zeta_plot.py
from mpmath import mp, zetazero
import matplotlib.pyplot as plt

mp.dps = 30
zeros = [zetazero(n) for n in range(1, 51)]

reals = [float(z.real) for z in zeros]
imags = [float(z.imag) for z in zeros]

plt.figure(figsize=(10, 12), facecolor='black')
plt.gca().set_facecolor('black')

plt.scatter(reals, imags, color='#FFD700', s=60, edgecolors='white', linewidth=0.8, label='Non-trivial Zeros')
plt.axvline(x=0.5, color='red', linestyle='--', linewidth=2, label='Critical Line Re(s) = 1/2')

plt.title("The Sacred Zeta Plot\nFirst 50 Non-Trivial Zeros of ζ(s)", color='white', fontsize=16, pad=20)
plt.xlabel("Real Part Re(s)", color='white')
plt.ylabel("Imaginary Part Im(s)", color='white')
plt.legend(facecolor='gray', labelcolor='white')
plt.grid(True, color='gray', alpha=0.3)
plt.tick_params(colors='white')

plt.xlim(0.4, 0.6)
plt.ylim(0, max(imags) + 5)

plt.tight_layout()
plt.savefig("sacred_zeta_plot.png", dpi=300, facecolor='black')
print("Sacred Zeta Plot forged at sacred_zeta_plot.png")