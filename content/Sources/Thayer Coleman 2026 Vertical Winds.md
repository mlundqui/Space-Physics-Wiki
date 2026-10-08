---
type: source
status: draft
updated: 2026-05-13
sources: 1
authors: Thayer, Coleman
year: 2026
tags: [thermosphere, vertical-winds, coordinate-systems, TIEGCM, airglow]
---

# Thayer & Coleman 2026 — Resolving Thermospheric Vertical Wind Ambiguities and Energy Processes

> **Note:** The filename ("Baroclinic Lifting Derivation") is misleading. This paper is about thermospheric vertical wind coordinate ambiguities — not ionospheric F-layer [[Lifting]] for patch formation.

## Summary

Derives a generalized vertical coordinate framework to disambiguate vertical winds defined in height coordinates (z-system) from those defined in pressure coordinates (p-system) in the upper thermosphere. The central finding is that vertical winds measured in height coordinates on a constant-pressure surface contain a **lifting wind** component ($w_L$) that is non-energetic — it does not contribute to adiabatic expansion/compression of the gas. Only the **divergent wind** ($w_D = w - w_L$) drives the thermodynamic internal energy equation. Fabry-Pérot interferometer (FPI) observations of vertical winds from 630 nm emissions are in the airglow's own coordinate system (s-system), introducing an inherent ambiguity: the FPI records both $w_D$ and $w_L$, not just the energetically relevant component. TIEGCM V3.0 simulations at ~400 km altitude demonstrate that lifting winds are appreciable and often opposite in sign to the divergent winds.

## Key claims

- The total height-based vertical wind on a constant-pressure surface decomposes as $w = w_L + w_D$, where the **lifting wind** is:
$$w_L = \left(\frac{\partial z}{\partial t}\right)_p - \vec{V}_h\cdot\vec{\nabla}_p z$$
(height tendency on a pressure surface + horizontal advection of height gradients along the pressure surface). In pressure coordinates, $\omega = -\rho g w_D$, not $-\rho g w$.

- The adiabatic heating/cooling rate is driven only by $w_D$ (the divergent component): $\dot{Q}_\text{adb} = -Wp/(\rho\bar{c}_p)$ in log-pressure coordinates, where $W \equiv DZ/Dt$ relates to $w_D$, not the total $w$.

- The lifting wind is **non-energetic**: it corresponds to isobaric, volumetric expansion that changes volume and height without altering internal energy. Its contribution to the thermodynamic energy equation is zero.

- In the upper thermosphere, horizontal flow is strongly ageostrophic, so $\vec{V}_h$ has a substantial component along the horizontal height gradient on a pressure surface. This makes the horizontal advection term in $w_L$ significant — it was routinely neglected in lower-atmosphere work where flow is largely geostrophic.

- TIEGCM simulations at $Z = 2.75$ (~400 km), $K_p = 4$, F10.7 = 150 show: (a) divergent vertical winds exceeding $\pm 30$ m/s in a structured alternating pattern on the nightside; (b) lifting winds of comparable magnitude but typically opposite sign; (c) adiabatic heating/cooling rates producing $\pm 6$% temperature perturbations.

- FPI observations of 630 nm vertical winds are in the airglow coordinate system (s-system). The recorded Doppler shift captures $w_D + w_L$ (not just $w_D$) whenever the airglow surface is non-stationary or has horizontal gradients. Discrepancies between FPI vertical winds and those derived from horizontal wind divergence can be attributed to the lifting wind component.

## Methods / data

Theory: generalized vertical coordinate transformations (Kasahara 1974 framework). Simulations: NCAR-TIEGCM V3.0 (Qian et al. 2014; Wu et al. 2025) run for June solstice, F10.7 = 150, Kp = 4, 20-day spin-up. Horizontal resolution 2.5° × 2.5°; vertical coordinate log-pressure $Z = \ln(p_0/p)$.

## Connections

- [[Ionospheric Energetics]] — adiabatic heating/cooling from divergent vertical winds produces significant thermospheric temperature perturbations; lifting winds do not contribute to internal energy
- [[Joule Heating]] — thermospheric energy budget includes adiabatic terms alongside Joule heat; the distinction between $w_D$ and $w_L$ is essential for correctly attributing temperature changes
- [[Airglow]] — FPI Doppler wind observations at 630 nm are in the airglow coordinate system; measured vertical winds are NOT purely in the z- or p-system, introducing a lifting wind ambiguity
- [[Lifting]] — completely separate concept; the ionospheric F-layer lifting (vertical ExB of plasma to higher altitudes) is not the same as the thermospheric "lifting wind" $w_L$ defined in this paper

## Open questions

- What observational strategy would allow ground-based FPIs to separate $w_D$ from $w_L$? (Requires knowledge of horizontal wind gradients and height gradients simultaneously.)
- During intense storms when the thermosphere is strongly heated, how large does $w_L$ become relative to $w_D$, and what is the impact on ISR-derived hmF2 changes?
