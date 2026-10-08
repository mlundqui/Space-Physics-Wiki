---
type: concept
status: mature
updated: 2026-10-08
sources: 5
---

# Polar Wind

Steady-state supersonic outflow of H$^+$ (and O$^+$ at higher altitudes) along open magnetic field lines in the polar cap. Analogous to the solar wind, driven by the ambipolar electric field and the pressure gradient of the light ion population.

## Classical Description

Polar-cap flux tubes are open all the way down. At low altitude the plasma is collision-dominated and close to [[Ambipolar Diffusion|diffusive equilibrium]]. Higher up, the light ions (H$^+$) pass from subsonic to supersonic flow in a Parker-type transonic solution (see [[Parker 1958 Solar Wind]], [[Polar Wind Transonic Outflow]]). In one S&N model case the H$^+$ Mach number reaches 1.17 near 1400 km (S&N Fig. 12.50); the sonic altitude depends on conditions. *(Corrected 2026-10-08: this previously said flux tubes "are open" above about 2500 km and put the sonic point at a fixed 2000–3000 km. Openness is a property of the whole field line, and the vault sources give no single sonic altitude.)* Parker (1958) showed that a hot ionized atmosphere on open field lines cannot be in static equilibrium and must expand supersonically; Banks & Holzer (1968) applied the identical formalism to the polar ionosphere, replacing coronal pressure with the ambipolar electric potential as the driving term.

Driving force: the ambipolar electric field $E_a = -(k_B/e)(T_e + T_i)/n \cdot \partial n/\partial s$ accelerates light ions upward while maintaining quasi-neutrality. O$^+$, which is heavier and collisionally tied to neutrals at lower altitudes, exerts friction that modulates the H$^+$ outflow.

## Key Physics

- **Sonic point**: where the outflow speed equals the acoustic speed; sets the transonic structure
- **Ion-neutral friction**: at lower altitudes O$^+$–H$^+$ and H$^+$–neutral collisions impede outflow; above the exobase collisions become rare
- **Electron temperature**: elevated $T_e$ (from photoelectron heating) enhances the ambipolar potential and increases H$^+$ flux
- **O$^+$ outflow**: at high altitudes (>3000 km) and during active conditions, O$^+$ can also escape via wave heating and parallel electric field acceleration; this is the "non-classical" polar wind

## Flux and Velocity

Typical escaping H$^+$ flux: ~10$^8$ cm$^{-2}$ s$^{-1}$ at the exobase. Terminal velocity ~20–50 km/s. During geomagnetic storms, O$^+$ fluxes can approach H$^+$ levels and significantly mass-load the magnetosphere.

## Moment hierarchy and model accuracy

The polar wind can be modeled at different levels of the moment hierarchy derived from the Boltzmann equation. [[Blelly Schunk 1993 Moment Comparison]] compares four approximations for an H$^+$–O$^+$ ionosphere from 200–8600 km:

| Approximation | Variables | Key limitation |
|---|---|---|
| Standard (5-moment) | $n_s$, $u_s$, $T_s$ | Overestimates F$_2$ peak density by ~$6\times$ (missing thermoelectric effects) |
| 8-moment | adds prognostic $q_s$ | Good accuracy; remains stable; used in [[IPWM]] |
| 13-moment | adds $T_\parallel$, $T_\perp$ | Unreliable in collisionless regime (anisotropy instability) |
| 16-moment | bi-Maxwellian; thermoelectric terms | Most complete; oscillating electron modes at high altitude |

The 8-moment is the practical optimum: it eliminates the standard model's factor-6 density overestimate while remaining numerically stable in the collisionless topside. The 13-moment **electron** solution blows up when the major ion (O$^+$) becomes supersonic. Blelly & Schunk therefore imposed subsonic O$^+$ (Mach 0.9) on all models. *(Corrected 2026-10-08 after re-reading the paper; see [[Blelly Schunk 1993 Moment Comparison]].)*

**Key quantitative results from Blelly & Schunk 1993 (steady-state, summertime polar cap):**
- Perturbation propagation speeds: ~4 km/s for O$^+$; ~20 km/s for H$^+$ (sonic wave mode)
- H$^+$ always escapes supersonically; O$^+$ can have downward subsonic flow at intermediate altitudes in higher-moment models
- Ionospheric composition $[H^+]/n_e \approx 1.0$–$1.3\%$ at the topside for 8/13/16-moment; standard gives ~2.5%
- Electron temperature: large values at high altitude driven by magnetospheric heat flow; below 3000 km Fourier's law is valid; above 3000 km anisotropy develops in 13- and 16-moment solutions

## Observations

First predicted theoretically (Banks & Holzer, 1968); later confirmed by DE, POLAR, and FAST satellites. EISCAT and RISR-class radars see the subsonic precursor below the sonic point.

## Related Concepts

- [[Atmospheric Escape]] — polar wind is the dominant ion escape mechanism from Earth
- [[Ambipolar Diffusion]] — governs the sub-sonic transition region
- [[Ionospheric Energetics]] — $T_e$ and $T_i$ profiles set the ambipolar potential
- [[IPWM]] — 3-D first-principles implementation of 8-moment polar wind equations

## Kinetic Structure and Collisional Transition (Schunk & Nagy §12.16)

The collision-dominated / collisionless transition occurs at different altitudes for different species. For H$^+$ the mean free path equals the scale height near ~1500 km; for O$^+$ the transition is lower (~800–1000 km). Below these altitudes the five-moment (fluid) description is accurate; above them kinetic effects develop.

**Temperature anisotropy:** Above the exobase, the magnetic mirror force preferentially reflects particles with small $v_\parallel$. This loss-cone effect depletes the low-$v_\parallel$ population, creating $T_\parallel > T_\perp$ in the escaping species. The 13-moment approximation captures this, but can become numerically unstable when H$^+$ becomes supersonic and $T_\parallel \gg T_\perp$.

