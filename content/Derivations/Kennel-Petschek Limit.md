---
type: derivation
status: draft
updated: 2026-10-07
sources: 4
tags: [derivations, radiation-belts, wave-particle-interactions, whistler, chorus, precipitation]
prerequisites: "[[Quasilinear Diffusion]]; [[Adiabatic Invariants and Magnetic Mirrors]]"
next: "[[Derivations Index]]"
---

# Kennel-Petschek Limit

**Part III (magnetosphere)** of the [[Derivations Index]] · Previous: [[Quasilinear Diffusion]]

## Where we're going

Pour energetic electrons into the radiation belts. Can the trapped flux grow without bound? Kennel & Petschek (1966) said no, and the argument is a beautiful feedback loop:

1. Trapped electrons have a **loss-cone (pancake) anisotropy**, $T_\perp > T_\parallel$. That anisotropy is free energy that drives **whistler-mode** waves through cyclotron resonance.
2. The waves **pitch-angle scatter** the electrons into the loss cone ([[Quasilinear Diffusion]] §3), and the electrons precipitate.
3. More trapped flux means more resonant particles, faster wave growth, more scattering, and more loss.

So there's a flux level, $J^*$, at which wave growth just balances wave losses. Above it, the system precipitates the excess. This **limit on stably trapped flux** is why the observed electron fluxes in the outer belt (dawn and dusk, $L\gtrsim4$) cluster near a ceiling ([[Kennel 1966 Limit Stably Trapped Fluxes|KP]] Fig. 3; [[Olifer 2023 KP Self-Limiting Precipitation|Olifer et al. 2023]]).

We'll derive the limit following the condensed SI version of Summers et al. (2009, App. B), check it against KP's numbers, and then explain why the published values differ by factors of several.

---

## 1. Ingredient 1: who resonates with a whistler?

For parallel-propagating whistlers in a dense plasma, $\omega_{pe}\gg|\Omega_e|$ and $\omega<|\Omega_e|$. Dropping the "1" in the cold-plasma R-mode relation gives

$$\frac{c^2k^2}{\omega^2} = \frac{\omega_{pe}^2}{\omega\,(|\Omega_e| - \omega)}.$$

An electron resonates when the Doppler-shifted frequency it sees equals its gyrofrequency, $\omega - k v_\parallel = -|\Omega_e|$. It must move *against* the wave, with $|v_R| = (|\Omega_e| - \omega)/k$. With $x\equiv\omega/|\Omega_e|$, the minimum resonant energy is

$$E_R = \tfrac12m_ev_R^2 = \frac{m_ec^2}{2}\,\frac{|\Omega_e|^2}{\omega_{pe}^2}\,\frac{(1-x)^3}{x}.$$

That is $\sim B^2/(2\mu_0n)$ per particle: the magnetic energy per electron. Low-density regions (the plasmatrough outside the plasmapause) therefore resonate with **tens-of-keV** electrons, exactly the population injected in substorms. Inside the dense plasmasphere, $E_R$ is lower ([[Thorne 1993 AOS 250B Course Reader|Thorne]] p. 101).

---

## 2. Ingredient 2: how fast do waves grow?

The linear growth rate of a parallel whistler from an anisotropic electron population (Kennel & Petschek 1966; Summers et al. Eq. B3) is

$$\omega_i = \pi|\Omega_e|\,\eta\left(1 - x\right)^2\left(A - A_c\right),\qquad A_c = \frac{x}{1-x},$$

where

- $\eta$ is the **fraction of particles near resonance** (proportional to the resonant flux),
- $A$ is their **pitch-angle anisotropy**,
- $A_c$ is the **critical anisotropy**.

*Read the structure:* growth requires $A>A_c$, i.e. $x<A/(1+A)$. Only frequencies below $A/(1+A)$ of the gyrofrequency can grow (Thorne Eq. 6.43). For $A\sim\frac12$–$1$, that's $\omega\lesssim(0.3$–$0.5)|\Omega_e|$, which is where **chorus** lives. The amount of growth is proportional to how many particles are resonant ($\eta$).

This growth rate is quoted from the sources, not re-derived here. It follows from the linearized Vlasov equation with cyclotron resonance, the magnetized analog of [[Landau Damping]].

---

## 3. Ingredient 3: how much growth is "enough"?

A wave packet grows convectively as it travels along the field line. KP's criterion is that the gain over one pass must make up for the fraction lost on reflection at the ends. With power reflection coefficient $R<1$ and path length $\sim LR_E$:

