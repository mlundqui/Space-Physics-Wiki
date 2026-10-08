---
type: source
status: draft
updated: 2026-05-19
authors: Roger H. Varney
year: 2012
---

# Varney 2012 — Photoelectron Transport and Energy Balance in the Low-Latitude Ionosphere

Cornell University PhD dissertation, 2012. Advisor: Prof. Michael Kelley.

## Summary

This thesis revisits the problem of photoelectron transport and ionospheric energetics to interpret improved plasma temperature measurements at the Jicamarca Radio Observatory (JRO). It documents SAMI2-PE, an extension of the NRL SAMI2 2-D ionosphere model that replaces SAMI2's semi-empirical electron heating scheme with a self-consistent Boltzmann-Fokker-Planck photoelectron transport solver. SAMI2-PE demonstrates that the principal failure of the original SAMI2 is the inability to reproduce the correct electron temperatures with a single free parameter (C_qe) at all altitudes simultaneously, and that physically first-principles photoelectron transport eliminates this problem — reproducing JRO T_e profiles above the F-peak to within ~30% throughout the day, including the rapid dawn temperature spike to ~3500 K.

## Key Claims

- The standard SAMI2 empirical heating model (parameter C_qe) systematically overestimates topside T_e at dawn and underestimates it in the afternoon for any fixed C_qe value; errors are 500–2000 K (25–50% of observed values). No single C_qe value fits the data at all altitudes.
- SAMI2-PE with full photoelectron transport reproduces the local-time shape, altitude profile, and magnitude of JRO T_e above the F-peak to within ~30%, including the rapid sunrise spike.
- Topside ionosphere heating is fundamentally **nonlocal**: photoelectrons are produced primarily in the off-equatorial F-regions and transported upward; the equatorial topside produces almost no photoelectrons locally. As a result, topside T_e depends indirectly on neutral winds and E×B drifts through their control of N_e distributions in the F-regions.
- The equatorial ionization anomaly (EIA) arcs at ±15° MLAT create "shadows" in the upward photoelectron flux, appearing as a T_e inflection point near 800 km altitude in the afternoon.
- N(²D) quenching by NO+ is the dominant electron heat source in the lower F-region (~240 km), changing T_e by >50%. Overestimation at this altitude suggests the neutral NO model is insufficient; better NO density specification is needed.
- Day-to-day T_e variability at JRO (~500 K differences between consecutive quiet days; July 8–13, 2008) is not reproduced by SAMI2-PE with climatological drivers. Best candidates for missing variability are variations in E×B drifts and meridional neutral winds.
- Topside T_e sensitivity to winds and electric fields operates through an indirect path: changed N_e in off-equatorial F-regions → changed photoelectron escape → changed nonlocal heating → changed T_e. This mechanism is qualitatively captured even in the original SAMI2.
- Changing winds from diverging (HWM07) to converging can change plasmaspheric N_e by a factor of 3 and T_e by ~500 K — the dominant source of inter-model variability.

## Methods / Data

**SAMI2:** NRL 2-D ionospheric model (Huba et al. 2000). Dipole grid, 90 field lines × 151 grid points per field line; max altitude ~1650 km at magnetic equator. Seven ion species (H⁺, He⁺, N⁺, O⁺, N₂⁺, NO⁺, O₂⁺); 5-moment fluid equations. Empirical E×B drift: Scherliess-Fejer [1999] model; neutral atmosphere: NRLMSISE-00; neutral winds: HWM93 (and HWM07 for sensitivity tests).

**SAMI2-PE:** Extends SAMI2 with a Boltzmann-Fokker-Planck transport equation for the photoelectron distribution function Φ(ℓ, ε, μ) — field-line position, energy, pitch-angle cosine. Four flux terms: parallel transport, magnetic mirror force, Coulomb energy loss, and pitch-angle diffusion. Sources include: HEUVAC solar EUV spectrum (Richards et al. 2006, 105 bins + 18 lines, 1.8–105 nm); Fennelly & Torr [1992] cross sections; Swartz [1985] energy cascade algorithm for 39 types of inelastic collisions. Numerics: donor-cell upwinded (DCU) scheme; Gauss-Legendre quadrature for the μ grid (even n_st, no μ=0 grid points); banded LAPACK SGBMV solver O(n_z · n_st²).

**Energy grid:** 0.25 eV bins (0–10 eV), 1 eV bins (10–60 eV), 10 eV bins (60–100 eV), 50 eV bins (100–450 eV), 100 eV bins (450–650 eV). Thermalization threshold ε_t = (3/2)k_B T_e. Reference configuration: 8 pitch-angle streams, full energy grid (~151 bins). Low-resolution fast configuration: 4 streams, 45 energy bins — 4.5 h runtime vs 18.5 h for reference, with only 5% error in T_e.

**JRO data:** Reference day March 25, 2009 (F10.7 = 68.2, Ap = 4.0, solar minimum, quiet). Six-day dataset July 8–13, 2008 (F10.7 = 67.7, Ap = 3.0) for day-to-day variability study. Full profile mode uses Hysell et al. [2008] Swartz-Farley ISR admittance formalism.

**Spectral features identified:** Enhanced flux at 20–30 eV (He II 30.4 nm line, 41 eV photoelectrons); depletion at 1.5–3 eV (N₂ vibrational excitation); edge at 2.5 eV (N(²D) quenching); high-altitude spectral maxima at 15–20 eV (low-energy electrons cannot escape easily).

## Connections

- [[SAMI2]] — primary model developed and validated here
- [[Jicamarca Radio Observatory]] — observational reference; data used for all model comparisons
- [[Ionospheric Energetics]] — provides a complete first-principles picture of the photoelectron heating problem
- [[Equatorial Ionosphere]] — EIA/equatorial arc shadow effect on photoelectron transport
- [[Ambipolar Diffusion]] — parallel transport mechanism in SAMI2 fluid equations
- [[Roger Varney]] — the thesis author, now Michael's advisor

## Open Questions

- What drives the observed ~500 K day-to-day T_e variability at JRO? Direct measurement of E×B drifts (via planned beam-steering upgrade) and off-equatorial meridional winds (via LISN ionosonde chain) needed.
- Can a new semi-empirical heating rate model derived from SAMI2-PE replace the full Boltzmann solver in SAMI3, enabling 3-D global photoelectron-aware simulations?
- The neutral NO density model near 240 km is the principal uncertain quantity for lower F-region T_e; better NO climatology would dramatically improve SAMI2-PE performance at this altitude.
