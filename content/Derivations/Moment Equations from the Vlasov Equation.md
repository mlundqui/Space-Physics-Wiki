---
type: derivation
status: draft
updated: 2026-10-07
sources: 4
tags: [derivations, plasma-foundations, kinetic-theory, fluid-equations, closure]
prerequisites: "[[Guiding-Center Drifts]] (for the Lorentz force); vector calculus with tensors"
next: "[[Ideal MHD from Kinetic Theory]]"
---

# Moment Equations from the Vlasov Equation

**Part I, page 4** of the [[Derivations Index]] · Previous: [[Adiabatic Invariants and Magnetic Mirrors]] · Next: [[Ideal MHD from Kinetic Theory]]

## Where we're going

Following every particle is hopeless. Even a cubic meter of F-region plasma holds about $10^{12}$ electrons. So we describe each species statistically, with a **distribution function** $f(\mathbf{r},\mathbf{v},t)$ living in 6-dimensional phase space. Then we ask a cheaper question: what do the *averages* over velocity (density, flow, pressure, heat flux) do?

Taking those averages ("moments") of the kinetic equation gives fluid equations. Every fluid model in this wiki comes out of this procedure: [[MHD]], the 5-moment equations behind [[Ambipolar Diffusion]], and the 8-moment equations in [[IPWM]]. We'll also find the catch. Every moment equation involves the *next* moment up, so the hierarchy never closes on its own. Where you cut it, and how, is a physical assumption. Different models make different cuts.

---

## 1. The kinetic equation

$f\,d^3r\,d^3v$ is the number of particles in a small box of phase space. Particles aren't created or destroyed (absent collisions and chemistry), so $f$ obeys a conservation law in 6-D. The "flux" in configuration space is $f\mathbf{v}$, and in velocity space it's $f\mathbf{a}$, where $\mathbf{a} = d\mathbf{v}/dt$:

$$\frac{\partial f}{\partial t} + \nabla\cdot(f\mathbf{v}) + \nabla_v\cdot(f\mathbf{a}) = \left(\frac{\partial f}{\partial t}\right)_c.$$

Now simplify, with two observations:

- $\mathbf{r}$ and $\mathbf{v}$ are *independent* phase-space coordinates, so $\nabla\cdot(f\mathbf{v}) = \mathbf{v}\cdot\nabla f$.
- For the forces we care about, $\nabla_v\cdot\mathbf{a} = 0$. That's obvious for $q\mathbf{E}/m$ and $\mathbf{g}$, which don't depend on $\mathbf{v}$. For the magnetic force it's a one-liner: $\partial_{v_i}(\mathbf{v}\times\mathbf{B})_i = \epsilon_{ijk}\delta_{ij}B_k = 0$. The magnetic force rotates velocity space without compressing it.

So

$$\boxed{\frac{\partial f}{\partial t} + \mathbf{v}\cdot\nabla f + \frac{q}{m}(\mathbf{E}+\mathbf{v}\times\mathbf{B})\cdot\nabla_v f = \left(\frac{\partial f}{\partial t}\right)_c}$$

With collisions, this is the **Boltzmann equation**. Set the right side to zero and it's the **Vlasov equation**. The left side is just $df/dt$ along a particle trajectory, so in the collisionless case $f$ is constant along orbits. That's **Liouville's theorem**, which we used in [[Debye Shielding and the Plasma Frequency]].

---

## 2. Moments: what we're going to track

Write $\mathbf{v} = \mathbf{u} + \mathbf{w}$, where $\mathbf{u}$ is the species' mean (bulk) velocity and $\mathbf{w}$ is the random or "peculiar" velocity, with $\langle\mathbf{w}\rangle = 0$. Averages are $\langle\chi\rangle = n^{-1}\int\chi f\,d^3v$. Then:

| Moment | Definition | Physical meaning |
|---|---|---|
| density | $n = \int f\,d^3v$ | how many |
| flow | $n\mathbf{u} = \int\mathbf{v}f\,d^3v$ | where they're going on average |
| pressure tensor | $\mathsf{P} = mn\langle\mathbf{w}\mathbf{w}\rangle$ | momentum flux from random motion |
| scalar pressure | $p = \tfrac13\mathrm{tr}\,\mathsf{P} = nk_BT$ | defines temperature |
| heat flux | $\mathbf{q} = \tfrac12mn\langle w^2\mathbf{w}\rangle$ | energy flux carried by random motion: the *skewness* of $f$ |

