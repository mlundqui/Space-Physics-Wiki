---
type: source
status: draft
updated: 2026-05-13
sources: 1
authors: Zou, Dorrian, Varney, Ren, Thomas, Lamarche
year: 2021
tags: [ion-upflow, SED, storm, SAPS, PFISR, DMSP, polar-cap]
---

# Zou et al. 2021 — Impact of Storm-Enhanced Density on Ion Upflow Fluxes During Geomagnetic Storms

## Summary

Multi-instrument case study of the March 6–7, 2016 CIR-driven geomagnetic storm (Sym-H$_\text{min} \approx -110$ nT) examining how [[Storm-Enhanced Density|SED]] modulates topside O$^+$ ion upflow fluxes into the cusp. The central finding is that ionospheric density — not electric field or precipitation alone — is the dominant controlling factor for upflow flux magnitude: the high-density SED plume delivers upward fluxes of $3\times10^{14}$ m$^{-2}$ s$^{-1}$ (exceeding the full nightside auroral zone total per unit area), while the subsequent negative storm phase reduces densities to ~30% of peak values and drops fluxes to $2$–$3\times10^{13}$ m$^{-2}$ s$^{-1}$ despite comparable convection. Two physically distinct upflow types are identified and attributed to different drivers.

## Key claims

- **Ion upflow flux scales with ionospheric density, not electric field.** During the negative storm phase, O/N$_2$ depletion reduces densities ~70% while convection remains active; upward fluxes drop by a factor of ~5 despite similar or larger electric fields. This demonstrates that the ionospheric plasma density reservoir is the rate-limiting control on upflow flux.
- **Peak upward flux = $3\times10^{14}$ m$^{-2}$ s$^{-1}$** when SED plasma meets cusp soft electron precipitation at ~23:05 UT. This exceeds the per-unit-area equivalent of the full nightside auroral zone and is comparable to the total nightside integrated flux despite the cusp covering a much smaller area ($\sim2$ h MLT $\times 2°$ mlat at 75° mlat).
- **Type 1 upflow** is SAPS-associated: large perpendicular electric field drives strong $\mathbf{E}\times\mathbf{B}$ flow and frictional heating. Low density below 300 km (plasma raised to high altitudes by the SAPS-associated poleward drift). No elevated $T_e$ at DMSP altitude (840 km). O$^+$ temperature 1000–3200 K at 200–500 km from frictional heating. Associated with the SAPS channel just equatorward of the auroral oval.
- **Type 2 upflow** is precipitation-driven: soft electron precipitation elevates $T_e$, enhancing the ambipolar electric field. High topside density from SED transport into the cusp. Elevated $T_e$ observed at DMSP 840 km altitude. This type produces the highest fluxes when SED plasma meets cusp precipitation.
- **Downward plasma flows inside the SED plume at sub-auroral latitudes.** PFISR and DMSP observe downward ion flows within the SED plume body at lower latitudes, consistent with downward-directed convection where the poleward-expanding convection pattern compresses plasma. This confirms earlier PFISR observations (Zou et al. 2014; Ren et al. 2019, 2020).
- **SED forms at $\sim16$–18 MLT** in the main phase as Region-2 FACs expand equatorward to 55–60° mlat; two polar cap plumes drift anti-sunward at ~17 and 20 UT. DMSP F15 (850 km) observes topside SED density $\sim2\times10^{11}$ m$^{-3}$ (tripled relative to background).
- **SAPS channel type-1 upflow flux** $\approx 6\times10^{13}$ m$^{-2}$ s$^{-1}$ — factor of ~5 lower than the SED+cusp type-2 peak, attributable to lower density in the SAPS channel (plasma depleted by fast poleward convection and delivered to the polar cap faster than it can be replenished).
- **Integrated dayside cusp upflow** $\sim2$–$4\times10^{25}$ s$^{-1}$; **nightside auroral zone total** $\sim4$–$6\times10^{25}$ s$^{-1}$. The cusp is a comparably important mass source despite its much smaller geographic area, when SED plasma is present.

## Methods / data

- **Event:** March 6–7, 2016 CIR-driven storm. Three phases defined by t$_1=11$:47 UT (IMF $B_y$ enhancement / storm onset), t$_2=21$:20 UT (Sym-H minimum), t$_3=06$ UT March 07 (solar wind driving ends). Peak AE $\approx 1500$ nT.
- **VISTA TEC:** Madrigal GPS TEC database + SoftImpute matrix completion algorithm; 5-min cadence; global but gap-filled.
- **SuperDARN convection maps:** Cross-polar-cap potential and convection pattern temporal evolution.
- **AMPERE FACs:** Iridium satellite constellation; Region-1/2 current system boundaries during storm.
- **DMSP SSIES + SSJ:** Ion density, $T_e$, $T_i$, cross-track drift from SSIES; precipitation identification from SSJ. F15 satellite at ~850 km.
- **PFISR:** Poker Flat ISR (Alaska, 65.1° mlat); full altitude profiles of $N_e$, $T_e$, $T_i$, $v_i$ at ~10-min cadence.
- **TIMED GUVI:** O/N$_2$ ratio from UV limb scans; shows equatorward expansion of thermospheric composition depletion during negative storm phase.

## Connections

- [[Storm-Enhanced Density]] — SED provides the high-density plasma reservoir that enables large upflow fluxes; positive vs negative storm phase determines whether SED forms or is suppressed
- [[Polar Wind]] — SED-driven ion upflow is the low-altitude driver for enhanced O$^+$ outflow; Type 2 upflow via ambipolar field is the ionospheric extension of polar wind theory
- [[Field-Aligned Currents]] — Region-2 FAC system drives the SAPS electric field and controls equatorward boundary of SED formation; AMPERE data shows boundary at 55–60° mlat during main phase
- [[Joule Heating]] — thermospheric Joule heating drives the negative storm phase O/N$_2$ composition change that depletes ionospheric density and reduces upflow flux
- [[Ionospheric Conductivity]] — Pedersen conductance determines how efficiently the SAPS electric field maps to the ionosphere; low conductance sub-auroral region enables the large SAPS electric fields
- [[Lifting]] — SAPS-associated poleward $\mathbf{E}\times\mathbf{B}$ drift lifts SED plasma to high altitudes, suppressing recombination and creating the dense topside reservoir
- [[DMSP]] — primary observational platform for upflow flux measurements at 840 km; hot/cold patch classification; SSIES and SSJ instruments
- [[RISR-N]] — volumetric ISR context; analogous upflow observations inside polar cap for LD events; [[Lundquist Varney 2026]] LD events are plausible post-cusp continuation of SED upflow

## Open questions

- What fraction of the O$^+$ delivered to the cusp at $3\times10^{14}$ m$^{-2}$ s$^{-1}$ ultimately reaches ring-current energies vs escapes as polar wind?
- How does the upflow flux profile evolve during CH/HSS-driven storms (without strong southward $B_z$) where SED still forms (L-type events of [[Lundquist Varney 2026]])?
- Is the Type 1 / Type 2 classification binary, or is there a continuum of mixed drivers (strong E field + strong precipitation simultaneously)?
- Does the dayside cusp upflow or the nightside auroral zone upflow dominate the total O$^+$ outflow budget, integrated over a full storm cycle?
