---
type: derivation
status: draft
updated: 2026-10-07
sources: 3
tags: [derivations, plasma-foundations, adiabatic-invariants, radiation-belts, loss-cone]
prerequisites: "[[Guiding-Center Drifts]]"
next: "[[Moment Equations from the Vlasov Equation]]"
---

# Adiabatic Invariants and Magnetic Mirrors

**Part I, page 3** of the [[Derivations Index]] · Previous: [[Guiding-Center Drifts]] · Next: [[Moment Equations from the Vlasov Equation]]

## Where we're going

A trapped radiation-belt particle does three things at once, on three wildly different clocks:

1. It **gyrates** around the field line (milliseconds or less).
2. It **bounces** between mirror points in the two hemispheres (seconds).
3. It **drifts** in longitude around the Earth (minutes to hours).

Here's the deep fact. *Whenever a motion is periodic and the system changes slowly compared to its period, the action of that motion, $\oint p\,dq$, is conserved.* Each of the three motions therefore has its own **adiabatic invariant**:

- the magnetic moment $\mu$,
- the bounce invariant $J$,
- the flux invariant $\Phi$.

These three numbers are why particles can stay trapped for years. They're also why you need *waves* to get them out. (Bellan §3.3–3.4 proves the general action theorem. Here we'll establish each invariant directly from the equation of motion, which is more physical.)

---

## 1. The first invariant: $\mu = W_\perp/B$

In [[Guiding-Center Drifts]] §4 the combination $\mu = mv_\perp^2/2B$ appeared as the magnetic moment of the gyration. Now we show it's conserved. There are two ways $B$ can change as the particle sees it: in time, or in space as the particle moves along the field. We'll do both.

### 1a. A field that grows slowly in time (betatron acceleration)

Let $B$ grow slowly. By Faraday's law, a changing flux through the gyro-orbit induces an EMF around it:

$$\oint\mathbf{E}\cdot d\boldsymbol\ell = -\frac{d}{dt}\int\mathbf{B}\cdot d\mathbf{A}.$$

Which way does that EMF push the particle? By Lenz's law it drives current that *opposes* the growing flux. The gyrating particle is already a current loop opposing $\mathbf{B}$ (plasmas are diamagnetic), so the EMF pushes it *along* its motion, and it speeds up. In one gyration it gains

$$\Delta W_\perp = |q|\,\pi r_L^2\,\dot B.$$

Divide by the gyroperiod $2\pi/\Omega$ to get a rate:

$$\frac{dW_\perp}{dt} = \frac{|q|\,r_L^2\,\Omega}{2}\,\dot B = \frac{|q|}{2}\frac{v_\perp^2}{\Omega}\,\dot B = \frac{mv_\perp^2}{2B}\,\dot B = \frac{W_\perp}{B}\frac{dB}{dt}.$$

That is $d\ln W_\perp = d\ln B$, i.e.

$$\boxed{\mu = \frac{W_\perp}{B} = \frac{mv_\perp^2}{2B} = \text{const}}$$

Squeeze the field slowly and the perpendicular energy rises in proportion. This is **betatron acceleration**, and it energizes plasma-sheet particles during substorm dipolarization. Equivalently, the flux through the gyro-orbit, $\pi r_L^2B = (2\pi m/q^2)\,\mu$, is constant. The particle "holds on" to its flux tube.

### 1b. A field that varies along the line (the magnetic mirror)

Now let $\mathbf{B}$ be static but converge along $z$, as in a dipole field line approaching the Earth. Near the axis of an axisymmetric field, $\nabla\cdot\mathbf{B}=0$ forces a small radial component:

$$\frac{1}{r}\frac{\partial(rB_r)}{\partial r} + \frac{\partial B_z}{\partial z} = 0 \quad\Longrightarrow\quad B_r \approx -\frac{r}{2}\frac{\partial B_z}{\partial z}.$$

Converging field lines *must* have this inward-tilted component. Now look at the axial force on a particle gyrating at radius $r_L$ around the axis:

