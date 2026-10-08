---
type: source
status: draft
updated: 2026-10-07
sources: 0
authors: R.L. Lysak, W. Lotko
year: 1996
doi: 10.1029/95JA03712
tags: [kinetic-alfven-waves, theory, landau-damping, dispersion-relation]
---

# Lysak Lotko 1996 Kinetic Alfvén Dispersion

## Summary

This is the first shear-Alfvén dispersion relation with full kinetic effects for both electrons and ions: full ion and electron gyroradius, and full electron Landau damping. It covers the low-frequency, low-β regime and bridges the two fluid limits, kinetic ($\rho_s$) and inertial ($\lambda_e$). The fluid dispersion relation turns out to be qualitatively right. **Landau damping is unimportant unless $k_\perp\rho_s$ or $k_\perp\lambda_e$ is about 1 or larger, and hot ions suppress it.** Applied to a model auroral field line at L = 10, waves with perpendicular wavelengths greater than about 10 km mapped to the ionosphere are not significantly Landau damped.

## Key claims

- **Fluid two-regime dispersion** (as used by Streltsov & Lotko):
$$\omega^2 = k_\parallel^2V_A^2\frac{1 + k_\perp^2\rho_s^2}{1 + k_\perp^2c^2/\omega_{pe}^2}$$
  - The numerator (electron pressure and ion FLR) *raises* the parallel phase speed.
  - The denominator (electron inertia) *lowers* it.
  - The boundary is at $\beta = m_e/m_i$, where $v_{te} \approx V_A$ and the phase speed is exactly $V_A$.
- **Hasegawa 1976 form with ion FLR:**
$$\omega^2 = k_\parallel^2V_A^2[1 + k_\perp^2\rho_i^2(\tfrac34 + T_e/T_i)]$$
  The $\tfrac34$ comes from expanding the Bessel functions. This matches [[Hasegawa Chen 1976 KAW Mode Conversion]].
- **Terminology.** The cold-plasma ($\beta \ll m_e/m_i$) limit is "sometimes called the inertial Alfvén wave." Some authors (e.g. [[Kletzing 1994 KAW Electron Acceleration]]) still call it "kinetic."
- **Where each regime applies.** Lysak & Carlson 1981 found the inertial limit appropriate **below about 4–5 $R_E$** along auroral field lines, and the kinetic limit above.
- **Perpendicular group velocity changes sign** between the two regimes, because $\omega$ increases with $k_\perp$ in the kinetic regime and decreases in the inertial regime. A wave crossing both can trace a "figure-eight" path. In the special symmetric case it closes on itself, allowing large field-line resonances (Streltsov & Lotko 1995).
- **Landau damping:**
  - $\gamma/\omega \lesssim 0.1$ whenever both $k_\perp\rho_s < 1$ and $k_\perp c/\omega_{pe} < 1$.
  - There is **no strong enhancement at $v_{te} = V_A$**. Damping increases monotonically with $T_e$ at fixed $k_\perp c/\omega_{pe}$.
  - **Higher $T_i/T_e$ suppresses damping**, because ion FLR pushes the phase velocity above $v_{te}$, into the tail of the electron distribution. (The weak-damping rate is $\propto \zeta e^{-\zeta^2}$, with $\zeta = \omega/k_\parallel a_e$, which peaks at $\zeta \approx 0.7$.)
- **Short wavelengths.** As $k_\perp \to$ large, the wave becomes electrostatic with parallel phase speed about $v_{te}$.
- **Caveat (authors'):** the local, homogeneous dispersion relation is strictly valid only for parallel wavelengths short compared with gradient scales. For field-line resonances it is only indicative.

## Methods/data

Low-frequency, long-parallel-wavelength reduction of the hot-plasma dielectric tensor (Bessel functions $\Gamma_n$, plasma dispersion function $Z$). Model L = 10 field line: exponential O⁺ ionosphere ($5\times10^5$ cm⁻³, 0.025 $R_E$ scale height) plus a power-law H⁺ population; $T_e = 1$ eV in the ionosphere rising to 100 eV beyond about 2.5 $R_E$; $\lambda_\perp = 1$ km at the ionosphere, where $k_\perp c/\omega_{pe}$ reaches about 7.5 in the low-β region.

## Connections

- [[Alfvén Waves]] — the dispersion relation, regime boundary and Landau damping
- [[Wave-Particle Interactions]] — Landau damping of $E_\parallel$
- [[Hasegawa Chen 1976 KAW Mode Conversion]], [[Kletzing 1994 KAW Electron Acceleration]], [[Chaston 2003 FAST Small-Scale Alfvén Waves]] (which cites this for Landau damping of upgoing waves)

## Open questions

- How much does the conclusion that damping is unimportant above about 10 km change for realistic, non-local field-line geometry?
