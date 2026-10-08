---
type: derivation
status: draft
updated: 2026-10-07
sources: 3
tags: [derivations, kinetic-theory, wave-particle-interactions, quasilinear-theory, pitch-angle-diffusion, radiation-belts]
prerequisites: "[[Landau Damping]]; [[Adiabatic Invariants and Magnetic Mirrors]]"
next: "[[Kennel-Petschek Limit]]"
---

# Quasilinear Diffusion

**Part I (kinetic extension)** of the [[Derivations Index]] · Previous: [[Landau Damping]] · Next: [[Kennel-Petschek Limit]]

## Where we're going

[[Landau Damping|Landau theory]] tells us how a *fixed* distribution damps or grows waves. But energy goes somewhere, so the distribution can't stay fixed. **Quasilinear (QL) theory** closes the loop:

- Waves cause the resonant particles to **diffuse in velocity space**.
- That diffusion changes the slope $\partial f/\partial v$.
- The slope sets the wave growth or damping.

The endpoint is a **plateau**, a flattened distribution that neither grows nor damps waves.

In the magnetosphere the same idea, with cyclotron resonances, becomes **pitch-angle diffusion**. It is the standard description of how chorus, hiss and EMIC waves empty the [[Radiation Belts]] into the atmosphere ([[Wave-Particle Interactions]]). It is also the engine behind the [[Kennel-Petschek Limit]].

---

## 1. The 1-D electrostatic derivation

Follow [[Bellan 2006 Fundamentals of Plasma Physics|Bellan]] §14.2: 1-D, unmagnetized, electrons only, fixed ions. Split the distribution into a slowly evolving, spatially uniform part and wave-like perturbations:

$$f(x,v,t) = f_0(v,t) + f_1(x,v,t) + f_2 + \cdots,\qquad f_n\sim\epsilon^n.$$

Substitute into the Vlasov equation and **spatially average**, writing $\langle\cdot\rangle$ for the average over $x$. Every wave quantity averages to zero, $\langle f_1\rangle = \langle E_1\rangle = 0$, and the only survivors are

$$\frac{\partial f_0}{\partial t} = \frac{e}{m}\frac{\partial}{\partial v}\left\langle E_1f_1\right\rangle + O(\epsilon^3).$$

That's the **quasilinear postulate**: keep the lowest nonlinear term, the correlation of two first-order quantities, and drop everything higher. So $f_0$ evolves at order $\epsilon^2$, slowly compared with the waves.

To evaluate $\langle E_1f_1\rangle$, use the *linear* relation between $f_1$ and $E_1$ (the same one used for [[Landau Damping]]):

$$\tilde f_1(k,v) = \frac{ie}{m}\,\tilde E_1(k)\,\frac{\partial f_0/\partial v}{\omega(k) - kv}.$$

Fourier-decompose, average over $x$ (which pairs $k$ with $-k$), and use the reality conditions $\tilde E_1(-k) = \tilde E_1^*(k)$ and $\omega(-k) = -\omega^*(k)$. The real and imaginary parts of $\omega$ are odd and even in $k$, respectively. The result is a diffusion equation in velocity:

$$\boxed{\frac{\partial f_0}{\partial t} = \frac{\partial}{\partial v}\left(D_{QL}\frac{\partial f_0}{\partial v}\right),\qquad D_{QL} = \frac{e^2}{\varepsilon_0m^2}\int dk\,\frac{2\omega_i(k)\,\mathcal{E}(k,t)}{\left[\omega_r(k)-kv\right]^2+\omega_i^2(k)}}$$

Here $\mathcal{E}(k,t)$ is the electric-field energy per unit $k$, which grows or decays as $\partial\mathcal{E}/\partial t = 2\omega_i\mathcal{E}$, with $\omega_i$ from the instantaneous [[Landau Damping|Landau formula]] (Bellan Eqs. 14.35–14.39).

**The resonant limit.** When the damping or growth is weak, the Lorentzian in $D_{QL}$ becomes a delta function, and only particles with $v = \omega_r/k$ diffuse:

$$D_{\text{res}}(v) = \frac{2\pi e^2}{\varepsilon_0m^2}\int dk\,\mathcal{E}(k)\,\delta\!\left(\omega_r(k) - kv\right).$$

> *A subtlety.* Taken literally, the Lorentzian gives $2\pi\,\mathrm{sgn}(\omega_i)\,\delta$, as if damped waves "anti-diffused" particles. The physically correct resonant coefficient is positive whether the waves grow or damp. It is fixed by Landau's causal prescription, and checked below by energy conservation: with a positive $D_{\text{res}}$, the energy lost by damping waves exactly equals the energy gained by resonant particles. Bellan's derivation is cleanest for growing modes, so carry it over to damped ones with this sign in mind.

