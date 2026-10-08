---
type: source
status: draft
updated: 2026-05-19
authors: R.M. Albarran, R.H. Varney, K. Pham, D. Lin
year: 2024
---

# Albarran 2023 N+ Polar Wind MAGE

*Characterization of N⁺ Abundances in the Terrestrial Polar Wind Using the Multiscale Atmosphere-Geospace Environment.* Albarran, R.M., Varney, R.H., Pham, K., & Lin, D. (2024). *Journal of Geophysical Research: Space Physics*, 129, e2023JA032311. doi:10.1029/2023JA032311.

## Summary

Uses the HIDRA model (successor to IPWM within the MAGE framework) to simulate N⁺ ion abundances in the polar wind as a function of season, solar activity, and magnetospheric convection. Fixes a critical bug in IPWM's N⁺ chemistry and demonstrates that N⁺ densities typically exceed He⁺ densities and reach ~10% of O⁺ at quiet times, rising to 50–100% of N⁺ concentration at storm time. Varney is lead PI/advisor; Albarran is a UCLA AOS graduate student (Michael's group).

## Key Claims

1. **IPWM bug fixed in HIDRA**: IPWM used the wrong charge exchange rate for N⁺ + O → N + O⁺ (2 orders of magnitude too high → erroneously suppressed N⁺ in IPWM). HIDRA uses the correct Richards (2011) rate.
2. **N⁺ densities typically exceed He⁺ densities** across all conditions modeled.
3. **N⁺ ≈ 10–14% of O⁺ at 1200 km** at quiet-time low solar activity (F₁₀.₇ = 80 sfu); ratio decreases with increasing solar activity.
4. **N⁺/O⁺ ratio is ~10% of O⁺ densities** at quiet time; N⁺ concentrations approach 50–100% of N⁺ fluxes during storm time.
5. **Metastable N⁺ chemical reactions** involving O⁺(²P), O⁺(²D), N₂⁺, O₂⁺ production pathways are critical — without them, simulated ion density profiles do not match satellite observations (Atmosphere Explorer C, OGO-6).
6. **HIDRA improvements over IPWM**: GAMERA-grid pole treatment (triangle cells near pole), partial interface method for perpendicular transport, adjustable equatorward boundary at L=3 (vs fixed L=4 in IPWM), corner-based electrostatic potential.
7. Inputs from GAMERA-REMIX (MAGE GR configuration) — global MHD + ring current model — drive self-consistent precipitation and convection.

## Methods/Data

- HIDRA = High-latitude Ionosphere Dynamics for Research Applications; 8-moment fluid equations for H⁺, He⁺, O⁺(⁴S), O⁺(²D), O⁺(²P), N⁺, N₂⁺, O₂⁺, electrons; HEUVAC photoionization.
- Grid: 82 altitude bins (97–8400 km), 32 latitude bins (~1.09°), 128 longitude bins (~2.8°); equatorward boundary L=3 (54.7° invariant lat).
- Drives: 6 GAMERA-REMIX simulations: 2 seasons (summer/winter 2013) × 3 F₁₀.₇ (80/120/200 sfu); all with same MAGE GR storm driving.
- Comparison: Atmosphere Explorer C in-situ N⁺ and OGO-6 ion mass spectrometer observations from 1970s.

## Connections

- [[Polar Wind]] — N⁺ component of the polar wind
- [[IPWM]] — HIDRA is the direct successor to IPWM
- [[MAGE]] — HIDRA is part of the MAGE model framework
- [[Atmospheric Escape]] — N⁺ as an escaping polar wind ion species
- [[Roger Varney]] — lead PI and corresponding author

## Open Questions

- Role of wave-particle interactions (Alfvén waves, lower hybrid waves) in further accelerating N⁺ at high altitudes — HIDRA ignores these.
- N⁺ has not been directly observed at the relevant RISR-N altitudes; comparisons rely on older satellite data from AE-C and OGO.
