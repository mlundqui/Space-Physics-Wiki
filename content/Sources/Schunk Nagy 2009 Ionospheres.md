---
type: source
status: mature
updated: 2026-05-19
sources: 0
authors: R.W. Schunk, A.F. Nagy
year: 2009
---

# Schunk Nagy 2009 Ionospheres

## Summary

*Ionospheres: Physics, Plasma Physics, and Chemistry* (2nd ed., Cambridge University Press, 2009) by Robert Schunk and Andrew Nagy is the primary graduate reference text on planetary ionospheric physics. It derives the full moment hierarchy from the Boltzmann equation, constructs simplified transport systems for collisional, weakly ionized, and collisionless regimes, and applies these to the terrestrial ionosphere at all latitudes, with particular depth on the high-latitude and polar cap system. The textbook is the foundational reference for polar wind theory, high-latitude O⁺ chemistry, photoionization energetics, and the transport equations underlying [[IPWM]], TIEGCM, and GITM. Roger Schunk's group at Utah State developed most of the numerical polar wind work presented in Chapter 12.

## Key claims

- **Full moment hierarchy (Ch. 3):** The Boltzmann equation (Eq 3.7) yields a moment sequence for species $s$: number density $n_s$ (3.10), drift velocity $\mathbf{u}_s$ (3.11), temperature $T_s$ (3.15), heat flux $\mathbf{q}_s$ (3.16), pressure tensor $\mathbf{P}_s$ (3.17), stress tensor $\tau_s$ (3.21). The general transport equations are continuity (3.30), momentum (3.36), energy (3.38), pressure tensor (3.39), and heat flow (3.40). The 13-moment distribution function (Eq 3.49) closes the hierarchy with a non-Maxwellian perturbed by stress and heat flow; closure expressions $\mu_s$ (3.50) and $Q_s$ (3.51) give the closed 13-moment system (3.57–3.63). The bi-Maxwellian (3.75), parameterized by $T_{s\parallel}$ and $T_{s\perp}$ (3.64–3.66), extends to collisionless regimes where magnetic mirroring drives anisotropy.

- **Simplified transport (Ch. 5):** The five-moment approximation (drifting Maxwellian; Eqs 5.22a–c) neglects stress and heat flow, valid when distributions are close to Maxwellian and collision dominance holds. Ion temperature in a weakly ionized plasma with relative drift: $T_i = T_n + (m_n/3k)|\mathbf{u}_i - \mathbf{u}_n|^2$ (Eq 5.36). Ambipolar diffusion coefficient: $D_a = 2kT_p/(m_i\nu_{in})$ (Eq 5.55), where $T_p = (T_e + T_i)/2$ is the plasma temperature. Plasma scale height: $H_p = 2kT_p/(m_ig)$ (Eq 5.59). The polarization electrostatic field: $eE_\parallel = -(1/n_e)\nabla_\parallel p_e$ (Eq 5.61). Minor ions lighter than $m_i/2$ experience a net upward force from the polarization field; this is the microscopic origin of the polar wind for H⁺.

- **O⁺ chemistry (Ch. 8):** From Table 8.3: O⁺ + N₂ → NO⁺ + N at $k_1 = 1.2\times10^{-12}$ cm³ s⁻¹ (strongly $T_{eff}$-dependent); O⁺ + O₂ → O₂⁺ + O at $k_2 = 2.1\times10^{-11}$ cm³ s⁻¹ (nearly temperature-independent); O⁺ + H → H⁺ + O at $k = 6.4\times10^{-10}$ cm³ s⁻¹ (nearly Langevin). Dissociative recombination (Table 8.5): NO⁺ + e at $4.0\times10^{-7}(300/T_e)^{0.5}$; O₂⁺ + e at $2.4\times10^{-7}(300/T_e)^{0.70}$. O(¹D) 630 nm production has eight channels (Eqs 8.57–8.68) including O₂⁺ dissociative recombination (dominant at night), photodissociation of O₂ (dayside), and electron impact; quenched by N₂ (rate $k_a$), O₂ ($k_b$), and electrons ($k_c$) with final VER formula (Eq 8.74).

