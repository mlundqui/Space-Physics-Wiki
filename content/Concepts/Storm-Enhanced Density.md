---
type: concept
status: draft
updated: 2026-05-19
sources: 6
tags: [ionosphere, storms, sed]
---

# Storm-Enhanced Density (SED)

A storm-time enhancement of [[F-Layer|F-region]] electron density at sub-auroral latitudes, commonly extending poleward as a plasma plume that connects to and feeds the [[Tongue of Ionization|polar-cap TOI]]. SEDs are a major channel for delivering dense mid-latitude plasma into the high-latitude ionosphere during geomagnetic storms.

## Why enhancement, not depletion?

The mid-latitude F-region density is set by balance between EUV photoproduction and O$^+$ chemical loss:

$$L = k_1[\text{O}^+][\text{N}_2] + k_2[\text{O}^+][\text{O}_2]$$

Geomagnetic storms do not change the photoproduction rate (which depends only on solar EUV flux and solar zenith angle). Storm-time effects modulate the loss rate through two competing pathways:

**Positive storm effects (density builds up):**
- The upward component of poleward $\mathbf{E}\times\mathbf{B}$ drift [[Lifting|lifts]] O$^+$ to higher altitudes where $[\text{N}_2]$ and $[\text{O}_2]$ are exponentially smaller, suppressing $L$.
- Prompt penetrating electric fields (PPEFs) drive strong poleward $\mathbf{E}\times\mathbf{B}$ drift within minutes of southward IMF onset, before magnetospheric shielding can respond.
- The disturbance dynamo — thermospheric winds driven by storm-time Joule heating — sustains enhanced poleward drift over timescales of hours on the storm main and early recovery phases.

**Negative storm effects (density lost):**
- Joule heating expands the thermosphere, pushing N$_2$ and O$_2$ upward relative to the O$^+$ layer, increasing $L$ (the O/N$_2$ depletion effect).
- Elevated $T_{eff}$ from frictional heating (large $|\mathbf{u}_i - \mathbf{u}_n|$) accelerates $k_1$ and $k_2$.

SED formation requires the positive pathway to dominate. Whether it does depends on the local dip angle, the magnitude of the electric field enhancement, and the thermospheric composition response — not all storms create SED.

## Lifting as the key process

Zou et al. (2013, PFISR) observed SEDs at $h_{mF2} \gtrsim 500$ km — far above the quiet-time F-region peak near 300 km. The poleward $\mathbf{E}\times\mathbf{B}$ drift in a dipole field must remain perpendicular to $\mathbf{B}$, forcing an upward component:

$$u_z = u_\perp \sin\theta_\text{dip}$$

where $\theta_\text{dip}$ is the local dip angle. At sub-auroral latitudes ($\theta_\text{dip} \sim 70°$), poleward drift of ~500 m/s produces upward velocities of ~470 m/s. Over the storm main phase ($\sim 1$ hr) this lifts $h_{mF2}$ by hundreds of km. Without the lifting, O$^+$ would recombine faster than the density could accumulate and no SED plume would form. See [[Lifting]] for full derivation.

## Connection to TOI and polar cap

SED plasma is pulled poleward into the polar cap by the two-cell convection pattern, feeding the [[Tongue of Ionization]]. An SED-supplied TOI is exceptionally dense — potentially the source of the highest-density polar cap patches ($N_e > 10^{12}$ m$^{-3}$, $f_{oF2} > 9$ MHz) observed at high latitudes.

The LD events identified by [[Lundquist Varney 2026]] — simultaneously lifted ($h_{mF2}$ anomalously high) and dense F2 peaks deep inside the polar cap at [[RISR-N]] — are plausible remnants of SED plasma that maintained both its altitude and density throughout the cross-polar-cap transit. These events are rare (93 in 16 years of RISR-N data) and prefer solar maximum, consistent with the enhanced EUV flux and more frequent storm-driven PPEF events at solar maximum.

## Storm suppression and IT preconditioning — a counter-example

[[Themens 2024 May Storm]] illustrates the negative pathway dominating over a multi-day storm. During the initial phase (May 10, 1700–2230 UT) SED plasma lifted to extreme altitudes: $h_{mF2}$ at Eglin AFB reached 630 km, rising ~300 km in ~1 hr. After a 2230 UT IMF reversal cleared the polar cap of patches, thermospheric composition changes driven by cumulative Joule heating took over: O/N$_2$ depleted by 50% across all but equatorial latitudes; temperatures rose 50%. On Day 2 (May 11), the F2-layer was nearly absent at ESR and PFISR — densities an order of magnitude below pre-storm — and did not recover fully for ~3 days. No polar cap patches or significant GNSS scintillation occurred on May 11 despite continuing severe geomagnetic activity, because the ionospheric density reservoir was exhausted. This **preconditioning effect** demonstrates that storm duration and ionosphere-thermosphere system memory are as important for space weather impact as instantaneous Kp or Dst.

