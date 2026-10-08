---
type: source
status: draft
updated: 2026-05-13
sources: 1
authors: Varney, Wiltberger, Lotko
year: 2014
---

# Varney 2014 — Supplemental Details on IPWM

## Summary

Technical supplement documenting the equations, coordinate system, and numerical implementation of the three-dimensional [[IPWM|Ionosphere Polar Wind Model]]. Covers the 8-moment thermal ion transport equations, the nonorthogonal coordinate blend used to span the dipole geometry from 97 km to 8400 km, nonthermal (ring current) ion handling, the quasineutral electron model, and horizontal finite-volume transport with van Leer slope limiting. Intended as a companion to the main IPWM publication (Varney et al. 2015, JGR).

## Key claims

- The full moment hierarchy starts with $\partial n_i/\partial t + \nabla\cdot[n_i \mathbf{u}_i] = \delta n_i/\delta t$; parallel momentum includes a centrifugal term $\mathbf{u}_i\mathbf{u}_i:\nabla\hat{b}$ arising from field-line curvature.
- In the gyro-dominated limit (collision frequency $\ll$ gyrofrequency) the perpendicular ion drift reduces to $\mathbf{u}_{\perp i} = \mathbf{E}\times\mathbf{B}/B^2$; only the parallel component needs the full moment equation.
- Nonthermal (energetic ring-current) ions are tracked separately using conservation of the first adiabatic invariant $\mu_j = p_{\perp j}/(n_j B)$, which holds as long as $\mu_j$ changes slowly relative to the gyroperiod.
- Electron density is obtained from quasineutrality; the parallel electric field is $E_{||} = -(1/n_e)\nabla_{||}p_e$, closing the system without a separate electron momentum equation.
- Coordinate system: $q^1 = r$, $q^2 = \chi = \sin^2\theta/r$, $q^3 = \varphi$ — a nonorthogonal blend of geocentric spherical and dipole that is nearly orthogonal throughout the domain.
- Grid: 78 altitude cells from 97 km to ~8400 km; $\sim$1° lat-lon spacing at 97 km; 2049 flux tubes; 32 parallel-processing domains.
- Horizontal transport uses a finite-volume scheme with the van Leer slope limiter; the scheme is conservative across domain boundaries and at the magnetic pole singularity.

## Methods / data

Purely analytical and numerical supplement — no observational data. Equations derived in the nonorthogonal coordinate frame; numerical implementation details for the 3-D extension of the prior 1-D IPWM.

## Connections

- [[IPWM]] — the model being documented
- [[Polar Wind]] — physical output: transonic H$^+$ and O$^+$ outflow on open polar cap field lines
- [[Field-Aligned Currents]] — the parallel electric field $E_{||}$ in the model is tied to the Birkeland current system via the Knight relation
- [[Radiation Belts]] — nonthermal ions modeled separately using adiabatic invariant conservation; relevant for ring-current O$^+$

## Open questions

- How sensitive are polar wind outflow fluxes to the choice of van Leer vs. other slope limiters in the horizontal transport?
- The $q^2 = \sin^2\theta/r$ coordinate is not orthogonal — what are the numerical error implications near the equatorial plane?
