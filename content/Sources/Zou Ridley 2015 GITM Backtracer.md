---
type: source
status: draft
updated: 2026-05-13
sources: 1
authors: Zou, Ridley
year: 2015
tags: [SED, GITM, backtracer, storm, convection]
---

# Zou & Ridley 2015 — Modeling of the Evolution of the Storm-Enhanced Density Plume during the 24–25 October 2011 Geomagnetic Storm

## Summary

[[GITM]] model study of the [[Storm-Enhanced Density]] (SED) plume formation during the 24–25 October 2011 geomagnetic storm ($\text{Sym-H}_\text{min} \approx -150$ nT). Uses backward particle tracing of plasma columns through the simulation to determine the origin of the plasma contributing to the SED plume. Key finding: plasmas from a wide range of latitudes and local time sectors (dawn, noon, dusk) all contribute to the SED plume, and the sector of origin is diagnosable from the joint $h_{mF2}$–TEC signature. Thermospheric wind plays a critical role in plume decay.

## Key claims

- Backward particle tracing in GITM shows that plasma contributing to the SED plume originates from both dawn and dusk sectors (and noon), spanning a wide range of local times — the SED is not a single-source structure.
- Dawn-sector plasma exhibits slow, steady increases in $h_{mF2}$, $N_{mF2}$, and TEC; dusk-sector plasma shows large, rapid $h_{mF2}$ variations (~300→400 km in 15 min) and steep TEC changes of ~25% in 30 min. The noon sector shows the largest $N_{mF2}$ but little $h_{mF2}$ variation.
- The joint $h_{mF2}$–TEC signature thus provides a fingerprint of the plasma's local-time origin within the SED plume — a diagnostic tool for ISR and GPS observations.
- The primary mechanism of TEC increase in the SED plume is upward vertical ion transport above ~350 km (topside density increase), not photochemical production. This is driven by northward ion velocity (observed as $V_{i,\text{up}} > 0$ at ~220–560 km at the PFISR location).
- The SED plume decay is caused by a rapid increase in northward thermospheric wind after ~2300 UT, which pushes plasma downward to lower altitudes where charge exchange and recombination rates are higher — consistent with Zou et al. [2013, 2014] PFISR observations.
- The pressure gradient below the F-layer peak increases with the plume and then tracks the TEC decay — positive (downward) pressure gradient indicates enhanced downward ambipolar diffusion within the plume during decay.
- GITM underestimates observed TEC by ~22% quiet-time and ~39% storm-time, partly because GITM's upper boundary at ~700 km excludes part of the plasmasphere.

## Methods / data

- [[GITM]] run at 1° lat × 2.5° lon resolution, 50 vertical levels from ~100 to ~700 km; driven by Weimer [1996] electrodynamic potential + Ovation-SM precipitation. Initialized 21 October 2011 to reach quasi-steady state before storm onset.
- Solar wind / IMF from ACE spacecraft, dynamically propagated to magnetopause.
- Backward tracing: plasma columns at 2320 UT (peak TEC) traced backward two hours; traced to starting locations at 2125 UT.
- Validation against Madrigal GPS TEC (Rideout & Coster, 2006) and PFISR vertical velocities.

## Connections

- [[Storm-Enhanced Density]] — GITM reproduces SED plume formation; backtracer identifies multi-sector plasma origins
- [[Lifting]] — upward ion transport above 350 km is the primary TEC enhancement mechanism; same physics as the lifting mechanism in patch formation
- [[Tongue of Ionization]] — SED plume feeds the TOI entering the polar cap; GITM shows the plume geometry relative to the two-cell convection pattern
- [[GITM]] — model used for simulation
- [[RISR-N]] — PFISR (sister AMISR at Poker Flat) used for observational validation of vertical velocities and TEC; RISR-N relevant for comparison
- [[Field-Aligned Currents]] — convection pattern driven by FAC system; Weimer model provides the potential
- [[Joule Heating]] — thermospheric wind increase is a response to Joule-heated momentum input during the storm

## Open questions

- Does a similar multi-sector origin structure apply to SED plumes driven by CH/HSS activity (no strong southward $B_z$), as in the L-type events in [[Lundquist Varney 2026]]?
- How sensitive is the $h_{mF2}$–TEC origin fingerprint to the choice of convection model (Weimer vs. SuperDARN-based)?
