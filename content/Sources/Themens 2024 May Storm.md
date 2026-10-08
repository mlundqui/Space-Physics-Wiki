---
type: source
status: draft
updated: 2026-05-13
sources: 1
authors: Themens, Elvidge, McCaffrey, Jayachandran, Coster, Varney, Galkin, Goodwin, Watson, Maguire, Kavanagh, Zhang, Goncharenko, Bhatt, Dorrian, Groves, Wood, Reid
year: 2024
tags: [geomagnetic-storm, SED, lifting, patches, scintillation, preconditioning, ionosphere-thermosphere]
---

# Themens et al. 2024 — The High Latitude Ionospheric Response to the Major May 2024 Geomagnetic Storm

## Summary

Synoptic multi-instrument study of the May 10–11, 2024 geomagnetic storm (Dst$_\text{min} \approx -412$ nT; first Kp 9 storm since 2003; sustained Kp $\geq 8$ for $>$24 hr). The storm's ionospheric evolution divides into two phases separated by a sudden IMF By/Bz swing to positive at 2230 UT May 10: an initial active phase (1700–2230 UT) featuring SED formation, extreme F-region lifting ($h_{mF2}$ to 630 km), patch formation, and widespread GNSS scintillation; and a second day (May 11) characterized by near-complete absence of F-region plasma, no polar cap patches, and negligible GNSS scintillation despite equally severe geomagnetic forcing. The central finding is that thermospheric composition and density preconditioning on Day 1 "suffocates" the ionospheric source necessary for TOI and patch formation on Day 2, demonstrating that storm duration and IT-system memory are as important for space weather impact as instantaneous geomagnetic forcing.

## Key claims

- **Extreme midlatitude plasma lifting:** Within the SED plume (Eglin AFB ionosonde, 30.5°N, 273.5°E), $h_{mF2}$ rises by ~150 km quickly after storm onset, then oscillates with LSTID-like oscillations (~2 hr period, amplitude 150–300 km). Maximum $h_{mF2}$ reaches 630 km; $f_{oF2}$ exceeds the ionosonde upper limit (>15 MHz). Rate of $h_{mF2}$ increase is up to 300 km in ~1 hour. SED plasma peak heights at ESR (78°N) exceed 475 km (the ESR maximum operational altitude).
- **Patch formation from lifted SED plasma:** After 2100 UT, a pronounced TOI forms and patches appear. First set of patches reaches ESR at 2140 UT and can be tracked continuously in TEC. Patch peak heights at ESR also exceed 475 km — patches inherit the extreme altitudes of the SED plasma from which they split. This confirms the midlatitude SED → lifted TOI → lifted patch transport chain under extreme storm conditions.
- **IMF By reversal clears the polar cap:** At 2230 UT, IMF Bz and By swing positive by 133 and 90 nT respectively. Patch activity clears southward from polar cap over ~1 hr — the ~30 min delay is consistent with climatological response times to IMF By reversals (Case et al. 2020). After 2230 UT, no significant polar cap scintillation occurs for the remainder of the storm.
- **Thermospheric preconditioning effect:** By Day 2 (May 11), O/N$_2$ ratio decreases 50% across all latitudes (Evans et al. 2024; TIMED GUVI). Thermospheric temperatures increase ~50%. At ESR and PFISR the F2-layer is essentially absent — densities ~1 order of magnitude lower than pre-storm. G-Condition at Eglin (F1-layer density exceeds F2 density) persists until sunset. F-region recovery does not reach pre-storm conditions until the morning of May 14. The absence of F-region plasma prevents TOI and patch formation despite severe continuing geomagnetic forcing: high-latitude convection is "suffocated" from dense plasma needed to form appreciable structures.
- **Sporadic-E at SAPS boundary:** Sporadic-E forms at the sub-auroral convective boundary edge of the SED at Eglin. Strongest Sporadic-E within 4 days of this storm. Plasma drift shears of several hundred m/s at the SED edge (SAPS-region) are the likely driver, consistent with the Kirkwood & Nilsson (2000) mechanism for magnetosphere-driven high-latitude Sporadic-E. The Sporadic-E enhancement coincides with the sub-auroral ion drift (SAID)/SAPS flow channel at ~0000 UT.
- **NEIALs at PFISR:** At ~1800 UT, anomalously large topside electron density enhancement in PFISR's field-aligned beam is attributed to Naturally Enhanced Ion Acoustic Lines (NEIALs). This corrupts the field-aligned beam at PFISR during the initial auroral expansion phase.
- **Scintillation chronology:** Phase scintillation ($\sigma_\text{Phi}$) appears initially within the cusp region at ~1700 UT, spreads to the auroral oval, then propagates across the polar cap as patches transport through. By 2230 UT, broad polar cap scintillation. On May 11, very minor polar cap $\sigma_\text{Phi}$ despite severe Kp — direct consequence of absent plasma structures.
- **SEP coincidence:** A second, stronger Solar Energetic Proton event arrives May 11 at ~0200 UT (peaking ~0700 UT). This causes near-complete HF radio blackout across high latitudes, disabling SuperDARN and most ionosondes for much of the May 11 period.

