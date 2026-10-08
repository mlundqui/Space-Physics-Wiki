---
type: source
status: draft
updated: 2026-05-12
authors: [M. T. Lundquist, R. H. Varney]
year: 2026
tags: [risr, polar-cap, f-region, statistical-survey]
---

# Lundquist & Varney 2026 — F-Region Peak Survey at RISR-N

*A Statistical Survey of F2 Layer Peak Properties in the Polar Cap Ionosphere Observed by RISR-N.* J. Geophys. Res. Space Physics, 131, e2025JA034676. doi:10.1029/2025JA034676.

## Summary

A 16-year statistical survey (2009–2025) of polar-cap [[F-Layer|F-region]] peak properties at [[RISR-N]]. An Epstein-form layer model is fit to every 1-min long-pulse electron-density profile to extract N_mF2, h_mF2, and bottomside/topside scale heights; each profile is then compared against [[E-CHAIM]] climatology. Profiles whose h_mF2 is anomalously high relative to E-CHAIM are flagged **L** (lifted); profiles whose N_mF2 is anomalously high are flagged **D** (dense); profiles meeting both criteria simultaneously are **LD**. The headline result is that L and D events have **nearly disjoint seasonal distributions and different solar-wind/geomagnetic signatures**, implying they are physically distinct phenomena rather than two facets of the same population — challenging the conventional grouping of polar-cap density structures under a single "[[Polar Cap Patch|patch]]" label.

## Key claims

- **L and D events are statistically distinct populations.** Counts over 2009–2025: 5,002 L / 2,470 D / 93 LD. Seasonally near-disjoint (D in winter; L in spring/early summer).
- **D events** are most common in winter; correlated with slow solar wind and southward IMF Bz; *not* correlated with AE or SYM-H. Consistent with prior [[Polar Cap Patch]] climatologies (David et al. 2016, Kagawa et al. 2021).
- **L events** prefer spring/early summer; correlated with fast solar wind, high AE/AU/AL, and high dynamic pressure; *not* correlated with negative Bz or SYM-H. The combination of conditions matches coronal-hole / [[High-Speed Streams|high-speed-stream]] driving, not classical CME-driven storms.
- **L events appear to be a previously unidentified phenomenon.** They lack the seasonal signature of polar cap patches and may have been missed by airglow surveys: low N_mF2 means dim red-line emission even when [[Lifting|lifted]] enhances per-altitude excitation rates.
- **LD events are rare** (93 in 16 years) and prefer solar maximum (high F10.7). They correlate with negative Bz but not with AE/SYM-H. Plausibly related to [[Storm-Enhanced Density]] plumes lifted into the polar cap by poleward-and-upward E×B drift (cf. Zou et al. 2014/2017).
- **Major storms** (SYM-H < −150 nT) produce L events but not D or LD events.
- **Lifetime of polar-cap density structures depends on altitude.** F-region loss rate is set by the O+·N2 / O+·O2 atom–ion interchange reactions, so [[Lifting|lifting]] plasma out of the molecular-rich lower thermosphere slows recombination. The distinction between L, D, and LD outcomes therefore encodes different Lagrangian altitude histories of the same plasma parcels.

## Methods / data

- **Instrument:** [[RISR-N]] uncoded long-pulse experiments (480 µs at 30 µs oversampling, or 330 µs at 20 µs; ~72 km / ~49.5 km effective range resolution). Single high-elevation beam (≥75° elevation, excluding 90° due to grating-lobe / steering-limit issues). The single-beam choice precludes algorithmically distinguishing isolated [[Polar Cap Patch|patches]] from a [[Tongue of Ionization|TOI]] writhing through the field of view — hence the deliberate "lifted / dense / LD" terminology in place of "patch."
- **Profile fit:** four-parameter Epstein model (N_mF2, h_mF2, H_b, H_t) via nonlinear least-squares (`scipy.optimize.leastsq`), with a library of 8 initial guesses; reduced-χ² acceptance band 0.1–10. Profiles with fewer than 6 surviving altitude points or large parameter errors are rejected.
- **Reference model:** [[E-CHAIM]] evaluated at every RISR-N timestamp. The authors note that E-CHAIM's training data includes RISR-N.
- **Event metrics:** Δh_mF2 = (h_RISR − h_ECHAIM)/h_ECHAIM and ΔN_mF2 = log(N_RISR)/log(N_ECHAIM). Threshold for L or D = database median + 1.5 × IQR. Minimum event length 2 min (two consecutive 1-min samples). L events additionally require N_mF2 ≥ 10¹¹ m⁻³.
- **Solar wind / geomagnetic context:** [[OMNI]] propagated to bow shock and interpolated to RISR-N timestamps using [[pySPEDAS]]. AE for dates after 2020 from the ELFIN proxy AE database (OMNI AE is unavailable for that period).
- **Statistics:** Welch's t-test (`scipy.stats.ttest_ind`) with a 24-hr decoupling rule to mitigate within-experiment autocorrelation. Bold t-scores/p-values in Tables 1–2 mark p < 10⁻³.
- **Exclusions:** the 10 May 2024 storm is manually excluded — NEIAL (naturally-enhanced ion-acoustic line) contamination corrupts the ACF fits, per Themens et al. (2024).

## Connections

- Instrument and family: [[RISR-N]], [[AMISR]]
- Models / data products: [[E-CHAIM]], [[OMNI]], [[pySPEDAS]]
- Concepts: [[Ionosphere]], [[F-Layer]], [[Polar Cap Patch]], [[Tongue of Ionization]], [[Lifting]], [[Dungey Cycle]], [[Storm-Enhanced Density]], [[High-Speed Streams]]
- People: [[Michael Lundquist]], [[Roger Varney]]

## Open questions

- What is the physical origin of L events, and why do CH/HSS conditions favor their formation? Flagged explicitly by the authors as needing follow-up.
- For LD events: what aspects of the 6 March 2016 storm (the dominant source of LD events in the database) made it conducive? More broadly, what 3-D Lagrangian transport histories produce lifted-and-still-dense parcels deep in the polar cap?
- Are L events optically detectable? They are predicted to be dim; confirming would require coincident airglow + ISR observations.
- Implications for ion upflow: LD events look like a plausible new candidate population for large outflow fluxes (Zou et al. 2017 PFISR / SED context). Worth a targeted follow-up.
- Should L/D be further split by electron temperature (hot vs cold, à la Zhang et al. 2021)? Not done here.

## Citation

Lundquist, M. T., & Varney, R. H. (2026). A statistical survey of F2 layer peak properties in the polar cap ionosphere observed by RISR-N. *Journal of Geophysical Research: Space Physics*, 131, e2025JA034676. https://doi.org/10.1029/2025JA034676