$$F_z = q(\mathbf{v}\times\mathbf{B})_z = -q\,v_\theta B_r.$$

For an ion, $v_\theta = -v_\perp$ (left-handed gyration). So

$$F_z = -q(-v_\perp)\left(-\frac{r_L}{2}\frac{\partial B}{\partial z}\right) = -\frac{q\,v_\perp r_L}{2}\frac{\partial B}{\partial z} = -\mu\frac{\partial B}{\partial z}.$$

For an electron both $q$ and $v_\theta$ flip sign, and the result is the same. So the **mirror force** is

$$\boxed{F_\parallel = -\mu\,\frac{\partial B}{\partial s}}$$

where $s$ is arc length along the field. It's the parallel half of the $\langle\mathbf{F}\rangle = -\mu\nabla B$ we found for the grad-$B$ drift.

**Is $\mu$ still conserved?** Energy is conserved, because $\mathbf{B}$ does no work. Then

$$\frac{dW_\parallel}{dt} = v_\parallel F_\parallel = -\mu\,v_\parallel\frac{\partial B}{\partial s} = -\mu\frac{dB}{dt}\bigg|_{\text{along orbit}},$$

so $dW_\perp/dt = +\mu\,dB/dt$. Writing $W_\perp = \mu B$ gives $\frac{d}{dt}(\mu B) = \mu\frac{dB}{dt}$, which leaves $B\,\frac{d\mu}{dt} = 0$. ✓

Same invariant, two completely different mechanisms. In the time-varying case an induced $E$ does the work. In the static mirror there's no work at all: energy is just transferred from $W_\parallel$ to $W_\perp$.

---

## 2. Mirroring and the loss cone

Write the pitch angle as $\alpha$, with $\sin\alpha = v_\perp/v$. Since $v$ is constant (static $\mathbf{B}$) and $v_\perp^2/B$ is constant,

$$\boxed{\frac{\sin^2\alpha}{B} = \text{const} = \frac{1}{B_m}}$$

As the particle moves into stronger field, $\alpha$ grows. At $B = B_m$, $\alpha = 90°$: all the energy is perpendicular, $v_\parallel = 0$, and the mirror force sends the particle back. A particle with equatorial pitch angle $\alpha_0$ mirrors where $B_m = B_0/\sin^2\alpha_0$.

**The loss cone.** If $B_m$ lies *below* the top of the atmosphere (about 100 km), the particle hits the atmosphere and is lost before it can mirror. So particles with $\alpha_0 < \alpha_L$ are lost within a single bounce, where $\sin^2\alpha_L = B_0/B_A$ and $B_A$ is the field at the atmosphere.

**Dipole result.** For a dipole, $B = B_E(R_E/r)^3\sqrt{1+3\sin^2\lambda}$, and a field line is $r = LR_E\cos^2\lambda$. At the equator, $B_0 = B_E/L^3$. At the footpoint ($r\approx R_E$, so $\cos^2\Lambda = 1/L$), $B_A = B_E\sqrt{1+3\sin^2\Lambda} = B_E\sqrt{4-3/L}$. Therefore

$$\boxed{\sin^2\alpha_L = \frac{1}{L^3\sqrt{4-3/L}}}$$

This puts the footpoint at the surface rather than at 100 km, which is a small correction. Plugging in numbers: $\alpha_L \approx 5.3°$ at $L=4$, and $\alpha_L \approx 2.5°$ at geosynchronous orbit ($L = 6.6$).

**That's a tiny cone,** and this is one of the most important facts in magnetospheric physics. Almost all particles are trapped, and the loss cone empties within one bounce period. Steady [[Aurora|diffuse aurora]] and radiation-belt loss therefore require something to *break* $\mu$ conservation and scatter particles into the cone. That something is wave–particle interaction: chorus, hiss, EMIC waves. See [[Wave-Particle Interactions]], [[Kennel 1966 Limit Stably Trapped Fluxes]], [[Thorne 2010 Chorus Diffuse Aurora]].

---

