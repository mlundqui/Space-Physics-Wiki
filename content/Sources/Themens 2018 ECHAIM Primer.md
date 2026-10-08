---
type: source
status: draft
updated: 2026-05-13
sources: 1
authors: Themens et al.
year: 2018
---

# Themens 2018 — The Empirical Canadian High Arctic Ionospheric Model (E-CHAIM) Primer

## Summary

User manual and scientific primer for the [[E-CHAIM]] empirical ionospheric model. Covers the model's scope (50°N+ geomagnetic latitude; 80–3500 km altitude), its sub-model architecture (NmF2, hmF2, topside via NeQuick, bottomside), the geomagnetic coordinate system (AACGM), driving indices (F10.7, IG, AE/PC, Dst, ap), three operational modes (Default, Satellite, Map), optional modules (storm NmF2, precipitation, D-region), and error flags. Available in MATLAB, C, and IDL.

## Key claims

- E-CHAIM replaces the IRI above 50°N geomagnetic latitude and was built specifically because IRI performs poorly in the polar cap and auroral zone where the ionosphere is strongly driven by geomagnetic activity.
- The horizontal expansion uses spherical cap harmonics in AACGM (Altitude Adjusted Corrected Geomagnetic) coordinates evaluated at 350 km altitude; seasonal variability is captured by a Fourier expansion, solar cycle variability by F10.7 and the IG12 index.
- The primary geomagnetic activity driver is the AE index; when AE is unavailable, the model falls back to the PC index ($\text{AE} \approx f(\text{PC})$), and if PC is also unavailable, $\text{PC} = 0$ is assumed (Flag B).
- The storm NmF2 model adds an activity-dependent perturbation driven by AE/PC and Dst; an optional precipitation module modifies the DENS profile (but not the reported NmF2 peak).
- The topside uses a NeQuick-style formulation with the shape parameter fixed to $g = 0.18$; the bottomside is parameterized separately from the F-layer peak down to the E layer.
- Altitude bounds: recommended 50°N MGLAT lower boundary (Flag G below 50°, NaN below 45°; Flags G/H). Output is NaN if forecasted F10.7 or IG12 are exhausted (Flags D, F).
- Three operational modes: **Default** (vertical profile at a geographic lat-lon grid); **Satellite** (one density value per location-altitude point); **Map** (horizontal electron density map at a fixed altitude). IDL distribution lacks Map mode.

## Methods / data

Empirical fit to an ensemble of high-latitude ionospheric observations (ISRs including RISR-N, ionosondes, satellite in-situ data). Training data biases E-CHAIM toward the climatological mean; the model does not capture episodic structures like polar cap patches.

## Connections

- [[E-CHAIM]] — this primer is the primary reference for the model's architecture and usage
- [[RISR-N]] — part of the training dataset; E-CHAIM and RISR-N are not statistically independent
- [[F-Layer]] — NmF2 and hmF2 are the model's primary outputs
- [[Ionosphere]] — full electron density profile from D-region (optional) through topside to 3500 km
- [[Polar Cap Patch]] — E-CHAIM is used as the climatological background against which patches are identified as density enhancements
- [[Lifting]] — hmF2 anomaly relative to E-CHAIM flags lifted events in [[Lundquist Varney 2026]]
- [[Storm-Enhanced Density]] — storm NmF2 module captures large-scale storm perturbations but not the sub-storm mesoscale SED structure

## Open questions

- How well does the storm NmF2 module perform during extreme events (e.g., May 2024 superstorm) where the climatological basis may be far from observed conditions?
- What is the magnitude of the systematic error introduced by the $g = 0.18$ topside shape assumption in the polar cap versus the auroral zone?
