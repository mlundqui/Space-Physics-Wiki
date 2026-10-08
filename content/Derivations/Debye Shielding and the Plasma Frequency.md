---
type: derivation
status: draft
updated: 2026-10-07
sources: 4
tags: [derivations, plasma-foundations, debye-length, plasma-frequency]
prerequisites: "Gauss's law, charge continuity, Boltzmann factor"
next: "[[Guiding-Center Drifts]]"
---

# Debye Shielding and the Plasma Frequency

**Part I, page 1** of the [[Derivations Index]] · Next: [[Guiding-Center Drifts]]

## Where we're going

What makes an ionized gas a *plasma*, rather than just a hot gas that happens to contain charges? Two collective behaviors:

1. It **shields** any local charge imbalance over a characteristic length, the **Debye length** $\lambda_D$.
2. If you do disturb its neutrality, it **rings** at a characteristic frequency, the **plasma frequency** $\omega_p$.

These are really one fact seen two ways: in space and in time. We'll derive both, and then see that $\lambda_D\,\omega_{pe}$ is just the electron thermal speed.

---

## 1. The plasma frequency

Start with the simplest plasma imaginable. It's cold (no thermal motion), unmagnetized and uniform, with background density $n_0$ for each species. Now give it a small electric field $\mathbf{E}$ and ask how it responds. For a cold plasma every particle of species $s$ moves with the same velocity $\mathbf{v}_s$, so Newton's law for each species reads

$$m_s\frac{\partial \mathbf{v}_s}{\partial t} = q_s\mathbf{E}.$$

I've quietly dropped two things here: the advective term $(\mathbf{v}_s\cdot\nabla)\mathbf{v}_s$ and the magnetic force. Both are products of two small quantities (velocity times velocity, velocity times wave field), so they're second order. This is **linearization**, and we'll use the same move in every wave derivation in this series.

The current density is $\mathbf{j} = \sum_s n_0 q_s \mathbf{v}_s$. Differentiate it in time and use the equation above:

$$\frac{\partial \mathbf{j}}{\partial t} = \sum_s \frac{n_0 q_s^2}{m_s}\,\mathbf{E}.$$

Notice the $q_s^2$: electrons and ions both push current in the direction of $\mathbf{E}$, whatever their sign. Now take the divergence of both sides. On the left, charge continuity gives $\nabla\cdot\mathbf{j} = -\partial\rho_q/\partial t$. On the right, Gauss's law gives $\nabla\cdot\mathbf{E} = \rho_q/\varepsilon_0$. So

$$\frac{\partial^2 \rho_q}{\partial t^2} = -\left(\sum_s \frac{n_0 q_s^2}{\varepsilon_0 m_s}\right)\rho_q \equiv -\omega_p^2\,\rho_q.$$

That's a simple harmonic oscillator for the charge density. Any charge imbalance oscillates at

$$\boxed{\omega_p^2 = \sum_s \omega_{ps}^2, \qquad \omega_{ps}^2 = \frac{n_s q_s^2}{\varepsilon_0 m_s}}$$

Because $m_i/m_e \geq 1836$, the ion term is tiny and $\omega_p \approx \omega_{pe}$. The physical picture: displace the electrons slightly, and the exposed ion charge pulls them back. They overshoot because they have inertia, and the cycle repeats. The ions are too heavy to take part on this timescale.

> **Why the $q^2/m$ scaling makes sense.** The restoring field is proportional to the displaced charge, $\propto q$. The force on each particle from that field brings another factor of $q$. The acceleration divides by $m$. Heavier particles ring more slowly; more of them (larger $n$) means a stiffer spring.

A useful number: $f_{pe} = \omega_{pe}/2\pi \approx 8.98\sqrt{n_e}$ Hz with $n_e$ in m$^{-3}$. This is the same 8.98 that appears in the ionosonde relation $f_oF_2 \approx 8.98\sqrt{N_mF_2}$. An HF wave below $f_{pe}$ cannot propagate, and that is what reflects it (see [[HF Radio Propagation]], [[F-Layer]]).

---

## 2. Debye shielding

Now let's ask a static question. Drop a test charge $Q$ into the plasma at the origin. Far from the plasma, its potential would be the bare Coulomb $Q/4\pi\varepsilon_0 r$. What does the plasma do to it?

The plasma particles rearrange themselves. If $Q > 0$, electrons crowd in and ions are pushed away, and the excess negative charge partly cancels $Q$. To find out by how much, we need each species' density in the presence of a potential $\phi(\mathbf{r})$.

