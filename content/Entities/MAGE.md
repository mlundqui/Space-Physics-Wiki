---
type: entity
status: draft
updated: 2026-05-19
sources: 2
tags: [model, coupled, magnetosphere, ionosphere, thermosphere]
---

# MAGE

The **Multiscale Atmosphere Geospace Environment** model — a first-principles, fully coupled whole-geospace simulation framework developed at NCAR. MAGE combines four physics-based component models into a two-way coupled system that self-consistently simulates the solar wind, global magnetosphere, ring current, ionospheric electrodynamics, and ionosphere-thermosphere (IT) system without the empirical parameterizations that standalone IT models require for their high-latitude inputs.

## Component models

| Component | Model | Function | Grid |
|---|---|---|---|
| Global magnetosphere | GAMERA | Single-fluid MHD; solar wind → magnetopause → magnetotail | $192\times192\times256$ cells; 7th-order reconstruction; ~600 km plasma-sheet resolution |
| Ring current | RCM | Bounce-averaged drift of ions and electrons in inner magnetosphere | $180\times361$ cells (lat/lon); 115 energy channels each species |
| Ionospheric electrodynamics | REMIX | Electrostatic potential solver (Poisson's eq.); monoenergetic precipitation from MHD; diffuse precipitation via RCM | 0.5° lat/lon; equatorward boundary at 45° magnetic latitude |
| Ionosphere-thermosphere | TIEGCM (high-res) | Chemistry, dynamics, and composition of neutrals and ions; 97–700 km at solar max | 0.625° lat/lon (ring-average filtered); quarter-scale-height vertical; $288\times576\times57$ cells |

## Coupling architecture

GAMERA provides electric field and field-aligned currents to REMIX. REMIX solves for electrostatic potential, maps to TIEGCM, and computes monoenergetic precipitation. RCM supplies diffuse precipitation (loss-cone electrons) to REMIX, improving conductance over MHD-only specifications. TIEGCM passes conductance back to REMIX; the loop is self-consistent.

The key advantage over standalone TIEGCM + empirical drivers (e.g., Weimer electric field): MAGE obtains convection pattern and precipitation from physics-based first principles, capturing mesoscale spatial structure in Joule heating that empirical models smooth out.

## Key advantage: localized Joule heating

MAGE's mesoscale Joule heating distribution is critical for simulating [[Traveling Atmospheric Disturbances|TADs]]. Empirical (Weimer-driven) TIEGCM produces spatially broad heating that generates TADs with incorrect amplitudes and propagation. MAGE's localized heating generates TADs with correct timing, speed, and amplitude as observed by CHAMP and GRACE at 400 km ([[Pham 2022 TADs]]). A coupled whole-geospace model with high spatial resolution is necessary to properly simulate storm-time thermospheric neutral density perturbations at all latitudes.

## Application: geospace plume (Bao 2023)

[[Bao 2023 Geospace Plume MAGE]] uses MAGE 1.0 to simulate the 31 March 2001 superstorm (Dst$_\text{min}$ −400 nT). Key results:

- MAGE self-consistently reproduces the co-evolution of the plasmaspheric drainage plume and the ionospheric SED/TEC plume, proving their linkage is electrodynamic (shared $\mathbf{E}\times\mathbf{B}$ field) rather than mass exchange.
- The ring current's energy-dependent gradient/curvature drifts determine the locations of the Region-2 current closure and diffuse electron precipitation, which intrinsically set the SAPS electric field that drives dusk-side plasmasphere erosion and ionospheric TEC depletion.
- DMSP F13/F15 observations of SAPS and electron density troughs are successfully reproduced.

## HIDRA — polar wind component

[[Albarran 2023 N+ Polar Wind MAGE]] introduces **HIDRA** (High-latitude Ionospheric Dynamics and Recombination Analysis) as the replacement for [[IPWM]] within the MAGE framework. HIDRA corrects a longstanding N$^+$ chemistry bug in IPWM (charge-exchange rate was ~$100\times$ too high), bringing the polar wind species inventory to H$^+$, O$^+$, He$^+$, and N$^+$. N$^+$ now reaches 10–14% of O$^+$ at 1200 km under quiet conditions and 50–100% during storm time. The lead PI for HIDRA is Roger Varney (UCLA); first author is Albarran from UCLA.

## Missing physics (current version)

- Plasmaspheric refilling (slow process, excluded in Bao 2023; mass exchange not required for main-phase plume dynamics).
- EMIC wave-driven ring current ion losses (Bao 2023 limitation).
- Cusp-region heating: direct soft electron precipitation (Zhang et al. 2015), Alfvén wave heating (Hogan et al. 2020) — causes MAGE to underestimate density peaks when CHAMP/GRACE traverse the cusp (Pham 2022 limitation).

## Sources

- [[Pham 2022 TADs]]
- [[Bao 2023 Geospace Plume MAGE]]
