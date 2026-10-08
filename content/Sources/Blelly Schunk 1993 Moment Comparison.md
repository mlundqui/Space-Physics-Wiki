---
type: source
status: draft
updated: 2026-10-07
sources: 1
authors: Blelly, Schunk
year: 1993
tags: [polar-wind, transport-equations, moments, H+, O+, IPWM]
---

# Blelly & Schunk 1993 — Comparative Study of 8-, 13- and 16-Moment Transport Formulations of the Polar Wind

## Summary

Systematic comparison of four fluid moment approximations for the polar-wind ionosphere (200–8600 km): the standard 5-moment set, the 8-moment set, the 13-moment set (Schunk 1977), and the 16-moment set (Demars & Schunk 1979). All four are derived from the Boltzmann equation and apply to H$^+$ and O$^+$ ions with an electron fluid, in a dipole magnetic field. The paper reports both steady-state equilibria (sunlit summer polar cap) and dynamic responses to a density depletion perturbation above 1500 km. The central findings are that the 8-, 13-, and 16-moment models give broadly consistent results at low altitudes but diverge in the collisionless regime above ~3000 km; the standard model systematically overestimates the F$_2$-region peak density; and the 13-moment electron solution blows up when the major ion (O$^+$) becomes supersonic, so subsonic O$^+$ outflow was imposed on all four models; and both the 13- and 16-moment sets develop oscillating electron-energy modes after a perturbation. *(Wiki inference, not stated in the paper: these results are consistent with [[IPWM]]'s later use of the 8-moment set. Varney 2014 describes that set as the 13-moment equations with zero stress and does not cite this paper for the choice.)*

## The four approximation levels

| Name | Variables per species | Heat flow | Pressure tensor | Notes |
|---|---|---|---|---|
| Standard (5-moment) | $n_s$, $u_s$, $T_s$ | Fourier's law (diagnostic) | Isotropic | Collision-dominated only |
| 8-moment | $n_s$, $u_s$, $T_s$, $q_s$ | Prognostic (with $\phi$, $\psi$ corrections) | Isotropic | Adequate into collisionless regime |
| 13-moment | $n_s$, $u_s$, $T_\parallel$, $T_\perp$, $q_s$ (one heat flow) | Prognostic, single $q_s$ (Eqs. 37–42) | Non-isotropic (stress → $T_\parallel \neq T_\perp$) | Electron solution blows up when O$^+$ goes supersonic |
| 16-moment | $n_s$, $u_s$, $T_\parallel$, $T_\perp$, $q_\parallel$, $q_\perp$ | Separate parallel and perpendicular heat flows (Eqs. 55–75) | Bi-Maxwellian | Most complete; smoother anisotropy than 13-moment |

*(Corrected 2026-10-07 after re-reading §2.3–2.4: the 13-moment row previously listed $q_\parallel, q_\perp$, which are the 16-moment variables. In this paper's 1-D field-aligned form, the 13-moment set has a single heat flow, and $T_\parallel/T_\perp$ come from the stress tensor.)*

The 8-moment equations are obtained from the Boltzmann equation via the 5 first moments of a Maxwellian distribution. The standard set differs from the 8-moment set by replacing the prognostic heat flow equation with Fourier's law $q_s = -K_s \nabla T_s$ where $K_s = \alpha_s T_s^{5/2}$. The 13-moment postulates a non-isotropic pressure tensor, introducing separate $T_\parallel$ and $T_\perp$ equations. The 16-moment is based on a bi-Maxwellian distribution with $E_s^\parallel = n_sk_BT_s^\parallel$, $E_s^\perp = n_sk_BT_s^\perp$ and mean energy $E_s = (E_\parallel + 2E_\perp)/2 = \frac{3}{2}n_s k_B T_s$, with $T_s = (T_\parallel+2T_\perp)/3$. It carries separate parallel and perpendicular heat flows, with mean $q_s = (q_\parallel + 2q_\perp)/2$. Thermoelectric and diffusion-thermal terms appear in the heat-flow equations of the 8-, 13- and 16-moment sets, but not in the standard set. *(Corrected 2026-10-07: the factor 1/2 in $E_s$ was missing, and these terms were previously attributed to the 16-moment set alone.)*

## Key claims

- **Standard model overestimates F$_2$-region peak density by a factor of ~6** relative to 8-, 13-, and 16-moment solutions, due to missing thermoelectric and diffusion-thermal effects that are present in the heat flow equations of higher-moment approximations. This is a non-negligible error for studies of the bottomside ionosphere.
- **All higher-moment models agree on ion densities** within ~1–2× at most altitudes, with ionospheric composition $[H^+]/n_e \approx 1.0$–$1.3\%$ for 8/13/16-moment vs ~2.5% for standard. Peak densities occur at the same altitude for 8-, 13-, and 16-moment; the standard set peaks at a *higher altitude*. Above about 1000 km the O$^+$ scale height follows $H_p = k_B(T_i^\parallel+T_e^\parallel)/m_iG$ (Eq. 98). The standard set has a lower $T_e$, so its scale height is *lower* (§3.3e). *(Corrected 2026-10-07: this previously said the standard set had a higher scale height.)*
- **H$^+$ always escapes supersonically** with upward propagating velocity at all altitudes. O$^+$ shows a region of downward flow at some altitudes in 8-, 13-, and 16-moment models due to the ambipolar diffusion restoring force acting against the upward polarization electric field that accelerates H$^+$.
- **13-moment becomes unreliable in the collisionless regime (§3.2c).** The 13-moment electron equilibrium depends on $n_e^2$ (Eq. 83). When the electron velocity rises near the top boundary, the gas becomes collisionless and the solution "blows up": $T_e^\parallel$ and $T_e^\perp$ increase sharply. This happens roughly when the major ion (O$^+$) becomes supersonic, matching Schunk & Watkins (1981). The authors call it "a serious limitation of the 13-moment approximation, which appears to be unstable in all the configurations", and **a subsonic O$^+$ outflow (Mach 0.9) was imposed on all four models** to keep them comparable. In the 13-moment solution the electron anisotropy has $T_e^\perp > T_e^\parallel$.
- **Ion anisotropies are modest (§3.3d).** The 8- and 13-moment mean ion temperatures agree, with $T_i^\parallel/T_i^\perp$ peaking at about 1.4. In the 16-moment set, the cooling term $u_iT_i^\perp A^{-1}\partial A/\partial r$ in Eq. 52 keeps H$^+$ $T_\perp < T_\parallel$ above about 4000 km.
- *(Corrected 2026-10-07: this bullet previously attributed the 13-moment instability to H$^+$ $T_\parallel \gg T_\perp$ via Eq. 52. Eq. 52 is actually the 16-moment H$^+$ perpendicular-energy equation; the instability is in the electron solution.)*
- **Dynamic perturbation propagation speeds:** For a flux-tube density depletion above 1500 km (factor of 10), perturbations propagate at ~4 km/s for O$^+$ and ~20 km/s for H$^+$ in all models. Each species carries modes at $u_s - c_s$, $u_s$ and $u_s + c_s$, so each front is broadened between $u_s\pm c_s$. Two *distinct* fronts appear on the H$^+$ profiles: one is the H$^+$ thermal response, and the other is the polarization electric field, which is tied to O$^+$ (conclusion 7). The speeds agree with Gombosi & Schunk (1988), who found 4.4 and 23 km/s. *(Corrected 2026-10-07: the two H$^+$ fronts were previously described as the $u_s\pm c_s$ edges.)*
- **13- and 16-moment sets produce oscillating electron-energy modes (§4.3, conclusion 8).** The oscillations come from coupling between $q_e$, $T_e^\parallel$ and $T_e^\perp$ (13-moment) or $q_e^\parallel$, $q_e^\perp$, $T_e^\parallel$ and $T_e^\perp$ (16-moment). The characteristic times separate: about 100 s for ion density and velocity, about 10 s for ion temperature and heat flow, and under 1 s for electron temperature and heat flow. That decouples the electron energy equations from the continuity and momentum equations. The oscillations are amplified by reflection off the imposed topside heat-flow boundary and off the dense lower ionosphere. They are absent in the standard and 8-moment sets, where Fourier's law holds for the electrons. *(Corrected 2026-10-07: this was previously stated for the 16-moment set only.)*
- **Electron temperatures:** The large downward electron heat flow imposed at the top boundary (simulating magnetospheric heating) drives $T_e$ to large values (>10,000 K) at high altitude in all models. Below 3000 km Fourier's law applies and the temperature profile can be deduced from the heat flow. Above 3000 km Fourier's law no longer holds for 13- and 16-moment models; electron anisotropy appears.
- **H$^+$–O$^+$ thermal coupling (§3.3c):**
  - Below about 400 km, collisions with neutrals keep ion temperatures near $T_n$.
  - Above that, H$^+$ (a light minor ion drifting through heavy O$^+$) is frictionally heated, and the heated H$^+$ in turn heats O$^+$ up to about 1000 km.
  - Above 1000 km, H$^+$ is still frictionally heated but O$^+$ is heated by nothing, so O$^+$ cools adiabatically in the expanding tube.
  - H$^+$ warms with altitude as long as frictional heating beats adiabatic cooling. That limit falls at 2500–3500 km in all approximations, and above it $T_{H^+}$ decreases.
  - Frictional heating starts at lower altitude in the 8-, 13- and 16-moment cases.
  - *(Corrected 2026-10-07: previously said H$^+$ above 1000 km is heated by O$^+$ through charge exchange, and attributed the trend to the standard model only.)*

## Methods / data

Numerical solution via flux-corrected transport (Boris, 1976). Lower boundary: chemical equilibrium at 200 km; neutral atmosphere from MSIS-86 (Hedin 1987), exospheric temperature 1200 K. Upper boundary: downward electron heat flow = $-5\times10^{-3}$ erg cm$^{-2}$ s$^{-1}$; O$^+$ Mach number condition ($M_s \approx 0.9$ at topside); H$^+$ positive upflow velocity. Photoionization coefficient $\beta \propto$ neutral O density (Schunk 1989). $B \propto r^{-3}$, so the flux-tube cross-section is $A \propto r^{3}$ (from $\partial_r(AB) = 0$). *(Corrected 2026-10-07 from $A \propto r^{-3}$.)* Photoionization frequency $\beta = 4\times10^{-7}$ s$^{-1}$, chosen to match EISCAT summer $F_2$ densities.

Dynamic test: initial steady-state depleted by factor 10 above 1500 km exobase; evolved for 1000 s.

## Connections

- [[Polar Wind]] — foundational comparative study of the transport equations describing polar wind; H⁺ supersonic escape, O⁺ behavior, propagation speeds, electron temperature profiles
- [[IPWM]] — uses 8-moment equations, described in Varney et al. 2014 as the 13-moment equations with zero stress. *Wiki inference:* the results here (standard-set factor-6 density error; 13-moment collisionless blow-up) favor the 8-moment choice, but Varney 2014 does not cite this paper for it.
- [[Ambipolar Diffusion]] — governs the sub-sonic lower ionosphere; ambipolar electric field drives H⁺ escape
- [[Ionospheric Energetics]] — electron heat flow from the magnetosphere as the energy source driving ion temperatures; T_e anisotropy development
- [[Field-Aligned Currents]] — thermoelectric terms in the 8-moment electron heat-flow equation (Eq. 27) matter when a field-aligned current flows; they can reduce $T_e$ by about 1000 K (§2.2)

## Open questions

- At what altitude does the 8-moment approximation break down due to growing T_∥/T_⊥ anisotropy in H⁺ — and does IPWM apply any correction for this?
- Does the oscillatory behavior of 16-moment electron solutions at high altitude invalidate the model for studies of O⁺ outflow at RISR-N-sampled altitudes (<1000 km)?
- How do the model differences change under storm-time conditions with very strong downward electron heat flux and elevated T_e?
