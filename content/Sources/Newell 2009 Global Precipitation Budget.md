---
type: source
status: draft
updated: 2026-10-07
sources: 0
authors: P.T. Newell, T. Sotirelis, S. Wing
year: 2009
doi: 10.1029/2009JA014326
tags: [aurora, precipitation, DMSP, auroral-energy-budget, empirical-model, OVATION]
---

# Newell 2009 Global Precipitation Budget

## Summary

Eleven years of [[DMSP]] SSJ/4 data (1988–1998, 9632 satellite-days) are used to build an empirical precipitation model that **separately classifies every spectrum** into one of four types: **monoenergetic** (quasi-static $E_\parallel$), **broadband** (dispersive Alfvén waves), **electron diffuse** and **ion diffuse**. Each is fit in every 0.25 h MLT × 0.25° MLAT bin against the solar-wind coupling function $d\Phi_{MP}/dt = v^{4/3}B_T^{2/3}\sin^{8/3}(\theta/2)$. This is the paper that defines the three electron-aurora categories used on [[Auroral Acceleration]]. *To my knowledge it is the basis of the OVATION Prime model, but the paper does not use that name, so treat this as unverified.*

**Headline result:** the **diffuse aurora dominates the energy budget**. It is 84% of hemispheric precipitating energy flux under low driving (63% electrons + 21% ions) and still 71% under moderately high driving. **Broadband aurora is the smallest by energy but the most dynamic** (8× increase with driving), and under active conditions it contributes more *number* flux than monoenergetic aurora.

## Key claims

- **Classification (DMSP, zenith-pointing, so only loss-cone particles):**
  - **Monoenergetic:** differential energy flux peak above $10^8$ eV cm⁻² s⁻¹ sr⁻¹ eV⁻¹, falling to 30% or less within 2 channels on both sides. A Maxwellian falls only to about 80% per channel (step factor 1.43). Average energy must be at least 80 eV.
  - **Broadband:** 3 or more channels above $2\times10^8$, reaching at least 140 eV (at least 300 eV at 9.5–14.5 MLT, to exclude cusp Maxwellians); not monoenergetic.
  - **Diffuse:** everything else (kappa-like), extrapolated to 50 keV.
- **Energy flux (GW, Table 1):**

  | Type | Low driving | High driving | Factor |
  |---|---|---|---|
  | Diffuse ions | 2.3 (21%) | 4.9 (14%) | 2.1 |
  | Diffuse electrons | 6.8 (63%) | 20.2 (57%) | 3.0 |
  | Monoenergetic | 1.1 (10%) | 5.8 (15%) | 5.3 |
  | Broadband | 0.6 (6%) | 4.8 (13%) | **8.0** |

  Over all conditions, combined diffuse is 77%. "Low" and "high" are 0.25× and 1.5× the mean driving.
- **Number flux (Table 2, high driving):**
  - Diffuse electrons 48%, **broadband 28%**, monoenergetic 21%, ions 4%.
  - Broadband number flux rises about 4× with driving.
  - *Implication:* the soft, abundant broadband electrons (no other type contributes such high energy flux below 1 keV) are likely what drives **ionospheric heating and ion outflow** in active times.
- **Morphology:**
  - Energy flux peaks on the **nightside** (premidnight for monoenergetic and broadband; postmidnight into morning for electron diffuse, following eastward E×B drift).
  - Number flux peaks on the **dayside** (cusp and boundary layers, including the LLBL).
  - Monoenergetic aurora maps to Region 1 (Iijima–Potemra).
- **Broadband occurrence:**
  - Probability peaks **late morning** (up to about 10% of spectra); energy flux peaks **premidnight**.
  - It is seen **throughout the oval**, including an irregular ring near 65° MLAT, not only at the poleward edge.
  - Possibly linked to magnetopause surface waves coupling into the ionosphere (Chaston 2005).
- **Monoenergetic aurora:**
  - More than 20% of spectra in the poleward and dusk oval.
  - Most such events have sharp edges and flat potentials, not gradual "inverted-V" ramps (Newell 2000).
  - UV insolation suppresses acceleration, and the largest potentials sit in deep nightside density cavities.
- **Diffuse aurora mechanism (as stated here):**
  - Ions are scattered by field-line curvature (current-sheet scattering).
  - Electrons are scattered "mostly by waves, especially broadband electrostatic waves," that is, ECH-type. **[[Thorne 2010 Chorus Diffuse Aurora]] disputes this and identifies chorus as dominant.**
- **Isotropy assumption.** DMSP sees only the loss cone, so treating all precipitation as isotropic may *understate* the diffuse fraction, because accelerated aurora is more field-aligned.

## Methods/data

DMSP F6–F13 SSJ/4 (845 km, 30 eV–30 keV). 46,080 per-bin linear regressions against $d\Phi_{MP}/dt$, plus per-bin occurrence-probability fits. Solar-cycle averaged; mean $\langle d\Phi_{MP}/dt\rangle = 4421$.

## Connections

- [[Auroral Acceleration]], [[Aurora]] — the three-type taxonomy and energy budget
- [[DMSP]] — instrument
- [[Thorne 2010 Chorus Diffuse Aurora]] — disagrees about the diffuse electron scattering mechanism
- [[Chaston 2007 DAW Auroral Acceleration Fraction]] — the larger DAW fraction is not directly comparable (see there)
- [[Field-Aligned Currents]] — monoenergetic aurora tracks R1; cf. [[Xiong 2020 FACs Precipitation DMSP]]
- [[Atmospheric Escape]] — broadband number flux and ion outflow; dayside boundary layers dominate number flux
- [[High-Speed Streams]] / [[Ionospheric Storms]] — solar-wind driving dependence

## Open questions

- Broadband events at about 65° MLAT (the equatorward oval) during non-storm times "deserve detailed study" (authors).
- The UV-insolation and hemisphere dependence was promised for a follow-up.
