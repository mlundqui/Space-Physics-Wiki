---
type: entity
status: draft
updated: 2026-10-07
sources: 6
tags: [instrument, radar, isr, polar-cap]
---

# RISR-N — Resolute Bay Incoherent Scatter Radar, North Face

An [[AMISR]] phased-array incoherent scatter radar at Resolute Bay, Nunavut, Canada (geographic 74.730° N, 265.094° E; corrected geomagnetic 82.49° N, 325.3° E as of 2015). Operating since 2009. Highest geomagnetic latitude of any operational ISR — essentially always sitting inside the polar cap on open field lines — which makes it the canonical ground-based instrument for polar-cap F-region density measurements. The southward-pointing companion face RISR-C came online in 2016.

## First science observations

[[Bahcivan 2010 Initial RISR-N Observations]] established the key operational signatures in RISR-N's first science campaign: F-region electron density enhancements are tied to IMF $|B_z| \geq 5$ nT southward turnings, with onset delays of 25–75 minutes that depend on magnetic local time. Altitudinally smooth plasma profiles in the polar cap carry the fingerprint of solar-produced (not particle-produced) plasma, and ~25 km substructures within the larger density enhancements hint at early-stage instability development.

## Velocity calibration

[[Gilles 2018 RISR SuperDARN Velocity Comparison]] cross-calibrated RISR-N line-of-sight ion velocities against the Rankin Inlet and Clyde River SuperDARN radars using $5.2\times10^5$ coincident measurements over 40 days. SuperDARN F-region velocities are ~75–85% of RISR-N before applying the refractive-index correction; after correction, the two systems agree. A significant daytime contamination from E-region echoes and ground/sea scatter in SuperDARN leads to systematic underestimates when these echoes are not properly screened.

## Comparison against E-CHAIM climatology

[[Larson 2023 E-CHAIM vs RISR]] validates [[E-CHAIM]] against RISR-N for 2010–2019 (excluding storm times). The E-CHAIM/RISR-N ratio is $\approx 1$ at the F2 peak ($N_mF2$, $h_{mF2}$) but E-CHAIM underestimates by ~10–20% in the topside and bottomside. Discrepancies are worst in summer/equinoctial nighttime (bottomside) and autumn nighttime (topside). E-CHAIM fails to predict the highest density events or the largest $h_{mF2}$ excursions — the extreme states driven by substorms, storms, and strong convection lie outside what the empirical baseline can represent.

## Geometry quirks

The field-aligned direction at Resolute (~86° elevation pointed south) is *outside* RISR-N's northward-facing FOV, so no beam is exactly along **B**. Beams at 75°+ elevation are within ~20° of parallel to **B**, which is the regime used for F-region profile work. The 90° elevation beam has very poor sensitivity and is typically excluded. The nominal grating-lobe steering limit is ±35° from boresight (~55° elevation).

## Common data products

Standard fitted parameters (Ne, Te, Ti, vlos) from the SRI AMISR database; 1-min integration is the shortest commonly available product. Uncoded long-pulse (LP) experiments — typically 480 µs at 30 µs oversampling or 330 µs at 20 µs (effective range resolutions ~72 km and ~49.5 km) — are used for F-region and topside profiles.

A 100 km polar cap structure drifting at a typical $E\times B$ speed of 500 m/s crosses the radar's FOV in ~200 s, which sets the upper limit on integration time for the "uniform plasma over a 1-min integration" assumption used in fitting.

## Volumetric 3-D imaging

Because AMISR electronically steers its beam to dozens of positions each integration cycle, RISR-N can reconstruct full volumetric images of electron density at cadences of ~1–2 min. Dahlgren et al. (2012) demonstrated 3-D volumetric imaging of a [[Polar Cap Patch|polar cap patch]], resolving its altitude extent as well as its horizontal structure — the only facility at polar cap latitudes capable of this. Limitations: the radar FOV diameter of ~400 km at F-region altitudes means patches larger than ~400 km extend beyond the FOV, and only structures small enough to fit completely inside can be unambiguously identified as isolated patches rather than a segment of a larger [[Tongue of Ionization|TOI]].

## Scintillation beacon conjunctions

Lamarche, Varney & Siefring (2020) used simultaneous RISR-N volumetric electron density measurements and CERTO radio beacon signals (150/400 MHz VHF/UHF) from low-Earth-orbit satellites to characterise plasma irregularities across the full range of scintillation-relevant scales. Wavelet analysis of the beacon signal amplitudes and relative TEC reveals the multi-scale cascade from the ~100 km patch scale down to the GPS Fresnel scale (~365 m). Statistical surveys of all beacon-RISR conjunctions show no statistically significant preference for irregularities on the trailing edge of patches — irregularities are distributed throughout the patch volume.

## See also

- [[Incoherent Scatter Spectrum]] — derivation of the spectrum RISR-N fits (ion line → $N_e$, $T_e$, $T_i$, $V_{los}$)

- Family: [[AMISR]]
- Most common reference model paired with RISR-N: [[E-CHAIM]]
- Convection context: [[SuperDARN]]

## Sources

- [[Lundquist Varney 2026]]
- Varney 2026 PatchesChapter
