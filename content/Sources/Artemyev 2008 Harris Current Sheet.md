---
type: source
status: draft
updated: 2026-05-19
authors: A. V. Artemyev
year: 2008
---

# Artemyev 2008 Harris Current Sheet

*Evolution of a Harris Current Sheet in an Electric Field.* Artemyev, A. V. (2008). *Moscow University Physics Bulletin*, 63(3), 193–196. doi:10.3103/S0027134908030089.

## Summary

Short theoretical paper (4 pp) studying the evolution of a 1D Harris current sheet (CS) in a magnetospheric tail geometry under an external cross-tail electric field $E_y$, using an explicit Vlasov-Maxwell numerical scheme. Two cases are treated: spatially uniform and spatially inhomogeneous $E_y$. A uniform field penetrates the CS via charge separation: the resulting ambipolar $E_z$ and the background $B_x(z)$ cause cross-field electron and ion drifts, compressing the sheet to the ion Larmor radius scale and accelerating particles near the magnetic neutral line.

## Key Claims

1. **Uniform $E_y$ penetrates the CS interior via charge separation**: the differing ion and electron Larmor radii in the inhomogeneous $B_x(z)$ field create a charge density $\rho$, which drives an ambipolar $E_z(z)$ that self-consistently closes the system.
2. **CS compression to ion Larmor radius**: under uniform $E_y$, particles drift with velocity $v_y = cE_y/B_x(z)$, which strongly increases near the neutral line ($B_x \to 0$), compressing the current sheet until $L \sim r_i$.
3. **Inhomogeneous $E_y$ (minimum at CS center)**: charge separation effect is suppressed; no significant compression occurs — particles at the periphery are accelerated toward the center without altering the neutral-line structure.
4. CS evolution is governed by Vlasov-Maxwell equations; the phase-volume conservation theorem (Liouville) is used to recalculate the distribution function.
5. Relevant to magnetospheric substorm onset physics — compression and thinning of the near-Earth current sheet.

## Methods/Data

- 1D Vlasov-Maxwell explicit numerical scheme.
- Harris CS initial conditions: $B_x(z) = B_0\tanh(z/L)$, $n(z) = n_0\cosh^{-2}(z/L)$; ion temperature $T_i = 1$ keV, $T_e = T_i/5 = 0.2$ keV; $L = 5r_i$.
- Two external field profiles: $E_y = \text{const}$ and $E_y$ with minimum at $z = 0$.

## Connections

- [[Magnetotail]] — current sheet thinning and substorm onset physics
- [[Field-Aligned Currents]] — reconnection onset in the tail drives FAC perturbations in the ionosphere

## Open Questions

- Behavior in 2D/3D geometry (this paper is strictly 1D).
- Role of kinetic instabilities (lower hybrid drift, tearing) during and after the compression phase.
