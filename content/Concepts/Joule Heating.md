---
type: concept
status: draft
updated: 2026-10-07
sources: 2
---

# Joule Heating

Ohmic dissipation of electromagnetic energy in the ionosphere, arising when the applied electric field drives Pedersen currents through a resistive medium. The dominant energy input to the high-latitude thermosphere during geomagnetic activity.

## Neutral-Frame Formula

The Joule heating rate (energy deposited per unit volume per unit time) is:

$$Q_J = \mathbf{J}_P \cdot (\mathbf{E} + \mathbf{u}_n \times \mathbf{B})$$

where $\mathbf{E} + \mathbf{u}_n \times \mathbf{B}$ is the electric field in the neutral-wind frame, $\mathbf{u}_n$ is the neutral wind, and $\mathbf{J}_P$ is the Pedersen current density. Height-integrated:

$$Q_J = \Sigma_P |\mathbf{E} + \mathbf{u}_n \times \mathbf{B}|^2$$

**Key subtlety**: using just $\mathbf{E}$ (the electric field in the inertial frame) overestimates Joule heating when the neutral wind is non-negligible; the neutral-frame correction can reduce $Q_J$ by 20–50% at auroral latitudes where $\mathbf{u}_n$ can reach hundreds of m/s.

## Ion Drag

The reaction force on the neutral gas:

$$\mathbf{F}_{drag} = \rho_n \nu_{in} (\mathbf{v}_i - \mathbf{u}_n)$$

This is what transfers momentum from the ion flow (driven by $\mathbf{E}\times\mathbf{B}$ and collisions) to the neutral thermosphere. Ion drag drives the global thermospheric circulation and is the dominant high-latitude neutral body force during storms.

## Thermospheric Forcing

At auroral/polar latitudes during active times:
- Joule heating rates can reach 1–100 mW m$^{-2}$ column-integrated, comparable to or exceeding EUV
- Drives thermospheric upwelling, density enhancement, and composition changes
- Produces [[Traveling Atmospheric Disturbances]] (TADs) that propagate equatorward at ~500–800 m/s
- Storm-induced O/N$_2$ ratio depletion at mid-latitudes follows Joule-heated upwelling at high latitudes

**Localization matters for TAD generation.** [[Pham 2022 TADs]] shows that the spatial structure of Joule heating is the controlling factor for TAD properties — not just the total power. The MAGE coupled geospace model produces mesoscale, localized heating zones that generate TADs correctly captured in CHAMP/GRACE neutral density data. An empirical Weimer-driven TIEGCM with 40–100% larger total Joule power in some intervals but a broader, smoother spatial distribution generates TADs that do not match observations. At 09:30 UT during the August 2005 storm, WEIMER produced 1429 GW of hemispherically integrated Joule heat vs MAGE's 647 GW — yet MAGE outperformed WEIMER in capturing neutral density morphology by a factor of ~2 in $R^2$ during the main phase.

## Comparison with Particle Precipitation

For global energy budget during geomagnetic storms: Joule heating typically exceeds particle (auroral) precipitation energy by a factor of ~2–5, though locally precipitation can dominate inside the aurora. During weaker substorms the balance is more comparable.

## Poynting Flux Framework

Joule heating is the dominant sink of electromagnetic (EM) energy from the Poynting flux $\vec{S} = (\vec{E}\times\vec{B})/\mu_0$ entering the IT system through field-aligned currents. Poynting's theorem:

$$\frac{\partial W}{\partial t} + \nabla\cdot\vec{S} + \vec{j}\cdot\vec{E} = 0$$

In the neutral-wind frame (Thayer & Vickrey 1992), the EM energy transfer splits cleanly:

$$\vec{j}\cdot\vec{E} = \vec{j}\cdot\vec{E}' + \vec{V}_n\cdot(\vec{j}\times\vec{B})$$

The first term is Joule heating; the second is work done by ion drag on the neutral gas. Globally, ~94% of the converging Poynting flux goes to Joule heat and ~6% to neutral-gas mechanical energy (Lu et al. 1995). Locally, the partition depends on neutral wind magnitude and direction.

**Energy budget comparison:** At moderate activity ($E \sim 20$ mV/m), height-integrated EM flux $\sim 1.7$ mW m$^{-2}$ is comparable to solar VUV ($\sim 8.3$ mW m$^{-2}$); at $E > 60$ mV/m, EM deposition exceeds solar VUV at all altitudes below 200 km. Auroral KE (particle) flux is comparable to EM flux at polar latitudes during active times.

**Aeronomic consequences:** Joule heating (a heat source) drives divergent thermospheric wind and significant O/N$_2$ composition changes. Ion drag (a momentum source) drives rotational wind with smaller composition changes — qualitatively different impacts on the thermosphere.

## Related Concepts

- [[Ionospheric Conductivity]] — $Q_J = \Sigma_P E_{eff}^2$; $\Sigma_P$ is critical; aurora enhances $\Sigma_P$ and feeds back on M-I energy transfer
- [[Ionospheric Dynamo]] — drives the Pedersen currents
- [[Field-Aligned Currents]] — FACs carry the Poynting flux; the convergence of $\vec{S}$ in the IT system is the energy source for Joule heating
- [[Aurora]] — KE flux (particle precipitation) competes with and couples to Joule heating; enhances $\Sigma_P$ → increases EM dissipation
- [[Ionospheric Energetics]] — thermospheric $T_n$ and $T_i$ increase from Joule heating

## Observational constraints and forecast uncertainty

Current estimates of global Joule heating vary by up to 500% depending on method, which is the principal motivation for the LAITIR "dipper" mission concept in the 2024 Decadal Survey. The lower thermosphere below ~200 km — where Joule heating is strongest — is the least sampled region in the ITM; the last dedicated in situ measurements below 150 km were made by Atmospheric Explorer-C in 1974. IS radars are specifically cited as providing unique Joule heating constraints through their complete field-line profiles (ion pressure gradients, ambipolar fields, electron heat fluxes, ion upflow).

## Derivations

- [[Frictional and Joule Heating]] — derivation of $Q_J=\sigma_P|\mathbf{E}'|^2$ from ion–neutral friction, and of the Poynting-theorem energy split

## Sources

- Seeded from AOS 205B course materials.
- [[Thayer Semeter 2004 Energy Flux]]
- [[Pham 2022 TADs]]
- [[Decadal Survey 2024]] (PSG 1.2, LAITIR mission)