$$\exp\!\left(\frac{2\omega_iLR_E}{v_g}\right) = \frac1R \qquad\Longleftrightarrow\qquad \omega_i = \frac{v_g\ln(1/R)}{2LR_E}.$$

KP wrote this as $\gamma\approx(\ln G)/T_w$, with wave escape time $T_w\approx LR_E/V_G$, and chose $\ln G\approx3$ (KP Eq. 5.1).

---

## 4. The limit

Solve the gain condition for $\eta$. Then convert $\eta$ to an omnidirectional integral flux using KP's diffusion-equilibrium distribution. KP Eq. 4.17 and Summers Eq. B7 both give $J(>E_R)\approx2\,v_RN_0\,\eta$. For the whistler relation, $v_Rv_g = 2c^2(|\Omega_e|-\omega)^3/(\omega_{pe}^2|\Omega_e|)$, and the density cancels:

$$J^*(>E_R) = \frac{2N_0c^2|\Omega_e|}{\pi\omega_{pe}^2}\,\frac{(1-x)\ln(1/R)}{LR_E\,(A-A_c)} = \boxed{\frac{2}{\pi}\,\frac{B_0}{\mu_0e\,LR_E}\,\frac{(1-x)\,\ln(1/R)}{A - A_c}}$$

In Gaussian units this is Summers' Eq. B8, $J^* = \frac{cB_0}{2\pi^2eLR_E}\frac{(1-x)\ln(1/R)}{A-A_c}$. In SI, $N_0c^2|\Omega_e|/\omega_{pe}^2 = B_0/\mu_0e$.

**Look at what's in it:**

- $B_0/(\mu_0 e)$ appears, but **not the density**: the limit is set by the magnetic field.
- With a dipole, $B_0 = B_E/L^3$, so

$$J^*\propto\frac{1}{L^4}.$$

**Numbers.** Take Summers' nominal parameters: $\ln(1/R) = 3$, $x = 0.25$, $A - A_c = 0.2$, $|\Omega_e|^2/\omega_{pe}^2 = 0.1$, $B_E = 0.312$ G. Then

$$J^*(>E_R)\approx\frac{1.7\times10^{10}}{L^4}\ \text{cm}^{-2}\,\text{s}^{-1},\qquad E_R\approx43\ \text{keV}.$$

Summers quotes this as "$\approx2\times10^{10}/L^4$ for $E_R\approx40$ keV." KP's own evaluation for $>40$ keV electrons at dawn and evening was $J^*\approx7\times10^{10}/L^4$ cm$^{-2}$ s$^{-1}$ (KP Eq. 5.4), with additional terms at noon and midnight.

---

## 5. Why the published limits differ

The two numbers above, $2\times10^{10}$ and $7\times10^{10}/L^4$, describe the *same* physics. The differences come from inputs that are only known to order of magnitude:

1. **Anisotropy and frequency choices.** KP used the diffusion-equilibrium anisotropy $A\approx1/6$ (their Eq. 4.16) and the $\omega\ll|\Omega_e|$ form of the limit (their Eq. 5.3), with $\ln G/\ell$ estimated as $3/L$. Summers used $x = 0.25$ and $A - A_c = 0.2$. Since $J^*\propto(1-x)/(A-A_c)$, these choices alone move the answer by factors of a few. KP estimated their result "accurate to a factor of 3."
2. **The gain criterion.** KP's criterion is *reflection*: waves bounce between hemispheres and must regain what's lost at each reflection. Observations show that whistler Poynting flux is directed *away* from the equator and that waves are not well ducted (Summers §2.3). Summers therefore replace reflection with a **convective gain** requirement over a growth length $H_P$: $G = \int\omega_i\,ds/v_g = 3/2$, i.e. 3 e-foldings in power, about 13 dB. This was chosen to be numerically equivalent to KP. CRRES and THEMIS chorus studies instead suggest that about **50 dB** is needed to grow from noise. That is $G\approx6$, which **raises the limit by about 4×** (Summers §2.3). The "limit" is only as precise as the required gain.
3. **Relativity.** For low-density regions (large $|\Omega_e|^2/\omega_{pe}^2$), resonant energies exceed about 100 keV. Relativistic growth rates then differ significantly from the nonrelativistic ones. Summers derived fully relativistic limits, which depend on the spectral index $l$ and pitch-angle index $s$ of the assumed distribution.
4. **What it is a limit on.** KP's limit applies to **weak diffusion** (partially empty loss cone). If the source keeps increasing, scattering eventually reaches the **strong-diffusion** rate, where the *precipitation rate* saturates at $\alpha_L^2/2T_B$ ([[Quasilinear Diffusion]] §3). Beyond that, the trapped flux *can* exceed $J^*$; "in principle... the trapped particle flux could increase indefinitely" (Summers §1, citing Kennel 1969). Parasitic scattering by other waves (plasmaspheric hiss, EMIC) usually keeps fluxes *below* the limit.