- **Ionization and energetics (Ch. 9):** Solar EUV modeled via EUVAC (37 intervals, 5–105 nm; Eq 9.20), scaled by F10.7. Chapman production function (Eq 9.21): $P_c = I_\infty \eta n\sigma^a \exp[-Hn\sigma^a\sec\chi]$; peak at optical depth $\tau=1$ (Eq 9.22). Photoelectron production rate (Eq 9.24) integrates over species, ion states, and wavelengths with branching ratios $p_s(\lambda,E_f)$. Electron heating rate (Eq 9.49): $Q_e = \int_{E_T}^\infty \Phi_e(z,E)(dE/dz)_e dE$ — the photoelectron flux times the stopping-power loss rate to thermal electrons. Key electron cooling rates: N₂ rotation $\propto n_e n(N_2)(T_e-T_n)/T_e^{1/2}$ (9.50); O₂ rotation (9.51); N₂ vibration (9.58); O₂ vibration (9.60); O fine structure (9.65); O(¹D) excitation (9.67). At high latitude, at high altitude Coulomb collisions with ions dominate (Figure 9.17). Ion heating primary source is thermal electrons, not photoelectrons.

- **High-latitude convection and chemistry (Ch. 12 §12.1–12.9):** Convection E-field models: Volland (simple) and Weimer (empirical multi-cell). Ion frictional heating: $T_i = T_n + (m_n/3k)(E'/B)^2$ (§12.3). A 2× increase in E-field raises $T_{eff}$ enough to increase $k_1$ by factor ~16, dramatically depleting O⁺. Plasma patch density 3–10× background, 200–1000 km scale, convect at 300 m/s–1 km/s. Polar holes (density depletions) form on the night side where long residence times under high E fields deplete O⁺. TOI is the continuous tongue of dayside plasma entering the polar cap; patches form from TOI by cutting, scooping, and variable-convection.

- **Polar wind kinetics (§12.16):** Below ~1500 km, H⁺ is collision-dominated (Maxwellian VDF). Above ~1500 km the collisionless transition develops temperature anisotropy $T_\parallel > T_\perp$ from the magnetic mirror force. H⁺ VDF evolves: nearly Maxwellian at 230 km → double-humped (loss-cone depleted) at 1000–1500 km → kidney-shaped at 1850 km (bulk of phase space is above the escape speed). Three-dimensional time-dependent model storm results: (1) H⁺ undergoes "blowout" when storm main phase collapses O⁺ density, removing the charge-exchange source of H⁺; (2) O⁺ dominates the ion content to 9000 km altitude during strong geomagnetic activity; (3) the H⁺ flux-limitation is proportional to $n(O^+)\cdot n(H)/n(O)$ at the source altitude.

- **Energetic ion outflow (§12.17):** Cleft ion fountain — open-field O⁺ and H⁺ flow from the cusp, accelerated by wave heating and parallel electric fields. DE-1 statistics: O⁺ outflow rate increases ×20 from Kp 0→6, ×5 from solar minimum to solar maximum. H⁺ outflow rate *decreases* ×2 from solar min to max (suppressed by O⁺ competition). Ionospheric ion supply is sufficient to account for the entire magnetospheric plasma inventory, making the ionosphere the dominant magnetospheric plasma source.

- **Neutral polar wind (§12.18):** IMAGE satellite measured 1–4×10⁹ cm⁻² s⁻¹ escaping neutral atoms, comparable to the ion outflow rate. Neutral H and O atoms are produced by charge exchange when accelerating ions pick up electrons from ambient neutrals; the resulting neutral atoms escape along ballistic straight-line trajectories. A fraction of these neutrals return as "neutral rain" onto the thermosphere at low latitudes, completing an ion–neutral recycling loop.

- **Space environment (Ch. 2):** Sun: $L = 3.9\times10^{26}$ W, solar constant 1370 W/m²; corona ~$10^6$ K; CMEs up to 1000 km/s. Interplanetary medium: Parker spiral at 43° at 1 AU; solar wind Table 2.3: $\bar{n}=8.7$ cm⁻³, $\bar{u}=468$ km/s, $T_p=1.2\times10^5$ K, $T_e=1.4\times10^5$ K, $\beta=2.17$. Earth magnetosphere: bow shock ~12 $R_E$, magnetopause ~9 $R_E$ subsolar; ring current 10–300 keV; plasmasphere 4–8 $R_E$. Planetary ionospheres (§2.4–2.6): Mercury (ion exosphere, no atmosphere); Venus (ionopause = tangential discontinuity; O₂⁺ dominant despite CO₂); Mars (no intrinsic B, crustal anomalies, Viking measurements); Titan ($1.467$ bar N₂/CH₄, exobase ~1430 km); Enceladus (water-plume ionosphere ~$10^6$ cm⁻³).

- **Collision frequencies (Ch. 4):** Resonant ion-neutral collision frequency for O⁺–O: $\nu_{O^+O} = 3.67\times10^{-11}n_O T_r^{1/2}(1-0.064\log T_r)^2$ (Table 4.5). Electron-neutral: momentum transfer rates for e–O, e–N₂, e–O₂ from Table 4.4 (used in electron cooling rates Ch. 9). Full Coulomb collision tables for $\nu_{ii}$, $\nu_{ie}$, $\nu_{ei}$ from §4.3–4.4.

- **Transport coefficients (§5.12–5.14):** Electron field-aligned current + heat flux (Eqs 5.140–5.141) with electron thermal conductivity $\lambda_e = 7.7\times10^5 T_e^{5/2}/(1+3.22\times10^4 T_e^2 n_e^{-1}\Sigma n_n Q^{(1)}_{en})$. Ion thermal conductivity (Eq 5.168): $\lambda_i \propto T_i^{5/2}/M_i^{1/2}$. Higher-order ambipolar diffusion with thermal diffusion correction $\Delta_{in}$ (Eq 5.165): $D_a = k(T_e+T_i)/(m_i\nu_{in}(1-\Delta_{in}))$.

- **Plasma waves and instabilities (Ch. 6):** Systematic derivation of all ionospheric wave modes: electron plasma/Langmuir (Bohm-Gross dispersion), ion acoustic ($u_s = \sqrt{k(T_e+\gamma_i T_i)/M}$), upper hybrid ($\omega_{UH}^2 = \omega_{pe}^2+\Omega_e^2$), lower hybrid ($\omega_{LH} = \sqrt{\Omega_i\Omega_e}$), R/L circularly polarized waves, O/X extraordinary modes, whistler mode ($n^2 = \omega_{pe}^2/\omega(\Omega_e-\omega)$), Alfvén/magnetosonic MHD limit. Two-stream instability: growth when $|u_e-u_i| > u_s$. Rankine-Hugoniot shock conditions (§6.14). Double layers (§6.15): quasi-static potential drops 0.5–5 kV at 5000–8000 km altitude on S3-3 satellite.

- **MHD (Ch. 7):** Single-fluid MHD equations, generalized Ohm's law (Hall term, $\nabla p_e$ term, resistivity). Frozen-in flux theorem. Plasma $\beta = nkT/(B^2/8\pi)$. Parker spiral at 43° at 1 AU ($\tan\phi = \Omega_\odot r/u_r$). CGL double-adiabatic invariants: $p_\perp/\rho B = $ const; $p_\parallel B^2/\rho^3 = $ const; firehose and mirror instability thresholds.

- **Exosphere and escape (§10.10–10.11):** Jeans escape flux (Eq 10.84): $\Gamma_{esc} = n(r_c)v_{mp}(1+\lambda_c)e^{-\lambda_c}/(2\sqrt{\pi})$. Liouville exospheric density (Eq 10.98): $n(r) = n(r_c) e^{-E(1-y)}[1-(1-y^2)^{1/2}e^{-Ey^2/(1+y)}]$. Charge exchange reactions (Eqs 10.85–10.86) producing superthermal H. Hot O corona from O₂⁺+e dissociative recombination at Venus/Earth/Mars.

- **Mid-latitude and equatorial ionosphere (Ch. 11):** Rayleigh-Taylor instability (§11.12): gravitational drift $u_{i0}=g/\omega_{ci}$ drives R-T growth when $\partial n_0/\partial z < 0$ (bottomside F layer); full linearized dispersion Eq 11.87. Sporadic-E (§11.13): metallic ion (Fe⁺, Mg⁺) wind-shear convergence; 0.6–2 km thick; intermediate layers 10–20 km at 120–180 km descend at night. F₃ layer and He⁺ layer (§11.14): F₃ forms when PRE-driven E×B lifts F₂ above 500 km; He⁺ up to 50% abundance at 750–1200 km solar maximum. Tides and nonmigrating tides (§11.15): semi-diurnal dominant; wavenumber-4 TEC pattern (~20%) from tropospheric latent heat nonmigrating tide. Ionospheric storms (§11.16): positive phase from E×B uplift + SAPS-SED-TOI; negative phase from O/N₂ composition change driven by Joule-heating upwelling; PPEFs during storm sudden commencement.

## Methods/data

Analytical derivation throughout; numerical results from Utah State group models (USM-PWPM polar wind, 3D time-dependent IPWM, GAIM data assimilation), Atmosphere Explorer satellite data, DE-1, DE-2, IMAGE, FAST, and EISCAT/Chatanika observations. Chapter structure: space environment (Ch. 2), kinetic theory and collision terms (Chs. 3–4), simplified transport (Ch. 5), plasma waves and instabilities (Ch. 6), MHD (Ch. 7), ionospheric composition (Ch. 7–8), chemical processes (Ch. 8), ionization and energetics (Ch. 9), neutral atmospheres/exosphere (Ch. 10), mid-latitude ionosphere (Ch. 11), high-latitude ionosphere (Ch. 12), equatorial ionosphere (Ch. 13), other planetary ionospheres (Ch. 14).

## Connections

- [[IPWM]] — 8-moment polar wind equations from this textbook; Utah State group implementation
- [[Polar Wind]] — §12.16–12.18 is the primary reference for polar wind physics and kinetic structure
- [[Ion Frictional Heating]] — Ch. 12 §12.3 derives the T_i enhancement formula; Ch. 5 §5.3 gives the formal derivation
- [[Ambipolar Diffusion]] — Ch. 5 §§5.5–5.6 gives the rigorous ambipolar diffusion derivation and polarization field
- [[Polar Cap Patch]] — §§12.4–12.9 covers patch taxonomy, cutting by frictional heating, scooping, variable-convection
- [[Tongue of Ionization]] — §12.7 describes TOI structure under different IMF conditions
- [[Joule Heating]] — ion frictional heating is the microscopic source; formally equivalent to Pedersen dissipation in the neutral frame
- [[Ionospheric Energetics]] — Ch. 9 gives photoelectron heating rate (Eq 9.49) and full electron cooling rate catalog (Eqs 9.50–9.67)
- [[Airglow]] — §8.7 gives O(¹D) production channels (Eqs 8.57–8.74) and quenching rates
- [[Atmospheric Escape]] — §§12.17–12.18 on energetic ion outflow (cleft ion fountain) and neutral polar wind
- [[Ionospheric Conductivity]] — §5.11 formal derivation of Pedersen and Hall conductivities (Eqs 5.119–5.120); §5.12 electron thermal conductivity (Eq 5.146)
- [[Equatorial Ionosphere]] — §11.12 R-T instability; §11.13 sporadic E; §11.14 F₃ and He⁺ layers; §11.15 tides
- [[Ionospheric Storms]] — §11.16 positive/negative storm phase mechanisms; SAPS-SED-TOI pathway
- [[Sporadic E]] — §11.13 metallic ion wind-shear convergence mechanism
- [[Atmospheric Escape]] — §10.10–10.11 Jeans escape, Liouville exospheric density, hot O corona
- [[MHD]] — Ch. 7 frozen-in flux, generalized Ohm's law, CGL, Parker spiral
- [[Plasma Waves]] — Ch. 6 full dispersion relation derivations, two-stream instability, double layers
- [[Traveling Atmospheric Disturbances]] — §10.4 Brunt-Väisälä frequency, AGW dispersion Eq 10.37
- [[F-Layer]] — §9.3 Chapman production function; §5.5–5.7 diffusive equilibrium and plasma scale height
- [[Roger Varney]] — Schunk was a key figure in the Utah State polar ionosphere group; IPWM descends from USM-PWPM

## Open questions

- The electron cooling rates (§9.7) are largely 1970s–1990s calculations; how well do they match modern quantum chemistry?
- The 3D polar wind storm results treat the magnetosphere as a fixed boundary condition — how sensitive are storm-time H⁺ blowout dynamics to the magnetospheric thermal pressure profile?
- The kidney-shaped H⁺ VDF at 1850 km implies significant non-Maxwellian pressure tensor components; what is the closure error when IPWM (8-moment) is applied at these altitudes?
- How does neutral polar wind recycling (neutral rain) modify thermospheric O/N₂ ratios during storms?
