---
type: entity
status: draft
updated: 2026-05-19
sources: 3
tags: [model, ionosphere, empirical, climatology]
---

# E-CHAIM — Empirical Canadian High Arctic Ionospheric Model

An empirical climatological model of the ionosphere specialized for northern-hemisphere high latitudes ($\geq$ 50°N geomagnetic latitude; 80–3500 km altitude). Developed by D. R. Themens and colleagues at the Canadian High Arctic Ionospheric Network (CHAIN). Replaces the IRI in the polar cap and auroral zone where IRI is known to perform poorly because the ionosphere is strongly geomagnetically driven. Notably, E-CHAIM's training set includes [[RISR-N]] data, so E-CHAIM and RISR-N are not statistically independent — a caveat to bear in mind when using E-CHAIM as a reference against RISR-N observations.

## Architecture

E-CHAIM is composed of four sub-models, each independently fitted:

| Sub-model | Coverage | Notes |
|---|---|---|
| NmF2 | F-layer peak density | Spherical cap harmonics in AACGM at 350 km |
| hmF2 | F-layer peak height | Same expansion; separate storm module |
| Topside | $h_{mF2}$ → 3500 km | NeQuick-style; shape parameter $g = 0.18$ fixed |
| Bottomside | $\sim$80 km → $h_{mF2}$ | Parameterized scale thickness layers |

Optional modules activated by keyword: `/storm_nmf2` (activity-dependent NmF2 perturbation), `/precip` (precipitation-modified DENS profile), `/dregion` (D-region density below ~90 km).

## Coordinate system

Horizontal expansion uses **AACGM** (Altitude Adjusted Corrected Geomagnetic) coordinates. Seasonal variability is represented by a Fourier expansion; solar cycle variability by the 27-day smoothed F10.7 and the IG12 index.

## Driving indices

- **Solar:** F10.7 (27-day smoothed), IG12 index
- **Geomagnetic activity:** AE index (primary); falls back to a synthetic AE from PC index when AE unavailable; synthetic AE = 0 if PC also unavailable
- **Storm model:** additionally uses Dst and ap

## Operational modes

Three modes available in MATLAB and C (IDL lacks the Map mode):

- **Default** — vertical profile at each geographic lat-lon location
- **Satellite** — single density value at each (lat, lon, alt) point; convenient for satellite track comparisons
- **Map** — horizontal electron density map at a fixed altitude

## Error flags

| Flag | Meaning |
|---|---|
| A | AE unavailable; PC-based synthetic AE used |
| B | PC unavailable; AE = 0 assumed |
| C | Input beyond available IG index; forecasted IG12 used |
| D | Input beyond forecasted F10.7 range; output → NaN |
| E | NOAA forecasted F10.7 used instead of standard |
| F | Input beyond forecasted IG12 range; output → NaN |
| G | Input below 50°N MGLAT (recommended lower bound); output unreliable |
| H | Input below 45°N MGLAT (hard lower bound); output → NaN |
| I | AP index outside available range; clipped to all-time median (9.1) |
| J | DST index outside available range; clipped to all-time median (−10.2) |

## Outputs commonly used

- $N_mF2$ and $h_{mF2}$ ([[F-Layer]] peak density and height) at arbitrary location and time
- Full electron density profile via NeQuick topside + bottomside model
- Ancillary outputs: AACGM coordinates, magnetic local time, F10.7, scale thicknesses (HBot, HF1, HE, HTop)

## Use in research

[[Lundquist Varney 2026]] uses E-CHAIM as the climatological reference against which RISR-N profiles are flagged as "lifted" ($\Delta h_{mF2}$ anomaly) or "dense" ($\Delta N_{mF2}$ anomaly). Empirical baseline + ISR observation is a standard pattern for polar-cap density-structure detection; the non-independence of E-CHAIM and RISR-N training data is acknowledged but treated as a second-order effect given that RISR-N constitutes a small fraction of the full training dataset.

## Validation against RISR-N

[[Larson 2023 E-CHAIM vs RISR]] (2010–2019, non-storm-time) finds:
- E-CHAIM/RISR-N ratio $\approx 1$ at the F2 peak for both $N_mF2$ and $h_{mF2}$ — the model is well calibrated on average.
- Topside and bottomside electron density are underestimated by ~10–20%.
- Bottomside error is worst in summer and equinoctial nighttime; topside error worst in autumn nighttime.
- E-CHAIM cannot predict the highest observed densities or largest $h_{mF2}$ anomalies — extreme events driven by storms and strong convection exceed the empirical envelope.
- Winter polar-cap training data are too sparse to constrain climatology reliably.

This validation reinforces the caveat that RISR-N is partially in E-CHAIM's training set — average-state agreement is expected; the key limitation is the failure at extremes.

## Acknowledgement (when used)

"E-CHAIM development was supported under Defence Research and Development Canada contract number W7714-186507/001/SS and is maintained by the Canadian High Arctic Ionospheric Network (CHAIN) with operations support from the Canadian Space Agency."

## Sources

- [[Lundquist Varney 2026]]
- [[Themens 2018 ECHAIM Primer]]
