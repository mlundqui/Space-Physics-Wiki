---
type: entity
status: draft
updated: 2026-05-19
sources: 1
tags: [model, ionosphere, low-latitude, equatorial]
---

# SAMI2 (and SAMI2-PE)

SAMI2 (Sami Is Another Model of the Ionosphere, version 2) is a 2-D, time-dependent ionosphere-plasmasphere model developed at NRL (Huba et al. 2000). It simulates the low-latitude ionosphere and plasmasphere along a grid of dipole field lines from ~85 km to ~20,000 km altitude. SAMI2-PE is an extended version developed by [[Roger Varney]] in his Cornell PhD thesis ([[Varney 2012 Thesis]]) that replaces the empirical electron heating model with a self-consistent Boltzmann-Fokker-Planck photoelectron transport solver.

## SAMI2 Core Model

**Grid:** 90 dipole field lines $\times$ 151 grid points per field line; maximum apex altitude ~20,000 km (plasmasphere). For [[Jicamarca Radio Observatory]] comparisons the model is centered on the Jicamarca longitude with field lines extending from ~85 km to ~1650 km apex altitude (smaller domain used in SAMI2-PE reference runs).

**Ion species:** 7 — H$^+$, He$^+$, N$^+$, O$^+$, N$_2^+$, NO$^+$, O$_2^+$.

**Transport equations:** 5-moment fluid equations (continuity, momentum, energy) for each ion species. Electron fluid handled via quasineutrality; electron energy equation includes thermal conduction along field lines.

**Key empirical drivers:**
- $E\times B$ drifts: Scherliess-Fejer [1999] statistical model (equatorial vertical drift climatology)
- Neutral atmosphere: NRLMSISE-00
- Neutral winds: HWM93 (or HWM07 in sensitivity tests)
- Solar EUV: EUVAC model (standard SAMI2); HEUVAC (SAMI2-PE)

**Electron heating (standard SAMI2):** Semi-empirical model with a free parameter $C_{qe}$ that scales the photoelectron heating rate. The key limitation: no single value of $C_{qe}$ can simultaneously reproduce T_e at all altitudes in JRO data — errors are 500–2000 K (25–50%) because the model assumes local, instantaneous heating while the physical process is nonlocal.

## SAMI2-PE — Photoelectron Transport Extension

SAMI2-PE replaces the empirical C_qe heating with a full Boltzmann-Fokker-Planck transport equation for the photoelectron distribution function $\Phi(\ell, \mathcal{E}, \mu)$ — field-line position, energy, pitch-angle cosine.

**Transport equation** (four flux terms):

$$\frac{\partial \Phi}{\partial t} + \frac{\partial}{\partial \ell}[\mu\Phi] - \frac{\partial}{\partial \mu}\!\left[\frac{\delta B(1-\mu^2)}{2B}\Phi\right] + \frac{\partial}{\partial \mathcal{E}}[L(\mathcal{E})\Phi] = S(\ell,\mathcal{E},\mu)$$

where $L(\mathcal{E})$ is the Coulomb energy loss rate and $S$ includes pitch-angle diffusion, neutral inelastic collisions, photoproduction, and thermalization.

**Solar input:** HEUVAC spectrum (Richards et al. 2006) — 105 energy bins + 18 individual lines spanning 1.8–105 nm; brightest line He II at 30.4 nm (41 eV photoelectrons). Beer-Lambert EUV attenuation with Chapman grazing-incidence function.

**Collision physics:**
- Neutral inelastic: 39 types (Fennelly & Torr [1992] cross sections); energy cascade via Swartz [1985] algorithm
- Coulomb with thermal electrons: Fokker-Planck formalism; energy loss rate $L(\mathcal{E})$ and pitch-angle diffusion $D(\mathcal{E})$ with Coulomb logarithm fixed at 20
- Thermalization: photoelectrons cascading below $\mathcal{E}_t = (3/2)k_BT_e$ instantly join the thermal population

**Energy grid:** 0.25 eV bins (0–10 eV), 1 eV bins (10–60 eV), 10 eV bins (60–100 eV), 50 eV bins (100–450 eV), 100 eV bins (450–650 eV). Total ~151 bins.

**Pitch-angle grid:** Gauss-Legendre quadrature (even $n_{st}$; no $\mu = 0$ grid points). Reference: $n_{st} = 8$.

