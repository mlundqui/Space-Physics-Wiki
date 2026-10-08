---
type: concept
status: draft
updated: 2026-10-08
sources: 4
tags: [magnetosphere, magnetotail, plasma-sheet, substorms, reconnection, current-sheet]
---

# Magnetotail

The nightside extension of the magnetosphere, stretched anti-sunward by the solar wind. Structurally it has three parts (200C textbook §9.8.1):

- **Two lobes.** Bundles of nearly uniform, low-density magnetic flux, one connected to each polar cap. The northern lobe field points toward Earth and the southern lobe field points away.
- **The plasma sheet.** A layer of hot plasma between the lobes, carrying the dawn-to-dusk **cross-tail current** that supports the field reversal.
- **The plasma mantle and the plasma-sheet boundary layer (PSBL).** Solar-wind plasma enters the tail through the mantle along newly opened flux. The PSBL lies on the edges of the plasma sheet and is the source region of Alfvén waves that reach the auroral ionosphere ([[Alfvén Waves]]).

The tail is the energy reservoir of the [[Dungey Cycle]]. Dayside reconnection adds open flux to the lobes, and nightside reconnection returns it. Substorms are the episodic unloading of that store ([[Milan Grocott 2021 High Latitude Convection]]).

## Plasma sheet

- **Origin of the plasma.** Mostly solar-wind plasma, as shown by composition and by the ion-to-electron temperature ratio. $T_i/T_e\approx8$ in both the magnetosheath and the plasma sheet, compared with about 0.9 in the upstream solar wind. The bow shock heats ions much more than electrons ([[Rankine-Hugoniot Jump Conditions]]; 200C §9.8.1). During storms, ionospheric O$^+$ from [[Ion Upflow]] adds to it.
- **Typical parameters.** $n\sim0.3$ cm$^{-3}$ and $T\sim10^7$ K (about 1 keV) ([[Debye Shielding and the Plasma Frequency]] table).
- **Harris current sheet.** The simplest self-consistent equilibrium (200C Eqs. 9.11–9.16):

$$B_x(z) = B_0\tanh(z/h),\qquad p(z) = \frac{B_0^2}{2\mu_0}\,\mathrm{sech}^2(z/h),\qquad j_y(z) = \frac{B_0}{\mu_0h}\,\mathrm{sech}^2(z/h).$$

Total pressure $p + B_x^2/2\mu_0 = B_0^2/2\mu_0$ is constant across the sheet: the lobe magnetic pressure confines the plasma-sheet thermal pressure. SymPy confirms that total pressure is constant and that $-\partial_zp + (\mathbf J\times\mathbf B)_z = 0$. The current is carried by particle drifts and by **meandering orbits** that cross the neutral sheet, where $B\to0$ and guiding-center theory fails ([[Guiding-Center Drifts]] §"where it breaks").

## Energy storage and substorms

- **Lobe flux and energy (200C §9.5 example).** A semicircular lobe of radius 25 $R_E$ at 30 nT holds about 1.2 GWb, and 10 $R_E$ of tail length stores about 900 TJ (both reproduced). For scale, mapped through a dipole ([[Dipole Field and L-Shells]] §3), 1.2 GWb of open flux corresponds to a polar-cap boundary near 67° latitude. That's an expanded, active-time polar cap. At typical boundaries (75–80°), the open flux is 0.25–0.5 GWb.
- **Growth phase** (200C §9.8.3; McPherron et al. 1973 model). With southward IMF, dayside reconnection outpaces nightside reconnection. Open flux piles into the lobes, lobe field and pressure rise, and the plasma sheet **thins**.
- **Current-sheet thinning.** A cross-tail electric field can compress a Harris sheet down to the ion-Larmor-radius scale by charge separation, a candidate precursor to onset ([[Artemyev 2008 Harris Current Sheet]]).
- **Onset and expansion.** Near-Earth reconnection is fast, collisionless and Hall-mediated, unlike [[Sweet-Parker Reconnection|Sweet–Parker]], which would take decades at tail parameters. It releases lobe flux. The near-Earth cross-tail current diverts through the ionosphere as the **substorm current wedge** ([[Field-Aligned Currents]]), the field **dipolarizes**, and particles are injected and betatron-heated ([[Adiabatic Invariants and Magnetic Mirrors]]). The ionospheric signatures are auroral brightening, the poleward bulge and the westward traveling surge ([[Aurora]]).
- **Bursty bulk flows** in the central plasma sheet map to auroral streamers ([[Aurora]]).
- **Timing.** [[THEMIS]] was designed to resolve onset timing in the near-Earth tail.

## Open questions

- Where does substorm onset begin: near-Earth current disruption, or mid-tail reconnection? The vault sources touch this only through [[Artemyev 2008 Harris Current Sheet]] and [[THEMIS]].
- How much of the storm-time plasma sheet is ionospheric O$^+$ rather than solar-wind H$^+$? This connects to [[Ion Upflow]] and [[Polar Wind]].

## Sources

- 200C textbook Ch. 9 §§9.5, 9.8 (`Atlas/Texts/Textbooks/200C Textbook/Ch9_SolarWindMagnetosphereCoupling.pdf`)
- [[Artemyev 2008 Harris Current Sheet]]
- [[Milan Grocott 2021 High Latitude Convection]]
- [[Auster 2007 THEMIS FGM]]