> **Wiki correction (2026-10-07).** [[Kennel 1966 Limit Stably Trapped Fluxes]] previously said that in strong diffusion "Flux cannot exceed this level." That conflates the two limits: strong diffusion caps the *loss rate*, not the trapped flux. The page has been corrected; see item 4.

---

## 6. Observational status

- **KP 1966.** Explorer 14 equatorial fluxes (>40 keV) lie "quite near the calculated upper limits" at $L\gtrsim4$. Precipitation (Injun 3) is strong only where trapped fluxes approach $J^*$ (KP Fig. 3).
- **Olifer et al. 2023.** Across 70 storms, dawn-side injections briefly push 54 keV fluxes above the K-P level. Chorus then returns them to an asymptotic cap (about $5\times10^3$ cm$^{-2}$ s$^{-1}$ sr$^{-1}$ keV$^{-1}$ at $L\approx4.5$), producing the most intense precipitation POES sees. The limit shapes the whole pitch-angle distribution, not just the equatorial flux. See [[Olifer 2023 KP Self-Limiting Precipitation]].

---

## What we assumed, and where it breaks

- **Parallel, linear, quasilinear whistlers.** Oblique waves and nonlinear chorus growth and trapping (Omura and colleagues) are outside the theory. Summers lists them as the next step.
- **A single resonant population with a fixed distribution shape.** The limit depends on the assumed energy spectrum and pitch-angle distribution.
- **A dipole field and local equatorial growth.** Real growth lengths depend on field-line geometry; Summers also give a current-sheet version.
- **Weak diffusion** (see §5, item 4).

---

## Verification

- **Sources agree.**
  - Self-limiting concept, reflection criterion $\gamma = \ln G/T_w$, $J/(V_RN\eta)\approx2$, the $>40$ keV evaluation $7\times10^{10}/L^4$, and strong-diffusion lifetime $4T_BL^3$: [[Kennel 1966 Limit Stably Trapped Fluxes|KP 1966]] §4–5, Eqs. 4.13, 4.17, 5.1–5.4.
  - Condensed derivation (Eqs. B1–B10), the gain-criterion change, relativistic extension, and the 50 dB / 4× caveat: [[Summers 2009 Relativistic KP Limit|Summers et al. 2009]].
  - Resonance, critical anisotropy $\omega_{\max}/\Omega = A/(1+A)$, and weak/strong diffusion: [[Thorne 1993 AOS 250B Course Reader|Thorne]] Eqs. 6.43, 7.7–7.17.
  - Observational capping: [[Olifer 2023 KP Self-Limiting Precipitation|Olifer et al. 2023]].
- **SymPy.**
  - From the gain condition, growth rate, $J\approx2v_RN_0\eta$ and whistler dispersion, the limit reduces exactly to the boxed form. In SI it is $\frac{2}{\pi}\frac{B_0}{\mu_0eLR_E}\frac{(1-x)\ln(1/R)}{A-A_c}$, matching Summers' Gaussian Eq. B8.
  - $E_R$ from the resonance condition matches Eq. B9.
  - $A_c = x/(1-x)\Leftrightarrow x_{\max} = A/(1+A)$, matching Thorne Eq. 6.43.
- **Numerical.**
  - Summers' nominal case evaluates to $1.7\times10^{10}/L^4$ cm$^{-2}$ s$^{-1}$ at $E_R = 43$ keV, in both Gaussian and SI ("≈ $2\times10^{10}$", "≈ 40 keV" in the paper).
  - The KP pitch-angle lifetime formula was checked numerically to within 0.2% (see [[Quasilinear Diffusion]]).
- **Not re-derived:** the whistler growth rate (§2) and KP's $\eta$-to-flux moment (Eq. 4.17). Both are quoted, and both appear consistently in KP and Summers.

## Sources

- [[Kennel 1966 Limit Stably Trapped Fluxes]] — the original limit; §4 diffusion equilibrium; §5 whistler-mode limit
- [[Summers 2009 Relativistic KP Limit]] — relativistic reformulation; convective-gain criterion; App. B classical derivation
- [[Thorne 1993 AOS 250B Course Reader]] — Ch. 6 (growth and critical anisotropy), Ch. 7 (pitch-angle diffusion and lifetimes)
- [[Olifer 2023 KP Self-Limiting Precipitation]] — storm-time observational confirmation