## Ion upflow connection

SED plumes provide both the altitude (low recombination, suppressed $L$) and the dense O$^+$ reservoir that enable large ion upflow fluxes. [[Zou 2021 SED Ion Upflow]] quantifies this during the March 6–7, 2016 CIR storm and identifies two mechanistically distinct upflow types:

**Type 1 (SAPS-associated):** Large perpendicular electric field drives fast poleward $\mathbf{E}\times\mathbf{B}$ drift and frictional heating. Plasma is depleted below ~300 km (raised to high altitudes). No elevated $T_e$ at DMSP altitude. Flux $\approx 6\times10^{13}$ m$^{-2}$ s$^{-1}$.

**Type 2 (precipitation-driven):** Soft electron precipitation in the cusp elevates $T_e$, amplifying the ambipolar electric field. Dense SED plasma arrives from poleward transport and meets cusp precipitation. Flux peaks at $3\times10^{14}$ m$^{-2}$ s$^{-1}$ — comparable per unit area to the entire nightside auroral zone.

The critical result is that **ionospheric density, not electric field, controls upflow flux magnitude.** During the negative storm phase O/N$_2$ composition depletion reduces densities to ~30% of peak while convection remains active; fluxes drop by a factor of ~5 despite similar electric fields. SED formation (positive storm phase) is therefore a prerequisite for anomalously large cusp upflow.

The lifted, dense polar cap LD events from [[Lundquist Varney 2026]] are natural candidates for O$^+$ outflow observations on open field lines deep inside the polar cap, extending this picture beyond the cusp.

## SAPS and the geospace plume

[[Subauroral Polarization Streams|SAPS]] (Sub-Auroral Polarization Streams) is the primary storm-time driver of poleward transport that creates the SED plume. The SAPS electric field is generated by Region-2 FACs closing through the low-conductance sub-auroral ionosphere (equatorward of the precipitation boundary), driving fast westward $\mathbf{E}\times\mathbf{B}$ drift at hundreds to ~2000 m/s in the dusk sector. This westward/sunward transport:

1. Lifts sub-auroral O$^+$ via the $u_z = u_\perp\sin\theta_\text{dip}$ component (poleward drift in a dipole).
2. Advects the dense mid-latitude plasma poleward toward the auroral zone and polar cap.
3. Simultaneously erodes the **plasmaspheric drainage plume** — the cold plasma analogue of the SED plume.

[[Bao 2023 Geospace Plume MAGE]] demonstrates with MAGE simulations that the ionospheric SED plume and the plasmaspheric plume co-evolve because both are driven by the same coupled M-I $\mathbf{E}\times\mathbf{B}$ field. Mass exchange between the plasmasphere and ionosphere is **not required** to explain their linkage. The intrinsic cause of SAPS (and thus of SED formation) is the energy-dependent gradient/curvature drifts of [[Ring Current|ring current]] electrons and ions that determine the Region-2 FAC geometry.

## PPEF Superfountain at the Equatorial Boundary

During extreme storms, **prompt penetrating electric fields (PPEFs)** of ~4 mV/m reach equatorial latitudes and drive a strong upward $E\times B$ drift of equatorial plasma — the "superfountain effect." [[Tsurutani 2013 PPEF Ionosphere Comment]] documents this during the 30 October 2003 Halloween superstorm: EIA peaks displaced from their normal ±10° MLAT location to ±22–30° MLAT, reaching ~210–270 TECu in CHAMP data. SAMI2 simulations reproduce the displacement and enhanced intensity only when the PPEF is included; without it, peaks remain near ±10° MLAT. Post-storm TEC at ±30° MLAT persisted 2 hr after the PPEF ended due to slow recombination at elevated altitudes.

This process is physically analogous to the sub-auroral SED lifting mechanism: in both cases, an enhanced $E\times B$ drift raises plasma to altitudes where N$_2$ and O$_2$ densities are smaller, suppressing recombination and producing extreme density enhancements. The equatorial superfountain feeds enhanced mid-latitude TEC that can be imported into the polar cap via the TOI/SED pathway.

## Sources

- [[Lundquist Varney 2026]]
- Varney 2026 PatchesChapter
- [[Zou 2021 SED Ion Upflow]]
- [[Themens 2024 May Storm]]
- [[Bao 2023 Geospace Plume MAGE]]
- [[Tsurutani 2013 PPEF Ionosphere Comment]]
