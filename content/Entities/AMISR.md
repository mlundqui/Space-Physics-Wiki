---
type: entity
status: draft
updated: 2026-10-07
sources: 3
tags: [instrument, radar, isr]
---

# AMISR — Advanced Modular Incoherent Scatter Radar

A family of electronically-steerable, phased-array incoherent scatter radars. The defining feature is pulse-to-pulse beam steering without moving parts: a typical AMISR experiment cycles between a fixed set of beam positions, and returns from the same beam direction are averaged in post-processing.

Each panel records raw voltage samples and integrated autocorrelation functions; the ACFs are fit (nonlinear least-squares) for plasma parameters — electron density, electron and ion temperatures, and line-of-sight velocity — using AMISR's nonlinear ACF fitting toolchain. Fitted parameters are distributed via the SRI AMISR database.

## Members

- [[RISR-N]] — Resolute Bay, north-facing (operating since 2009).
- RISR-C — Resolute Bay, south-facing companion (since 2016).
- PFISR — Poker Flat, Alaska. *(referenced by Zou et al. 2017 in ion-upflow context; no dedicated page yet.)*

## Reference

The AMISR system is described in Valentic et al. (2013), "AMISR: The Advanced Modular Incoherent Scatter Radar," in *2013 IEEE International Symposium on Phased Array Systems and Technology* — cited by every AMISR-using paper.

## Derivations

- [[Incoherent Scatter Spectrum]] — physics of the incoherent scatter spectrum

## Sources

- [[Lundquist Varney 2026]]
- [[Bahcivan 2010 Initial RISR-N Observations]]
- [[Gilles 2018 RISR SuperDARN Velocity Comparison]]
- [[Sivadas 2020 Thesis Energetic Precipitation]] — PFISR D/E-region ionization inverted to 5–300 keV electron spectra (maximum entropy), validated against conjugate THEMIS; steerable 2-D energy-flux maps
