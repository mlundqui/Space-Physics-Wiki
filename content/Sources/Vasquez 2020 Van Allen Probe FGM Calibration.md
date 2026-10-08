---
type: source
status: draft
updated: 2026-05-19
authors: B.J. Vasquez, C.W. Smith, K.W. Paulson, C.A. Kletzing
year: 2020
---

# Vasquez 2020 Van Allen Probe FGM Calibration

**Citation:** Vasquez, B. J., C. W. Smith, K. W. Paulson, and C. A. Kletzing (2020), *Flight Calibration of the Van Allen Probe Magnetometers*, Astrophys. J. Suppl., 250, 4, doi:10.3847/1538-4365/aba62e.

## Summary

Describes a flight calibration procedure for the triaxial fluxgate magnetometers on the two Van Allen Probes (RBSP), extending the Farrell et al. (1995) spin-based approach to account for a linearly changing background B — necessary because the Van Allen Probes traverse highly elliptical 9-hour orbits (1.1–5.5 R_E) where B can change by more than a factor of 100 within a single pass. Daily ensemble averaging of 1-minute interval calibrations (in ranges 1 and 3) corrects for instrument bias, spin-plane gains, and inter-orthogonality. The calibration iterates to convergence, with the updated alignment matrix used as the starting point for the next iteration.

## Key claims

- Transformation chain: B_calibrated = A · G → T · (B_raw − B₀), where A is the alignment matrix, G is the gain diagonal matrix, T is the inter-orthogonality upper-diagonal matrix, and B₀ is the instrument bias.
- Two operational ranges used in science data: Range 1 (±4096 nT, 0.125 nT/count) at apogee; Range 3 (±65,536 nT, 2 nT/count) near perigee where B is strong.
- Spin-axis bias B_z0 cannot be independently determined from spin-plane Fourier analysis; preflight value retained throughout mission.
- Calibration converges in a few daily iterations; subsequent days use updated A as the starting point.
- General approach applicable to other spinning spacecraft with similar triaxial magnetometer configurations.

## Methods/data

- Spinning spacecraft (spin period 11 s); spin-plane sensors (X, Y) analyzed via Fourier decomposition of spin-tone harmonics; spin-axis sensor (Z) not updated.
- 1-minute intervals selected from magnetosphere and solar wind to span a range of B magnitudes; ensemble averaging reduces interval-to-interval noise.

## Connections

- [[Van Allen Probes]] — this is the calibration procedure for the EMFISIS-MAG instrument on Van Allen Probes.
- [[Kletzig 2013 EMFISIS]] — instrument description for the EMFISIS suite of which this FGM is the DC magnetic component.
- [[Radiation Belts]] — calibrated DC field data is required for accurate pitch-angle calculation and adiabatic invariant determination.

## Open questions

- Can the technique be extended to three-axis stabilized spacecraft where spin-tone analysis is unavailable?