**Numerics:** Donor-cell upwinded (DCU) scheme (Godunov's method). Banded LAPACK SGBMV solve; operation count $O(n_z \cdot n_{st}^2)$ — so 8-stream is $16\times$ slower than 2-stream. Higher-order flux-limiter corrections (van Leer, minmod, superbee) available but omitted by default — they change results by only ~1–2% below 1500 km while adding a $4\times$ computation penalty.

**Guiding-center approximation:** Justified at JRO altitudes because gyroperiod ~$1.43\times10^{-6}$ s $\ll$ field-line crossing time; all perpendicular drifts ($E\times B$ ~25 m/s, curvature ~1 m/s, $\nabla B$ ~0.76 m/s) are negligible vs. parallel velocity ~$5.93\times10^5$ m/s.

## Scientific Findings from SAMI2-PE

**SAMI2-PE vs JRO agreement:** For the reference day (March 25, 2009; F10.7 = 68.2, Ap = 4.0), modeled and measured T_e above the F-peak agree to within ~30% throughout the entire day, including the rapid sunrise spike to ~3500 K. This is a large improvement over standard SAMI2.

**Nonlocal heating mechanism:** The equatorial topside ionosphere produces almost no photoelectrons locally (low neutral densities at high altitudes). Instead, it is heated by photoelectrons transported upward from the dense F-regions in both hemispheres. Consequently, topside T_e depends on neutral winds and $E\times B$ drifts through their control of F-region N_e: anything that reduces F-region density → more photoelectrons escape to topside → increased heating but lower thermal N_e → higher T_e, lower thermal energy density.

**EIA arc shadows:** In the afternoon when the equatorial ionization anomaly (EIA) arcs form at ±15° MLAT, the dense arcs absorb photoelectrons traveling between hemispheres, creating local minima ("shadows") in the photoelectron flux. These manifest as an inflection in T_e near 800 km altitude on field lines connected to the arcs.

**N($^2$D) quenching:** Quenching of metastable N($^2$D) by NO$^+$ is the dominant electron heat source at ~240 km (lower F-region), changing T_e at that altitude by >50%. The model overestimates temperatures at 240 km when quenching is enabled, suggesting the neutral NO chemistry model is insufficient at this altitude.

**Driver sensitivities (topside T_e can change by >30% from):**
- Neutral wind model (HWM93 vs HWM07; diverging vs converging winds can change plasmaspheric N_e by $\times 3$ and T_e by ~500 K)
- $E\times B$ drift amplitude (25% reduction shifts topside N_e and T_e substantially)
- Neutral density model (20% reduction → ~100–200 K topside T_e change; Emmert et al. [2010] NRLMSISE-00 corrections at solar minimum)

**Day-to-day variability:** SAMI2-PE with climatological inputs produces nearly identical T_e from day to day, while JRO data during July 8–13, 2008 (6 consecutive quiet days) shows ~500 K day-to-day differences. The best candidates for this missing variability are measured variations in $E\times B$ drifts (estimable from ΔH magnetometer data) and neutral winds (not measurable without off-equatorial ionosondes or beam-steering).

**Computational cost:** Reference simulation (8-stream, full energy grid) — 18.5 h/day on a single processor vs. 28 min for standard SAMI2. Low-resolution run (4-stream, 45 energy bins) — 4.5 h/day with only 5% T_e error. Skip-60 strategy (photoelectron transport every 60th time step, full resolution at sunrise/sunset) — 7.5 h/day with <10 K error at midday.

## Relationship to Other Models

**vs. FLIP (two-stream):** FLIP assumes fixed mean pitch-angle cosines ($\langle\mu\rangle = 0.577$) and treats inelastic collisions via an average energy loss approximation. SAMI2-PE uses multi-stream with self-consistent pitch-angle distributions — essential in the topside where mirror force and transport create anisotropic distributions not predictable from a single electron's collisionless trajectory.

**vs. SAMI3:** SAMI3 is the 3-D generalization. Inserting the SAMI2-PE photoelectron solver into SAMI3 is feasible in principle but requires the skip-step and pitch-angle reduction strategies to be explored first. The SAMI2-PE photoelectron routine could also be used to build a better empirical heating model for SAMI3, bypassing the full transport cost.

**vs. IPE (Ionosphere-Plasmasphere-Electrodynamics model):** IPE was the first 3-D global model with an embedded photoelectron solver (Maruyama et al. 2011), using FLIP's two-stream routine inside a Lagrangian 3-D framework.

**IPWM connection:** [[IPWM]]'s 8-moment parallel transport framework builds on the 5-moment fluid foundation established by SAMI2 for the low-latitude ionosphere. The key distinction is that IPWM is designed for high-latitude open field lines with a full multi-moment treatment, while SAMI2 targets the closed-field-line equatorial/low-latitude geometry.

## Sources

- [[Varney 2012 Thesis]]
