---
type: derivation
status: draft
updated: 2026-10-07
sources: 4
tags: [derivations, ISR, incoherent-scatter, kinetic-theory, RISR-N, landau-damping]
prerequisites: "[[Debye Shielding and the Plasma Frequency]]; [[Landau Damping]]"
next: "[[Derivations Index]]"
---

# Incoherent Scatter Spectrum

**Part II (ionospheric measurement)** of the [[Derivations Index]] · Prerequisites: [[Debye Shielding and the Plasma Frequency]], [[Landau Damping]]

## Where we're going

An incoherent scatter radar such as [[RISR-N]] fires a UHF pulse into the ionosphere and listens to an echo about $10^{-28}$ m² per electron strong. From the *shape* of that echo's Doppler spectrum we get the electron density, the electron and ion temperatures, the line-of-sight ion velocity, and even the ion composition. How can one spectrum hold so much?

The answer is that the radar doesn't see individual electrons. It sees electron-density fluctuations at one wavelength, and in a plasma those fluctuations are organized by **Debye shielding** and by **ion-acoustic waves** that are **Landau damped**. This page derives the spectrum, following the fluctuation–dissipation approach of Swartz & Farley (1979) as presented in [[Varney 2012 Thesis|Varney (2012)]] Ch. 2, and recast in the "dressed particle" form used by Kudeki & Milla (2011). Then it reads off what each feature measures.

---

## 1. What the radar measures

A monostatic radar at wavelength $\lambda_R$ is sensitive to density structure at the **Bragg wavenumber** $k = 4\pi/\lambda_R$. For RISR-N at 441.9 MHz ([[Bahcivan 2010 Initial RISR-N Observations]]), $\lambda_R = 0.68$ m, $k = 18.5$ m$^{-1}$, and the probed wavelength is $2\pi/k = 0.34$ m.

The scattered power per unit frequency is the Thomson cross-section times the **spectrum of electron-density fluctuations** (Varney Eqs. 2.5–2.6):

$$\sigma(\omega_0+\omega)\,d\omega = \sigma_e\,\left\langle|n_e(\mathbf{k},\omega)|^2\right\rangle\frac{d\omega}{2\pi},\qquad \sigma_e = 4\pi r_e^2\approx10^{-28}\ \text{m}^2.$$

If electrons were scattered randomly, with no correlations, each would contribute its own Doppler shift $\omega = kv$. The spectrum would just be the electron velocity distribution,

$$\left\langle|n_e|^2\right\rangle_{\text{free}} = \frac{2\pi N_e}{k}\hat f_e(\omega/k),$$

a Gaussian with standard deviation $kv_{te}/2\pi\approx510$ kHz for RISR-N at $T_e = 2000$ K, so about 1 MHz wide. That's what Gordon (1958) expected. The real spectrum is only about ±10 kHz wide, set by the *ion* thermal speed. The plasma is telling us the electrons are not free.

---

## 2. The physics: every electron is "dressed"

When $k\lambda_D\ll1$ (for RISR-N, $k\lambda_{De}\approx0.06$ in the F region), each particle is surrounded by its shielding cloud ([[Debye Shielding and the Plasma Frequency]]). Electron-density fluctuations at wavelength $2\pi/k$ come from two sources:

- **Bare thermal electrons**, $n_{te}$, *partly cancelled* by their own electron shielding cloud.
- **Bare thermal ions**, $n_{ti}$, each carrying a cloud of electrons that shields it. As the ion moves, its electron cloud moves with it, and the radar sees those electrons moving at ion speeds.

The second effect is why the spectrum is narrow. Let's make it quantitative.

### Linear response

Let each species respond to the fluctuating potential $\phi$ through its susceptibility $\chi_s(k,\omega)$ (the same function that appears in [[Landau Damping]]). The total densities are the "bare" thermal parts plus induced parts:

