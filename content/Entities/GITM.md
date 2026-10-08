---
type: entity
status: draft
updated: 2026-05-13
sources: 1
tags: [model, ionosphere, thermosphere, simulation]
---

# GITM — Global Ionosphere-Thermosphere Model

A three-dimensional, time-dependent fluid model of the coupled Earth's ionosphere and thermosphere, developed at the University of Michigan (Ridley et al. 2006; Deng et al. 2008a, 2008b; Pawlowski and Ridley 2008, 2009). GITM uses altitude (rather than pressure) as the vertical coordinate, which allows it to realistically capture thermospheric upwelling and density changes in the upper boundary region — a critical capability for storm-time simulations where large vertical mass flux occurs.

## Model description

- **Domain:** ~100 to ~700 km altitude; 50 vertical levels; 1° latitude $\times$ 2.5° longitude horizontal resolution (typical configuration)
- **Neutral species:** O($^3$P), O($^1$D), O$_2$, N$_2$, N($^4$S), NO
- **Ion species:** O$^+$($^4$S), O$^+$($^2$D), O$^+$($^2$P), O$_2^+$, N$^+$, N$_2^+$, NO$^+$
- **Solved quantities:** 3-D neutral and ion velocities, neutral and electron/ion temperatures, mass densities
- **Upper boundary:** ~700 km — mass loss from the top boundary means GITM underestimates TEC by ~10–40% relative to GPS observations during active times, since part of the plasmasphere is outside the domain

## Driving inputs

- **High-latitude electrodynamics:** empirical potential models (Weimer 1996 or Heelis) or data-assimilation-based convection maps
- **Auroral precipitation:** Ovation-SM or other statistical precipitation models
- **Solar flux:** F10.7-based EUV parameterization
- **Lower boundary:** tides from GSWM or similar

## Applications relevant to this wiki

- [[Storm-Enhanced Density]] — GITM simulates SED plume formation via backward plasma column tracing; demonstrates multi-sector plasma origins and identifies $h_{mF2}$–TEC joint signature as a plasma-origin diagnostic
- [[Polar Cap Patch]] — GITM (Wang et al.) simulations show Region 1/2 FAC boundary can cut a continuous [[Tongue of Ionization]] into patches without requiring temporal reconnection variability ("cutting" mechanism)
- [[Lifting]] — upward ion transport in GITM is the primary SED TEC enhancement mechanism; consistent with PFISR ISR observations

## Limitations for polar cap research

- Upper boundary at ~700 km excludes plasmaspheric contributions to TEC; TEC underestimate ~22% quiet, ~39% storm-time
- The Weimer potential model may not capture rapid, small-scale convection structure in the polar cap
- Precipitation model determines auroral conductance; errors here propagate into Joule heating and plasma transport

## Sources

- [[Zou Ridley 2015 GITM Backtracer]]
