---
type: concept
status: draft
updated: 2026-10-08
sources: 5
---

# Plasma Waves

Oscillatory disturbances in a plasma. Classified by whether they require a magnetic field (electrostatic vs. electromagnetic), propagation direction relative to $\mathbf{B}$, and whether they involve electrons, ions, or both.

## Cold Plasma Theory

Standard framework for linear wave propagation in a uniform, cold ($T = 0$), magnetized plasma. The dielectric tensor (Stix notation) gives refractive index $n^2 = (kc/\omega)^2$.

General dispersion (biquadratic in $n^2$):

$$A n^4 - B n^2 + C = 0$$

with Stix parameters $R$, $L$, $P$, $S = (R+L)/2$, $D = (R-L)/2$:
- $R = 1 - \sum_\alpha \omega_{p,\alpha}^2/[\omega(\omega+\Omega_\alpha)]$ (right-hand circularly polarized resonance)
- $L = 1 - \sum_\alpha \omega_{p,\alpha}^2/[\omega(\omega-\Omega_\alpha)]$ (left-hand circularly polarized)
- $P = 1 - \sum_\alpha \omega_{p,\alpha}^2/\omega^2$ (plasma oscillations)

**Cutoffs** ($n \to 0$; evanescent beyond): $R = 0$, $L = 0$, $P = 0$
**Resonances** ($n \to \infty$): upper hybrid (UH), lower hybrid (LH), cyclotron resonances

## Electrostatic Modes