**The density response.** Assume each species is in thermal equilibrium at temperature $T_s$. Then its density follows the Boltzmann factor

$$n_s(\mathbf{r}) = n_0\exp\!\left(-\frac{q_s\phi}{k_BT_s}\right),$$

with $\phi \to 0$ and $n_s \to n_0$ far away.

[[Strangeway Ch3 Physics of Magnetized Plasmas|Strangeway (Ch. 3)]] reaches the same result more carefully. Liouville's theorem says phase-space density is conserved along orbits. So a Maxwellian at infinity maps onto a Maxwellian everywhere, scaled by $e^{-q_s\phi/k_BT_s}$, because energy $\tfrac12mv^2 + q_s\phi$ is conserved. Integrate over velocity and you recover the Boltzmann factor. Both arguments give the same density.

**Linearize.** Far enough from the test charge, $|q_s\phi| \ll k_BT_s$, so expand $e^{-x}\approx 1-x$:

$$\rho_q = \sum_s q_s n_s \approx \underbrace{\sum_s q_s n_0}_{=\,0\ \text{(neutral background)}} - \sum_s \frac{n_0 q_s^2}{k_BT_s}\,\phi.$$

The $q_s^2$ appears again, for the same reason as before: every species responds so as to oppose the potential.

**Poisson's equation.** Including the test charge, $\nabla^2\phi = -[Q\delta^3(\mathbf{r}) + \rho_q]/\varepsilon_0$, so

$$\nabla^2\phi - \frac{\phi}{\lambda_D^2} = -\frac{Q}{\varepsilon_0}\delta^3(\mathbf{r}), \qquad \frac{1}{\lambda_D^2} = \sum_s\frac{n_0q_s^2}{\varepsilon_0k_BT_s}.$$

Away from the origin, and in spherical symmetry, this is $\frac{1}{r^2}\frac{d}{dr}\left(r^2\frac{d\phi}{dr}\right) = \phi/\lambda_D^2$. You can check by direct substitution that the solution which matches Coulomb as $r\to0$ and vanishes as $r\to\infty$ is

$$\boxed{\phi(r) = \frac{Q}{4\pi\varepsilon_0 r}\,e^{-r/\lambda_D}}$$

That's the bare Coulomb potential cut off exponentially beyond $\lambda_D$. A charge in a plasma is invisible from more than a few Debye lengths away.

For a single species, or for electrons alone,

$$\boxed{\lambda_{D} = \left(\frac{\varepsilon_0k_BT_e}{n_e e^2}\right)^{1/2}}$$

With several species, the inverse squares add, $\lambda_D^{-2} = \lambda_{De}^{-2} + \lambda_{Di}^{-2}$, so the *shortest* Debye length wins.

> **A caution about the ions.** Including the ions in $\lambda_D$ assumes they have had time to reach the Boltzmann distribution. Strangeway's Eq. 3.81 keeps both species. Many treatments keep only the electrons, because when the test charge is moving or the disturbance is fast, the ions can't respond in time. Use $\lambda_{De}$ for fast phenomena (for example, the electron response in incoherent scatter) and the combined form for genuinely static shielding.

---

## 3. One fact, two faces: $\lambda_D\,\omega_{pe} = v_{th}$

Multiply the two results:

$$\lambda_{De}\,\omega_{pe} = \sqrt{\frac{\varepsilon_0k_BT_e}{n_e e^2}}\sqrt{\frac{n_e e^2}{\varepsilon_0m_e}} = \sqrt{\frac{k_BT_e}{m_e}} \equiv v_{th,e}.$$

The densities and charges all cancel, which is a strong hint that something simple is going on. A thermal electron travels about one Debye length in about one plasma period ($1/\omega_{pe}$). Shielding is the electrons rushing to cover a charge, and they can only do it as fast as they move. So $\lambda_D$ is just "how far an electron gets in the time it takes to respond." Strangeway writes the same relation as $\lambda_D = v_T/(\sqrt2\,\omega_p)$. The $\sqrt2$ is because he defines the thermal speed with $\tfrac12mv_T^2 = k_BT$. Watch for this factor whenever you compare sources.

---

## 4. When is it a plasma? The plasma parameter

The linearization in §2 assumed $|e\phi| \ll k_BT$, and the whole "cloud" picture assumes there are *many* particles in the shielding cloud. Both assumptions hold when the number of particles in a Debye sphere is large:

