---
type: concept
status: draft
updated: 2026-10-07
sources: 11
tags: [plasma-waves, MHD, auroral-acceleration, M-I-coupling]
---

# Alfvén Waves

The low-frequency ($\omega \ll \Omega_i$) transverse wave of a magnetized plasma. Its restoring force is magnetic tension. In ideal [[MHD]], the **shear Alfvén wave** has $\omega = k_\parallel v_A$, with $v_A = B_0/\sqrt{\mu_0 n m_i}$ in SI ($B/\sqrt{4\pi\rho}$ in Gaussian, as on [[MHD]]). It is how the magnetosphere communicates changes in stress and field-aligned current to the ionosphere. When the perpendicular scale becomes comparable to electron or ion kinetic scales, the wave becomes **dispersive** and carries a parallel electric field. Dispersive Alfvén waves (DAWs) are therefore a direct electron accelerator, the driver of **broadband (Alfvénic) aurora**, and a significant fraction of the auroral energy budget. See [[Auroral Acceleration]].

## Propagation through the magnetosphere

- **Guided energy flow.** For the shear mode the group velocity is $v_A\hat{\mathbf{b}}$, independent of $k_\perp$. Poynting flux travels along the field line to the wave's own magnetic footpoint.
  - Polar observations at 25,000–38,000 km show the downward Alfvén-wave Poynting flux **traces the auroral oval** and matches auroral luminosity, with almost no upward return flux ([[Keiling 2003 Alfvén Wave Poynting Flux]]).
- **Sources** (magnetospheric, not local — [[Chaston 2003 FAST Small-Scale Alfvén Waves]]):
  - **Reconnection** at the open/closed boundary: the cusp on the dayside, the plasma sheet boundary layer (PSBL) on the nightside.
  - **Mode conversion.** The unfolding reconnection separatrix acts as a compressional wave that **mode-converts to shear Alfvén waves on perpendicular $v_A$ gradients in the PSBL** (Hasegawa & Chen; Allan & Wright 2000).
  - Fast-flow and BBF instabilities.
  - Waves generated directly at $\lambda_e$ or $\rho_s$ scales in the reconnection diffusion region.
  - Substorm injections ([[Sivadas 2020 Thesis Energetic Precipitation]]; [[Artemyev 2015 KAW Electron Trapping]]).
  - Magnetopause surface waves on the dayside ([[Newell 2009 Global Precipitation Budget]], citing Chaston 2005).
- **Mode conversion as the origin of the KAW.** At a resonance surface where $\omega = k_\parallel v_A(x)$, the ideal-MHD shear-mode equation is singular. Finite $\rho_i$ and $\rho_s$ resolve the singularity and convert the incident wave into a KAW that carries energy away and dissipates ([[Hasegawa Chen 1976 KAW Mode Conversion]], laboratory context; field-line resonances are the magnetospheric analogue).
- **Getting to small $k_\perp$.** Phase mixing, field-line-resonance narrowing and ionospheric feedback drive $k_\perp$ upward. It is unresolved whether phase mixing alone reaches the observed scales: Allan & Wright's smallest mapped scale is about 50 km, versus about 1 km observed ([[Chaston 2003 FAST Small-Scale Alfvén Waves]]; [[Chaston 2007 DAW Auroral Acceleration Fraction]]).
- **Observed widths.** The median Alfvénic current-filament width mapped to 100 km is **about 1 km** (range 100 m to more than 10 km). Alfvénic aurora should have about 1 km structure ([[Chaston 2003 FAST Small-Scale Alfvén Waves]]).
- **Ionospheric boundary and the IAR.**
  - The ionosphere reflects the wave.
  - Steep $v_A$ gradients above it form the **ionospheric Alfvén resonator** (Lysak 1991), which can make field-aligned Poynting flux vary with altitude without dissipation.
  - Lessard & Knudsen 2001 argue that the resonator cannot operate for $\lambda_\perp < 2$ km and $f > 0.4$ Hz (via [[Chaston 2003 FAST Small-Scale Alfvén Waves]]).
