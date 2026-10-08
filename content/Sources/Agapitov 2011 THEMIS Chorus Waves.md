---
type: source
status: draft
updated: 2026-05-19
authors: O. Agapitov, V. Krasnoselskikh, Yu. Zaliznyak, V. Angelopoulos, O. Le Contel, G. Rolland
year: 2011
---

# Agapitov 2011 THEMIS Chorus Waves

*Observations and modeling of forward and reflected chorus waves captured by THEMIS.* Agapitov, O., et al. (2011). *Annales Geophysicae*, 29, 541–550. doi:10.5194/angeo-29-541-2011.

## Summary

THEMIS Search Coil Magnetometer (SCM) and Electric Field Instrument (EFI) observations at $L \geq 8$ show discrete ELF/VLF chorus wave packets propagating both toward and away from the equatorial source region. Reflected chorus waves are systematically attenuated by a factor of 10–30 and have ~10% higher frequency than concurrently observed forward waves. Ray-tracing simulations confirm the equatorial source location and explain reflected wave properties as arising from divergence of non-ducted ray paths during poleward propagation.

## Key Claims

1. **Both forward and reflected chorus waves are present** near the magnetic equator at $L \geq 8$; both have discrete rising-tone structure but reflected waves are much weaker.
2. **Reflected waves are attenuated 10–30× relative to forward waves** — consistent with ray-path divergence of non-ducted propagation, not absorption.
3. **Reflected waves are ~10% higher frequency** than co-located forward waves — explained geometrically: reflected waves originate at lower $L$-shells where local gyrofrequency $f_{ce}$ is larger, shifting the source band upward.
4. **Ray tracing with realistic plasma density** (geometrical optics) reproduces the observed Poynting flux directions and the frequency shift, locating the chorus source within 1000–2000 km of the geomagnetic equatorial plane.
5. **Lightning-generated whistlers** used as calibration signal to validate the Poynting vector and wave normal reconstruction method; whistler properties match theoretical predictions.

## Methods/Data

- THEMIS THA spacecraft (26 July 2008, $R_\text{GSE} = [1.1, 2.9, 0.17]\ R_E$); EFI and SCM waveform burst mode data at 8192 samp/s.
- Poynting flux direction from $\mathbf{S} = (1/2)\text{Re}(\mathbf{E}(f) \times \mathbf{B}(f)^*)$.
- Wave normal vector from Means method (minimum variance of spectral matrix) + SVD (Santolik 2003); 180° ambiguity resolved using $\mathbf{S}\cdot\mathbf{k} > 0$.
- Ray tracing using geometrical optics in realistic Appleton-Hartree magnetospheric plasma.

## Connections

- [[Wave-Particle Interactions]] — chorus waves scatter radiation belt electrons via cyclotron resonance; reflected waves extend chorus interaction to higher latitudes
- [[Radiation Belts]] — chorus is primary driver of outer belt electron acceleration and loss
- [[THEMIS]] — observing platform (SCM + EFI instruments)
- [[Plasma Waves]] — ELF/VLF chorus, whistler-mode propagation

## Open Questions

- Whether reflected chorus waves make a quantitatively significant contribution to radiation belt electron dynamics (scattering at off-equatorial latitudes).
- Conditions under which chorus becomes ducted vs non-ducted and how this affects the reflection/propagation geometry.
