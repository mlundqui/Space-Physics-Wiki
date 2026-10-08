---
type: source
status: draft
updated: 2026-05-13
sources: 1
authors: Pham, Zhang, Sorathia, Dang, Wang, Merkin, Liu, Lin, Wiltberger, Lei, Bao, Garretson, Toffoletto, Michael, Lyon
year: 2022
tags: [thermosphere, TADs, neutral-density, MAGE, CHAMP, GRACE, Joule-heating, coupled-model]
---

# Pham et al. 2022 — Thermospheric Density Perturbations by TADs During August 2005 Storm

## Summary

Case study using the MAGE coupled whole-geospace model to demonstrate that most neutral mass density enhancements observed by CHAMP and GRACE at ~400 km altitude during the August 24–25, 2005 geomagnetic storm (Dst$_\text{min} \approx -170$ nT) are caused by [[Traveling Atmospheric Disturbances|TADs]] generated at high latitudes rather than by local energy deposition at the enhancement sites. The critical model requirement is accurate representation of the localized, mesoscale structure of Joule heating at high latitudes: the standalone TIEGCM driven by the empirical Weimer (2005) electric-field specification (WEIMER run) fails to capture most observed density perturbations, while MAGE — which obtains self-consistent convection and precipitation from physics-based magnetospheric models — captures significantly more TAD-associated density structures including their timing, location, and amplitude.

## Key claims

- **TADs explain most CHAMP/GRACE density peaks.** Only a small fraction of density enhancements are generated locally at the satellite's position; the majority are TADs that originated from localized Joule heating at high latitudes, propagated equatorward, and happened to intersect with the satellite track.
- **Intersection amplifies density.** When two TADs generated in opposite hemispheres propagate equatorward and intersect at low latitudes, they produce constructive interference with larger-amplitude density enhancements than either TAD alone. The 13:20 UT CHAMP enhancement traces back to a northern hemisphere TAD generated at 09:30 UT that intersected with a southern-hemisphere-originating TAD.
- **Localized Joule heating distribution is essential for TAD generation.** The WEIMER run has correct total Joule power at some times but a spatially broad, smooth distribution, leading to TADs with incorrect propagation properties. The MAGE run has mesoscale, highly localized heating zones that generate TADs with correct amplitudes and speeds. At 09:30 UT, WEIMER produces 1429 GW of hemispherically integrated Joule heating vs MAGE's 647 GW — yet MAGE captures the density enhancements and WEIMER does not, because the spatial distribution matters more than the total power.
- **Quantitative MAGE improvement over WEIMER:** During the main phase, MAGE RMSE is 40% lower than WEIMER for CHAMP and 8% lower for GRACE. $R^2$ (morphology) improves by 70% for CHAMP and 19% for GRACE. Recovery phase: MAGE achieves 100% better RMSE and $R^2$ compared to WEIMER, driven by MAGE's inner magnetosphere (ring current / RCM) dynamics that realistically capture the recovery-phase magnetospheric state.
- **Two specific TAD events characterized:**
  - 07:00 UT density enhancement: TAD backtracked to ~60°S latitude at ~06:45 UT, near the southern cusp; a high-latitude Joule heating burst generates the TAD which propagates northward and reaches the CHAMP track at 07:00 UT.
  - 13:20 UT density enhancement: TAD backtracked to northern hemisphere high-latitude sources near 09:30 UT; propagates southward for ~4 hr, intersecting with a northward-propagating southern TAD near CHAMP's equatorial location at 13:20 UT.
- **DMSP horizontal velocity validation.** MAGE-simulated horizontal velocities agree well with DMSP F13 and F15 measurements in the northern hemisphere during the 09:30–10:00 UT pass. Southern hemisphere passes (F14, F16) show more discrepancy, suggesting room for improvement in southern hemisphere Joule heating specification.
- **Missing physics:** MAGE misses two large GRACE density peaks near 11:30–12:00 UT when GRACE crosses the cusp in both hemispheres. Cusp-specific heating mechanisms not yet in MAGE — direct soft electron precipitation (Zhang et al. 2015) and Alfvén wave heating (Hogan et al. 2020) — are likely responsible.
- **Connection to TIDs.** TADs drive traveling ionospheric disturbances (TIDs) via neutral wind momentum transfer to plasma; improved TAD simulation implies improved TID simulation, though TIDs are not analyzed in this paper.

## Methods / data

- **Event:** August 24, 2005 storm; Dst$_\text{min} \approx -170$ nT. IMF Bz: +50 nT → −50 nT, sustains $\approx -50$ nT for extended period. Storm phases: quiet (before SSC at 06:00 UT), main (06:00–13:00 UT), recovery (13:00–24:00 UT).
- **CHAMP and GRACE neutral density:** Accelerometer-derived (Sutton 2011); mapped to 400 km altitude assuming diffusive equilibrium at MSIS temperature. Both satellites at similar altitudes but different local times.
- **MAGE:** GAMERA (global MHD magnetosphere, 7th-order, ~600 km plasma-sheet resolution, 192×192×256 cells) + RCM (ring current, 180×361 cells, 115 energy channels) + REMIX (ionospheric electrodynamics, 0.5° lat/lon) + high-resolution TIEGCM (0.625° lat/lon, quarter-scale-height vertical, 97–700 km, 288×576×57 cells). Starts 23 Aug 2005 12:00 UT for spin-up.
- **WEIMER:** Standalone TIEGCM with same high-resolution configuration, driven by Weimer (2005) empirical electric field specification instead of physics-based GAMERA/REMIX.
- **Virtual satellites:** MAGE and WEIMER output sampled at CHAMP/GRACE positions and altitudes; RMSE and $R^2$ computed against observed neutral density.

## Connections

- [[Joule Heating]] — spatial distribution of Joule heating is more important than total power for TAD generation; localized mesoscale heating produces well-propagating TADs, broad empirical heating does not; MAGE vs WEIMER comparison is a key validation
- [[Traveling Atmospheric Disturbances]] — this paper is the primary source for TAD physics in the wiki; bi-hemispheric generation, equatorward propagation, constructive interference
- [[Field-Aligned Currents]] — MAGE self-consistently computes FACs from first-principles magnetospheric dynamics; localized FAC structure determines localized Joule heating → TAD generation
- [[Ionospheric Energetics]] — adiabatic heating/cooling from TAD passage (thermospheric expansion/compression); density-temperature-wind coupling during TAD propagation
- [[Aurora]] — diffuse electron precipitation (RCM loss-cone physics) contributes to MAGE conductance, shaping the Joule heating distribution
- [[GITM]] — not used in this paper, but TIEGCM serves the same ionosphere-thermosphere role in MAGE as GITM does in other coupled frameworks; comparison illustrates trade-offs in IT model selection for coupled simulations

## Open questions

- Can MAGE (with cusp precipitation and Alfvén wave heating added) capture the two large GRACE cusp-region enhancements at 11:30–12:00 UT that are currently missed?
- How does the TAD-to-TID conversion efficiency depend on the background ionospheric density and conductance — is it modulated by storm-phase density changes (cf. [[Themens 2024 May Storm]] preconditioning)?
- Do TADs from opposite hemispheres constructively interfere systematically at specific latitudes and local times, and if so, can this be used to predict low-latitude density enhancement probability?