Notice that $\mathbf{q}$ is a third-order moment. A drifting Maxwellian is symmetric about $\mathbf{u}$, so it has $\mathbf{q} = 0$. Heat flux measures how *lopsided* the distribution is.

---

## 3. The general moment equation

Multiply the Boltzmann equation by some function $\chi(\mathbf{v})$ and integrate over all velocities. Term by term:

- **Time derivative:** $\chi$ doesn't depend on $t$, so this is $\partial_t(n\langle\chi\rangle)$.
- **Streaming:** $\chi$ doesn't depend on $\mathbf{r}$, so this is $\nabla\cdot(n\langle\mathbf{v}\chi\rangle)$.
- **Force:** integrate by parts in velocity. The surface term vanishes because $f\to0$ as $|\mathbf{v}|\to\infty$, and $\nabla_v\cdot\mathbf{a}=0$ again, so this becomes $-n\langle\mathbf{a}\cdot\nabla_v\chi\rangle$.

Putting them together:

$$\boxed{\frac{\partial}{\partial t}\big(n\langle\chi\rangle\big) + \nabla\cdot\big(n\langle\mathbf{v}\chi\rangle\big) - n\left\langle\mathbf{a}\cdot\nabla_v\chi\right\rangle = \int\chi\left(\frac{\partial f}{\partial t}\right)_c d^3v}$$

Stare at the second term. The time rate of change of $\langle\chi\rangle$ depends on $\langle\mathbf{v}\chi\rangle$, **one power of $v$ higher**. That's the closure problem in one line ([[Strangeway Ch3 Physics of Magnetized Plasmas|Strangeway]] Eq. 3.95).

---

## 4. Climbing the ladder

### $\chi = 1$: continuity

$\nabla_v 1 = 0$, so the force term drops out:

$$\boxed{\frac{\partial n}{\partial t} + \nabla\cdot(n\mathbf{u}) = P - L}$$

Here the collision integral has become production minus loss. Elastic collisions conserve particles, so only chemistry (photoionization, recombination, charge exchange) survives on the right. This is the equation that, with $P - L$ from [[F-Layer|F-region chemistry]], sets the shape of the ionosphere.

### $\chi = m\mathbf{v}$: momentum

The force term is $n\langle m\mathbf{a}\rangle = nq(\mathbf{E} + \mathbf{u}\times\mathbf{B}) + nm\mathbf{g}$. That works because $\mathbf{a}$ is *linear* in $\mathbf{v}$, so averaging just replaces $\mathbf{v}\to\mathbf{u}$. The flux term is $\nabla\cdot(mn\langle\mathbf{vv}\rangle)$, and

$$\langle\mathbf{vv}\rangle = \langle(\mathbf{u}+\mathbf{w})(\mathbf{u}+\mathbf{w})\rangle = \mathbf{uu} + \langle\mathbf{ww}\rangle,$$

since the cross terms average to zero. So

$$\frac{\partial(mn\mathbf{u})}{\partial t} + \nabla\cdot(mn\mathbf{uu}) + \nabla\cdot\mathsf{P} = nq(\mathbf{E}+\mathbf{u}\times\mathbf{B}) + nm\mathbf{g} + \mathbf{R},$$

where $\mathbf{R}$ is the momentum exchanged in collisions. Subtract $m\mathbf{u}$ times the continuity equation (take $P-L = 0$ for clarity) to put it in convective form:

$$\boxed{mn\frac{D\mathbf{u}}{Dt} = -\nabla\cdot\mathsf{P} + nq(\mathbf{E}+\mathbf{u}\times\mathbf{B}) + nm\mathbf{g} + \mathbf{R}}, \qquad \frac{D}{Dt} = \frac{\partial}{\partial t}+\mathbf{u}\cdot\nabla.$$

This is $F = ma$ for a fluid element. In the ionosphere the collision term is usually written as friction against every other species $t$: $\mathbf{R}_s = \sum_t mn_s\nu_{st}(\mathbf{u}_t - \mathbf{u}_s)$ ([[Schunk Nagy 2009 Ionospheres]], 5-moment form). **And here's the catch:** to find $\mathbf{u}$ we need $\mathsf{P}$, the second moment.

### $\chi = \tfrac12mv^2$: energy

