---
type: source
status: mature
updated: 2026-05-19
authors: Bao, S.; Wang, W.; Sorathia, K.; Merkin, V.; Toffoletto, F.; Lin, D.; Pham, K.; Garretson, J.; Wiltberger, M.; Lyon, J.; Michael, A.
year: 2023
---

# Bao 2023 Geospace Plume MAGE

## Summary

Presents the first whole-geospace MAGE simulation to self-consistently reproduce the coupled evolution of the plasmaspheric drainage plume and the ionospheric SED/TEC plume during the 31 March 2001 superstorm (Dst$_\text{min}$ −400 nT, CME-driven). Addresses three science questions: (a) what causes the linkage between the two plumes, (b) what specific processes shape the geospace plume, and (c) how does ring current buildup relate to geospace plume development. All three are answered using MAGE 1.0 (GAMERA + REMIX + RCM + TIEGCM) with DMSP validation.

## Key claims

- **Plume linkage is electrodynamic, not mass exchange.** Both the plasmaspheric plume (RCM) and the ionospheric TEC plume (TIEGCM) co-evolve because they are driven by the same coupled M-I $\mathbf{E}\times\mathbf{B}$ electric field. Excluding plasmaspheric refilling (turned off in simulation) does not prevent the joint evolution — proving mass exchange is not required.
- **SAPS is the dominant dusk-side erosion mechanism.** The sub-auroral polarization stream drives sunward ion flux at the dusk plasmapause, eroding the plasmaspheric plume and depleting the sub-auroral ionospheric TEC trough. SAPS velocity peaked at ~2000 m/s at 07:03 UT in this storm.
- **Two coexisting WID channels.** During the main phase, a SAPS channel at midlatitude (~45–50 MLAT) overlaps the plasmapause and causes erosion; a Convection Return Flow (CRF) channel at higher latitude (~57° MLAT) does not interact with the plasmasphere.
- **Ring current controls SAPS intrinsically.** The energy-dependent gradient/curvature drifts of ring current protons (westward) and electrons (eastward) determine the locations of the Region-2 current closure and the diffuse electron precipitation boundary, which together set the spatial extent and strength of the SAPS electric field. The hot ring current protons penetrate to deeper L-shells on the dayside while hot electrons cannot (due to their smaller gradient/curvature drift energy invariant), maintaining the SAPS field self-consistently throughout main phase.
- **Plasmasphere finger forms in the initial phase.** A single WID velocity peak extending from high to midlatitudes during the initial phase drives a plasmaspheric "finger" at the dusk edge of the plasmapause before the full SAPS double-peak structure develops.
- **DMSP validation successful.** MAGE reproduces the SAPS and CRF velocity peaks, the co-located electron density troughs, and the plasmapause location as measured by DMSP F13 and F15 during their passes over the dusk sector on 31 March 2001. Model overestimates precipitation energy flux but captures the flow structure.

## Methods / data

- **Model**: MAGE 1.0 (GAMERA 96×96×128, REMIX 1°×1° MLAT, RCM 1°×1/3°, TIEGCM 1.25°×1.25°, 57 pressure levels). Simulation covers 16 UT 30 March – 48 hr.
- **Solar wind**: OMNI (CDAWeb); SYM-H$_\text{min}$ = −400 nT at ~07 UT 31 March.
- **Validation**: DMSP F13 and F15 (06:57–07:09 UT and 08:26–08:41 UT); IMAGE EUV plasmasphere imaging; World-wide GPS TEC (Madrigal).
- **Novel diagnostics**: RCM effective electric potential for proton and electron energy channels (Eqs. 3–4) to explain spatial distribution of ring current pressure and diffuse precipitation.

## Connections

- [[MAGE]] — Bao 2023 is the primary geospace plume demonstration of MAGE; updates the entity page
- [[Ring Current]] — primary source for ring current → SAPS causal chain
- [[Subauroral Polarization Streams]] — primary source for SAPS mechanism and storm-time behavior
- [[Storm-Enhanced Density]] — SAPS drives the poleward transport that forms the ionospheric SED/TEC plume
- [[Tongue of Ionization]] — SED plume fed by SAPS ultimately becomes the TOI
- [[Field-Aligned Currents]] — Region-2 FACs are the key intermediary between ring current and SAPS
- [[DMSP]] — validation instrument
- [[Radiation Belts]] / [[Wave-Particle Interactions]] — limitations section notes EMIC and hiss wave processes not yet in MAGE

## Open questions

- How does plasmaspheric refilling (excluded in this simulation) modify the storm-recovery geospace plume structure?
- What role do EMIC-wave-driven ring current ion losses play in modulating the SAPS electric field on the dayside?
- Can MAGE reproduce the observed NEIALs at PFISR by including detailed auroral precipitation modeling?