- **Observational test.** In an Alfvén wave, $E_\perp/B_\perp \approx v_A(1 + k_\perp^2\lambda_e^2)^{1/2}$. In a quasi-static current system, $E/B \approx 1/(\mu_0\Sigma_P)$. Above the oval $v_A \gg 1/(\mu_0\Sigma_P)$, so the two are separable ([[Chaston 2007 DAW Auroral Acceleration Fraction]]; [[Strangeway Ch11 The Aurora]]).

### The Alfvén speed profile along an auroral field line

$v_A$ is **not** monotonic. It peaks a few thousand km above the ionosphere, where density is low but $B$ is still strong.
- **About 7000 km:** $n = 15$ cm⁻³ and $B = 0.065$ G give $v_A \approx 36{,}600$ km/s. With $1/k_\perp = 0.38$ km, inertial dispersion slows the wave to about 9800 km/s. About 7000 km is roughly where $v_A$ starts rising steeply going down ([[Kletzing 1994 KAW Electron Acceleration]]).
- **Steep gradients** sit near 7000 km on the nightside and about 13,000 km on the dayside. These reflect most of the incident wave: only about 10% of nightside Poynting flux from 30,000 km gets below 4175 km, versus about 50% on the dayside ([[Chaston 2003 FAST Small-Scale Alfvén Waves]], simulation).
- **Dayside lower bound:** at least $6\times10^3$ km/s at an altitude of at least 3000 km, inferred from about 100 eV cusp electrons ([[Chaston 2003 FAST Small-Scale Alfvén Waves]]).

This resolves an earlier tension with [[MHD]]'s "$v_A \approx 200$–$1000$ km/s at 1 $R_E$." That figure fits the outer and equatorial magnetosphere. Over the auroral zone at 1–2 $R_E$ altitude, $v_A$ is of order $10^4$ km/s.

### Two dispersive regimes

| Regime | Condition | Perpendicular scale | What supports $E_\parallel$ | Where |
|---|---|---|---|---|
| **Kinetic Alfvén wave (KAW)** | $v_{te} > v_A$ ($\beta \gtrsim m_e/m_i$) | $\rho_s = c_s/\Omega_i$ and $\rho_i$ | electron pressure (plus ion FLR) | hot plasma sheet, equatorial inner magnetosphere |
| **Inertial Alfvén wave (IAW)** | $v_{te} < v_A$ ($\beta \lesssim m_e/m_i$) | $\lambda_e = c/\omega_{pe}$ | electron inertia | above the auroral zone, **below about 4–5 $R_E$** |

- **Boundary.** The regimes divide at $\beta = m_e/m_i$, where the phase velocity is exactly $V_A$ ([[Lysak Lotko 1996 Kinetic Alfvén Dispersion]]).
- **Transition altitude.** The inertial limit holds below about 4–5 $R_E$ and the kinetic limit above (Lysak & Carlson 1981, via [[Lysak Lotko 1996 Kinetic Alfvén Dispersion]]). This replaces an earlier from-memory guess on this page.
- **What FAST sees.** Above the oval, $\lambda_e$ generally exceeds the gyroradii, so inertia is the dominant correction at FAST altitudes ([[Chaston 2007 DAW Auroral Acceleration Fraction]]). In the auroral cavity, $\lambda_e \approx 5$ km at 1 cm⁻³ ([[Strangeway Ch11 The Aurora]]).
- **Terminology varies.** "Kinetic Alfvén wave" is sometimes used for both regimes: [[Kletzing 1994 KAW Electron Acceleration]] calls the cold, inertial case "kinetic." "DAW" covers both.
- **Group velocity reverses.** The perpendicular group velocity has opposite sign in the two regimes, because $\omega$ rises with $k_\perp$ in the kinetic regime and falls in the inertial one. A wave crossing both can follow a "figure-eight" path (Streltsov & Lotko 1995, via [[Lysak Lotko 1996 Kinetic Alfvén Dispersion]]).
- **Plasma-sheet numbers.** At geosynchronous orbit β is about 0.1–0.2, which is $\gg m_e/m_i$, so the kinetic form applies at L ≥ 6.6 ([[Artemyev 2015 KAW Electron Trapping]]). Order-of-magnitude check (my arithmetic): $n \sim 0.3$ cm⁻³, $B \sim 20$ nT, $T_e \sim 1$ keV gives $v_A \approx 800$ km/s and $v_{te} \approx 13{,}000$ km/s.

