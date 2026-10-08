---
type: source
status: draft
updated: 2026-10-07
sources: 0
authors: N. Sivadas (advisor J.L. Semeter)
year: 2020
tags: [thesis, precipitation, ISR, PFISR, THEMIS, substorms, aurora]
---

# Sivadas 2020 Thesis Energetic Precipitation

## Summary

Boston University PhD dissertation (292 pp; advisor Joshua Semeter) on remote sensing the energy spectra of energetic (roughly 5–300 keV) electron precipitation. It inverts PFISR D/E-region ionization profiles with a maximum-entropy method and validates the result against magnetically conjugate THEMIS loss-cone fluxes. It then uses these spectra to pin down the magnetospheric sources of precipitation during substorms. Chapter 2 is a broad review of auroral forms and precipitation mechanisms, and this ingest focuses on it (§2.6–2.7), plus the Ch. 4 discussion of EMIC and kinetic Alfvén waves.

## Key claims

**Review (Ch. 2), with its citations:**
- **Auroral spectra (§2.6.1):**
  - <1 keV electrons deposit energy above 200 km, giving 630.0 nm red line (110 s lifetime, quenched below 200 km).
  - 1–10 keV electrons deposit at 100–150 km, giving 557.7 nm green line.
  - 427.8 nm N₂⁺ is prompt and scales with total energy flux.
  - The ratio $I_{630}/I_{427.8}$ gives spectral hardness.
- **Discrete arcs (§2.6.2):** mostly <10 keV electrons. Their source is "magnetic field-aligned electric fields produced by double layers or dispersive Alfven waves in the AAR."
- **Diffuse aurora:**
  - Equatorward oval; "associated with pitch angle scattering of plasma sheet electrons in the magnetosphere by chorus waves" (Thorne et al. 2010).
  - At least about 2000 km × 500 km in extent; source electrons 0.1–30 keV.
  - The precipitation is isotropic at low energy and anisotropic above about 5 keV, the signature of wave pitch-angle scattering.
- **Structured diffuse aurora (SDA):** fine structure in diffuse aurora, possibly from whistler-mode wave and density structure near the equator.
- **Pulsating aurora:** a few to tens of keV, up to 200–500 keV, from lower-band chorus cyclotron resonance. Nishimura 2010 showed the chorus–aurora correlation directly.
- **Precipitation mechanisms (§2.7.1, Lyons 1997 / Birn 2012):**
  1. Parallel $E$ fields — double layers, or "parallel components of dispersive Alfven waves"
  2. Betatron acceleration — raises pitch angle, *reduces* precipitation
  3. Current-sheet / Fermi type A–B acceleration
  4. Wave-particle interactions
  5. Turbulence
- **Current-sheet scattering:** controlled by the curvature parameter $\kappa^2 = R_c/\rho_{max}$.
  - $\kappa^2 \gg 1$: adiabatic.
  - $\kappa^2 \ll 1$: Speiser motion.
  - In between: strong pitch-angle scattering. This sets the isotropic boundary.
- **Most plasma-sheet electron precipitation is 0.3–20 keV.** Too low-energy for current-sheet scattering, so it comes either from discrete arcs (parallel $E$) or from wave-driven diffuse aurora.
- **Morphology:** soft (auroral) precipitation peaks near 23 MLT; energetic precipitation peaks near 8 MLT, consistent with lower-band chorus peaking at 6–12 MLT.
- **Conductance:** discrete arcs give the highest local conductance (Σ_H up to about 120 S), but the diffuse aurora probably dominates the *net* conductance because it covers far more area.

**Original results (Chs. 4–7):**
1. Validated ISR energy spectra for 5–300 keV against THEMIS (Sivadas et al. 2017).
2. Built 2-D energy-flux maps from steerable PFISR. A latitudinal gradient in mean energy suggests current-sheet scattering (Sivadas et al. 2019).
3. Identified EMIC-wave precipitation near the central plasma sheet during substorm expansion, and radiation-belt precipitation during the growth phase.
4. Showed that growth-phase structured diffuse aurora marks the **outer radiation belt boundary**.
5. Showed that D-region conductance makes up the majority of ionospheric conductance during substorm onset and expansion.

**Kinetic Alfvén waves (Ch. 4 §4.3.6, 26 March 2008 substorm):**
- KAWs are "highly likely" present, because the low-frequency $E/B \approx v_A \sim 10^6$ m/s.
- KAW generation is "closely related to particle injections from the magnetotail."
- Their $E_\parallel$ can trap electrons and accelerate them along the field in the plasma sheet, with energy gain "limited to several kilo-electron volts" (citing Artemyev et al. 2015).
- They may contribute to the inferred parallel potential drop. Together with AAR acceleration, they could produce up to about 10 keV electrons.
- Processes acting along the field (Fermi, potential drops, Alfvén waves, Speiser motion) produce *negative* pitch-angle anisotropy (field-aligned distributions). Betatron acceleration produces positive anisotropy.

## Methods/data

- PFISR ([[AMISR]]) electron density profiles inverted with the maximum-entropy method (Semeter & Kamalabadi 2005; cf. [[Rietsch 1977 Maximum Entropy Inverse Problems]]), using Sergienko & Ivanov 1993 Monte Carlo production rates.
- [[THEMIS]] conjugate particle and wave data.
- Magnetic field model variance analysis for mapping.
- White-light all-sky imagers and riometers.

## Connections

- [[Aurora]], [[Auroral Acceleration]] — the diffuse/discrete taxonomy and mechanisms
- [[Alfvén Waves]] — KAW evidence and trapping in the plasma sheet
- [[Wave-Particle Interactions]], [[Plasma Waves]] — chorus, EMIC, hiss
- [[Radiation Belts]] — structured diffuse aurora marks the outer belt boundary
- [[Ionospheric Conductivity]] — D-region conductance during substorms
- [[AMISR]] (PFISR), [[THEMIS]]
- [[Thayer Semeter 2004 Energy Flux]] — same group (Semeter)
- [[Artemyev 2015 KAW Electron Trapping]] — the KAW trapping paper this thesis cites (now ingested)
- [[Thorne 2010 Chorus Diffuse Aurora]] — cited for chorus-driven diffuse aurora (now ingested)

## Open questions

- Chs. 3 and 5–8 were not read in detail in this ingest. The ISR inversion method (Ch. 3) could be ingested later if it becomes relevant to [[RISR-N]] precipitation studies.
- What fraction of the "several keV" KAW-trapped electrons in the plasma sheet actually reaches the ionosphere, compared with pitch-angle scattered diffuse precipitation?