$$N_D = \frac{4\pi}{3}n\lambda_D^3 \gg 1.$$

This is the working definition of a plasma. When $N_D \gg 1$, collective (long-range, many-body) effects dominate over individual binary encounters. In practice this also means that collisions are weak relative to collective behavior.

---

## Sanity check: numbers

| Region | $n$ (m$^{-3}$) | $T_e$ (K) | $\lambda_D$ | $f_{pe}$ | $N_D$ |
|---|---|---|---|---|---|
| F region, ~300 km | $10^{12}$ | 2000 | 3.1 mm | 9.0 MHz | $1.2\times10^5$ |
| Plasmasphere, L ≈ 3 | $10^{9}$ | 5000 | 15 cm | 280 kHz | $1.5\times10^7$ |
| Solar wind, 1 AU | $5\times10^{6}$ | $10^5$ | 9.8 m | 20 kHz | $1.9\times10^{10}$ |
| Plasma sheet | $3\times10^{5}$ | $10^7$ | ~400 m | 4.9 kHz | ~$8\times10^{13}$ |

*(Representative values chosen for illustration. Computed with CODATA constants.)*

Two consequences for this wiki's core instruments:

- **ISR.** [[RISR-N]] transmits at 441.9 MHz ([[Bahcivan 2010 Initial RISR-N Observations]]), a wavelength of 0.68 m. A backscatter radar probes density fluctuations at half its wavelength, 0.34 m (the Bragg condition). That is about 100 times the ~3 mm F-region Debye length. The radar therefore scatters off *collective* fluctuations (shielded ion-acoustic and electron-plasma waves), not off individual electrons, which is why the spectrum carries ion temperature and composition information. See [[AMISR]].
- **Ionosondes.** $f_{pe}$ at the F2 peak is the ordinary-mode critical frequency $f_oF_2$. Measuring it gives $N_mF_2$ directly.

---

## What we assumed, and where it breaks

- **Cold plasma** (§1). Thermal pressure adds a $k^2$ term and turns the plasma oscillation into the dispersive Langmuir (Bohm–Gross) wave. That will be derived later in Part III.
- **Unmagnetized** (§1). With $\mathbf{B}$, oscillations across the field mix with gyration and give the upper-hybrid frequency.
- **Linear response**, $|q\phi| \ll k_BT$ (§2). This fails right next to the test charge. It's fine for $N_D\gg1$.
- **Thermal equilibrium** (§2). Real space plasmas are often non-Maxwellian. Solar-wind electrons, for example, have a suprathermal halo and a field-aligned strahl on top of a thermal core ([[Pierrard 2001 Solar Wind Electrons]]). The Boltzmann-factor step then fails and the effective shielding length changes. (That non-Maxwellian tails modify the shielding length is a general kinetic-theory result, not a claim from Pierrard.)

---

## Verification

- **Sources agree:** the plasma-frequency derivation (linearized cold fluid → harmonic oscillator for $\rho_q$) matches [[Strangeway Ch3 Physics of Magnetized Plasmas|Strangeway Ch. 3]] Eqs. 3.71–3.73. The Debye length and Yukawa potential match Strangeway Eqs. 3.76–3.85 and [[Bellan 2006 Fundamentals of Plasma Physics|Bellan]] §1.6. The two-species form $\lambda_D^{-2} = \lambda_{De}^{-2}+\lambda_{Di}^{-2}$ is Strangeway Eq. 3.84.
- **SymPy:** confirmed that $\phi = Qe^{-r/\lambda}/(4\pi\varepsilon_0 r)$ satisfies $r^{-2}(r^2\phi')' = \phi/\lambda^2$ for $r>0$.
- **Numerical:** confirmed $\lambda_{De}\omega_{pe} = \sqrt{k_BT_e/m_e}$ to machine precision and the 8.98 Hz coefficient (8.9787). The table values were computed in Python.

## Sources

- [[Strangeway Ch3 Physics of Magnetized Plasmas]] — §3.4.1 (plasma oscillations), §3.4.3 (Debye shielding via Liouville's theorem)
- [[Bellan 2006 Fundamentals of Plasma Physics]] — §1.6 (Debye shielding)
- [[Thorne 1993 AOS 250B Course Reader]] — Ch. 3, *Collective Effects in a Plasma* (Debye shielding, plasma oscillations)
- [[Bahcivan 2010 Initial RISR-N Observations]] — RISR-N transmit frequency (441.9 MHz)
