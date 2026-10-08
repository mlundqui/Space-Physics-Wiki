---
type: source
status: draft
updated: 2026-10-07
sources: 0
authors: C.C. Chaston, C.W. Carlson, J.P. McFadden, R.E. Ergun, R.J. Strangeway
year: 2007
doi: 10.1029/2006GL029144
tags: [alfven-waves, FAST, auroral-energy-budget, ion-outflow]
---

# Chaston 2007 DAW Auroral Acceleration Fraction

## Summary

More than 5000 [[FAST]] polar passes (November 1996 to March 1999, near solar minimum) are used to measure what fraction of auroral particle energization happens inside **dispersive Alfvén waves (DAWs)**. Result: **25–39% of the total electron energy deposited** in the high-latitude ionosphere, and **15–34% of energetic ion outflow**, can be attributed to DAWs, both rising with auroral activity. Near the **cusp** and the **premidnight poleward oval** during active times, DAWs are the *dominant* driver of both electron precipitation and ion outflow. Overall: "significant, though generally not dominant."

## Key claims

- **Definition.** A DAW is a shear Alfvén wave with transverse scale about $\lambda_e = c/\omega_{pe}$ (inertial) or about $\rho_i$ or $\rho_s$ (kinetic). Above the auroral oval **$\lambda_e$ generally exceeds the gyroradii**, so inertia is the dominant dispersive correction (Goertz & Boswell 1979).
- **Selection criterion:**
  - Quasi-static FAC: $\Delta E_x/\Delta B_y \approx 1/(\mu_0\Sigma_P)$.
  - DAW: $\Delta E_x/\Delta B_y \approx V_A(1 + k_x^2\lambda_e^2)^{1/2}$.
  - Above the oval $V_A \gg 1/(\mu_0\Sigma_P)$ and $2\pi\lambda_e < 10$ km, so events are selected by $0.1V_A < \Delta E/\Delta B < 10V_A$ and width < 10 km.
  - Field-line resonances with long parallel wavelength can slip through as "quasi-static."
- **DAW-accelerated electrons** are identified by a monotonic (unpeaked) field-aligned spectrum, which separates them from inverted-V and unaccelerated plasma-sheet or magnetosheath electrons.
- **Occurrence:** throughout the oval; most common near noon (cusp), next near midnight (high-latitude tail).
- **DAW power toward the ionosphere:** about 2 GW on average, up to about 10 GW when active. Midnight DAWs are several times more energetic than dayside ones.
- **Total electron energy deposition:** about 18 GW average, more than 100 GW when active, peaked near midnight.
  - The DAW fraction is about 50% near noon and premidnight and 31% overall.
  - It rises from 25% to 39% with activity.
- **Ion outflow:** total about $2.5\times10^{24}$ s⁻¹ at FAST altitudes, peaked at the cusp with a smaller premidnight peak.
  - 40–50% is in DAW wavefields in those regions; 22% overall; 15–34% depending on activity.
  - This is attributed to DAWs by coincidence only: DAWs may power ion heating directly or via secondary waves.
- **Open problem:** how large-scale magnetospheric variability is transported down to the small dispersive scales where acceleration happens. DAWs need continuous energy resupply along high-latitude field lines.

## Methods/data

FAST fields and particles (4 eV to 30 keV electrons, within the loss cone). DAW intervals selected by $E/B$ ratio and width. Fluxes integrated along track and binned in MLT and ILAT. Activity from NOAA POES.

## Connections

- [[Auroral Acceleration]] — the Alfvénic share of precipitation. **Compare [[Newell 2009 Global Precipitation Budget]]** (broadband 6–13% of *total* energy flux) and [[Keiling 2003 Alfvén Wave Poynting Flux]] (30–35% of luminosity)
- [[Alfvén Waves]], [[FAST]], [[Chaston 2003 FAST Small-Scale Alfvén Waves]]
- [[Atmospheric Escape]] / [[Polar Wind]] — DAW-driven energetic ion outflow (O⁺ mass loading)

## Open questions

- Denominators differ across studies:
  - This paper: FAST electrons 4 eV–30 keV only, no ions.
  - Newell 2009: DMSP, includes diffuse ions and electrons.
  - Keiling 2003: UVI luminosity.
  
  So "25–39%" (Chaston), "6–13%" (Newell) and "30–35%" (Keiling) are not directly contradictory, but they have not been reconciled in the wiki.
