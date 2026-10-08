---
type: derivation
status: draft
updated: 2026-10-07
sources: 3
tags: [derivations, kinetic-theory, plasma-waves, wave-particle-interactions, landau-damping]
prerequisites: "[[Moment Equations from the Vlasov Equation]] §1; [[Debye Shielding and the Plasma Frequency]]"
next: "[[Quasilinear Diffusion]]"
---

# Landau Damping

**Part I (kinetic extension)** of the [[Derivations Index]] · Prerequisites: [[Moment Equations from the Vlasov Equation]], [[Debye Shielding and the Plasma Frequency]] · Next: [[Quasilinear Diffusion]]

## Where we're going

Here's a genuine puzzle. A collisionless plasma has no friction: the Vlasov equation is time-reversible and conserves entropy. Yet an electron plasma wave launched into it **dies away**. Where does the energy go?

Landau's answer (Landau 1946) is that it goes into the small population of particles moving at nearly the wave's phase speed, the **resonant particles**. Slightly slower ones get pushed forward by the wave and take energy from it. Slightly faster ones push on the wave and give energy back. For a Maxwellian there are always more slow particles than fast ones at any $v>0$, so the wave loses on net.

This is the foundational wave–particle interaction. The same physics, with Doppler-shifted cyclotron resonances, is how chorus and EMIC waves scatter radiation-belt particles ([[Wave-Particle Interactions]]), how kinetic Alfvén waves accelerate auroral electrons ([[Alfvén Waves]]), and how ion Landau damping shapes the incoherent-scatter ion line ([[Incoherent Scatter Spectrum]]). The fluid equations can't see it: moments average it away ([[Moment Equations from the Vlasov Equation]] §5).

---

## 1. Linearize Vlasov–Poisson

Take the simplest setting: 1-D, electrostatic, mobile electrons on a fixed uniform ion background. Split the electron distribution into equilibrium plus perturbation, $f = n_0\hat f_0(v) + f_1$ with $\int\hat f_0\,dv = 1$, and let $f_1, E_1 \propto e^{i(kx-\omega t)}$. The linearized Vlasov equation,

$$\frac{\partial f_1}{\partial t} + v\frac{\partial f_1}{\partial x} - \frac{e}{m}E_1\,n_0\hat f_0' = 0,$$

gives