| Wave | Frequency | Key features |
|------|-----------|-------------|
| Electron plasma (Langmuir) wave | $\omega \approx \omega_{pe}$ | $n^2{=}P{=}0$ cutoff; Bohm-Gross: $\omega^2 = \omega_{pe}^2 + \tfrac{3}{2} k^2 v_{th}^2$ with $v_{th}^2 = 2k_BT_e/m_e$ (i.e. $\omega_{pe}^2 + 3k^2k_BT_e/m_e$) |
| Ion acoustic | $\omega/k = u_s = \sqrt{k_B(T_e+\gamma_i T_i)/M}$ | Requires $T_e \gg T_i$; otherwise strong Landau damping |
| Upper hybrid | $\omega_{UH}^2 = \omega_{pe}^2 + \Omega_e^2$ | Electrostatic; perpendicular to $\mathbf{B}$ |
| Lower hybrid | $\omega_{LH}^2 = \Omega_i^2 + \omega_{pi}^2/(1+\omega_{pe}^2/\Omega_e^2)$; $\approx(\Omega_i \Omega_e)^{1/2}$ only when $\omega_{pe}\gg\Omega_e$ | Mixed ion/electron; key for wave heating. *(Corrected 2026-10-08: the dense-plasma limit was given as the general formula. It's 11% high at $L = 4$ outside the plasmapause and fails in the auroral cavity; see [[Cold-Plasma Waves]] §3.)* |
| Ion cyclotron (EIC) | $\omega^2 = \Omega_i^2 + k^2 u_s^2$ | Perpendicular to $\mathbf{B}$ |

## Electromagnetic Modes Along B

**Whistler (R-mode)**, $\Omega_i < \omega < \Omega_e$:

$$n^2_w = \frac{\omega_{pe}^2}{\omega(\Omega_e - \omega)}$$

Dispersive; group velocity $\propto \sqrt{\omega}$ so high frequencies arrive first (natural "whistler" pitch). Right-hand circularly polarized. Guided along $\mathbf{B}$; ray paths within ~19.5° of field line in homogeneous plasma.

**L-mode** (left-hand circularly polarized): $n^2 = L$; resonance at $\omega = \Omega_i$ (EMIC waves)

**Ordinary mode** (perpendicular to $\mathbf{B}$): $n^2 = P$; cuts off at $\omega = \omega_{pe}$ (ionosonde reflection)

**Extraordinary mode** (perpendicular to $\mathbf{B}$): $n^2 = RL/S$; upper hybrid resonance

## Key Magnetospheric Wave Modes

**Plasmaspheric hiss** (100 Hz – 2 kHz): diffuse, structureless whistler-mode; inside the plasmapause; principal scatterer of slot-region electrons (lifetimes ~days at $L = 4$)

**Chorus** ($0.1$–$0.8\,\Omega_e$): discrete, rising-tone whistler-mode emissions in the outer radiation belt ($L = 3$–$7$); driven by freshly injected anisotropic electrons ($T_\perp > T_\parallel$); accelerates outer belt electrons to MeV; onset triggered by substorm injection

**EMIC waves** (Electromagnetic Ion Cyclotron): L-mode; $f \sim$ 0.1–5 Hz (near ion gyrofrequency); driven by proton pitch-angle anisotropy; precipitates energetic protons and (via nonlinear cross-coupling) MeV electrons; dominant loss mechanism for relativistic electrons in storm-time inner belt

## Ionospheric Plasma Wave Taxonomy (S&N Ch. 6)

Schunk & Nagy Ch. 6 provides a systematic derivation of the dispersion relations for each mode from the linearized multi-fluid (or two-fluid) plasma equations, including finite temperature and collisions.

**Two-stream instability (§6.13):** Driven when $\mathbf{u}_e \neq \mathbf{u}_i$ (electron drift relative to ions). Growth condition: relative drift exceeds the ion acoustic speed, $|u_e - u_i| > u_s$. In the ionosphere, suprathermal electron beams from particle precipitation can excite electron plasma waves; the Farley-Buneman instability in the E-region electrojet arises from the $E\times B$ electron drift exceeding $u_s$ (see [[Ionospheric Instabilities]]).

**Rankine-Hugoniot shock conditions (§6.14):** Relating upstream (1) to downstream (2) fluid quantities across a planar shock front moving at speed $u_s$. For a strong perpendicular shock ($M_A \gg 1$): density ratio $n_2/n_1 = (\gamma+1)/(\gamma-1)$ → 4 for $\gamma=5/3$; pressure ratio $p_2/p_1 = 2M^2(\gamma-1)/(\gamma+1)^2$; temperature jumps proportional to $M^2$. Applied to CME-driven interplanetary shocks and bow-shock formation at magnetospheric obstacles.

**Double layers (§6.15):** Localized, quasi-static electrostatic potential drops that accelerate ions in one direction and electrons in the other, carrying a net current. Observed by S3-3 satellite at ~5000–8000 km altitude; potential drops of 0.5–5 kV associated with inverted-V electron precipitation. Double layers require an electron beam population capable of sustaining the layer against diffusion. They contribute to auroral acceleration alongside Alfvénic and quasi-static parallel electric fields.

## MHD Limit

For $\omega \ll \Omega_i$: plasma supports Alfvén waves (shear/torsional) and fast magnetosonic waves. Alfvén speed: $v_A = B / \sqrt{\mu_0\rho}$ (SI; corrected 2026-10-07 from the Gaussian $B/\sqrt{4\pi\rho}$). ULF Alfvén waves (mHz) drive radial diffusion of radiation belt particles (violation of the $\Phi$ invariant). See [[MHD]] for the full MHD wave and frozen-flux treatment.

**Dispersive Alfvén waves.** When $k_\perp\rho_s$ or $k_\perp\lambda_e$ becomes of order 1, the shear Alfvén wave becomes the **kinetic** ($v_{te} > v_A$, plasma sheet) or **inertial** ($v_{te} < v_A$, auroral cavity) Alfvén wave:
$$\omega^2 = k_\parallel^2v_A^2\frac{1 + k_\perp^2(\rho_s^2 + \tfrac34\rho_i^2)}{1 + k_\perp^2\lambda_e^2}$$
([[Hasegawa Chen 1976 KAW Mode Conversion]]; [[Lysak Lotko 1996 Kinetic Alfvén Dispersion]]). It carries $E_\parallel$, accelerates electrons by Landau resonance, and drives broadband aurora. Unlike chorus, it is guided all the way to the ionosphere and *accelerates* electrons rather than pitch-angle scattering them. See [[Alfvén Waves]] for the derivation and the chorus comparison.

**Electron cyclotron harmonic (ECH) waves.** Electrostatic emissions in bands between harmonics of $f_{ce}$. They propagate nearly perpendicular to $\mathbf{B}$, stay within a few degrees of the magnetic equator, and are driven by loss-cone gradients. They scatter plasma-sheet electrons only near the loss cone, so they are a minor contributor to diffuse aurora compared with chorus ([[Thorne 2010 Chorus Diffuse Aurora]]).

**Chorus bands.** Upper and lower bands are separated by a gap at $f_{ce}/2$. Upper-band chorus scatters electrons below a few keV; lower-band chorus scatters a few keV to 100 keV ([[Thorne 2010 Chorus Diffuse Aurora]]).

**Auroral kilometric radiation (AKR).** R-X mode cyclotron-maser emission from inverted-V electron beams in the very low-density ($\sim0.3$ cm⁻³) acceleration region. There, once the relativistic mass increase of keV electrons is included, the R-X cutoff drops below the *non-relativistic* $f_{ce}$ ([[Strangeway Ch11 The Aurora]]). *(Clarified 2026-10-08: in cold-plasma theory the R-X cutoff $f_R = f_{ce}/2 + \sqrt{f_{ce}^2/4 + f_{pe}^2}$ is always above $f_{ce}$; see [[Cold-Plasma Waves]].)*

## Landau Damping

Electrostatic waves at $\omega/k = v_{th}$ damp on the bulk of the particle distribution. Growth (Landau instability) requires $\partial f/\partial v > 0$ at the phase velocity. See [[Wave-Particle Interactions]] for details.

## Related Concepts

- [[Wave-Particle Interactions]] — resonance conditions; growth, damping, and diffusion
- [[Radiation Belts]] — waves are principal source and loss mechanism
- [[Ionospheric Instabilities]] — Farley-Buneman / gradient-drift are electrostatic ionospheric modes
- [[MHD]] — low-frequency limit: Alfvén, fast, slow magnetosonic modes
- [[Alfvén Waves]] — kinetic and inertial Alfvén waves, $E_\parallel$, auroral electron acceleration
- [[Auroral Acceleration]] — which waves drive which aurora

## Derivations

- [[Appleton-Hartree Equation]] — the electron-only magneto-ionic index (O/X modes)
- [[Landau Damping]] — derivation and verified damping rates for Langmuir and ion-acoustic waves
- [[Debye Shielding and the Plasma Frequency]] — derivation of $\omega_{pe}$ and $\lambda_D$
- [[MHD Wave Modes]] — derivation of the shear Alfvén, fast and slow modes
- [[Cold-Plasma Waves]] — Stix S/D/P, cutoffs and resonances, whistler group velocity, nose frequency, Storey angle

## Sources

- [[Schunk Nagy 2009 Ionospheres]] (Ch. 6: full ionospheric wave taxonomy including dispersion relations, cut-offs, resonances, two-stream instability, Rankine-Hugoniot shocks, double layers)
- AOS 250B course materials (Thorne 1993 course reader, Chapters 3–5)
- [[Strangeway Ch11 The Aurora]] (§11.5: AKR, inertial Alfvén $E_\parallel$)
- [[Sivadas 2020 Thesis Energetic Precipitation]] (chorus-driven diffuse and pulsating aurora; KAW evidence in the plasma sheet)
- [[Thorne 2010 Chorus Diffuse Aurora]] (chorus upper and lower bands; ECH waves)
- [[Hasegawa Chen 1976 KAW Mode Conversion]], [[Lysak Lotko 1996 Kinetic Alfvén Dispersion]] (kinetic Alfvén wave dispersion)