## 3. The second invariant: $J$ and the bounce period

Bouncing between mirror points is itself periodic, so its action is conserved too:

$$\boxed{J = \oint p_\parallel\,ds = 2\int_{s_m'}^{s_m}\sqrt{2m\mu\,(B_m - B(s))}\,ds}$$

The second form uses $p_\parallel^2/2m = W - \mu B = \mu(B_m - B)$, because at the mirror point all of $W$ is $\mu B_m$. $J$ is conserved as long as the field changes slowly compared with the bounce period.

> **Fermi acceleration.** Squeeze the mirror points together slowly and $J$ conservation forces $p_\parallel$ up, roughly as $p_\parallel \times(\text{length}) = $ const. [[Thorne 1993 AOS 250B Course Reader|Thorne]] derives this directly: each reflection off a mirror approaching at speed $U$ adds $\Delta p_\parallel = 2mU$. That's the mechanism by which particles trapped between converging structures (e.g. between a planetary bow shock and an incoming CME shock) gain energy.



**Bounce period.** The time for one full bounce is

$$\tau_b = \oint\frac{ds}{v_\parallel} = \frac{4LR_E}{v}\,F(\lambda_m),$$

where $F$ is a dimensionless dipole integral that depends on the mirror latitude $\lambda_m$ (Thorne Eq. 1.30a). It varies slowly, from $F(0) = \pi/(3\sqrt2)\approx0.74$ to $F(\pi/2)\approx1.38$. A handy fit is $F \approx 1.30 - 0.56\sin\alpha_0$.

*Where does $\pi/(3\sqrt2)$ come from?* For a particle that mirrors close to the equator, expand the dipole there:

$$B \approx B_0\left(1 + \tfrac92\lambda^2\right), \qquad s \approx LR_E\,\lambda,$$

so $B \approx B_0\left(1 + \frac{9s^2}{2L^2R_E^2}\right)$. The mirror force $-\mu\,dB/ds = -\frac{9\mu B_0}{L^2R_E^2}s$ is a linear restoring force, so the particle executes simple harmonic motion with

$$\omega_b^2 = \frac{9\mu B_0}{mL^2R_E^2} = \frac{9v_\perp^2}{2L^2R_E^2} \;\Longrightarrow\; \tau_b = \frac{2\pi\sqrt2}{3}\frac{LR_E}{v} = \frac{4LR_E}{v}\cdot\frac{\pi}{3\sqrt2}.\;✓$$

For a 100 keV proton at $L=4$ this is about 17 s; for a 100 keV electron, about 0.46 s (using the relativistic speed).

---

## 4. The third invariant: the flux $\Phi$

The bounce-averaged drift around the Earth is also periodic. Its invariant is the magnetic flux enclosed by the drift shell:

$$\boxed{\Phi = \oint_{\text{drift shell}}\mathbf{B}\cdot d\mathbf{A}}$$

It is conserved if the field changes slowly compared with the drift period. The drift period (from [[Guiding-Center Drifts]] §5) for equatorial particles is $T_D = 2\pi qB_ER_E^2/(3WL)$, about 106 min for 100 keV at $L=4$. Because $T_D$ is so long, $\Phi$ is the **most fragile** invariant. Compressions of the magnetosphere and ULF waves with periods near $T_D$ break it easily, and the result is **radial diffusion**: particles random-walk across $L$ while keeping $\mu$ and $J$. That is the main transport mechanism of the outer [[Radiation Belts]]. *In a dipole*, $\Phi$ conservation is equivalent to staying on the same $L$-shell, which is why $L$ itself (strictly, Roederer's $L^*$) is used as a coordinate.

---

## 5. The hierarchy of timescales

For a 100 keV proton at $L = 4$, equatorially mirroring:

| Motion | Period | Invariant | Broken by |
|---|---|---|---|
| Gyration | about 0.14 s | $\mu$ | waves near $\Omega$ (EMIC, chorus), or sharp field gradients |
| Bounce | about 17 s | $J$ | waves near the bounce frequency |
| Drift | about 104–106 min | $\Phi$ | ULF waves, storm-time compressions |

The ordering $\tau_g \ll \tau_b \ll \tau_D$ is what makes the guiding-center picture work. Each slower motion sees the faster ones as averaged out. Break the fast invariant and you scatter in pitch angle (loss). Break the slow one and you diffuse in $L$ (transport).

---

## What we assumed, and where it breaks

- **Adiabaticity.** Each invariant needs the field to change slowly relative to its own period. In the stretched nightside tail the field-line curvature radius gets close to the gyroradius, and $\mu$ is violated ("current-sheet scattering"). This is a non-wave route into the loss cone.
- **Non-relativistic.** For relativistic particles the invariant is $p_\perp^2/B$, not $W_\perp/B$. These agree when $\gamma$ is constant, which it is in a static magnetic field. Thorne stresses this distinction (his p. 14).
- **Pure dipole.** The real field is compressed on the dayside and stretched on the nightside, so particles with different pitch angles on the same field line drift onto different shells (*drift-shell splitting*, Thorne p. 25).
- **Atmosphere at the surface.** The loss-cone formula puts the absorbing boundary at $r = R_E$. Using $R_E + 100$ km changes $\alpha_L$ slightly.

---

## Verification

- **Sources agree:**
  - $\mu$ invariance (time-varying and mirror cases): [[Strangeway Ch3 Physics of Magnetized Plasmas|Strangeway]] Eqs. 3.19–3.30 and [[Thorne 1993 AOS 250B Course Reader|Thorne]] pp. 12–14.
  - $J$ (Strangeway Eqs. 3.31–3.33, Thorne p. 15) and $\Phi$ (Strangeway §3.3.7, Thorne p. 16).
  - Loss cone: Thorne Eqs. 1.31–1.31a. Bounce period and $F(\lambda_m)$: Thorne Eqs. 1.30–1.30a.
  - [[Bellan 2006 Fundamentals of Plasma Physics|Bellan]] §3.5.5–3.5.8.
- **SymPy:**
  - Dipole expansions $B/B_0 = 1 + \tfrac92\lambda^2 + O(\lambda^4)$ and $ds = LR_E(1+\lambda^2+\dots)\,d\lambda$, used for the harmonic bounce limit.
- **Numerical:**
  - **Test-particle orbit.** A 100 keV proton at $L=4$, $\alpha_0 = 30°$, in a pure dipole had an integrated bounce period of 23.215 s. Quadrature of the $F(\lambda_m)$ integral predicts 23.28 s (0.3% agreement).
  - **Orbit diagnostics.** The instantaneous $\mu$ varied by about 8% over the orbit. That is gyrophase ripple: it was computed from the particle velocity, not the guiding center. The peak field reached was 3.85 $B_0$ against a predicted mirror field of $4.0\,B_0$, a gap of about 4% that is consistent with sampling $B$ at the particle rather than at the guiding center. A cleaner guiding-center-averaged test is still to do.
  - **Quadrature.** $F(\pi/2) = 1.380$, matching Thorne's 1.38.
  - **Thorne's Table 6.1** (100 keV proton, $r_0 = 4.08R_E$, equatorial): bounce period 17.59 s vs 17.57 s; drift period 6480 s vs 6495 s (with $B_E = 3.11\times10^{-5}$ T); gyroperiod 0.143 s vs 0.139 s (3% difference, probably from a different field constant in the table's source).

## Sources

- [[Strangeway Ch3 Physics of Magnetized Plasmas]] — §3.3.3 (magnetic moment, mirror, $J$), §3.3.7 (three invariants)
- [[Thorne 1993 AOS 250B Course Reader]] — Ch. 1 (invariants, Fermi acceleration, bounce and drift periods, loss cone, Table 6.1, drift-shell splitting)
- [[Bellan 2006 Fundamentals of Plasma Physics]] — §3.3–3.5 (general adiabatic-invariant proof, mirrors, $J$, $\Phi$)
