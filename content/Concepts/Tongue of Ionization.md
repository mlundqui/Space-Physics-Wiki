---
type: concept
status: draft
updated: 2026-05-19
sources: 3
tags: [ionosphere, polar-cap, density-structures]
---

# Tongue of Ionization (TOI)

A planetary-scale (1,000–3,000 km) continuous channel of enhanced [[F-Layer]] electron density drawn from the dayside sub-auroral ionosphere across the open-closed magnetic field line boundary (OCB) into the polar cap by antisunward convection. The TOI is the large-scale parent structure from which mesoscale [[Polar Cap Patch|polar cap patches]] are commonly carved by structuring, scooping, or cutting processes.

## Formation

The two-cell polar convection pattern — the ionospheric projection of the [[Dungey Cycle]] — pulls mid-latitude sunlit plasma poleward when the pattern expands equatorward far enough to reach it. Formation requires IMF $B_z$ south or $B_y$-dominated driving; the four-cell lobe-reconnection pattern active during northward $B_z$ drives sunward convection in the cusp throat and cannot transport dayside plasma poleward.

The mid-latitude ionosphere produces far more O$^+$ via EUV photoionisation than the polar cap can produce locally, so the TOI supplies anomalously dense plasma that would be impossible from in-situ production alone. Large density contrasts (needed for patch detection by the factor-of-2 criterion) are most easily created by this mid-latitude plasma supply.

## OCB crossing and transit timescale

For the TOI to enter the polar cap, flux tubes carrying dense plasma must be opened by dayside magnetic reconnection. The OCB is therefore approximately co-located with the dayside reconnection line's ionospheric footprint and the Region 1 [[Field-Aligned Currents|FAC]] boundary.

Newly opened flux tubes still carry high F-region densities from when they were on closed field lines. Both the chemical timescale for O$^+$ recombination and the timescale for plasma to evaporate into the magnetosphere (~28 hrs for a typical flux tube) exceed the cross-polar-cap transport timescale of ~1–2 hrs. Direct TEC tracking of individual structures (Zhang et al. 2013, Science; Zhang et al. 2015) confirms transit times of 1–2 hrs across the polar cap and 3–4 hrs for a complete [[Dungey Cycle|Dungey convection cycle]].

## Geospace plume

The electric field structure driving the TOI maps along equipotential field lines to the equatorial plane. On closed field lines the same electric field drives outflow from the plasmasphere, forming the **plasmaspheric drainage plume**. The term **geospace plume** (Foster et al. 2005) refers collectively to the plasmaspheric drainage plume (in the magnetosphere) and the ionospheric TOI as two manifestations of the same large-scale electromagnetic structure. The crossing of the TOI across the OCB in the ionosphere corresponds to the point where the plasmaspheric drainage plume touches the dayside magnetopause — extra plasma mass that can affect the rate and location of magnetopause reconnection.

## Storm-enhanced density and the TOI

[[Storm-Enhanced Density|SED]] plumes at sub-auroral latitudes are enhanced versions of the plasma the TOI draws from. During geomagnetic storms, prompt penetrating electric fields and the disturbance dynamo amplify poleward $\mathbf{E}\times\mathbf{B}$ drift. The upward component of this drift in dipole geometry [[Lifting|lifts]] the mid-latitude ionosphere, suppressing O$^+$ loss and allowing the density to accumulate into an SED. When this SED plasma is subsequently pulled into the polar cap, it creates an exceptionally dense TOI and, potentially, the densest class of polar cap patches ($N_e > 10^{12}$ m$^{-3}$).

## Segmentation into patches

A continuous TOI can be structured into mesoscale features through three classes of process (see [[Polar Cap Patch]] for detail):

1. **Variable convection:** IMF $B_y$ variability and $B_z$ reversals twist and fold the TOI. With enough variability, the TOI structure becomes observationally indistinguishable from isolated patches.
2. **Scooping:** Intermittent dayside reconnection (~10-min bursts) scoops discrete boluses of plasma across the OCB rather than a continuous flow.
3. **Cutting:** Localised loss-rate enhancements (fast flow channels, N$_2$ anomalies) sever the TOI into segments.

## Distinguishing TOI from patches

Observationally ambiguous from a single measurement point. A satellite traversing a twisted TOI folded back on itself records what appears to be three separate density enhancements. A single ISR beam cannot differentiate a long continuous TOI from a sequence of isolated patches passing through the field of view. 2-D TEC maps and all-sky airglow imaging provide the best spatial context for topology determination, though GNSS orbit inclination limits coverage directly over the pole (GPS at 55° inclination → no vertical TEC above 55° geographic latitude).

## Observation modalities

- GPS/GNSS TEC maps (David et al. 2016; Chartier et al.) — large-scale morphology but geometry-limited at high latitudes; slant measurements may pass through multiple structures
- [[SuperDARN]] convection contours overlaid on TEC — shows whether structures follow $\mathbf{E}\times\mathbf{B}$ streamlines
- Red-line (630 nm) all-sky airglow — traces enhanced O$^+$ as a brightness arc; altitude ambiguity from $h_{mF2}$ changes (see [[Airglow]])
- [[RISR-N]] / ISR — direct altitude-resolved electron density profiles and volumetric 3-D images

## Extreme TOI during superstorms

[[Foster 2004 Multiradar TOI]] documents the 20 November 2003 superstorm as the definitive multi-radar TOI case. SED TEC exceeded 150 TECu — roughly $5\times$ quiet-time sub-auroral values. A coordinated network of three ISRs (Millstone Hill, Sondrestrom, EISCAT Tromsø) plus SuperDARN convection maps and DMSP in-situ data traced the complete SED → cusp crossing → polar cap entry chain in real time:

- F2-peak electron density exceeded $1.5\times10^{12}$ m$^{-3}$ simultaneously at all three ISR sites along the TOI
- Plasma was **cold** ($T_e/T_i \approx T_n \approx 2500$ K) — consistent with transport of sunlit mid-latitude plasma with minimal precipitation heating
- O$^+$ upflow exceeding 10$^{13}$ m$^{-2}$ s$^{-1}$ was observed in the cusp region, representing the mass loading of the dayside magnetosphere by TOI plasma entering through the cusp throat
- The TOI structure entered the polar cap with a coherent density "tongue" spanning from sub-auroral latitudes to the pole

This case directly confirms the SED–TOI–polar cap patch evolutionary chain and provides one of the highest-density polar cap density measurements on record.

## Sources

- [[Lundquist Varney 2026]]
- Varney 2026 PatchesChapter
- [[Foster 2004 Multiradar TOI]]
