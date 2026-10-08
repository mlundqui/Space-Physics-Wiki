---
type: concept
status: draft
updated: 2026-10-07
sources: 8
---

# Aurora

Optical emission from the upper atmosphere produced by precipitation of energetic electrons (and ions) from the magnetosphere. The visible signature of the Region 1 [[Field-Aligned Currents|FAC system]], particle injection during substorms, and solar particle events.

## Precipitation and Ionization

Precipitating electrons (typically 1–30 keV) lose energy by collisions with N$_2$, O$_2$, and O in the upper atmosphere:
- Ionization rate peaks near 110 km for ~10 keV electrons; higher energy → deeper penetration
- Each 35 eV of electron energy creates one ion-electron pair (ionization efficiency ~34 eV)
- Ion production rate $Q(z) \sim n_e^2 / 2H$ for a Chapman-layer profile

**Precipitation types:**
- **Diffuse aurora**: precipitation into the drift loss cone from wave-particle scattering ([[Wave-Particle Interactions]]); fills a broad region; responsible for most of the energy deposition
- **Discrete aurora**: narrow arcs associated with upward [[Field-Aligned Currents|FACs]] and parallel electron acceleration

**Global energy budget** ([[Newell 2009 Global Precipitation Budget]], DMSP):
- The diffuse aurora carries **71–84%** of hemispheric precipitating energy flux (electrons 57–63%, ions 14–21%).
- Monoenergetic aurora carries 10–15%.
- Broadband aurora carries 6–13%, but rises 8× with solar-wind driving and provides 28% of number flux when active.
- The electron diffuse aurora is driven mainly by **chorus** scattering ([[Thorne 2010 Chorus Diffuse Aurora]]; Newell instead credits electrostatic, ECH-type waves; see [[Auroral Acceleration]]).
- Alfvén-wave Poynting flux from high altitude can power about 30–35% of auroral luminosity ([[Keiling 2003 Alfvén Wave Poynting Flux]]).

**Three-way electron taxonomy.** See [[Auroral Acceleration]] for the full comparison.
- **Diffuse aurora:** chorus pitch-angle scattering, no acceleration.
- **Monoenergetic (inverted-V):** quasi-static $\Phi_\parallel$; this is the discrete-arc case above.
- **Broadband (Alfvénic):** $E_\parallel$ of inertial and kinetic [[Alfvén Waves]]; field-aligned, bidirectional electrons. Median energies range from about 100 eV (cusp) to about 4 keV (premidnight) ([[Chaston 2003 FAST Small-Scale Alfvén Waves]]). Found throughout the oval; most intense at the premidnight poleward boundary.

([[Strangeway Ch11 The Aurora]], [[Sivadas 2020 Thesis Energetic Precipitation]])

**Emission and energy (Sivadas §2.6.1):**
- <1 keV electrons give 630.0 nm above 200 km.
- 1–10 keV electrons give 557.7 nm at 100–150 km, which is why green dominates.
- $I_{630}/I_{427.8}$ measures spectral hardness.

Diffuse aurora is at least about 2000 × 500 km and isotropic below about 5 keV. Pulsating aurora is lower-band chorus modulated, with energies reaching hundreds of keV.

## Optical Emissions

| Wavelength | Species | Altitude | Notes |
|-----------|---------|---------|-------|
| 427.8 nm  | N$_2^+$ (1NG) | 100–200 km | prompt emission; linear in flux |
| 557.7 nm  | O($^1$S)   | ~100 km | green; produced by O recombination + Penning reactions |
| 630.0 nm  | O($^1$D)   | ~200–300 km | red; long-lived (110 s lifetime); see [[Airglow]] |
| 391.4 nm  | N$_2^+$ (1NG) | 100–200 km | commonly used for energy flux proxy |

630 nm red arcs at high altitudes mark soft electron precipitation (sub-keV) or chemical production from elevated $T_e$.

## Conductance Parameterization

Robinson et al. (1987) empirical relations for auroral Pedersen and Hall conductances from precipitation energy flux $\Phi_E$ (mW m$^{-2}$) and characteristic energy $E_0$ (keV):

$$\Sigma_P = \frac{40\, E_0}{16 + E_0^2} \sqrt{\Phi_E} \quad \text{[Siemens]}$$

$$\Sigma_H = 0.45\, E_0^{0.85}\, \Sigma_P$$

These are widely used in coupled ionosphere-magnetosphere models.

## Knight Relation (Parallel Acceleration)

For discrete arcs where $J_\parallel$ exceeds the thermal current limit:

$$J_\parallel \approx K \, \Phi_\parallel, \qquad K = \frac{e^2 n_e}{\sqrt{2\pi m_e k_B T_e}} \quad \text{(Knight 1973, linear regime)}$$

