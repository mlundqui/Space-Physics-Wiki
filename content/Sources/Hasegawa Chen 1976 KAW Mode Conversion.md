---
type: source
status: draft
updated: 2026-10-07
sources: 0
authors: A. Hasegawa, L. Chen
year: 1976
doi: 10.1063/1.861427 (Phys. Fluids); ingested copy is PPPL-1286 tech report, OSTI 10.2172/7258509
tags: [kinetic-alfven-waves, theory, mode-conversion, landau-damping, lab-plasma]
---

# Hasegawa Chen 1976 KAW Mode Conversion

> **Context caveat:** this is a **tokamak-heating** paper, not a magnetospheric one. It is the theoretical origin of the kinetic Alfvén wave (KAW) concept that later auroral work builds on. The auroral application is Hasegawa 1976, *JGR* 81, 5083 ("Particle acceleration by MHD surface wave and formation of aurora"), which is **not** in the vault. The PDF is a scanned typescript with poor OCR, so equations below were read from the text layer and cross-checked against [[Lysak Lotko 1996 Kinetic Alfvén Dispersion]], which quotes the same dispersion relation.

## Summary

An oscillating field applied to a nonuniform plasma resonantly mode-converts, at the location where $\omega = k_\parallel v_A(x)$ (the shear Alfvén resonance), into a **kinetic Alfvén wave**: a shear Alfvén wave whose perpendicular wavelength is comparable to the ion gyroradius. In ideal MHD that resonance is a singularity, because the shear mode cannot propagate across $\mathbf{B}$. Finite ion gyroradius ($\rho_i$) and electron effects ($\rho_s$) remove the singularity and let the wave carry energy away from the resonance. The KAW then dissipates. Because it carries a **parallel electric field**, electron Landau damping heats electrons along $\mathbf{B}$.

## Key claims

- **The resonance is a mode conversion.** The ideal-MHD singularity at $\omega = k_\parallel v_A(x_0)$ is resolved within $|x - x_0| \lesssim \rho_i$ by ion finite-Larmor-radius effects, and within $\lesssim \rho_s = \rho_i(T_e/T_i)^{1/2}$ by electron effects. This is the same physics as field-line resonances in the magnetosphere.
- **KAW dispersion relation** (small $k_\perp\rho_i$):
$$\omega^2 = k_\parallel^2v_A^2\left[1 + k_\perp^2\rho_i^2\left(\tfrac34 + \tfrac{T_e}{T_i}\right)\right]$$
  This equals $1 + k_\perp^2(\tfrac34\rho_i^2 + \rho_s^2)$. **It confirms the ion-FLR term** used on [[Alfvén Waves]].
  - For $k_\perp\rho_i \gg 1$: $\omega^2 \approx k_\parallel^2v_A^2k_\perp^2\rho_i^2(1 + T_e/T_i)$.
- **Direction of propagation.** After conversion, the KAW propagates toward the higher-density side, where $k_\parallel^2v_A^2(x) < \omega^2$. This is analogous to a Bernstein wave.
- **Absorption rate.** If the converted wave dissipates well inside the plasma, the absorption rate equals the ideal-MHD resonant-absorption rate, independent of the dissipation mechanism.
- **Dissipation regimes:**
  - **Collisional:** electrons and ions are heated at about equal rates.
  - **Collisionless, $\beta < 0.1$:** electrons are heated linearly by Landau damping of $E_\parallel$, along $\mathbf{B}$. Ions are heated nonlinearly by decay into ion acoustic waves, perpendicular to $\mathbf{B}$.
  - **$\beta > 0.1$:** ion Landau damping becomes comparable to electron Landau damping.
- **Nonlinear decay.** The parametric coupling to ion acoustic waves is stronger than classical estimates because the KAW's $k_\perp c_s/\omega_{ci}$ is of order 1.

## Methods/data

Ion Vlasov and electron drift-kinetic equations in a slab with a density gradient. The mode-conversion region is solved with Airy-type functions (WKB away from it). Linear Landau and collisional damping are computed, plus a parametric-decay threshold analysis. Numbers are for tokamaks: about 1 MHz drive and 50 G applied field.

## Connections

- [[Alfvén Waves]] — origin of the KAW and of its dispersion relation
- [[Wave-Particle Interactions]] — Landau damping by $E_\parallel$
- [[Lysak Lotko 1996 Kinetic Alfvén Dispersion]] — full kinetic generalization
- [[Chaston 2003 FAST Small-Scale Alfvén Waves]] — cites Hasegawa & Chen 1975 mode conversion in the plasma sheet boundary layer as a magnetospheric source

## Open questions

- The magnetospheric version (Hasegawa 1976 *JGR*: surface waves on the plasma sheet boundary mode-converting to KAWs that accelerate auroral electrons) is the paper actually relevant to aurora. **Worth adding to the reading list.**