## Derivation: two-fluid dispersion relation and $E_\parallel$

**Assumptions:**
- Uniform $\mathbf{B}_0 = B_0\hat z$
- $\omega \ll \Omega_i$ and $k_\perp \gg k_\parallel$
- Isothermal electrons; cold ions (ion FLR added at the end)
- No displacement current. Including it gives the $\omega_{pe}^2/c^2$ form in [[Strangeway Ch11 The Aurora]] Eq. 11.42.

**Potentials:**
- $\mathbf{E}_\perp = -\nabla_\perp\phi$
- $E_\parallel = -\partial_z\phi - \partial_t A_\parallel$
- $\delta\mathbf{B}_\perp = \nabla\times(A_\parallel\hat z)$

All perturbations vary as $e^{i(k_\perp x + k_\parallel z - \omega t)}$.

1. **Ampère's law (parallel):**
$$k_\perp^2 A_\parallel = \mu_0 J_\parallel$$

2. **Electron parallel momentum** (generalized Ohm's law; [[Strangeway Ch11 The Aurora]] Eq. 11.38, with $J_\parallel = -nev_{\parallel e}$):
$$E_\parallel = \underbrace{\frac{m_e}{n_0e^2}\partial_t J_\parallel}_{\text{inertial}}\;\underbrace{-\;\frac{T_e}{n_0e}\partial_z\delta n}_{\text{kinetic}}$$

3. **Electron continuity.** The $E\times B$ drift is incompressible in uniform $B$:
$$\partial_t\delta n = \frac{1}{e}\partial_z J_\parallel \;\Rightarrow\; \delta n = -\frac{k_\parallel}{\omega e}J_\parallel$$

4. **Current closure**, $\nabla\cdot\mathbf{J} = 0$, with the ion polarization current $\mathbf{J}_\perp = (n_0m_i/B_0^2)\,\partial_t\mathbf{E}_\perp$ (the same closure Kletzing uses):
$$J_\parallel = \frac{\omega k_\perp^2}{\mu_0 v_A^2 k_\parallel}\,\phi$$

5. **Faraday's law (parallel):**
$$E_\parallel = -ik_\parallel\phi + i\omega A_\parallel$$

**Identities for the coefficients:**
- $m_e/(n_0e^2) = \mu_0\lambda_e^2$
- $T_e/(n_0e^2) = \mu_0\rho_s^2v_A^2$, with $\rho_s^2 = T_em_i/(e^2B_0^2)$

**Two expressions for $E_\parallel$.** Substituting (3) into (2):
$$E_\parallel = -i\omega\mu_0J_\parallel\left[\lambda_e^2 - \frac{k_\parallel^2\rho_s^2v_A^2}{\omega^2}\right]$$

Substituting (1) and (4) into (5):
$$E_\parallel = -\frac{i\mu_0J_\parallel}{\omega k_\perp^2}\left(k_\parallel^2v_A^2 - \omega^2\right)$$

**Dispersion relation.** Set the two equal:
$$\boxed{\omega^2 = k_\parallel^2v_A^2\,\frac{1 + k_\perp^2\left(\rho_s^2 + \tfrac34\rho_i^2\right)}{1 + k_\perp^2\lambda_e^2}}$$

The cold-ion derivation gives the $\rho_s^2$ and $\lambda_e^2$ terms. The **$\tfrac34\rho_i^2$ ion-FLR term is now sourced**:
- Hasegawa's form is $\omega^2 = k_\parallel^2v_A^2[1 + k_\perp^2\rho_i^2(\tfrac34 + T_e/T_i)]$, where $\rho_i^2T_e/T_i = \rho_s^2$ and the $\tfrac34$ comes from expanding the Bessel function $\Gamma_0$ ([[Hasegawa Chen 1976 KAW Mode Conversion]]; [[Lysak Lotko 1996 Kinetic Alfvén Dispersion]]).
- The full kinetic solution (all gyroradius effects plus Landau damping) is qualitatively the same as this fluid form ([[Lysak Lotko 1996 Kinetic Alfvén Dispersion]]).

**Polarization.** Use $E_\perp = -ik_\perp\phi$ and the dispersion relation:
$$\boxed{\frac{E_\parallel}{E_\perp} = \frac{k_\parallel k_\perp\left(\lambda_e^2 - \rho_s^2\right)}{1 + k_\perp^2\lambda_e^2}}$$

Consequences:
- When $\rho_s \to 0$ this reduces to [[Strangeway Ch11 The Aurora]] Eq. 11.42 and to the local relation used in [[Chaston 2003 FAST Small-Scale Alfvén Waves]] (cross-check).
- When $k_\perp \to 0$, $E_\parallel \to 0$ and ideal MHD is recovered.
- The sign of $E_\parallel$ **reverses** between the inertial and kinetic regimes.
- $E_\parallel$ requires $k_\perp\lambda_e$ or $k_\perp\rho_s$ of order 1.
- **Plasma sheet vs. auroral zone.** KAW $E_\parallel$ can be many times larger in the plasma sheet than above the ionosphere (Watt & Rankin 2009, via [[Artemyev 2015 KAW Electron Trapping]]).

**Why only the shear mode?** The fast mode carries only perpendicular current. Since $\mathbf{k}$, $\mathbf{B}_0$ and $\mathbf{b}$ are coplanar for the fast mode, Faraday's law forces $\mathbf{E}\perp\mathbf{B}_0$. For the shear mode, $\mathbf{E}$, $\mathbf{k}$ and $\mathbf{B}_0$ are coplanar, so $E_\parallel \neq 0$ is allowed ([[Strangeway Ch11 The Aurora]] §11.5.3).

## Electron acceleration mechanisms

Three distinct KAW–electron interactions ([[Artemyev 2015 KAW Electron Trapping]]):

**1. Linear Landau resonance and damping** ($\omega = k_\parallel v_\parallel$).
- Electrons near the parallel phase speed exchange energy with $E_\parallel$. Damping heats electrons along $\mathbf{B}$ ([[Hasegawa Chen 1976 KAW Mode Conversion]]: electrons are heated in parallel for $\beta < 0.1$, ions perpendicular).
- **Landau damping is weak ($\gamma/\omega \lesssim 0.1$) unless $k_\perp\rho_s$ or $k_\perp\lambda_e$ is about 1 or larger.**
  - Waves with $\lambda_\perp \gtrsim 10$ km mapped to the ionosphere are not significantly damped.
  - **Hot ions suppress damping**, because ion FLR raises the phase speed into the electron tail.
  - There is **no peak in damping at $v_{te} = v_A$** ([[Lysak Lotko 1996 Kinetic Alfvén Dispersion]]).
  - *Correction:* an earlier version of this page said plasma-sheet KAWs simply Landau-damp on the bulk electrons. That holds only at small enough perpendicular scales.
- **Resonant energy.**
$$\mathcal{E}_{res} \approx \tfrac12 m_e v_A^2\,\frac{1 + k_\perp^2\rho_s^2}{1 + k_\perp^2\lambda_e^2}$$
  - $v_A = 10^4$ km/s gives about 0.3 keV; $3\times10^4$ km/s gives about 2.6 keV (my arithmetic).
  - **At the equator** (L = 6–9) the phase speed is too low for linear Landau resonance with about 100 eV electrons. Above the auroral zone, high $v_A$ allows it ([[Artemyev 2015 KAW Electron Trapping]]).

**2. Fermi reflection off the moving $E_\parallel$ front** (inertial regime, [[Kletzing 1994 KAW Electron Acceleration]]).
- In the wave frame, the front is a potential wall $\phi_z$ moving at the KAW speed $V$. Electrons with
$$v_i \geq V - \sqrt{2e\phi_z/m_e}$$
  are reflected to
$$v_f = 2V - v_i$$
  so they reach up to about **twice the (dispersive) Alfvén speed**.
- The background electrons are accelerated only modestly (about 10–30 eV; they carry the current).
- Example near 7000 km: resonant electrons reach about 0.65–1 keV.
- The effect needs small $1/k_\perp$ (about 0.4 km at 7000 km) but fails if the scale is too small.
- **Prediction:** resonant electrons outrun the front and arrive before the fields (about 200 ms lead in rocket data).
- At the equator, Fermi reflection gives less than 100 eV, so it heats cold ionospheric electrons but cannot make keV electrons there ([[Artemyev 2015 KAW Electron Trapping]]).

**3. Nonlinear trapping** (kinetic regime, inner magnetosphere, [[Artemyev 2015 KAW Electron Trapping]]).
- $E_\parallel$ plus the mirror force form a moving potential well, given a potential of about 100–400 V and $\lambda_\perp \sim \rho_i$.
- Electrons up to about 100 eV (even about 500 eV) are carried to about 40° latitude and accelerated to **several keV**.
- Because $\mu$ is conserved, the equatorial pitch angle collapses (about 80° to below 30°), forming **field-aligned beams** at about 5–30 × 10³ km/s.
- Trapping probability can approach 80%, which implies strong wave damping, so some amplification process must compensate.

**Where the auroral acceleration happens.**
- Statistically, most Alfvénic electron acceleration is **above FAST apogee, at about 1–2 $R_E$ altitude**, where the descending wave meets the $v_A$ peak and partial reflection enhances $E_\parallel$. The most energetic electrons originate about 2–3 $R_E$ up ([[Chaston 2003 FAST Small-Scale Alfvén Waves]]).
- At FAST, downgoing electron energy flux *exceeds* the remaining wave Poynting flux.
- Upgoing electrons accompany reflected waves, giving the **bidirectional** electrons of Alfvénic aurora ([[Strangeway Ch11 The Aurora]]).

**Why the result is broadband.** $v_A$ varies along the field, the wave is time-dependent (reflection, resonator) and $k_\perp$ covers a range. The resonant velocity is therefore smeared out, giving a field-aligned, unpeaked spectrum.
- Median characteristic energies are **about 4 keV premidnight** and **about 100 eV in the cusp** ([[Chaston 2003 FAST Small-Scale Alfvén Waves]]).
- Strangeway's "typically about 100 eV" matches the cusp value. Premidnight events are harder.

**Ions.** $E_\perp$ in small-scale Alfvén waves heats ions transversely, producing **ion conics** ([[Strangeway Ch11 The Aurora]]). DAW wavefields contain 15–34% of energetic ion outflow, and 40–50% near the cusp and premidnight ([[Chaston 2007 DAW Auroral Acceleration Fraction]]). See [[Atmospheric Escape]].

## How much of the aurora is Alfvénic?

| Study | Measure | Alfvénic share |
|---|---|---|
| [[Keiling 2003 Alfvén Wave Poynting Flux]] | high-altitude wave Poynting flux vs. UVI luminosity | about 30–35% |
| [[Chaston 2007 DAW Auroral Acceleration Fraction]] | FAST electron energy deposition (4 eV–30 keV) | 25–39% (about 50% near noon and premidnight; dominant there when active) |
| [[Newell 2009 Global Precipitation Budget]] | DMSP *total* precipitating energy flux, including diffuse electrons and ions | 6% (quiet) to 13% (active); 28% of *number* flux when active |

These are **different denominators**, not a direct contradiction. Newell's total includes the diffuse aurora (71–84%), which the other two studies largely exclude. Not reconciled; kept as reported.

## Contrast with whistler-mode chorus

| Property | Kinetic / inertial Alfvén wave | Whistler-mode chorus |
|---|---|---|
| Branch | shear Alfvén, dispersive at $k_\perp\rho_s$ or $k_\perp\lambda_e$ of order 1 | R-mode, electron-cyclotron branch |
| Frequency | $\omega \ll \Omega_i$ (mHz–Hz; FAST sees 0.2–20 Hz, Doppler-shifted) | $0.1$–$0.8\,f_{ce}$; upper and lower bands with a gap at $f_{ce}/2$ |
| Free energy | reconnection, flow shear and braking, injections, FLR mode conversion | electron anisotropy from injections |
| Propagation | energy guided strictly along $\mathbf{B}$ to the ionosphere; reflected by $v_A$ gradients | grows at the equator; field-aligned over a wide latitude range ([[Thorne 2010 Chorus Diffuse Aurora]]); L below about 8 |
| Resonance | Landau ($n = 0$), Fermi reflection, trapping | cyclotron ($n = \pm1$) |
| Effect on electrons | parallel **acceleration** into field-aligned, broadband beams | **pitch-angle scattering** into the loss cone, *plus* momentum scattering at 1–10 keV (upper-band chorus stochastically accelerates electrons above 10 keV) ([[Thorne 2010 Chorus Diffuse Aurora]]) |
| Aurora | broadband / Alfvénic | diffuse and pulsating |

*Correction:* an earlier version of this table said chorus diffusion is "nearly constant-energy" at keV energies. [[Thorne 2010 Chorus Diffuse Aurora]] shows substantial momentum diffusion at 1–10 keV.

**Possible coupling.** KAW-trapped field-aligned beams in injection regions move at about the phase speed of lower-band chorus, so **beam-driven whistler generation** is proposed. This would be an *indirect* KAW route into the chorus-driven diffuse aurora ([[Artemyev 2015 KAW Electron Trapping]]; speculative).

## Open questions / tensions

- Can phase mixing reach about 1 km scales, or must small-scale waves be generated directly (for example in the reconnection diffusion region)?
- How much of the wave-energy decrease below 4000 km is dissipation versus ionospheric-resonator phasing?
- The magnetospheric KAW paper Hasegawa 1976 (*JGR* 81, 5083) is still not in the vault. [[Hasegawa Chen 1976 KAW Mode Conversion]] is the lab-plasma companion.

## Derivations

- [[MHD Wave Modes]] — ideal-MHD derivation of the shear Alfvén wave (Walén relation, guided group velocity, $j_\parallel\propto k_\perp$)

## Sources

- [[Strangeway Ch11 The Aurora]] — generalized Ohm's law origin of KAW and IAW $E_\parallel$; Alfvén aurora; ion conics
- [[Sivadas 2020 Thesis Energetic Precipitation]] — KAW identification by $E/B \approx v_A$; link to injections
- [[Hasegawa Chen 1976 KAW Mode Conversion]] — KAW origin; mode conversion; dispersion with $\tfrac34\rho_i^2$; Landau heating regimes
- [[Kletzing 1994 KAW Electron Acceleration]] — wave-front $E_\parallel$; Fermi reflection to about $2V$; $v_A$ at 7000 km
- [[Lysak Lotko 1996 Kinetic Alfvén Dispersion]] — full kinetic dispersion; Landau damping weak above about 10 km; 4–5 $R_E$ regime boundary
- [[Chaston 2003 FAST Small-Scale Alfvén Waves]] — DAW statistics; acceleration at 1–2 $R_E$; $v_A$ profile and reflection; 1 km widths; sources
- [[Keiling 2003 Alfvén Wave Poynting Flux]] — oval-wide wave Poynting flux; 30–35% of luminosity
- [[Chaston 2007 DAW Auroral Acceleration Fraction]] — 25–39% of electron energy; 15–34% of ion outflow
- [[Newell 2009 Global Precipitation Budget]] — broadband aurora energy and number budget
- [[Thorne 2010 Chorus Diffuse Aurora]] — chorus properties for the contrast table
- [[Artemyev 2015 KAW Electron Trapping]] — trapping mechanism; plasma-sheet KAWs; beam to whistler link
- [[Schunk Nagy 2009 Ionospheres]] — MHD shear Alfvén baseline (via [[MHD]])
