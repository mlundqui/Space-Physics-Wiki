---
type: entity
status: draft
updated: 2026-10-07
sources: 3
tags: [instrument, satellite, in-situ, ionosphere, LEO]
---

# DMSP

The Defense Meteorological Satellite Program — a series of US Air Force low-Earth-orbit satellites in sun-synchronous polar orbits at ~840 km altitude. Each satellite provides in-situ plasma measurements along the spacecraft track, making DMSP a primary source of high-latitude topside ionospheric data. Multiple satellites operate simultaneously, providing multiple daily passes over the polar cap in both hemispheres.

## Instruments relevant to ionospheric research

- **SSJ/4–5 (particle spectrometer):** Energetic particle fluxes (30 eV – 30 keV); used to identify auroral precipitation zones and distinguish them from polar cap open-field-line environments (no precipitation).
- **SSIES (ion drift meter + Langmuir probe):** Cross-track horizontal ion drift velocity (proxy for perpendicular $\mathbf{E}\times\mathbf{B}$), ion number density, electron density, ion temperature $T_i$, electron temperature $T_e$.
- **SSM (fluxgate magnetometer):** Vector magnetic field; used to estimate field-aligned current (FAC) density from the curl of $\mathbf{B}$.

## Role in polar cap patch research

**Hot/cold patch classification.** Ma et al. (2021) used DMSP SSIES temperatures to classify [[Polar Cap Patch|polar cap patches]] into two populations at 840 km altitude:
- Hot patches: $T_i/T_e < 0.8$; elevated $T_e$, high FAC density, enhanced ion upflow. Consistent with local production by soft particle precipitation.
- Cold patches: $T_i/T_e > 0.8$; normal photochemical equilibrium. Consistent with transport from the sunlit mid-latitude ionosphere.

The two populations have distinct spatial distributions and different dependences on IMF clock angle, supporting the view that they arise from different physical mechanisms.

**Patch occurrence statistics.** Statistical surveys using DMSP (and the analogous ESA Swarm Langmuir probe at ~460 km) have established the UT/seasonal/hemispheric patch occurrence rate. Kagawa et al. (2021) organise this statistic by the $D$ parameter (distance from solar terminator to geomagnetic pole at noon in AACGM), showing patches peak near $D \approx 1200$ km in both hemispheres.

**Ion upflow above patches.** Some patches show enhanced O$^+$ parallel flux at 840 km, while others show downflow. Enhanced upflow correlates with faster $\mathbf{E}\times\mathbf{B}$ driving conditions: fast convection raises $T_i$ via frictional heating, which amplifies the charge-exchange production of H$^+$ and can accelerate O$^+$ outward. Patches drifting into the nightside auroral oval show a sharp increase in ion upflow flux as auroral particle precipitation heats the plasma.

## Key limitation

DMSP provides a single-altitude, 1-D cut along the satellite track. A satellite traversing a folded or twisted [[Tongue of Ionization]] may record what appear to be three separate patches rather than one connected structure. Comparison with volumetric ISR data ([[RISR-N]]) or GPS TEC maps is needed to disambiguate.

## See also

- [[SuperDARN]] — convection maps that complement DMSP in-situ drift measurements
- [[RISR-N]] — full altitude profiles and volumetric imaging, complementary to DMSP's single-altitude cuts

## Storm-time ion upflow observations

[[Zou 2021 SED Ion Upflow]] uses DMSP F15 (SSIES + SSJ) at ~850 km to characterize ion upflow during the March 6–7, 2016 storm. Key observational signatures distinguish the two upflow types at DMSP altitude:

| Property | Type 1 (SAPS) | Type 2 (cusp precip) |
|---|---|---|
| $T_e$ at 840 km | Near-ambient | Elevated |
| $N_e$ at 840 km | Moderate | Enhanced (SED) |
| Precipitation (SSJ) | Weak/absent | Soft electrons present |
| Upward flux | $\sim6\times10^{13}$ m$^{-2}$ s$^{-1}$ | $\sim3\times10^{14}$ m$^{-2}$ s$^{-1}$ |

DMSP F15 observes SED topside density $\sim2\times10^{11}$ m$^{-3}$ (tripled relative to background) when the plume arrives at the cusp. Within the SED plume body at sub-auroral latitudes, DMSP measures **downward** ion flows, consistent with poleward convection expansion compressing plasma downward.


## Role in auroral precipitation research

**Global precipitation budget** ([[Newell 2009 Global Precipitation Budget]]). Eleven years of SSJ/4 spectra (1988–1998) are classified one by one into **monoenergetic**, **broadband** and **diffuse** electron aurora (plus ion aurora), using spectral-shape criteria: a sharp peak for monoenergetic, three or more flat accelerated channels for broadband.
- The diffuse aurora carries 71–84% of hemispheric energy flux.
- Broadband aurora is the smallest by energy but rises 8× with solar-wind driving.
- The zenith-pointing SSJ/4 apertures see only loss-cone particles at auroral latitudes.

See [[Auroral Acceleration]].

## Sources

- Varney 2026 PatchesChapter
- [[Zou 2021 SED Ion Upflow]]
- [[Newell 2009 Global Precipitation Budget]]
