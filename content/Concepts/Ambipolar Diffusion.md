---
type: concept
status: draft
updated: 2026-10-07
sources: 1
---

# Ambipolar Diffusion

Diffusion of plasma in which electrons and ions must move together (quasi-neutrality condition $n_e = n_i$) despite having very different thermal velocities. The coupling creates an ambipolar electric field that retards electron diffusion and accelerates ion diffusion toward a common rate.

## Derivation (Five-Moment, Schunk & Nagy Ch. 5)

The rigorous derivation starts from the five-moment momentum equations for ions and electrons moving along **B** in a partially ionized plasma. For a major ion species in diffusive equilibrium ($\partial\mathbf{u}/\partial t = 0$, subsonic) the ion and electron momentum equations (S&N Eqs 5.51–5.52) are:

$$\nabla_\parallel p_i + (\nabla\cdot\tau_i)_\parallel - n_i e E_\parallel - n_i m_i G_\parallel = n_i m_i \nu_{in}(\mathbf{u}_n - \mathbf{u}_i)_\parallel$$
$$\nabla_\parallel p_e + (\nabla\cdot\tau_e)_\parallel + n_e e E_\parallel - n_e m_e G_\parallel = n_e m_e \nu_{en}(\mathbf{u}_n - \mathbf{u}_e)_\parallel$$

Adding these (using $n_e = n_i$, $\mathbf{u}_e = \mathbf{u}_i = \mathbf{u}_\parallel$, and $n_i m_i \nu_{ie} = n_e m_e \nu_{ei}$), the polarization field $E_\parallel$ cancels (Eq 5.53), yielding the combined momentum balance (S&N Eq 5.54):

$$\mathbf{u}_{i\parallel} = \mathbf{u}_{n\parallel} - D_a\left[\frac{1}{n_i}\nabla_\parallel n_i + \frac{1}{T_p}\nabla_\parallel T_p - \frac{m_i G_\parallel}{2kT_p} + \frac{(\nabla\cdot\tau_i)_\parallel}{2n_ikT_p}\right]$$

with the **ambipolar diffusion coefficient**:
$$D_a = \frac{2kT_p}{m_i\nu_{in}}, \qquad T_p = \frac{T_e + T_i}{2} \quad\text{(Eq 5.55–5.56)}$$

The polarization electrostatic field is obtained separately from the electron momentum equation (neglecting electron mass, Eq 5.61):
$$eE_\parallel = -\frac{1}{n_e}\nabla_\parallel p_e$$

This is the Boltzmann relation driver. Its solution for isothermal electrons is (Eq 5.63): $n_e = (n_e)_0 e^{e\Phi/kT_e}$, valid for subsonic, slowly-varying electron flows.

Setting quasi-neutrality ($\partial v_e/\partial t = \partial v_i/\partial t$) and eliminating $E_\parallel$ yields the simpler textbook form of the ambipolar diffusion coefficient:

$$D_a = \frac{k_B(T_e + T_i)}{m_i \nu_{in}}$$

The ambipolar diffusion speed for a perturbation of scale $h$:

$$v_{diff} = D_a / h$$

## Minor Ion Diffusion (S&N §5.7)

For trace ions (density $\ll$ majority ion density), the Coulomb collision frequency $\nu_{\ell i} \gg \nu_{\ell n}$, and the minority species is dragged along by the majority ion. The minor ion drift velocity (S&N Eq 5.70) is:

$$u_{\ell\parallel} = u_{i\parallel} - D_\ell\left[\frac{1}{n_\ell}\nabla_\parallel n_\ell + \frac{1}{T_\ell}\nabla_\parallel(T_\ell + T_e) - \frac{m_\ell G_\parallel}{kT_\ell} + \frac{T_e}{T_\ell n_e}\nabla_\parallel n_e + \cdots\right]$$

where the minor ion diffusion coefficient $D_\ell = kT_\ell/(m_\ell \nu_{\ell i})$ (Eq 5.71). The **key result** (Eq 5.79): for a minor ion with $m_\ell < m_i/2$, the polarization field (set by the majority ions and electrons to balance *their* gravity) is stronger than the gravity on the lighter minor ion, producing a **net upward force**. This is the kinematic origin of the polar wind for H$^+$ ($m_{H^+} = 1 < m_{O^+}/2 = 8$): the O$^+$-electron polarization field accelerates H$^+$ upward beyond its own scale height, driving it supersonic on open field lines.

## Plasma Scale Height

In diffusive equilibrium (drift velocities → 0, no production/loss), the density profile is a Chapman-layer-like exponential with the plasma scale height:

$$H_p = \frac{k_B(T_e + T_i)}{m_i g}$$

This is twice the neutral scale height for the same species (at equal $T$), because the ambipolar electric field holds the ions up against gravity. For O$^+$ at $T_e = T_i = 1000$ K: $H_p \sim 110$ km.

## F-Region Vertical Structure

Above the F2 peak (topside F region) where chemical recombination is negligible, plasma is in diffusive equilibrium:

$$n(z) = n_0 \exp\!\left(-\int \frac{m_i g + \frac{d}{dz} k_B(T_e+T_i)}{k_B(T_e + T_i)} \, dz\right)$$

This follows from $\frac{d}{dz}\left[n k_B (T_e+T_i)\right] = -n m_i g$. *(Corrected 2026-10-07: the temperature-gradient term previously had a minus sign. A rising plasma temperature makes density fall off faster, not slower.)*

The density falls off with scale $H_p$; elevated $T_e$ increases $H_p$ and raises the effective topside density. At the topside, diffusion along the inclined field lines provides the restoring force that maintains the F2 peak structure.

## Transition to Polar Wind

Below ~2500 km on polar cap field lines, diffusive equilibrium holds (sub-sonic flow). Above this altitude, the flux tubes are open and the ambipolar electric field can accelerate H$^+$ past the sonic point into the supersonic [[Polar Wind]].

## Cross-Field Diffusion

Perpendicular to $\mathbf{B}$, diffusion is greatly inhibited. The cross-field diffusion coefficient:

$$D_\perp = D_a \left(\frac{\nu_{in}}{\Omega_i}\right)^2 \ll D_a$$

This suppression of cross-field diffusion is why ionospheric plasma structures (patches, bubbles, arcs) maintain their density contrast over long distances.

## Related Concepts

- [[Polar Wind]] — supersonic extension of ambipolar diffusion on open field lines
- [[F-Layer]] — topside profile governed by ambipolar diffusion
- [[Ionospheric Energetics]] — $T_e$ and $T_i$ set $H_p$ and diffusion rates
- [[Equatorial Ionosphere]] — fountain effect uses ambipolar diffusion along tilted field lines

## Derivations

- [[Plasma Diffusion Along B]] — step-by-step derivation with SymPy checks
- [[Chapman Layer]] — how diffusion and chemistry set the F2 peak

## Sources

- [[Schunk Nagy 2009 Ionospheres]] (Ch. 5 §§5.5–5.7: ambipolar diffusion derivation, polarization field, minor ion diffusion)
- AOS 205B course materials
