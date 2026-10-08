---
type: source
status: mature
updated: 2026-05-19
authors: C.J. Coleman
year: 1992
---

# Coleman 1992 Ionospheric Ray Tracing

**Citation:** Coleman, C. J. (1993), *A General Purpose Ionospheric Ray Tracing Procedure*, DSTO Surveillance Research Laboratory Technical Report SRL-0131-TR, Commonwealth of Australia.

## Summary

Describes HASEL, a FORTRAN subroutine implementing 3-D HF ionospheric ray tracing via numerical integration of the Haselgrove ODEs. The procedure uses the full Appleton-Hartree refractive index including Earth's magnetic field (represented as a tilted dipole) and an adaptive Runge-Kutta-Fehlberg (RKF) integrator. Outputs include ray trajectories, phase path P, group path P', and ionospheric Doppler shift Δf. Three ionospheric representations are supported: analytic function (ELDEN subroutine), layered Chapman-function parameters on a geographic grid, or height-sample arrays. Directly relevant to SuperDARN ray-path modeling and polar cap patch HF backscatter interpretation.

## Key claims

- Haselgrove (1955–1963) ODEs: dx_i/dτ = Ju_i − Kv_i and du_i/dτ = L∂X/∂x_i + Σ(Ku_j + Mv_j)∂(Yv_j)/∂x_j, where X = 8.06×10⁻⁶N/f², Y = f_H/f.
- Full Appleton-Hartree refractive index handles O/X mode split; Earth's magnetic field as tilted dipole B = −∇(M·(x−x₀)/|x−x₀|³).
- Adaptive RKF step (4th/5th order); 9-component state vector: position (3), wave normal (3), phase path P, group path P', Doppler shift Δf.
- Three ionospheric representations: (1) analytic ELDEN function; (2) Chapman E/F1/F2 layers on lat/lon grid with C¹ cubic or Lagrange interpolation; (3) height-sample grid (most efficient for large ray counts).
- Up to 3 hops with Earth's magnetic field; up to 10 hops without.
- Relevant to SuperDARN HF backscatter: patches must refract HF rays to near-perpendicularity with B for Bragg scatter from field-aligned irregularities; ray tracing determines which patch geometries satisfy this condition.

## Methods/data

- Purely numerical/analytical; no observational data. Validated against a Chapman layer ionosphere with rising hmF2 (constant-velocity lifting).

## Connections

- [[HF Radio Propagation]] — provides the numerical implementation of Haselgrove/Appleton-Hartree theory.
- [[SuperDARN]] — HF coherent scatter from patches requires ray-path geometry to satisfy the Bragg condition; Coleman's procedure enables quantitative modeling.
- [[Polar Cap Patch]] — patches refract HF rays in SuperDARN observations; ray tracing links patch density structure to backscatter occurrence.
- [[Ionospheric Instabilities]] — gradient-drift-driven field-aligned irregularities are the scattering targets; ray tracing determines whether they are geometrically accessible for a given radar.

## Open questions

- Can modern implementations extend HASEL to 3-D time-varying ionospheres (e.g., volumetric patch structures from RISR-N observations)?
- How does the O/X mode choice affect polar cap ray paths where B geometry is extreme (nearly vertical)?
