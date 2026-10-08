---
type: source
status: draft
updated: 2026-05-19
authors: R.G. Gillies, G.W. Perry, A.V. Koustov, R.H. Varney, A.S. Reimer, E. Spanswick, J.-P. St.-Maurice, E. Donovan
year: 2018
---

# Gilles 2018 RISR SuperDARN Velocity Comparison

*Large-Scale Comparison of Polar Cap Ionospheric Velocities Measured by RISR-C, RISR-N, and SuperDARN.* Gillies, R.G., et al. (2018). *Radio Science*, 53, 624–639. doi:10.1029/2017RS006435.

## Summary

Statistical comparison of 5.2×10⁵ line-of-sight velocity measurements from the two Resolute Bay ISRs and the Rankin Inlet SuperDARN radar during 40 days of operations. Finds that F-region SuperDARN velocities are systematically lower than RISR but agree well after correcting for the refractive index effect. E-region echoes and groundscatter are major contamination sources in daytime SuperDARN data.

## Key Claims

1. **After refractive-index correction, F-region SuperDARN LOS velocities agree with RISR** in regions free of E-region echoes and groundscatter.
2. **Without correction, SuperDARN LOS velocities are ~75–85% of RISR values** — consistent with prior literature showing HF Doppler underestimation relative to ISR.
3. **Combined RISR-C/N FOV overlaps Rankin Inlet SuperDARN ranges from ~600 to ~2200 km** — a uniquely large comparison region for statistical validation.
4. **Daytime groundscatter contaminates most SuperDARN range gates** at ranges 18–45, degrading comparison significantly.
5. **E-region echoes produce Doppler shifts significantly slower than F-region velocities** because nonlinear wave processes drive E-region irregularities to near their threshold speed, decoupled from background ExB.
6. Ray tracing (IRI-2016 model) illustrates multiple viable propagation paths (O/X modes, 1/2-hop, E and F region) for a single beam/range — echo geolocation is ambiguous without independent density information (Fig. 2).
7. Correcting for the refractive index requires knowledge of the background electron density at the scattering volume; uncertainty in this correction is a persistent limitation.

## Methods/Data

- 40 days of combined RISR World Day mode operations; velocity data restricted to 5-min intervals with both RISR and RKN coverage.
- Comparison performed on 35 RKN range gates (spanning 1575 km).
- IRI-2016 used for ray tracing to characterize propagation geometry and estimate refractive index.
- RISR data binned to match SuperDARN temporal/spatial resolution.

## Connections

- [[RISR-N]] — northern face RISR used as velocity reference
- [[AMISR]] — both RISR radars are AMISR instruments
- [[SuperDARN]] — Rankin Inlet radar (RKN) is the comparison instrument
- [[HF Radio Propagation]] — refractive index effect, O/X mode ray paths, E vs F region echoes

## Open Questions

- When E-region echoes are removed, comparison statistics improve but are not perfect; residual differences may reflect ionospheric inhomogeneity or RISR beam geometry.
- Extension of this comparison to other SuperDARN radars (non-polar-cap) would test generalizability.