$$n_e = n_{te} + \frac{\varepsilon_0k^2}{e}\chi_e\,\phi,\qquad n_i = n_{ti} - \frac{\varepsilon_0k^2}{e}\chi_i\,\phi.$$

As a check, in the static limit $\chi_e\to1/k^2\lambda_{De}^2$, the electron term becomes the Boltzmann response $n_0e\phi/k_BT_e$. Poisson's equation, $\varepsilon_0k^2\phi = e(n_i - n_e)$, then gives

$$\frac{\varepsilon_0k^2}{e}\phi = \frac{n_{ti}-n_{te}}{1+\chi_e+\chi_i},$$

and therefore

$$\boxed{n_e = \frac{(1+\chi_i)\,n_{te} + \chi_e\,n_{ti}}{1+\chi_e+\chi_i}}$$

The denominator $\epsilon = 1+\chi_e+\chi_i$ is the plasma's dielectric function: the same function whose zeros are the normal modes. The spectrum will therefore have peaks near the frequencies of the electrostatic waves, broadened by their damping.

### Square and average

Bare electron and ion thermal fluctuations are uncorrelated, so

$$\left\langle|n_e|^2\right\rangle = \frac{|1+\chi_i|^2\left\langle|n_{te}|^2\right\rangle + |\chi_e|^2\left\langle|n_{ti}|^2\right\rangle}{|1+\chi_e+\chi_i|^2}.$$

For a Maxwellian, the bare spectrum $\langle|n_{ts}|^2\rangle = (2\pi N/k)\hat f_s(\omega/k)$ is the same thing as $2Nk^2\lambda_{Ds}^2\,\mathrm{Im}\,\chi_s/\omega$. This is the **fluctuation–dissipation theorem**: random thermal noise is tied to the same imaginary part ($\mathrm{Im}\,\chi$) that causes Landau damping. The result is Varney's Eq. 2.23 (Swartz & Farley 1979):

$$\boxed{\left\langle|n_e(\mathbf{k},\omega)|^2\right\rangle = 2k^2N_e\,\frac{|1+\chi_i|^2\lambda_{De}^2\,\mathrm{Im}\{\chi_e\}/\omega_e + |\chi_e|^2\lambda_{Di}^2\,\mathrm{Im}\{\chi_i\}/\omega_i}{|1+\chi_e+\chi_i|^2}}$$

Here $\omega_s = \omega - \mathbf{k}\cdot\mathbf{U}_s$ is the Doppler-shifted frequency in each species' frame. For collisionless, unmagnetized Maxwellians,

$$\chi_s = \frac{1}{k^2\lambda_{Ds}^2}\left[1 + \theta_sZ(\theta_s)\right],\qquad \theta_s = \frac{\omega_s}{\sqrt2\,k\,v_{ts}},$$

