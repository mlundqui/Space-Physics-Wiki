---
type: concept
status: draft
updated: 2026-10-08
sources: 2
tags: [plasma-physics, MHD, waves]
---

# MHD

Magnetohydrodynamics — the single-fluid description of a plasma in the limit where the plasma behaves as a conducting fluid on timescales long compared to all plasma frequencies and gyrofrequencies ($\omega \ll \Omega_i$, $kd_i \ll 1$). MHD is the foundation for coronal and solar wind dynamics, magnetospheric equilibria, and the large-scale structure of ionospheric currents.

## MHD Equations (S&N Ch. 7)

The single-fluid MHD equations are obtained by summing the two-fluid (ion + electron) moment equations, using $n_e = n_i = n$, $\rho = n m_i$, $\mathbf{J} = ne(\mathbf{u}_i - \mathbf{u}_e)$:

**Continuity:** $\partial\rho/\partial t + \nabla\cdot(\rho\mathbf{u}) = 0$

**Momentum:** $\rho\left(\frac{\partial\mathbf{u}}{\partial t} + \mathbf{u}\cdot\nabla\mathbf{u}\right) = -\nabla p + \mathbf{J}\times\mathbf{B}$

**Ohm's law (ideal):** $\mathbf{E} + \mathbf{u}\times\mathbf{B} = 0$ (perfect conductor; $\sigma \to \infty$)

**Faraday's law:** $\partial\mathbf{B}/\partial t = -\nabla\times\mathbf{E} = \nabla\times(\mathbf{u}\times\mathbf{B})$

**No monopoles:** $\nabla\cdot\mathbf{B} = 0$

**Equation of state:** adiabatic $p \propto \rho^\gamma$ or isothermal.

## Generalized Ohm's Law

The ideal MHD Ohm's law $\mathbf{E} + \mathbf{u}\times\mathbf{B} = 0$ is the zeroth-order result. Higher-order terms enter from the electron momentum equation:

$$\mathbf{E} + \mathbf{u}\times\mathbf{B} = \frac{1}{ne}\mathbf{J}\times\mathbf{B} - \frac{\nabla p_e}{ne} + \eta\mathbf{J}$$

The three correction terms are the Hall term, electron pressure gradient (diamagnetic), and resistivity $\eta$. The Hall term becomes important when $\omega \sim \Omega_i$ (Hall MHD regime); the pressure gradient drives electrothermal effects and field-aligned currents in the ionosphere.

## Frozen-In Flux

In ideal MHD ($\eta = 0$), the magnetic flux through any surface convecting with the fluid is conserved:

$$\frac{d\Phi_B}{dt} = 0, \qquad \Phi_B = \int\mathbf{B}\cdot d\mathbf{A}$$

Equivalently, magnetic field lines "move with the plasma." This is Alfvén's theorem. Consequence: plasma on a given field line stays on that field line; field lines can be thought of as elastic strings threading the plasma.

Frozen-in flux breaks down at current sheets, X-lines, and in the presence of non-ideal terms (resistivity, Hall, electron inertia) — this is **magnetic reconnection**. Reconnection at the magnetopause allows solar wind mass and energy to enter the magnetosphere.

## Plasma Beta

$$\beta = \frac{p}{B^2/(2\mu_0)} = \frac{2\mu_0 nkT}{B^2}$$

*(Corrected 2026-10-07: formula was in Gaussian units ($B^2/8\pi$), inconsistent with the SI used elsewhere on this page.)*

The ratio of thermal to magnetic pressure. At the solar wind at 1 AU: $\beta \approx 2$ (S&N Table 2.3). In the magnetosphere: $\beta \ll 1$ in the lobes, $\beta \sim 1$ in the plasma sheet. In the ionosphere: $\beta \ll 1$. For $n = 10^{12}$ m$^{-3}$, $T_e + T_i = 3000$ K and $B = 5\times10^{-5}$ T, $\beta \approx 4\times10^{-5}$. The geomagnetic field is essentially unperturbed by ionospheric plasma pressure.

*(Corrected 2026-10-07: this line previously said $\beta \gg 1$ in the ionosphere, which is wrong by about five orders of magnitude.)*

## MHD Wave Modes

For small perturbations $\mathbf{B} = \mathbf{B}_0 + \mathbf{B}_1$, $\rho = \rho_0 + \rho_1$, linearizing yields three wave modes:

**Shear Alfvén wave:** Transverse oscillation of field lines; dispersion $\omega = k_\parallel v_A$ where $v_A = B/\sqrt{\mu_0\rho}$ (SI; corrected 2026-10-07 from the Gaussian $B/\sqrt{4\pi\rho}$).
- Restoring force: magnetic tension $(\mathbf{B}\cdot\nabla)\mathbf{B}/\mu_0$
- Group velocity along $\mathbf{B}$; carries field-aligned currents (FACs) from magnetosphere to ionosphere
- Relevant for: ULF field line resonances, auroral Alfvén waves, ionosphere-magnetosphere coupling
- Ideal MHD forces $E_\parallel = 0$. At small perpendicular scales the wave becomes kinetic or inertial and carries $E_\parallel$; see [[Alfvén Waves]].