**H$^+$ velocity distribution evolution:**
| Altitude | VDF shape | Physics |
|---|---|---|
| 230 km | Maxwellian | Fully collision-dominated |
| ~1000 km | Slightly non-Maxwellian | Onset of collisionless regime |
| 1850 km | Double-humped | Loss cone depleted; some particles below escape speed |
| >2000 km | Kidney-shaped | Most particles escape; non-Maxwellian core |

**H$^+$ flux limitation:** The outward H$^+$ flux is limited by the charge-exchange supply rate $\Gamma(H^+) \propto n(O^+)\cdot n(H)/n(O)$ at source altitudes (~300–600 km). During the storm main phase, when $n(O^+)$ collapses from enhanced recombination, H$^+$ supply drops catastrophically — the *H$^+$ blowout* phenomenon.

**Storm-time 3D model results (USM-PWPM):**
1. H$^+$ blowout occurs when storm-phase O$^+$ collapse eliminates the H$^+$ source
2. O$^+$ remains the dominant species to 9000 km during strong activity (Kp > 5)
3. Recovery of H$^+$ lags O$^+$ recovery by several hours after storm main phase
4. Storm-enhanced convection elevates T_i at source altitudes, increasing D_a and modifying the sonic point location
5. Post-storm H$^+$ buildup follows the O$^+$ recovery via the charge-exchange rate
6. Conjugate-hemisphere effects: asymmetric solar illumination → asymmetric H$^+$ flux between conjugate points
7. Ionospheric composition (H/O ratio) at source altitude is the primary control on long-term H$^+$ supply to magnetosphere

## Energetic Ion Outflow — Cleft Ion Fountain (§12.17)

At the dayside cusp/cleft, open field lines intersect the boundary layer where magnetosheath plasma entry occurs. Wave heating (electromagnetic ion cyclotron waves, lower-hybrid waves) and parallel electric fields associated with upward FACs accelerate O$^+$ and H$^+$ to suprathermal energies (1–100 eV) well above the thermal polar wind. This structure is called the **cleft ion fountain**.

**Observed dependencies (DE-1 statistics):**
- O$^+$ outflow rate: increases $\times 20$ from Kp 0 → 6
- O$^+$ outflow rate: increases $\times 5$ from solar minimum → solar maximum
- H$^+$ outflow rate: *decreases* $\times 2$ from solar minimum → maximum (O$^+$ competition suppresses H$^+$ at source altitudes)
- Total ionospheric ion supply sufficient to account for the entire magnetospheric plasma inventory

The $\times 5$ solar-cycle variation in O$^+$ outflow is largely driven by the EUV-controlled O/N$_2$ ratio and photoionization rate: at solar maximum the topside is richer in O$^+$ and the upwelling flux is larger. The decrease in H$^+$ at solar max reflects the increased O$^+$ density suppressing H$^+$ via charge exchange (O$^+$ + H → H$^+$ + O runs *forward* only when $T_p < ~4000$ K; at high altitude O$^+$ blocks H$^+$ flow).

## Neutral Polar Wind (§12.18)

Above ~500 km, ion-neutral charge exchange converts a fraction of the escaping ion flux into fast neutral atoms:
$$\text{H}^+ + \text{O} \rightarrow \text{H} + \text{O}^+, \qquad \text{O}^+ + \text{H} \rightarrow \text{O} + \text{H}^+$$

The resulting neutral H and O atoms inherit the ion momentum and escape along straight ballistic trajectories (not bound to field lines), spreading laterally as they travel.

**IMAGE satellite observations:** Neutral escape fluxes of $1$–$4\times10^9$ cm$^{-2}$ s$^{-1}$, comparable in magnitude to the ion outflow rate. This makes the neutral polar wind a significant, often overlooked, component of atmospheric escape.

**Neutral rain:** A fraction of escaping neutrals re-ionize at high altitude (photoionization, charge exchange) and return along field lines to the thermosphere at low latitudes, depositing their momentum and energy in the thermosphere — completing an ion–neutral recycling loop.

## N$^+$ in the polar wind

[[Albarran 2023 N+ Polar Wind MAGE]] shows that N$^+$ is an important but long-underestimated polar wind species. Earlier IPWM simulations used a charge-exchange rate for N$^+$ + O → N + O$^+$ that was ~$100\times$ too high (compared to Richards 2011 laboratory values), artificially destroying N$^+$. With the corrected rate in the HIDRA model:

- N$^+$ comprises ~10–14% of O$^+$ at 1200 km under quiet conditions, comparable to He$^+$
- Storm-time N$^+$ can reach 50–100% of O$^+$ at magnetospheric altitudes
- N$^+$ generally exceeds He$^+$ throughout the polar cap polar wind

The polar wind should therefore be treated as a four-species system (H$^+$, O$^+$, He$^+$, N$^+$) rather than three, with N$^+$ becoming significant during active periods.

## Derivations

- [[Polar Wind Transonic Outflow]] — Mach-number equation, sonic point, transonic solution
- [[Plasma Diffusion Along B]] — minor-ion scale height; why H$^+$ is pushed upward when $m_j < m_i/2$
- [[Parker Solar Wind and Spiral]] — the A ∝ r² parent problem
- [[Ion Upflow]] — the low-altitude O⁺ supply (concept page)

## Sources

- [[Schunk Nagy 2009 Ionospheres]] (§§12.16–12.18 for kinetic structure, storm response, energetic outflow, neutral wind)
- [[Blelly Schunk 1993 Moment Comparison]]
- [[Parker 1958 Solar Wind]]
- [[Albarran 2023 N+ Polar Wind MAGE]]
- AOS 205B course materials