**Two pieces of physics in one equation:**

- **Resonant particles** diffuse and flatten $f_0$ where $v\approx\omega/k$. Flattening drives $\partial f_0/\partial v\to0$, so $\omega_i\to0$, and the waves stop growing or damping. That is the **plateau** (Bellan Fig. 14.1).
- **Nonresonant particles** respond reversibly (the off-resonance part of $D_{QL}$). This is the "sloshing" energy that makes a Langmuir wave's total energy **twice** its electric-field energy.

---

## 2. Conservation laws, and a numerical check

Because the right side is a velocity divergence, particles are conserved automatically. Using the linear dispersion relation, Bellan shows that momentum is conserved (particles plus waves). Energy is also conserved, *provided* the wave energy is counted correctly. For Langmuir waves that means $W_{\text{wave}} = 2\int\mathcal{E}\,dk$.

**Numerical test.** I integrated the resonant QL system for a bump-on-tail distribution, using a Maxwellian core plus a 5% beam at $5v_t$, units $\omega_{pe} = v_t = 1$, Landau $\omega_i(k)$ updated self-consistently, and implicit diffusion. The results:

| | Initial | Final ($t = 3000\,\omega_{pe}^{-1}$) |
|---|---|---|
| Max positive slope in resonant band | 0.0187 | 0.0026 (plateau forming) |
| Max growth rate | 0.54 | 0.10, still falling |
| Particle number error | — | $10^{-14}$ |
| Momentum and energy error (particles + waves) | — | $5\times10^{-4}$ (time-splitting) |
| Energy released by particles vs $2\times$(final field energy) | — | 0.0768 vs 0.0762 (0.8%) |

The wave energy saturated: it changed by 0.1% between $t = 1000$ and $2000\,\omega_{pe}^{-1}$. The factor of 2 between particle energy and field energy, Bellan's "half the wave energy is in coherent particle motion," is confirmed directly.

---

## 3. Magnetized plasmas: cyclotron resonance and pitch-angle diffusion

In a magnetized plasma, a particle resonates with a wave when the wave's Doppler-shifted frequency is a harmonic of its gyrofrequency:

$$\omega - k_\parallel v_\parallel = n\,\frac{\Omega}{\gamma},\qquad n = 0,\pm1,\pm2,\ldots$$

- $n = 0$ is Landau (transit-time) resonance.
- $n = \pm1$ are the cyclotron resonances that dominate radiation-belt scattering.

[[Thorne 1993 AOS 250B Course Reader|Thorne]] (§7, Eqs. 7.26–7.31) shows why. Go to the frame moving at $\omega/k_\parallel$, where the wave is static. The parallel equation of motion picks up a secular (non-averaging) term only when $k_\parallel z = N\Omega t$. Higher harmonics contribute through $J_N(k_\perp\rho)$, which is small for small $k_\perp\rho$, so $N = \pm1$ dominates.

**Which way do particles diffuse?** In that wave frame the field is purely magnetic, so *particle energy is conserved there*:

$$v_\perp^2 + \left(v_\parallel - \frac{\omega}{k_\parallel}\right)^2 = \text{const}.$$

Diffusion is therefore along circles centered on the parallel phase velocity. For low-frequency waves ($\omega\ll\Omega$, so $\omega/k_\parallel\ll v$), those circles are almost constant-energy surfaces, and the scattering is **almost pure pitch-angle diffusion**. Thorne gets the same result from a quantum picture, emitting a quantum $\hbar\omega$ with momentum $\hbar k$ (his Eqs. 7.5–7.6): $\Delta E_\perp/\Delta E_\parallel = -1/(1 - \omega/\Omega)\approx-1$.

Particles that *give* energy to the wave ($\Delta E<0$) are scattered *toward* the loss cone. That's the instability-driven precipitation underlying the [[Kennel-Petschek Limit]].

**The bounce-averaged equation.** Average the pitch-angle diffusion equation over a bounce and express it with the equatorial pitch angle $\alpha_0$ (Lyons, Thorne & Kennel 1972, as given by Thorne Eq. 7.18):

$$\boxed{\frac{\partial f_0}{\partial t} = \frac{1}{T(\alpha_0)\sin2\alpha_0}\frac{\partial}{\partial\alpha_0}\left(T(\alpha_0)\sin2\alpha_0\,\langle D_{\alpha_0\alpha_0}\rangle\frac{\partial f_0}{\partial\alpha_0}\right) - \frac{f_0}{\tau_{\text{loss}}}}$$