with $Z$ the plasma dispersion function. (Varney's Eq. 2.25 prints $\lambda_\alpha$ in the denominator; it should be $\lambda_{D\alpha}^2$, as in Bellan Eq. 5.65.) Several ion species simply sum: $\chi_i\to\sum_j\chi_j$ (Varney Eq. 2.24).

Swoboda's open-source **ISRSpectrum** code, built on Kudeki & Milla (2011), assembles the spectrum the same way: an ion line $\propto|\chi_e|^2\times$(ion thermal term) and an electron line $\propto|1+\chi_i|^2\times$(electron thermal term), both over $|1+\chi_e+\sum\chi_i|^2$.

---

## 3. Reading the spectrum

**The ion line** (low frequency, $|\omega|\sim kv_{ti}$) carries nearly all the power when $k\lambda_D\ll1$.

- **Two humps at $\pm$ the ion-acoustic frequency.** These are ion-acoustic waves traveling toward and away from the radar. The hump positions scale with $\sqrt{(T_e + 3T_i)/m_i}$, so they set the **temperatures**.
- **Hump sharpness.** This is set by ion [[Landau Damping]], which is strong when $T_e\lesssim T_i$ and weak when $T_e\gg T_i$ ([[Landau Damping]] §6). The depth of the central dip therefore measures **$T_e/T_i$**.
  - For a pure O$^+$ plasma at $k\lambda_{De} = 0.2$, the peaks sit at $\theta_i\approx0.96$, 1.46, 1.73 and 1.91 for $T_e/T_i = 1$–4, reproducing Varney's Fig. 2.1.
  - For RISR-N ($T_i = 1000$ K, O$^+$), that's about 2.9–5.2 kHz from the carrier.
- **A shift of the whole line.** This is the line-of-sight ion **drift** $\mathbf{k}\cdot\mathbf{U}_i$. This is the ion velocity that feeds $\mathbf{E}\times\mathbf{B}$ convection estimates ([[Guiding-Center Drifts]] §2; [[Gilles 2018 RISR SuperDARN Velocity Comparison]]).
- **Composition.** A pure H$^+$ plasma gives a line four times wider than O$^+$, since $v_{ti}\propto m_i^{-1/2}$. Mixtures give a narrow core plus broad wings, so the H$^+$ fraction is measurable (Varney Fig. 2.2).

**Total power and "raw" density.** Integrated over the ion line, the power is about

$$\sigma_{\text{ion}}\approx\frac{N_e\sigma_e}{(1+k^2\lambda_{De}^2)(1+k^2\lambda_{De}^2+T_e/T_i)}\;\longrightarrow\;\frac{N_e\sigma_e}{2}\ \text{for } T_e = T_i,\ k\lambda_D\to0.$$

That's why a "raw" ISR density (power converted assuming $T_e = T_i$) must be corrected for $T_e/T_i$ once the spectrum is fitted.

**The plasma line** is a weak, narrow peak offset by the Langmuir frequency $\omega\approx\sqrt{\omega_{pe}^2 + 3k^2v_{te}^2}$, about 9 MHz at $10^{12}$ m$^{-3}$. Its frequency gives an absolute density. It's enhanced by suprathermal (photo-) electrons, which have little effect on the ion line (Varney §2.1.1).

**The large-$k\lambda_D$ limit.** For $k\lambda_{De}\gg1$, shielding is irrelevant, $\chi\to0$, and the spectrum reverts to the free-electron Gaussian with total power $N_e\sigma_e$.

---

## 4. Why different "ISR theories" give different spectra

Eq. 2.23 holds for any stable plasma once the right $\chi_s$ are used (Swartz & Farley 1979). The theories in the literature differ only in **which susceptibility they use**:

| Effect | Change to $\chi_s$ | Where it matters | References (via Varney Ch. 2) |
|---|---|---|---|
| Magnetic field | Gordeyev integral over gyro-orbits; adds a gyro line; plasma line moves toward upper hybrid | aspect angles away from $\perp\mathbf{B}$ are close to the unmagnetized case; near $\perp\mathbf{B}$ the ion line collapses to a narrow spike | Farley et al. 1961; Fejer 1961; Hagfors 1961; Salpeter 1961 |
| Ion–neutral collisions | collisional (BGK/Fokker–Planck) $\chi$ | ion line becomes Lorentzian in the D region; minor in the F region | Dougherty & Farley 1963; Tanenbaum 1968; Hagfors & Brockelman 1971 |
| Coulomb collisions near $\perp\mathbf{B}$ | test-particle simulation of orbits | Jicamarca $T_e/T_i$ anomaly (Pingree 1990) resolved | Sulzer & González 1999; Woodman 2004; Kudeki & Milla 2011; Milla & Kudeki 2011 |
| Suprathermal electrons | non-Maxwellian $f_e$ | enhanced plasma line; ion line almost unchanged | Perkins & Salpeter 1965 |

**A subtlety about total power.** The closed-form total ion-line power above, the "Salpeter/Buneman" form, comes from a static (Debye–Hückel) argument. It is exact only in thermal equilibrium. Integrating Eq. 2.23 numerically:

- it matches the closed form to five digits for $T_e = T_i$;
- for $T_e\neq T_i$ it gives slightly *more* ion-line power: about 1% at $T_e/T_i = 2$ and about 7% at $T_e/T_i = 4$ (for $k\lambda_{De} = 0.05$).

Fejer & Kohl (1980, *JGR*) titled their paper "an analytical result and a clarification" of the total cross-section versus $T_e/T_i$. I read only its abstract, which says the result holds for large temperature ratios and small Debye-length-to-wavelength ratios. **For quantitative work, fit the full spectrum** rather than using the closed form. Analysis codes do this.

---

## What we assumed, and where it breaks

- **Stable plasma.** Unstable waves (two-stream, NEIALs) give *coherent* echoes that are orders of magnitude above thermal ([[NEIALs]], [[Akbari 2014 NEIAL Aspect Angle]]).
- **Maxwellian, unmagnetized, collisionless species** in the boxed $\chi_s$. Use the generalized $\chi_s$ (§4) as needed.
- **Statistical stationarity** over the integration time. Turning the spectrum into measured lag products with finite pulses is a separate estimation problem; see [[Varney 2021 ISR Probability]].

---

## Verification

- **Sources agree.**
  - Spectrum formula, susceptibilities and physical interpretation: [[Varney 2012 Thesis|Varney 2012]] §2.1.1, Eqs. 2.1–2.27, Figs. 2.1–2.2.
  - Independent implementation with the same structure: ISRSpectrum (Swoboda; after Kudeki & Milla 2011). Code inspected via GitHub, 2026-10-07.
  - Susceptibility and Landau-damping physics: [[Bellan 2006 Fundamentals of Plasma Physics|Bellan]] §5.2.
- **SymPy.** The dressed-particle relation $n_e = [(1+\chi_i)n_{te}+\chi_en_{ti}]/(1+\chi_e+\chi_i)$ follows from linear response plus Poisson.
- **Numerical.**
  - The fluctuation–dissipation identity $2Nk^2\lambda_D^2\mathrm{Im}\chi/\omega = (2\pi N/k)\hat f(\omega/k)$ holds to 6 digits.
  - Varney's Fig. 2.1 peak positions are reproduced ($\theta_i = 0.96$, 1.46, 1.73, 1.91).
  - The large-$k\lambda_D$ limit tends to the free-electron Gaussian (within 0.4% at $k\lambda_D = 20$).
  - Integrated power matches the equilibrium form exactly for $T_e = T_i$ (e.g. 0.50980 vs 0.50980 at $k\lambda_D = 0.2$), with the $T_e\neq T_i$ deviations noted in §4.
  - RISR-N Bragg scale, $k\lambda_{De}$ and ion-line frequencies were computed.
- **Not checked directly:** Kudeki & Milla (2011) is paywalled, and Fejer & Kohl (1980) was seen only as an abstract.

## Sources

- [[Varney 2012 Thesis]] — Ch. 2.1 (ISR theory, Swartz–Farley admittance formulation, multi-ion spectra, review of magnetized and collisional theories)
- [[Bellan 2006 Fundamentals of Plasma Physics]] — Ch. 5 (susceptibility, plasma dispersion function, ion-acoustic Landau damping)
- [[Bahcivan 2010 Initial RISR-N Observations]] — RISR-N frequency
- [[Varney 2021 ISR Probability]] — statistical estimation of ISR parameters (next step after the spectrum)
- Kudeki, E., and M. A. Milla (2011), Incoherent scatter spectral theories—Part I, *IEEE Trans. Geosci. Remote Sens.*, 49(1), 315–328, doi:10.1109/TGRS.2010.2057252 (not in vault; paywalled)
- Swoboda, J., ISRSpectrum (Python, MIT license), https://github.com/jswoboda/ISRSpectrum — independent implementation
- Fejer, J. A., and H. Kohl (1980), The total cross section for incoherent scattering: an analytical result and a clarification, *J. Geophys. Res.* (abstract seen via search only; volume, page and DOI not verified)
