---
type: source
status: draft
updated: 2026-10-07
sources: 0
authors: C.A. Kletzing
year: 1994
doi: 10.1029/94JA00345
tags: [kinetic-alfven-waves, inertial-alfven-waves, electron-acceleration, fermi-acceleration, theory]
---

# Kletzing 1994 KAW Electron Acceleration

## Summary

An analytic, time-domain solution for the parallel electric field in the *wave front* of a small-$k_\perp$-scale Alfvén wave launched from a magnetospheric voltage generator in uniform plasma (cold electrons, $v_A \gg v_{te}$). The paper calls it "kinetic," but by [[Lysak Lotko 1996 Kinetic Alfvén Dispersion]]'s terminology it is the **inertial** regime. Mapping a Maxwellian through these fields with Liouville's theorem gives **two effects**:
1. A modest bulk acceleration (about 10–30 eV) of the background electrons, which carry the current.
2. **Fermi-like resonant reflection** of a small population up to about **twice the (kinetic) Alfvén speed**, giving about 0.6–1 keV for parameters near 7000 km altitude, where $v_A$ peaks.

## Key claims

- **Wave equation.** Combining polarization-drift current continuity, Ampère's law and Faraday's law with free cold-electron parallel motion gives a single equation for $E_x$. The resulting **KAW velocity along $\mathbf{B}$** is
$$V = v_A\big/\sqrt{1 + k_\perp^2c^2/\omega_{pe}^2}$$
  Short perpendicular scales slow the wave below $v_A$.
- **$E_\parallel$ exists only in the wave front**, where $E_x$ varies along $z$.
  - A ramp driver gives a unipolar square pulse of $E_\parallel$.
  - A pulse driver gives a bipolar $E_\parallel$, which accelerates and then decelerates.
- **Resonant (Fermi) reflection.** In the wave frame the front is a moving potential wall $\phi_z$. Electrons with
$$v_i \geq V - \sqrt{2e\phi_z/m_e}$$
  are reflected to $v_f = 2V - v_i$. These electrons leave the front *ahead* of the wave.
  - The effect strengthens as the scale shrinks, because $V$ and $\phi_z$ both scale as $1/k_\perp$ at large $k_\perp$.
  - It breaks down if the scale is too narrow, because then too much of the background is accelerated.
- **Worked example (about 7000 km):** $n = 15$ cm⁻³, $B = 0.065$ G, $T = 10$ eV, $E_x = 250$ mV/m, $1/k_\perp = 0.38$ km.
  - $v_A = 36{,}600$ km/s, but the KAW speed is only **9800 km/s**.
  - Resonant electrons reach about **650 eV**; the bulk reaches about 10 eV; the current is about 4.5 µA m⁻².
  - With $1/k_\perp = 0.53$ km, the resonant population disappears (only a stretching of the distribution remains). At larger scales the wave is too fast to catch many electrons.
- **Altitude dependence.** About 7000 km is roughly where $v_A$ starts rising steeply going down. Below that, the KAW speed outruns electrons, so 7000 km is representative of where resonant acceleration ends. At higher altitudes the lower density supplies fewer electrons.
- **Instability.** The current behind a ramp front is above an instability threshold over a long region, so it loses much energy to waves. A pulse is above threshold for only about 30 ms (about one e-folding).
- **Timing prediction (observational test).** Resonant electrons escape the front and arrive at low altitude **before** the wave fields: about 35 ms early at 7000 km, growing to about 0.25 s lower down. Rocket data (Boehm et al. 1990, about 600 km altitude) show electron bursts leading the fields by about 200 ms.

## Methods/data

Analytic 2-D (x, z) solution in uniform $B$ and $n$, solved with Fourier and Laplace transforms, with an infinitely conducting ionosphere (irrelevant before the front arrives). Electron distributions are built by back-tracing trajectories and applying Liouville's theorem. Compared with Boehm et al. 1990 rocket data.

## Connections

- [[Alfvén Waves]] — the inertial-regime acceleration mechanism and the "about $2v_A$" result
- [[Auroral Acceleration]] — broadband/Alfvénic electrons
- [[Artemyev 2015 KAW Electron Trapping]] — contrasts Fermi reflection, which gives <100 eV at the equator, with trapping
- [[Chaston 2003 FAST Small-Scale Alfvén Waves]] — cites this among simulations showing efficient inertial-wave acceleration

## Open questions

- The uniform-plasma model ignores the $v_A$ gradient. Kletzing notes the wave itself accelerates as it descends below about 4000 km, which may keep electrons in the front longer than modeled.