## Methods / data

- **Madrigal GPS TEC:** MIT Haystack; 1°×1°, 5-min cadence; vertical TEC maps and scintillation indices (S4, $\sigma_\text{Phi}$); IPP at 350 km; 30° elevation cutoff. Scintillation plotted only where index >0.15.
- **ESR (EISCAT Svalbard Radar):** 42 m dish, 78.09°N, 16.02°E; near-vertical field-aligned IPY27 mode; electron density altitude profiles May 10–14.
- **PFISR:** 65.13°N, 212.53°E; IPY27, MSWinds, THEMIS36, and LLITED modes during event; field-aligned beam provides Ne profiles.
- **Eglin AFB ionosonde:** 30.50°N, 273.50°E; manually scaled (Reinisch & Galkin 2011); $f_{oF2}$, $h_{mF2}$, $f_{oF1}$, $h_{mF2}$, $f_{oEs}$, $h_{Es}$; plasma drift from Reinisch et al. (1998) and Kouba & Knížová (2012).
- **OMNI solar wind / geomagnetic indices:** IMF in GSM coordinates shifted to L1-magnetopause propagation time.
- **TIMED GUVI:** O/N$_2$ ratio from UV limb scans (Evans et al. 2024).

## Connections

- [[Storm-Enhanced Density]] — quantifies midlatitude SED lifting to $h_{mF2}$ = 630 km; SAPS-associated Sporadic-E at SED convective boundary; SED plasma the direct source of lifted patches
- [[Lifting]] — quantified rate: 300 km rise in ~1 hr at Eglin; LSTID-like $h_{mF2}$ oscillations (150–300 km amplitude, ~2 hr period); patch peak heights at ESR >475 km inherited from lifted SED source
- [[Polar Cap Patch]] — storm suppression counter-example; patches form in first phase from SED-origin plasma; absent entirely on Day 2 due to preconditioning
- [[Tongue of Ionization]] — TOI forms after 2100 UT as the source of patches; entirely absent on May 11 due to plasma depletion "suffocating" convection
- [[Joule Heating]] — dominant thermospheric energy source driving the O/N$_2$ composition change (50% depletion) and 50% temperature increase; preconditioning effect is a Joule heating consequence
- [[Ionospheric Instabilities]] — Sporadic-E formation at SAPS boundary; NEIALs at PFISR during initial auroral expansion
- [[E-CHAIM]] — Themens is the E-CHAIM lead developer; this storm is a severe test of high-latitude empirical models; G-Condition (ionosonde limitation) encountered at Eglin
- [[Aurora]] — auroral oval expands to ~55°N geomagnetic latitude during storm; scintillation spreads from cusp to auroral oval
- [[RISR-N]] — not used in this study (ESR and PFISR are the ISRs); but storm suppression of polar cap patches at high-latitude ISRs is confirmed at ESR/PFISR

## Open questions

- Why does the TOI-to-patch conversion happen efficiently in the initial storm phase but not in later intervals with comparable convection? Is the 2230 UT IMF By reversal the sole explanation, or is there a density threshold below which the TOI cannot sustain scintillation-producing irregularities?
- Can self-consistent coupled IT models (TIEGCM, WACCM-X) reproduce the preconditioning effect — specifically the F2-layer absence on May 11 — without post-hoc tuning of composition or heating rates?
- How common is the extreme Sporadic-E / SAPS interaction observed here, and what fraction of SAPS events produce Sporadic-E at comparable intensities?
- What is the altitude profile of the preconditioning O/N$_2$ depletion — does it extend deep enough to affect the E-region and Sporadic-E formation?
