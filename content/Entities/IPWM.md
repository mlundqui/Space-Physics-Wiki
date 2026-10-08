---
type: entity
status: draft
updated: 2026-10-07
sources: 4
tags: [model, plasma, polar-wind, ionosphere, magnetosphere]
---

# IPWM — Ionosphere Polar Wind Model

A three-dimensional, first-principles kinetic-fluid model of the coupled ionosphere and polar wind, developed by Varney, Wiltberger, and Lotko. IPWM self-consistently solves ion transport on a global set of dipole-aligned flux tubes from 97 km altitude out to ~8400 km, spanning the ionosphere through the inner plasmasphere. It is the primary simulation tool used by the Varney group to interpret [[RISR-N]] observations of ion upflow, [[Polar Wind]] jets, and the preconditioning of the polar cap ionosphere by energetic ion outflow.

## Physics

IPWM solves the **8-moment** thermal ion transport equations for each ion species (H$^+$, O$^+$, He$^+$, and nonthermal ring-current species). Varney et al. (2014) describe these as the 13-moment equations of Schunk & Nagy (2009) with zero stress tensor. *Wiki inference (not stated by Varney 2014):* the 8-moment set is a practical optimum for the full altitude range 97–8400 km, since [[Blelly Schunk 1993 Moment Comparison]] shows the standard 5-moment model overestimates the F$_2$-region peak density by a factor of ~6 (missing thermoelectric and diffusion-thermal effects), while the 13-moment model becomes numerically unreliable in the collisionless supersonic regime. The 8-moment equations eliminate the factor-6 error while remaining stable throughout the model domain.

$$\frac{\partial n_i}{\partial t} + \nabla\cdot[n_i \mathbf{u}_i] = \frac{\delta n_i}{\delta t}$$

Higher moments evolve analogously, with parallel momentum including a centrifugal correction term $\mathbf{u}_i\mathbf{u}_i:\nabla\hat{b}$ from field-line curvature.

In the gyro-dominated limit (relevant at all altitudes in the model domain), the perpendicular velocity reduces to $\mathbf{u}_{\perp i} = \mathbf{E}\times\mathbf{B}/B^2$ and is specified externally from a convection model; only the parallel component requires the full moment hierarchy.

Electrons are handled via quasineutrality ($n_e = \sum_i n_i$) with a parallel electric field $E_{||} = -(1/n_e)\nabla_{||}p_e$ closing the system.

Nonthermal (ring-current) ions are tracked separately under conservation of the first adiabatic invariant:

$$\mu_j = \frac{p_{\perp j}}{n_j B} = \text{const}$$

## Coordinate system

IPWM uses a nonorthogonal coordinate blend designed to remain well-behaved throughout the dipole geometry:

$$q^1 = r, \quad q^2 = \chi = \frac{\sin^2\theta}{r}, \quad q^3 = \varphi$$

$q^2$ follows dipole field lines exactly (constant $\chi$ = constant $L$-shell footpoint), while $q^1$ and $q^3$ are standard geocentric radius and longitude. The system is nearly orthogonal throughout the inner magnetosphere but deviates near the equatorial plane.

## Grid

| Parameter | Value |
|---|---|
| Altitude range | 97 km – ~8400 km |
| Altitude cells | 78 |
| Flux tubes | 2049 |
| Parallel domains | 32 |
| Horizontal spacing | ~1° lat-lon at 97 km |

## Horizontal transport

The $E\times B$ drift advects plasma across flux tubes. IPWM implements this as a finite-volume scheme using the **van Leer slope limiter**, which is second-order accurate in smooth regions and reverts to first-order at sharp density gradients. The scheme is conservative at domain boundaries and handles the magnetic pole singularity without special treatment.

## Physical outputs

- Parallel velocity $u_{||}$, density $n$, temperature $T_\parallel$, $T_\perp$ on each flux tube as functions of altitude and time
- Global maps of $N_mF2$, $h_{mF2}$, ion upflow flux, and [[Polar Wind]] escape rate
- Ring-current ion populations from adiabatic invariant transport

## Connections

- [[Polar Wind]] — IPWM's defining physical output; transonic H$^+$ solution on open polar cap field lines
- [[Polar Cap Patch]] — patch-driven ion upflow and polar wind jets are diagnosed using IPWM
- [[RISR-N]] — observational counterpart; IPWM simulations are compared against RISR-N vertical velocities and density profiles
- [[Field-Aligned Currents]] — $E_{||}$ and the Knight relation for parallel acceleration connect IPWM to the FAC system
- [[Radiation Belts]] — nonthermal ring-current ion transport uses adiabatic invariant conservation, linking IPWM to the inner magnetosphere

## HIDRA — IPWM successor in MAGE

[[Albarran 2023 N+ Polar Wind MAGE]] introduces **HIDRA** (High-latitude Ionospheric Dynamics and Recombination Analysis), the IPWM successor integrated into the [[MAGE]] coupled framework. Key change: a **N$^+$ chemistry bug** was fixed. The IPWM charge-exchange rate for N$^+$ + O → N + O$^+$ was ~2 orders of magnitude too high compared to laboratory measurements (Richards 2011), causing IPWM to underestimate N$^+$ by the same factor. With the corrected rate:

- N$^+$ densities are ~10–14% of O$^+$ at 1200 km under quiet conditions — comparable to or exceeding He$^+$
- During geomagnetic storms, N$^+$ can reach 50–100% of O$^+$ at magnetospheric altitudes
- N$^+$ typically exceeds He$^+$ throughout the polar wind at all conditions

This has implications for mass loading of the magnetosphere: prior IPWM simulations underestimated the nitrogen contribution to outflowing polar wind mass flux.

## Relationship to SAMI2

[[SAMI2]] is the low-latitude sibling model to IPWM. Both are ionosphere-plasmasphere models built on fluid transport equations along dipole field lines, but they address different geographic regimes. SAMI2 uses 5-moment equations optimized for the closed-field-line equatorial and low-latitude geometry (90 field lines, 85 km–20,000 km apex), while IPWM uses 8-moment equations designed for open polar cap field lines where the supersonic polar wind requires the higher-order thermal flux treatment. The [[Blelly Schunk 1993 Moment Comparison]] motivating IPWM's 8-moment choice applies equally to the high-altitude regime of SAMI2-PE (see [[Varney 2012 Thesis]]). IPWM's van Leer horizontal transport scheme and its handling of the parallel electric field as a closure for the electron fluid share structural choices with SAMI2's fluid architecture.

## Sources

- [[Varney 2014 IPWM Supplement]]
- [[Blelly Schunk 1993 Moment Comparison]]
- [[Albarran 2023 N+ Polar Wind MAGE]]
- [[Varney 2012 Thesis]]