**Fast magnetosonic wave:** Compressional; dispersion $\omega^2 = k^2(v_A^2 + c_s^2)$ perpendicular to $\mathbf{B}$.
- Propagates in all directions relative to $\mathbf{B}$; mediates pressure pulses
- Relevant for: CME shocks, magnetopause pulses, impulsive heating

**Slow magnetosonic wave:** Compressional; plasma and magnetic pressure perturbations are in antiphase. For nearly perpendicular propagation $\omega^2 \approx k_\parallel^2 c_s^2 v_A^2/(v_A^2+c_s^2)$ (the "cusp" or tube speed). That expression is a limit, not the general dispersion relation. Often heavily damped in collisionless plasmas.

General dispersion relation for the fast (+) and slow (−) modes, with $\theta$ the angle between $\mathbf{k}$ and $\mathbf{B}_0$:
$$\frac{\omega^2}{k^2} = \frac{1}{2}\left[(c_s^2+v_A^2) \pm \sqrt{(c_s^2+v_A^2)^2 - 4c_s^2v_A^2\cos^2\theta}\right]$$
Full derivation: [[MHD Wave Modes]].

Alfvén speed at 1 RE in the magnetosphere: $v_A \approx 200$–$1000$ km/s; in the solar wind at 1 AU: $v_A \approx 44$ km/s.

*Note:* along auroral field lines $v_A$ peaks at roughly $10^4$ km/s a few thousand km up (e.g. about 36,600 km/s at 7000 km in [[Kletzing 1994 KAW Electron Acceleration]]). The 200–1000 km/s figure applies to the equatorial and outer magnetosphere. See [[Alfvén Waves]].

## CGL (Double Adiabatic) Equations

In a collisionless magnetized plasma, pressure is anisotropic: $p_\parallel \neq p_\perp$ relative to $\mathbf{B}$. The Chew-Goldberger-Low (CGL) equations replace the scalar pressure with two conservation laws:

$$\frac{d}{dt}\!\left(\frac{p_\perp}{\rho B}\right) = 0 \qquad \text{(first adiabatic invariant: }p_\perp/B = \mu_1\text{)}$$
$$\frac{d}{dt}\!\left(\frac{p_\parallel B^2}{\rho^3}\right) = 0$$

When $p_\parallel - p_\perp > B^2/\mu_0$, the **firehose instability** grows: parallel-streaming particles exert a centrifugal force on a bent flux tube that overwhelms magnetic tension. When $p_\perp > p_\parallel$ by enough, the **mirror instability** grows. The threshold is $p_\perp/p_\parallel > 1 + 1/\beta_\perp$ in kinetic theory and $p_\perp/p_\parallel > 6(1 + 1/\beta_\perp)$ in the CGL fluid model (Siscoe 1983, §IV.1). Both are relevant to the solar wind and magnetosheath.

*(Corrected 2026-10-07: the firehose and mirror conditions were previously swapped, with the firehose given as $p_\perp > p_\parallel + B^2/4\pi$ and the mirror as $p_\perp < p_\parallel$.)*

## Parker Spiral

The interplanetary magnetic field (IMF) forms a Parker spiral in the equatorial plane. With solar rotation rate $\Omega_\odot = 2.7\times10^{-6}$ rad/s, radial solar wind speed $u_r$:

$$\tan\phi = \frac{\Omega_\odot r}{u_r}$$

At 1 AU ($r = 1.5\times10^{11}$ m) with $u_r = 400$ km/s: $\tan\phi \approx 1.0$, so $\phi \approx 45°$. *(Corrected 2026-10-07 from 43°; the stated numbers give 45°.)* The spiral angle modulates the IMF $B_z$ component and thus reconnection efficiency at the magnetopause.

## Related Concepts

- [[Ideal MHD from Kinetic Theory]] — full derivation of the equations on this page
- [[MHD Wave Modes]] — derivation of the shear, fast and slow modes

- [[Plasma Waves]] — wave mode taxonomy; Alfvén, magnetosonic, whistler modes
- [[Alfvén Waves]] — dispersive (kinetic and inertial) extension of the shear mode
- [[Ionospheric Conductivity]] — Pedersen and Hall currents are the ionospheric limit of resistive MHD
- [[Joule Heating]] — energy dissipation in resistive MHD: $Q_J = \eta J^2 = \Sigma_P E^2$
- [[Polar Wind]] — Parker wind-type solution for sonic outflow on open field lines

## Derivations

- [[Parker Solar Wind and Spiral]] — transonic solar wind and the spiral as an exact ideal-MHD solution
- [[Rankine-Hugoniot Jump Conditions]] — MHD shocks and discontinuities from conservation laws
- [[Sweet-Parker Reconnection]] — breaking the frozen-in condition in a resistive current sheet

## Sources

- [[Schunk Nagy 2009 Ionospheres]] (Ch. 7: MHD equations, generalized Ohm's law, frozen-in flux, plasma $\beta$, Parker spiral, CGL double-adiabatic, Alfvén and magnetosonic waves)
- [[Kletzing 1994 KAW Electron Acceleration]] ($v_A$ along auroral field lines)
- [[Siscoe 1983 Solar System MHD]] (§IV.1: firehose and mirror thresholds)
