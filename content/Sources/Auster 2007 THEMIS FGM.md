---
type: source
status: draft
updated: 2026-05-19
authors: H.U. Auster et al.
year: 2007
---

# Auster 2007 THEMIS FGM

**Citation:** Auster, H. U., et al. (2008), *The THEMIS Fluxgate Magnetometer*, Space Sci. Rev., 141, 235–264, doi:10.1007/s11214-008-9365-9.

## Summary

Describes the fluxgate magnetometer (FGM) instrument on the five THEMIS spacecraft. Each probe carries a single fluxgate sensor on a compact 2-m boom — a novelty compared to heritage two-sensor designs. The FGM measures background B and low-frequency fluctuations up to 64 Hz with 0.01 nT resolution. Designed to detect abrupt magnetospheric reconfigurations during substorm onset. Digital fluxgate technology (direct sensor digitization, software-based analog hardware replacement) reduces mass while improving robustness. First-half-year in-orbit results confirm the instrument meets or exceeds mission requirements.

## Key claims

- Sensitivity: 0.01 nT at amplitudes ≥ 0.01 nT; frequency range DC to 64 Hz; measurement range covers solar wind, magnetosheath, magnetotail, and outer magnetosphere (to 30 R_E).
- Single sensor on 2-m boom (heritage instruments used two sensors on 5-m boom); digital fluxgate replaces analog hardware with onboard software.
- THEMIS probe apogees: 10–30 R_E (inner to outer probe); perigee ~1 R_E; elliptical, inclined orbits provide coast-phase (substorm) and tail-season (reconnection) science windows.
- In-flight calibration: UCLA group, spin-tone analysis of 1ω and 2ω Fourier components; calibration updated regularly over mission lifetime.
- Companion calibration paper for Van Allen Probe magnetometers using related methodology: [[Vasquez 2020 Van Allen Probe FGM Calibration]].

## Methods/data

- Digital fluxgate: sensor output digitized directly onboard; software determines calibration corrections in flight.
- Preflight: absolute calibration, inter-orthogonality matrix, alignment matrix measured in ground facility (IGEP Braunschweig; IWF Graz; UCB/UCLA).
- In-flight: spin-tone analysis at perigee where B is stable; applied to update bias and alignment parameters.

## Connections

- [[THEMIS]] — this paper is the primary instrument description for the THEMIS FGM.
- [[Field-Aligned Currents]] — THEMIS multi-probe magnetic field data used to determine FAC timing and spatial structure during substorms via curlometer technique.
- [[Aurora]] — THEMIS mission resolved the substorm-onset controversy with conjugate ground-based all-sky imagers and ionospheric radar data; field-line timing between THEMIS probes and auroral breakup.
- [[Dungey Cycle]] — THEMIS outer probe solar wind measurements provide upstream driving conditions for magnetospheric convection models used in polar cap patch studies.

## Open questions

- What is the effect of spacecraft attitude maneuvers on calibration drift at large apogee distances where B is weak?