$$f_1 = \frac{i\,e\,n_0}{m}\,\frac{\hat f_0'(v)}{\omega - kv}\,E_1.$$

Poisson's equation, $ikE_1 = -(e/\varepsilon_0)\int f_1\,dv$, then requires

$$\boxed{D(k,\omega) \equiv 1 - \frac{\omega_{pe}^2}{k^2}\int_{-\infty}^{\infty}\frac{\hat f_0'(v)}{v - \omega/k}\,dv = 0}$$

(using $1/(\omega - kv) = -k^{-1}/(v - \omega/k)$). This is the dispersion relation, and it has an obvious problem: the integrand blows up at $v = \omega/k$, exactly at the resonant particles.

---

## 2. Landau's prescription: causality picks the contour

Vlasov (1945) took the principal value and found undamped waves. Landau argued that the question itself was posed wrongly. A wave isn't an eternal Fourier mode; it's the response to a disturbance switched on at $t=0$. So solve the *initial-value* problem with a Laplace transform in time. The transform converges only for $\mathrm{Im}\,\omega > 0$, and there the pole $v = \omega/k$ lies **above** the real $v$ axis, so the integral is perfectly fine. To continue the answer to physical, damped values ($\mathrm{Im}\,\omega \le 0$), the $v$ contour must be deformed to pass **below** the pole ([[Bellan 2006 Fundamentals of Plasma Physics|Bellan]] §5.2, Fig. 5.4). For a weakly damped wave with $k>0$, this gives

$$\int\frac{\hat f_0'}{v - \omega/k}\,dv \;\longrightarrow\; \mathcal{P}\!\!\int\frac{\hat f_0'}{v - \omega/k}\,dv + i\pi\,\hat f_0'\!\left(\frac{\omega}{k}\right).$$

That extra $i\pi\hat f_0'$ is the whole effect. It comes purely from causality, with no collisions anywhere. The long-time behavior is then set by the root of $D$ with the largest imaginary part. Other solutions (the initial "ballistic" free streaming) phase-mix away.

---

## 3. Weakly damped Langmuir waves

Write $\omega = \omega_r + i\gamma$ with $|\gamma|\ll\omega_r$, and split $D = D_r + iD_i$. Taylor-expanding around $\omega_r$ gives two conditions:

$$D_r(\omega_r) = 0, \qquad \gamma = -\frac{D_i(\omega_r)}{\partial D_r/\partial\omega|_{\omega_r}}.$$

**Real part.** For a fast wave ($\omega/k\gg v_t$), expand $1/(v-\omega/k)$ in powers of $kv/\omega$ and integrate by parts. With $v_t^2 = k_BT_e/m_e$,

$$D_r \approx 1 - \frac{\omega_{pe}^2}{\omega^2}\left(1 + \frac{3k^2v_t^2}{\omega^2}+\dots\right) \quad\Longrightarrow\quad \omega_r^2 \approx \omega_{pe}^2 + 3k^2v_t^2 = \omega_{pe}^2\left(1+3k^2\lambda_D^2\right).$$

This is the Bohm–Gross relation: the thermal correction to [[Debye Shielding and the Plasma Frequency|the plasma frequency]]. The fluid theory got it too, but only with the right adiabatic index.

**Imaginary part.** $D_i = -\pi(\omega_{pe}^2/k^2)\,\hat f_0'(\omega_r/k)$, and $\partial D_r/\partial\omega\approx2\omega_{pe}^2/\omega_r^3$. So

$$\boxed{\gamma = \frac{\pi}{2}\,\frac{\omega_r^3}{k^2}\,\hat f_0'\!\left(\frac{\omega_r}{k}\right)}$$

**This is the general result, and it's worth pausing on.** The sign of $\gamma$ is the sign of the *slope* of the distribution at the phase velocity:

- $\hat f_0' < 0$ (every Maxwellian, for $v>0$): damping.
- $\hat f_0' > 0$ (a beam or bump on the tail): **growth**. This is the bump-on-tail instability, and the same formula describes both.

**Maxwellian.** With $\hat f_0 = (2\pi v_t^2)^{-1/2}e^{-v^2/2v_t^2}$, $\hat f_0'(v) = -v\,\hat f_0/v_t^2$. Set $\omega_r\approx\omega_{pe}$ in the prefactor and keep the full $\omega_r$ in the exponent:

$$\boxed{\gamma \approx -\sqrt{\frac{\pi}{8}}\,\frac{\omega_{pe}}{(k\lambda_D)^3}\exp\!\left(-\frac{1}{2k^2\lambda_D^2} - \frac32\right)}$$

This is Bellan's Eq. 5.85. The $-\tfrac32$ comes from $\omega_r^2/(2k^2v_t^2) = 1/(2k^2\lambda_D^2) + \tfrac32$. The damping is **exponentially weak** for long waves ($k\lambda_D\ll1$): their phase speed sits far out on the Maxwellian tail where there are almost no resonant particles. As $k\lambda_D\to$ a few tenths, the phase speed drops into the bulk and the wave dies in a few oscillations. That's why Langmuir waves with wavelengths below about $10\lambda_D$ effectively don't exist.

---

## 4. Why textbook formulas differ, and which is right

You'll see at least three versions in print:

1. **Bellan's form** (above), with the $e^{-3/2}$.
2. **The same, without $e^{-3/2}$**: $\gamma = -\sqrt{\pi/8}\,\omega_{pe}(k\lambda_D)^{-3}e^{-1/2k^2\lambda_D^2}$. This uses $\omega_{pe}$ instead of $\omega_r$ in the exponent. It is common in numerical-methods papers (e.g. Finn et al. 2023; see Sources).
3. **Different thermal-speed conventions.** With $v_{th}^2 = 2k_BT/m$, the same result reads $\propto(\omega_{pe}/kv_{th})^3$ with different numerical prefactors. A prefactor written as "0.22" is $e^{-3/2}\approx0.223$ in disguise.

These aren't different physics. They're different *approximations* to the root of the exact dispersion relation. For a Maxwellian, the exact relation is

$$1 + \frac{1}{k^2\lambda_D^2}\left[1 + \zeta Z(\zeta)\right] = 0, \qquad \zeta = \frac{\omega}{\sqrt2\,kv_t},$$

where $Z$ is the Fried–Conte plasma dispersion function (Bellan Eqs. 5.65–5.67). Solving it numerically shows which approximation to trust:

| $k\lambda_D$ | exact $\omega_r/\omega_{pe}$ | exact $\gamma/\omega_{pe}$ | form 1 (with $e^{-3/2}$) | form 2 (without) |
|---|---|---|---|---|
| 0.2 | 1.0640 | $-5.5\times10^{-5}$ | $-6.5\times10^{-5}$ | $-2.9\times10^{-4}$ |
| 0.3 | 1.1599 | $-1.26\times10^{-2}$ | $-2.0\times10^{-2}$ | $-9.0\times10^{-2}$ |
| 0.4 | 1.2851 | $-6.6\times10^{-2}$ | $-9.6\times10^{-2}$ | $-0.43$ |
| 0.5 | 1.4157 | $-0.153$ | $-0.151$ | $-0.68$ |

**Verdict:** keep the $e^{-3/2}$. It's within tens of percent where damping is weak; dropping it overestimates damping by a factor of 5–7. Beyond $k\lambda_D\approx0.4$ neither expansion is reliable (the agreement at 0.5 is partly coincidence), so use the exact $Z$-function root.

---

## 5. Where did the energy go?

No energy is lost; it moves from the wave into the resonant particles. Bellan (§3.8, §5.2.7) checks this explicitly. The power the wave loses equals the power gained by near-resonant particles, *provided* you remember that half the wave's energy is in coherent particle sloshing, not in $\varepsilon_0E^2$. The distribution near $v = \omega/k$ gets flattened. Following that flattening self-consistently is the job of [[Quasilinear Diffusion]], and it ends with a plateau where $\hat f_0' = 0$ and damping stops.

Landau damping was confirmed experimentally by Malmberg & Wharton (1964), as Bellan notes.

---

## 6. Ion-acoustic waves: the $T_e/T_i$ dependence

The same machinery applies when $v_{ti}\ll\omega/k\ll v_{te}$. Electrons respond isothermally (they shield), ions respond dynamically, and the result is the ion-acoustic wave, $\omega_r^2\approx k^2c_s^2/(1+k^2\lambda_{De}^2) + 3k^2k_BT_i/m_i$. Its damping has two pieces (Bellan §5.2.8):

- a small electron part, since electrons see a nearly flat $\hat f_0$ at $v\approx c_s\ll v_{te}$;
- an ion part $\propto\exp(-\omega^2/2k^2v_{ti}^2)\sim\exp(-T_e/2T_i - \tfrac32)$.

When $T_e\lesssim T_i$, ion Landau damping is **strong** and the ion-acoustic wave barely exists. When $T_e\gg T_i$, it's weak. That single fact sets the shape of the incoherent-scatter ion line, which is how [[RISR-N]] measures $T_e/T_i$. See [[Incoherent Scatter Spectrum]].

---

## What we assumed, and where it breaks

- **Linear theory.** If the wave is strong enough to trap resonant particles before it damps (bounce frequency $\omega_b = \sqrt{ekE/m}\gtrsim|\gamma|$), the damping stops and oscillates: nonlinear Landau damping (O'Neil 1965).
- **1-D, unmagnetized, electrostatic.** In a magnetized plasma the resonance generalizes to $\omega - k_\parallel v_\parallel = n\Omega$. The $n=0$ case is Landau (and transit-time) resonance; $n\neq0$ are cyclotron resonances.
- **Smooth $\hat f_0$.** Real distributions with beams or loss cones can make $\gamma>0$, giving instability.

---

## Verification

- **Sources agree.**
  - Dispersion relation, Landau contour, weak-damping expansion and the $e^{-3/2}$ form: [[Bellan 2006 Fundamentals of Plasma Physics|Bellan]] §5.2, Eqs. 5.65–5.85.
  - Ion-acoustic damping: Bellan §5.2.8.
  - The standard weak-damping formula with and without $e^{-3/2}$ is confirmed in the published literature (web search, 2026-10-07; see Sources).
  - Collective effects, Vlasov and Landau damping are also covered in [[Thorne 1993 AOS 250B Course Reader|Thorne 1993]] Ch. 3 (syllabus confirmed; detailed equations not yet read).
- **Numerical.**
  - Solved the exact Maxwellian dispersion relation with $Z(\zeta) = i\sqrt\pi\,w(\zeta)$ (Faddeeva function). The root at $k\lambda_D = 0.5$, $\omega/\omega_{pe} = 1.4157 - 0.1534i$, matches the standard tabulated value.
  - Built the comparison table above from those roots.
  - Checked the large-argument asymptotic expansion of $Z$ used in §3.
- **By hand:** signs of $D_i$ and $\gamma$; the bump-on-tail sign reversal.

## Sources

- [[Bellan 2006 Fundamentals of Plasma Physics]] — Ch. 5 (Landau problem, plasma dispersion function, Langmuir and ion-acoustic damping, power balance)
- [[Thorne 1993 AOS 250B Course Reader]] — Ch. 3 (collective effects, Vlasov, Landau damping)
- Finn, D. S., M. G. Knepley, J. V. Pusztay, M. F. Adams (2023), "A Numerical Study of Landau Damping with PETSc-PIC," [arXiv:2303.12620](https://arxiv.org/abs/2303.12620). The abstract notes that simple approximations to the dispersion relation are inadequate for the damping rate, consistent with §4. Its use of the no-$e^{-3/2}$ form is per a search summary; the equation itself was not checked.
- Landau, L. D. (1946), *J. Phys. USSR* 10, 25 — original. Not in vault; cited via Bellan.
- Malmberg & Wharton (1964) — experimental confirmation. Not in vault; cited via Bellan.
- O'Neil, T. (1965), *Phys. Fluids* 8, 2255 — nonlinear Landau damping (standard reference; not in vault).
