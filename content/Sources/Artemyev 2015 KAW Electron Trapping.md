---
type: source
status: draft
updated: 2026-10-07
sources: 0
authors: A.V. Artemyev, R. Rankin, M. Blanco
year: 2015
doi: 10.1002/2015JA021781
tags: [kinetic-alfven-waves, electron-trapping, inner-magnetosphere, nonlinear-wave-particle, theory]
---

# Artemyev 2015 KAW Electron Trapping

## Summary

Theory and test-particle model of **nonlinear trapping** of cold (up to about 100 eV, and even up to about 500 eV) electrons by KAWs launched from the equatorial inner magnetosphere at L = 6–9. The KAW parallel electric field combines with the mirror force to form an effective potential well that carries trapped electrons poleward to about 40° latitude, accelerating them to **several keV**. Effective wave potentials are about 100–400 V and perpendicular wavelengths about the ion gyroradius. Since $\mu$ is conserved, the energy gain is parallel and the **equatorial pitch angle collapses**: about 80° becomes less than 30° in one trapping event. The result is **field-aligned electron beams** (about 5–30 × 10³ km/s) that can in turn drive **whistler waves**.

## Key claims

- **No ordinary Landau resonance at the equator.** At L = 6–9 the KAW phase velocity is too low for linear Landau resonance with about 100 eV electrons, unlike the auroral region, where high $v_A$ allows it (Chaston 2000, 2002). The large wave potential nevertheless widens the effective resonance range enough to trap.
- **Parallel field strength.** KAW $E_\parallel$ can be many times larger in the plasma sheet than above the ionosphere (Watt & Rankin 2009).
- **Three KAW–electron mechanisms:**
  1. Diffusive heating (Hasegawa & Mima 1978 and others)
  2. Reflection from the moving potential wall (Fermi; [[Kletzing 1994 KAW Electron Acceleration]])
  3. **Trapping** (this paper)
  
  At the equator, Fermi reflection gives less than 100 eV for $\Phi_0 < 400$ V. It can heat cold ionospheric electrons below 10 eV but cannot easily make a keV population. Trapping can.
- **The perpendicular field doesn't matter here.** Transverse $E$ (much larger than $E_\parallel$) is unimportant: cyclotron resonance needs electron energies far above thermal, and gyroradius effects need $\lambda_\perp \sim \rho_e$, whereas $\lambda_\perp \sim \rho_s$.
- **Trapping probability** can approach about 80% in some cases, which should strongly damp the KAW. Continued KAW detection implies a compensating process, such as transient particles decelerating as they reflect off the potential (each losing about 40 eV, of order $m v_A\sqrt{e\Phi_0/m}$).
- **Field geometry.** In a stretched (non-dipole) nightside field, the equatorial resonant energy ($\propto v_{A,eq}^2 \propto B_{eq}^2$) drops, but the final energy is set at the high-latitude escape point and is about unchanged.
- **Energy cascade:** KAW (ion scale) → trapped beams → electron holes, double layers and very oblique whistlers (electron scale). The beams' parallel speed matches the phase speed of lower-band parallel chorus at L = 6–9 (about 5000–10,000 km/s), so **beam-driven whistler generation** in injection regions is proposed (Mozer 2014; Malaspina 2015).
- **KAWs accompany injections:** intense KAWs are seen in plasma injection regions (Chaston 2014; Ergun 2015).

## Methods/data

Hasegawa dispersion $\omega = k_\parallel v_A[1 + k_\perp^2\rho_s^2(1 + T_i/T_e)]^{1/2}$, valid for $\beta \gg m_e/m_i$ (β about 0.1–0.2 at geosynchronous orbit). Dipole field, $n_e \propto \cos^{-5}\lambda$ (Denton 2006, valid for L ≤ 7). $T_e = 100$ eV, $T_i = 1000$ eV, wave period 2 s. Hamiltonian trapping theory plus $10^6$ test-particle trajectories.

## Connections

- [[Alfvén Waves]] — the kinetic-regime acceleration mechanism in the plasma sheet
- [[Auroral Acceleration]] — upstream energization of field-aligned electrons; possible indirect link to diffuse aurora via beam-driven whistlers
- [[Sivadas 2020 Thesis Energetic Precipitation]] — cites this for the "several keV" KAW limit
- [[Wave-Particle Interactions]], [[Plasma Waves]] — nonlinear trapping; whistler generation
- [[Radiation Belts]] — inner-magnetosphere hot electron source

## Open questions

- The self-consistent wave amplitude evolution, including trapped vs. transient particle currents, is left for future work.
- Do these KAW-made beams actually precipitate (equatorial pitch angle below the loss cone) or mainly feed whistler growth?
