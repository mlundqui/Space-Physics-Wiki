---
type: source
status: draft
updated: 2026-05-19
authors: G.W. Perry, K.D. Ruzic, K. Sterne, A.D. Howarth, A.W. Yau
year: 2022
---

# Perry 2021 SuperDARN Poynting Flux

*Modeling and Validating a SuperDARN Radar's Poynting Flux Profile.* Perry, G.W., Ruzic, K.D., Sterne, K., Howarth, A.D., & Yau, A.W. (2022). *Radio Science*, 57, e2021RS007323. doi:10.1029/2021RS007323.

## Summary

Develops and validates a model of the Poynting flux profile of the Saskatoon Super Dual Auroral Radar Network (SuperDARN) radar at ionospheric altitudes, using ray tracing software to propagate the vacuum Poynting flux profile through the ionosphere. Validated against Radio Receiver Instrument (RRI) measurements from CASSIOPE/e-POP spacecraft during 5 conjunctions in August 2017.

## Key Claims

1. **Great-circle path assumption is reasonable** for the 5 events studied: modeled and measured RRI antenna voltages show good agreement, validating that the main lobe follows approximately a great-circle trajectory.
2. **Simulated Poynting flux agrees well with RRI measurements** in 5 experiments, though model underperforms in some cases (likely non-uniform ionospheric conditions).
3. **Model fills a knowledge gap**: the scattering volume altitude for SuperDARN echoes has been poorly constrained — standard geolocation assumes great-circle paths but refraction and multi-hop propagation complicate this.
4. **E-region echoes have different Poynting flux profiles** than F-region echoes — useful for discriminating between E and F-region scatter sources.
5. The model can help interpret RRI measurements by distinguishing signal features due to the radar's beam geometry from those due to geophysical phenomena.
6. **Secondary maxima in SuperDARN Poynting flux profiles are common** (Bristow 2019; Burrell et al. 2015, 2018) — the model is the first tool that accounts for these properly.

## Methods/Data

- Saskatoon SuperDARN radar (Chisham et al. 2007) — one of the longest-operating SuperDARN radars.
- IRI ionosphere model for background electron density used in ray tracing.
- RRI instrument on CASSIOPE/e-POP (James et al. 2015) at LEO: measures received antenna voltages from SuperDARN transmissions.
- 5 conjunctions: 4–8 August 2017.
- Ray tracing accounts for O-mode propagation with Appleton-Hartree refractive index.

## Connections

- [[SuperDARN]] — Saskatoon radar is the modeled instrument; result applies broadly
- [[HF Radio Propagation]] — Poynting flux, ray tracing, O/X modes, secondary maxima
- [[Ionospheric Instabilities]] — field-aligned irregularities are the scattering target

## Open Questions

- Whether the great-circle assumption holds for other radars (non-polar-cap) or during extreme ionospheric disturbances.
- Extension to predicting F-region backscatter geolocation uncertainty using the Poynting flux model.