Now $\nabla_v(\tfrac12mv^2) = m\mathbf{v}$, and $\mathbf{a}\cdot m\mathbf{v}$ kills the magnetic force ($(\mathbf{v}\times\mathbf{B})\cdot\mathbf{v}=0$). Magnetic fields do no work, even for a fluid. The force term is therefore $nq\mathbf{E}\cdot\mathbf{u} + nm\mathbf{g}\cdot\mathbf{u}$.

For the density and flux terms, expand with $\mathbf{v}=\mathbf{u}+\mathbf{w}$:

$$n\langle\tfrac12mv^2\rangle = \tfrac12\rho u^2 + \tfrac32p,$$

$$n\langle\tfrac12mv^2\,\mathbf{v}\rangle = \left(\tfrac12\rho u^2 + \tfrac32p\right)\mathbf{u} + \mathsf{P}\cdot\mathbf{u} + \mathbf{q}.$$

Read the flux term piece by piece. Kinetic plus thermal energy is carried along with the flow, the pressure does work on the flow ($\mathsf{P}\cdot\mathbf{u}$), and there's the genuinely new heat flux $\mathbf{q}$. The total-energy equation is then

$$\frac{\partial}{\partial t}\left(\tfrac12\rho u^2 + \tfrac32p\right) + \nabla\cdot\left[\left(\tfrac12\rho u^2+\tfrac32p\right)\mathbf{u} + \mathsf{P}\cdot\mathbf{u} + \mathbf{q}\right] = nq\,\mathbf{E}\cdot\mathbf{u} + \rho\,\mathbf{g}\cdot\mathbf{u} + Q_c.$$

That's correct but cluttered. Let's isolate the *thermal* energy by subtracting the bulk kinetic energy. Dot the momentum equation with $\mathbf{u}$:

$$\rho\frac{D}{Dt}\left(\tfrac12u^2\right) = -\mathbf{u}\cdot(\nabla\cdot\mathsf{P}) + nq\mathbf{E}\cdot\mathbf{u} + \rho\mathbf{g}\cdot\mathbf{u} + \mathbf{u}\cdot\mathbf{R}.$$

Subtract it from the total-energy equation. The $\mathbf{E}$ and $\mathbf{g}$ work terms cancel exactly: they change bulk kinetic energy, not heat. The pressure terms leave $\nabla\cdot(\mathsf{P}\cdot\mathbf{u}) - \mathbf{u}\cdot(\nabla\cdot\mathsf{P}) = \mathsf{P}:\nabla\mathbf{u}$ (for symmetric $\mathsf{P}$). That's the work done by compression and shear. So

$$\frac{\partial}{\partial t}\left(\tfrac32p\right) + \nabla\cdot\left(\tfrac32p\,\mathbf{u}\right) + \mathsf{P}:\nabla\mathbf{u} + \nabla\cdot\mathbf{q} = Q_c - \mathbf{u}\cdot\mathbf{R}.$$

For an isotropic pressure, $\mathsf{P} = p\mathsf{I}$ and $\mathsf{P}:\nabla\mathbf{u} = p\nabla\cdot\mathbf{u}$, which gives

$$\boxed{\frac{D}{Dt}\left(\tfrac32p\right) + \tfrac52p\,\nabla\cdot\mathbf{u} + \nabla\cdot\mathbf{q} = \text{(collisional heating)}}$$

Equivalently, $\tfrac32nk_B\frac{DT}{Dt} + p\nabla\cdot\mathbf{u} + \nabla\cdot\mathbf{q} = \dots$. Compression ($\nabla\cdot\mathbf{u}<0$) heats, expansion cools, and heat flux redistributes. **And again** the equation for $p$ needs $\mathbf{q}$, the third moment.

---

## 5. The closure problem, and how models cut it

The pattern is now clear:

$$n \to \mathbf{u} \to \mathsf{P} \to \mathbf{q} \to \cdots$$

Each equation needs the next moment, so we must truncate, replacing some moment with an expression in lower ones. Common choices:

| Closure | Assumption | Where it's used |
|---|---|---|
| Cold plasma | $\mathsf{P} = 0$ | high-frequency waves, [[Debye Shielding and the Plasma Frequency]] §1 |
| Isothermal | $p = nk_BT$, $T$ fixed | quick estimates, ambipolar diffusion |
| Adiabatic | $\nabla\cdot\mathbf{q} = 0$ ⟹ $p\rho^{-5/3}$ = const | ideal [[MHD]] ([[Ideal MHD from Kinetic Theory]]) |
| 5-moment (Fourier) | drifting Maxwellian; $\mathbf{q} = -K\nabla T$ | collisional ionosphere (Schunk & Nagy Ch. 5) |
| 8-, 13-, 16-moment | evolve $\mathbf{q}$ (and stress, or $T_\parallel$/$T_\perp$) with their own equations, closed one level higher | collisionless polar wind; [[IPWM]] uses 8-moment ([[Blelly Schunk 1993 Moment Comparison]]) |
| Double adiabatic (CGL) | separate $p_\parallel$, $p_\perp$; $\mathbf{q}=0$ | anisotropic collisionless plasma ([[MHD]] §CGL) |

