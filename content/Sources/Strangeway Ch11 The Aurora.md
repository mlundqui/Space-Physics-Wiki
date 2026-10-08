---
type: source
status: draft
updated: 2026-10-07
sources: 0
authors: R.J. Strangeway (from PDF metadata)
year: unknown (likely ~2016)
tags: [textbook-chapter, aurora, auroral-acceleration, alfven-waves]
---

# Strangeway Ch11 The Aurora

> **Provenance caveat:** The PDF metadata lists the author as Bob Strangeway, and the chapter refers to other chapters (Ch. 3 MHD, Ch. 13 plasma waves) and to "spacephysics exercises." That matches Russell, Luhmann & Strangeway, *Space Physics: An Introduction* (Cambridge, 2016), but this is **inferred, not confirmed**. Used as the EPSS 200C textbook. Equation numbering in the PDF is inconsistent (e.g. [11.38] vs 11.5.38).

## Summary

A 34-page textbook chapter on aurora: emissions, morphology, magnetosphere–ionosphere coupling, auroral field-aligned currents, conductivity channels, and planetary aurora. Its most useful content for this wiki is §11.5, which uses a FAST pass to split auroral field-aligned currents into three types: **inverted-V** (upward current, quasi-static potential), **return current** (downward current, upgoing electrons) and **Alfvén aurora** (mixed small-scale currents carried by Alfvén waves). It derives the Knight relation from Liouville's theorem, and shows from the generalized Ohm's law how the shear Alfvén wave carries $E_\parallel$ once its perpendicular scale is small.

## Key claims

- **Three auroral current regions (§11.5, Fig. 11.7, FAST):**
  - Inverted-V electrons carry upward current.
  - Low-energy bidirectional electrons and upgoing electrons carry the return and mixed regions.
  - The mixed region ("boundary-layer or Alfvénic aurora") has many small-scale currents that largely cancel, and "represents that part of the current system that is not yet in large-scale equilibrium."
- **Thermal current limit (Eq. 11.17):** $j_0 = n_0 e v_T/(2\pi^{1/2})$, with $m_e v_T^2 = 2k_BT$ (the chapter's convention). This is about 0.85 µA m⁻² for $n = 1$ cm⁻³ and $T = 1$ keV. Larger upward currents require parallel acceleration.
- **Velocity-space boundaries:** conserving energy and $\mu$ gives two curves, which together produce the "horseshoe" distribution seen by FAST (Fig. 11.8).
  - The acceleration ellipse, $v_\parallel^2 + v_\perp^2(1 - B_m/B) = 2e\phi/m_e$ (Eq. 11.21; signs reconstructed from energy and $\mu$ conservation because the PDF text extraction dropped the operators).
  - The loss-cone hyperbola (Eq. 11.23).
- **Knight relation (Eq. 11.32):**
$$j = j_0\frac{B_I}{B_m}\left\{1 - \left(1-\frac{B_m}{B_I}\right)\exp\!\left[-\frac{e\Phi_I}{k_BT\,(B_I/B_m - 1)}\right]\right\}$$
  - It saturates at $j_0 B_I/B_m$ (flux-tube convergence).
  - In the linear limit (Eq. 11.33), $j \approx j_0(1 + e\Phi_I/k_BT)$. Global MHD models use this limit to infer precipitation energy, because they cannot compute $\Phi$ themselves.
  - Potential constraints: $d\phi/dB > 0$ and $d^2\phi/dB^2 < 0$.
- **Inverted-V aurora:** electrons accelerated through an electrostatic potential to a few keV produce the discrete aurora. They are the source of auroral kilometric radiation (AKR) via the R-X mode cyclotron maser. The acceleration region is very low density: about 0.3 cm⁻³, inferred from the whistler cutoff at $f_{pe}$.
- **Return current:** downward current carried by upgoing ionospheric electrons, which empties the ionosphere and can appear as "black aurora." It is not exactly balanced with the upward current locally.
- **Alfvén aurora (§11.5.3):**
  - Above the ionosphere, $E/b \approx v_A$, not $1/(\mu_0\Sigma_P)$.
  - It is found near the polar cap boundary, mapping to the plasma sheet boundary layer, but is not restricted to it.
  - Precipitating electrons are "more typically around 100 eV."
  - The waves are accompanied by ion conics from transverse ion heating, a source of O⁺ outflow.
- **$E_\parallel$ in the shear Alfvén mode:** the parallel generalized Ohm's law (Eq. 11.38) is
$$E_\parallel = -\frac{\nabla_\parallel P_e}{ne} + \frac{m_e}{ne^2}\frac{\partial j_\parallel}{\partial t}$$
  The pressure term gives *kinetic* Alfvén waves and the inertia term gives *inertial* Alfvén waves. The fast mode cannot carry $E_\parallel$, because $\mathbf{k}$, $\mathbf{B}_0$ and $\mathbf{b}$ lie in one plane. The shear mode can.
- **Inertial $E_\parallel$ (Eq. 11.42):**
$$\frac{E_\parallel}{E_\perp} = \frac{k_\parallel k_\perp c^2/\omega_{pe}^2}{1 + k_\perp^2c^2/\omega_{pe}^2}$$
  This includes displacement current so that $v_A < c$. For $n = 1$ cm⁻³, $c/f_{pe} \approx 33$ km, so $\lambda_e \approx 5$ km. The oscillating field accelerates electrons both up and down the field line, producing bidirectional electrons.
- **Conductance from precipitation (Robinson 1987, Eqs. 11.35–11.36):** already on [[Aurora]] and [[Ionospheric Conductivity]].

## Methods/data

Textbook derivation, illustrated with FAST electron, ion and magnetometer data (Figs. 11.7, 11.8, 11.10). See [[Carlson 2001 FAST Plasma Instrument]] for the particle instrument.

## Connections

- [[Auroral Acceleration]] — the three-current-region framework and the Knight relation
- [[Alfvén Waves]] — the inertial/kinetic $E_\parallel$ derivation
- [[Aurora]], [[Field-Aligned Currents]], [[Ionospheric Conductivity]]
- [[Plasma Waves]] — AKR, whistler cutoff in the acceleration region
- [[Polar Wind]] / [[Atmospheric Escape]] — ion conics as an O⁺ outflow source

## Open questions

- The "about 100 eV" typical Alfvén-aurora energy matches the **cusp** median in [[Chaston 2003 FAST Small-Scale Alfvén Waves]]. Premidnight medians reach about 4 keV, so the chapter's figure understates nightside events.

- The chapter treats Alfvén aurora as a "not yet in equilibrium" state of M-I coupling. How much of the *total* precipitating energy does it carry, compared with the inverted-V and diffuse aurora? (Not quantified in the chapter.)
- The chapter does not treat the kinetic (pressure) branch quantitatively. See [[Alfvén Waves]] for the two-fluid derivation that includes both.
- Sections 11.2–11.4 and 11.6–11.7 (emissions, morphology, conductivity channels, planetary aurora) were skimmed but not read in depth in this ingest.
