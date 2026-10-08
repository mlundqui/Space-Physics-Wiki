---
type: source
status: draft
updated: 2026-05-13
sources: 1
authors: Thayer, Semeter
year: 2004
tags: [energy-flux, Poynting-flux, aurora, Joule-heating, IT-coupling]
---

# Thayer & Semeter 2004 — The Convergence of Magnetospheric Energy Flux in the Polar Atmosphere

## Summary

Review and synthesis paper examining the three sources of energy flux that converge in the polar upper atmosphere (80–200 km): (1) electromagnetic (EM) energy flux / Poynting flux from the magnetosphere–ionosphere (M-I) coupling; (2) kinetic energy (KE) flux from auroral particle precipitation; (3) solar vacuum ultraviolet (VUV) flux. Derives the Poynting theorem framework for the ionosphere-thermosphere (IT) system, shows how each source deposits energy at different altitudes and through different mechanisms, and discusses their mutual interaction. Key conclusion: EM and KE fluxes can be comparable to or exceed solar VUV in the polar IT system during active times, and the IT system actively feeds back on magnetospheric energy sources through ionospheric conductance modifications.

## Key claims

- Poynting's theorem in differential form: $\partial W/\partial t + \nabla\cdot\vec{S} + \vec{j}\cdot\vec{E} = 0$, where $\vec{S} = (\vec{E}\times\vec{B})/\mu_0$ is the Poynting flux and $W = B^2/(2\mu_0) + \varepsilon_0 E^2/2$ is the EM energy density. The $\vec{j}\cdot\vec{E}$ term is the EM-to-kinetic energy transfer rate (Joule heating + mechanical work).
- In the neutral-wind (center-of-mass) frame, the EM energy transfer splits into Joule heating and mechanical energy transfer (Thayer & Vickrey 1992): $\vec{j}\cdot\vec{E} = \vec{j}\cdot\vec{E}' + \vec{V}_n\cdot(\vec{j}\times\vec{B})$, where the first term is Joule heating and the second is the work done by ion drag on neutrals.
- Globally integrated over the hemisphere, ~94% of the Poynting flux convergence goes to Joule heating and ~6% to mechanical energy of the neutral gas (Lu et al. 1995). Locally, the partitioning depends on the neutral wind.
- Neutral winds reduce E-region EM energy deposition by a factor of ~3: at 120 km, heating with vs. without neutral winds is substantially different, with wind reducing the net deposition rate significantly.
- At moderate activity ($E \sim 20$ mV/m), height-integrated EM flux ~1.7 mW m$^{-2}$ is comparable to solar VUV (~8.3 mW m$^{-2}$); at high activity ($E > 60$ mV/m), EM deposition exceeds solar VUV at all altitudes below 200 km.
- Auroral KE flux partitioning in 80–200 km: ~50% heating, ~45% ionization, ~5% optical production. Heating efficiency is approximately constant at ~50% below 200 km (Rees et al. 1983), dropping to ~5% at 400 km.
- Average energy deposited per ion-electron pair: $W_\text{ion} \approx 35.5$ eV at 100 km (invariant with incident energy, charge, or mass); ionization efficiency $\gamma_\text{ion} \approx 45$%.
- KE flux (aurora) enhances Pedersen conductance, which in turn increases EM (Poynting) flux dissipation at that location. The IT system is not a passive recipient but actively modulates the magnetospheric energy sources through this conductance feedback.
- The ionospheric response to Joule heating (a heat source) creates divergent wind and large composition changes, while the response to ion drag (a momentum source) creates rotational wind and smaller composition changes — the two have dramatically different aeronomic consequences.

## Methods / data

Review/synthesis paper with observational examples from ISR (Sondrestrom), satellite (TIMED/SEE for VUV), and FAST satellite (auroral particle spectra). Theoretical derivations in MHD framework using the IT transport equations.

## Connections

- [[Joule Heating]] — provides the Poynting flux framework and the neutral-wind correction; 94% global partitioning to Joule heat
- [[Aurora]] — KE flux partitioning in the aurora; ionization efficiency; ionospheric density response equation $dN_e/dt = P - \alpha N_e^2$
- [[Ionospheric Conductivity]] — IT conductance modulates both EM flux dissipation and feeds back on the magnetosphere
- [[Field-Aligned Currents]] — FACs carry the Poynting flux; $E_{||}$ associated with Knight relation connects to KE flux
- [[Ionospheric Energetics]] — complete energy budget picture linking solar EUV, EM, and KE sources in the polar atmosphere
- [[Wave-Particle Interactions]] — Alfvén waves carry some of the Poynting flux at small scales; not fully included in the DC picture

## Open questions

- How is the partitioning between Joule heating and mechanical energy (ion drag) affected during extreme events when neutral wind velocities can reach 400+ m/s?
- At what spatial and temporal scales does the DC Poynting flux framework break down and Alfvénic (wave) energy transport become dominant?