> **Why it matters for this vault's research.** On open polar-cap field lines, the plasma goes from collision-dominated (F region) to collisionless (above a few thousand km). A Fourier-law closure assumes collisions keep $f$ nearly Maxwellian, and it fails exactly where the polar wind goes supersonic. That is the physical reason [[IPWM]] carries a prognostic heat-flow equation (8-moment) instead.

[[Strangeway Ch3 Physics of Magnetized Plasmas|Strangeway]] makes a subtle point about the MHD closure: the assumption is really $\nabla\cdot\mathbf{q} = 0$, not $\mathbf{q}=0$. A plasma can carry heat flux; what matters is whether it *converges*.

**Something important was lost.** Moments average away the detailed shape of $f$, and with it every **wave–particle resonance**: Landau damping, cyclotron resonance, the loss-cone instabilities of [[Wave-Particle Interactions]]. No fluid closure recovers these. They need the Vlasov equation itself.

---

## What we assumed, and where it breaks

- **$\nabla_v\cdot\mathbf{a}=0$.** This is true for Lorentz and gravity forces. It's false for velocity-dependent friction, which is why friction goes into the collision term instead.
- **"Localization."** Fluid equations assume the local state depends only on local quantities. In a collisional gas, collisions enforce this. In a collisionless plasma, the magnetic field localizes motion *across* $\mathbf{B}$ (gyration) but not *along* it. Strangeway (§3.5) is candid that the fluid description of collisionless plasmas works better than it has any right to.
- **Smooth $f$.** Beams, loss cones and strahl electrons (see [[Pierrard 2001 Solar Wind Electrons]]) are poorly represented by low-order moments.

---

## Verification

- **Sources agree.** General moment equation and continuity/momentum/energy: [[Strangeway Ch3 Physics of Magnetized Plasmas|Strangeway]] Eqs. 3.90–3.106, 3.124. [[Bellan 2006 Fundamentals of Plasma Physics|Bellan]] §2.2–2.4. [[Schunk Nagy 2009 Ionospheres|Schunk & Nagy]] Ch. 3 (full hierarchy, Eqs. 3.30–3.40) and Ch. 5 (5-moment collision terms). Closure hierarchy: Schunk & Nagy Ch. 3 and [[Blelly Schunk 1993 Moment Comparison]].
- **SymPy:**
  - $\nabla_v\cdot(\mathbf{v}\times\mathbf{B}) = 0$.
  - The energy-flux decomposition $nm\langle\tfrac12v^2\mathbf{v}\rangle = (\tfrac12\rho u^2+\tfrac32p)\mathbf{u} + \mathsf{P}\cdot\mathbf{u} + \mathbf{q}$, expanding $\mathbf{v}=\mathbf{u}+\mathbf{w}$ with $\langle\mathbf{w}\rangle=0$ and general symmetric $\mathsf{P}$.
  - The tensor identity $\nabla\cdot(\mathsf{P}\cdot\mathbf{u}) - \mathbf{u}\cdot(\nabla\cdot\mathsf{P}) = \mathsf{P}:\nabla\mathbf{u}$.
  - $D(p\rho^{-5/3})/Dt = 0$ follows from the isotropic energy equation with $\nabla\cdot\mathbf{q}=0$.

## Sources

- [[Strangeway Ch3 Physics of Magnetized Plasmas]] — §3.4.2 (Boltzmann/Vlasov), §3.5.1–3.5.3 (moments, closure)
- [[Bellan 2006 Fundamentals of Plasma Physics]] — §2.2–2.4 (Vlasov equation, moments, two-fluid equations)
- [[Schunk Nagy 2009 Ionospheres]] — Ch. 3 (moment hierarchy, 13-moment closure), Ch. 5 (5-moment transport, collision terms)
- [[Blelly Schunk 1993 Moment Comparison]] — 5/8/13/16-moment closures compared for the polar wind
