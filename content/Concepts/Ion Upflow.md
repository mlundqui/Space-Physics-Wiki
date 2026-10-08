---
type: concept
status: draft
updated: 2026-10-08
sources: 6
tags: [ion-upflow, ion-outflow, polar-wind, O+, frictional-heating, ambipolar, cusp, SED, patches]
---

# Ion Upflow

Bulk **upward** motion of ionospheric ions, mainly O$^+$, along $\mathbf B$ in the topside high-latitude F region, typically at a few hundred m/s up to about 1 km/s, below about 1000 km. Upflow is the first stage of **ion outflow**. Most upflowing O$^+$ is still gravitationally bound and falls back unless it gets more energy higher up. Upflow therefore sets the *supply* that outflow processes can draw on.

> **Terminology.** *Upflow* is the low-altitude, sub-escape bulk flow seen by ISRs (e.g. [[RISR-N]]) and [[DMSP]]. *Outflow* is ions actually escaping into the magnetosphere: the [[Polar Wind]] (mostly H$^+$), plus energized O$^+$ (beams, conics, the cleft ion fountain). The two are linked but not the same.

## Why O⁺ needs help

A classical thermal wind can't lift O$^+$ out of Earth's gravity at ionospheric temperatures. Its sonic point lies about 7–14 $R_E$ out for $T_e + T_i = 3000$–6000 K, while H$^+$ escapes easily ([[Polar Wind Transonic Outflow]] §3). Upflow requires raising the O$^+$ **scale height**, i.e. raising $T_i$ or $T_e$, so that diffusive equilibrium pushes plasma upward ([[Plasma Diffusion Along B]]). There are two mechanisms, and they give the standard classification (as reviewed in [[Zou 2021 Polar Cap Density Structure Advances]]):

| | **Type 1 — frictional heating** | **Type 2 — electron heating / ambipolar** |
|---|---|---|
| Driver | Fast $\mathbf E\times\mathbf B$ drift through neutrals | Soft electron precipitation and FACs |
| Heated species | Ions ($T_i$ rises) | Electrons ($T_e$ rises) |
| How it lifts | Larger plasma scale height from $T_i$ | Stronger ambipolar field $\propto\nabla(n_eT_e)/n_e$ |
| Physics page | [[Frictional and Joule Heating]] ($T_i = T_n + m_n\lvert\Delta\mathbf u\rvert^2/3k_B$) | [[Plasma Diffusion Along B]] (ambipolar $E_\parallel$) |
| Typical setting | SAPS channels, convection reversals, patches entering fast flow | Cusp, nightside auroral boundary |
| Typical speed | ~100–750 m/s below 1000 km | Often larger fluxes |

## Fluxes and what controls them

| Setting | O$^+$ upflow flux (m$^{-2}$ s$^{-1}$) | Source |
|---|---|---|
| SAPS channel (Type 1), March 2016 storm | $\approx6\times10^{13}$ | [[Zou 2021 SED Ion Upflow]] |
| SED plume meeting cusp precipitation (Type 2) | peak $\approx3\times10^{14}$ | [[Zou 2021 SED Ion Upflow]] |
| SED plume crossing the open–closed boundary (PFISR) | $\approx2\times10^{14}$ | Zou et al. 2017, via [[Zou 2021 Polar Cap Density Structure Advances]] |
| Within SED at the nightside polar boundary (DMSP) | $\approx1.2\times10^{14}$ | Yuan et al. 2008, via the same review |
| Cusp during the 20 Nov 2003 superstorm TOI | $>10^{13}$ | [[Foster 2004 Multiradar TOI]] |

Integrated over area, the dayside cusp supplies about $2$–$4\times10^{25}$ s$^{-1}$, comparable to the whole nightside auroral zone ($4$–$6\times10^{25}$ s$^{-1}$) when SED plasma is present ([[Zou 2021 SED Ion Upflow]]).

**Density, not the electric field, limits the flux.** In the negative storm phase, O/N$_2$ depletion cut densities to about 30% of peak while convection stayed strong, and upflow flux fell by a factor of about 5 ([[Zou 2021 SED Ion Upflow]], [[Storm-Enhanced Density]]). The flux is $n\,u_\parallel$: heating sets $u_\parallel$, but the reservoir sets $n$.

## Where it shows up in this wiki

- **[[Polar Cap Patch|Patches]].** Net ion flux at 840 km is mostly *downward* inside patches. Upflow appears on patch margins and when patches enter the nightside auroral oval (DMSP, via Varney 2026 PatchesChapter). Patches also enhance topside H$^+$ by charge exchange, giving a predicted co-drifting polar-wind "jet".
- **[[Storm-Enhanced Density]] / [[Tongue of Ionization]].** These provide the dense O$^+$ reservoir that the largest upflow fluxes need.
- **[[NEIALs]].** Type 2 NEIAL events carry upward bulk velocities of about 660–800 m/s, consistent with auroral upflow ([[Akbari 2014 NEIAL Aspect Angle]]).
- **Lifted and dense polar-cap events.** The lifted/dense (LD) events of [[Lundquist Varney 2026]] are candidate sources of large outflow on open field lines deep in the polar cap. This hasn't been tested yet; see the open questions in [[overview]].
- **Higher up.** Transverse ion heating produces **ion conics**, measured by [[FAST]] ([[Carlson 2001 FAST Plasma Instrument]]). This is the next stage, which can lift O$^+$ to escape ([[Polar Wind]], cleft ion fountain).
- **Mission context.** The 2024 Decadal Survey's SOURCE+ concept targets upwelling and outflow from the ITM boundary ([[Decadal Survey 2024]]).

## Modeling

- Fluid models need to go beyond 5-moment closure once the flow becomes supersonic or anisotropic ([[Moment Equations from the Vlasov Equation]] §5; [[Blelly Schunk 1993 Moment Comparison]]).
- [[IPWM]] uses 8-moment equations along convecting flux tubes.
- Storm-time N$^+$ can rival O$^+$ upflow once its chemistry is treated correctly ([[Albarran 2023 N+ Polar Wind MAGE]]).

## Sources

- [[Zou 2021 SED Ion Upflow]]
- [[Zou 2021 Polar Cap Density Structure Advances]]
- Varney 2026 PatchesChapter
- [[Akbari 2014 NEIAL Aspect Angle]]
- [[Foster 2004 Multiradar TOI]]
- [[Carlson 2001 FAST Plasma Instrument]]
- [[Albarran 2023 N+ Polar Wind MAGE]]
- [[Decadal Survey 2024]]
- [[Schunk Nagy 2009 Ionospheres]] — via [[Polar Wind]] and [[Polar Wind Transonic Outflow]]