Here $K$ is the Knight conductance (S m$^{-2}$) and $\Phi_\parallel$ is the parallel potential drop. This is the $1 \ll e\Phi/k_BT \ll R-1$ limit of the full relation. *(Corrected 2026-10-07: $K$ was previously written $n_e(e/2\pi m_ek_BT_e)^{1/2}$, which has the wrong units.)*

In practice, field-aligned potential drops of 1–20 kV accelerate the electrons producing the brightest arcs. Kinetic Alfvén waves can produce the fluctuating small-scale FAC structure within arcs.

The full textbook form (Liouville's theorem plus conservation of energy and $\mu$; [[Strangeway Ch11 The Aurora]] Eq. 11.32) saturates at $j_0B_I/B_m$ and reduces to $j \approx j_0(1 + e\Phi/k_BT)$ for small $\Phi$. That is linear in $\Phi$ with an offset $j_0$. It reduces to the bare $J = K\Phi$ once $e\Phi \gg k_BT$, because $K = j_0e/k_BT$. The forms are reconciled on [[Knight Relation]]; see also [[Auroral Acceleration]].

## Substorm Aurora

- **Auroral oval**: ring of diffuse/discrete aurora at ~65–75° magnetic latitude
- **Substorm onset**: sudden brightening of an arc near midnight, followed by poleward bulge expansion
- **Recovery phase**: gradual equatorward recession over ~30–60 min
- **Poleward-propagating wave**: after onset, a westward-traveling surge crosses the nightside oval

## Related Concepts

- [[Field-Aligned Currents]] — discrete aurora marks upward FAC
- [[Ionospheric Conductivity]] — Robinson parameterization connects aurora to $\Sigma_P$, $\Sigma_H$
- [[Airglow]] — 630 nm red line is shared between aurora and chemical airglow
- [[Wave-Particle Interactions]] — scattering into the loss cone produces diffuse aurora
- [[Auroral Acceleration]] — diffuse vs. inverted-V vs. broadband mechanisms
- [[Alfvén Waves]] — Alfvénic (broadband) aurora

## Auroral Form Taxonomy and Electrodynamics

[[Treumann 2002 Auroral Electrodynamics]] (Chapter 6 of the *Auroral Plasma Physics* review volume) provides the definitive treatment of ionospheric electrodynamics for different auroral form types:

- **Discrete arcs**: a quasi-static current circuit where the arc's enhanced conductivity channels Pedersen current across the arc while Hall current produces electrojets; the associated electric field pattern depends on the ratio of field-aligned to Pedersen conductance.
- **Westward Traveling Surge (WTS)**: optical signature of the substorm expansion onset; electrodynamics driven by FAC divergence at the leading edge.
- **Omega Bands**: periodic structures at the poleward diffuse-aurora boundary during substorm recovery; associated with the magnetospheric Kelvin-Helmholtz instability producing periodic FAC sheets.
- **Auroral Streamers**: north-south-aligned forms at the poleward boundary, ionospheric signature of bursty bulk flows (BBFs) in the central plasma sheet.
- **Polar cap aurora / transpolar arcs**: appear during northward IMF; associated with lobe convection and cusp-to-nightside reconnection; overlap with the polar-cap aurora section of [[Polar Cap Patch]].

In all forms, FAC closure through Pedersen and Hall conductance is the central electrodynamic constraint.

## STEVE (Strong Thermal Emission Velocity Enhancement)

[[Gallardo-Lacourt 2018 STEVE Statistics]] characterizes 28 STEVE events using the THEMIS all-sky imager network. STEVE appears as a latitudinally very narrow (~20 km) but zonally extensive (~2145 km) mauve/purple emission band at ~63–64° MLAT, equatorward of the auroral oval — in the same latitude band as [[Subauroral Polarization Streams|SAPS]]. Key properties:
- All 28 events occurred ~1 hr after substorm onset, following a prolonged ($\geq$1 hr) expansion phase.
- **Not caused by conventional particle precipitation**: no energetic particle impact ionization at STEVE's location; requires a different emission mechanism (likely thermal emission from the hot SAPS ion population or thermospheric wind-driven heating).
- STEVE's sub-auroral location and substorm-linked timing are consistent with it tracing the intense narrow SAPS/SAID velocity channel; the two phenomena appear to be physically linked.

## Derivations

- [[Knight Relation]] — derivation of the current–voltage relation behind discrete-arc acceleration

## Sources

Seeded from AOS 205B course materials.
- [[Treumann 2002 Auroral Electrodynamics]]
- [[Gallardo-Lacourt 2018 STEVE Statistics]]
- [[Strangeway Ch11 The Aurora]]
- [[Sivadas 2020 Thesis Energetic Precipitation]]
- [[Newell 2009 Global Precipitation Budget]]
- [[Thorne 2010 Chorus Diffuse Aurora]]
- [[Keiling 2003 Alfvén Wave Poynting Flux]]
- [[Chaston 2003 FAST Small-Scale Alfvén Waves]]