Here $T(\alpha_0)\approx1.30 - 0.56\sin\alpha_0$ is the bounce-period function from [[Adiabatic Invariants and Magnetic Mirrors]] §3. The factor $\sin2\alpha_0\,T(\alpha_0)$ is the phase-space Jacobian of the bounce-averaged coordinates.

### Weak vs strong diffusion

Particles inside the loss cone are removed in about a quarter-bounce time $T_B$. The competition between scattering and that loss defines two regimes (Thorne Eqs. 7.9–7.17; Kennel & Petschek Eqs. 4.4–4.13):

- **Weak diffusion** ($D\,T_B\ll\alpha_L^2$): the loss cone is nearly empty, and the lifetime scales as $1/D$. Particles leak out at the scattering rate.
- **Strong diffusion** ($D\,T_B\gg\alpha_L^2$): the loss cone stays full, and the lifetime bottoms out at

$$\tau_{\min}\approx\frac{2T_B}{\alpha_L^2}.$$

*Why:* an isotropic distribution has a fraction $1 - \cos\alpha_L\approx\alpha_L^2/2$ of its particles in the loss cone, and it loses them every $T_B$. With the dipole loss cone of [[Adiabatic Invariants and Magnetic Mirrors]] §2, $\alpha_L^2\approx1/(2L^3)$, so $\tau_{\min}\approx4T_BL^3$. That's Kennel & Petschek's Eq. 4.13. However hard you scatter, you can't empty the belts faster than this: it's Kennel's "leaky bucket" (Kennel 1969, as described by Thorne).

---

## What we assumed, and where it breaks

- **Random phases and a broad spectrum.** QL assumes the resonant particles see many incoherent waves. Coherent, large-amplitude chorus elements trap particles (when the trapping frequency exceeds the inverse resonance time), and diffusion is replaced by nonlinear phase trapping and bunching. Summers et al. 2009 flag this as an open problem.
- **Weak turbulence**, with $D$ from linear orbits. This breaks when wave amplitudes become large.
- **Separation of timescales**, which justifies bounce averaging.
- **Energy diffusion neglected** in the pure pitch-angle form. That's fine for $\omega\ll\Omega$; above it, cross terms $D_{\alpha E}$ matter (Thorne Eq. 7.4).

---

## Verification

- **Sources agree.**
  - 1-D QL equation, coefficient and conservation laws: [[Bellan 2006 Fundamentals of Plasma Physics|Bellan]] §14.2 (Eqs. 14.3–14.51).
  - Cyclotron resonance, wave-frame diffusion surfaces, Fokker–Planck pitch-angle diffusion, bounce averaging, weak and strong limits: [[Thorne 1993 AOS 250B Course Reader|Thorne]] Ch. 7 (Eqs. 7.1–7.31).
  - Same lifetimes: [[Kennel 1966 Limit Stably Trapped Fluxes|Kennel & Petschek 1966]] §4.2 (Eqs. 4.4–4.13).
- **Analytic (by hand).** The resonant-coefficient normalization $2\pi e^2/(\varepsilon_0m^2)$ was derived independently by requiring particle-plus-wave energy and momentum conservation with Landau $\omega_i$. It matches the resonant limit of Bellan's Eq. 14.38.
- **Numerical.**
  - QL bump-on-tail integration: plateau formation, conservation and the factor-of-2 wave energy (§2 table).
  - Direct numerical solution of the steady pitch-angle diffusion problem: reproduces Kennel & Petschek's lifetime formula (Eq. 4.11) to within 0.2% over $D^*T_B = 10^{-6}$ to $10$, including both the weak and strong limits.
  - $1 - \cos\alpha_L\approx\alpha_L^2/2$ checked.

## Sources

- [[Bellan 2006 Fundamentals of Plasma Physics]] — §14.2 (quasilinear velocity-space diffusion, conservation laws)
- [[Thorne 1993 AOS 250B Course Reader]] — Ch. 6–7 (resonance conditions, Fokker–Planck pitch-angle diffusion, bounce averaging, weak and strong diffusion, leaky bucket)
- [[Kennel 1966 Limit Stably Trapped Fluxes]] — §4 (diffusion equilibrium with a loss cone; lifetimes)
- [[Summers 2009 Relativistic KP Limit]] — §5 (limits of QL / KP; nonlinear trapping)
