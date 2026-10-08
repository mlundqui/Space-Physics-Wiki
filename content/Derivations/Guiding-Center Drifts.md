---
type: derivation
status: draft
updated: 2026-10-07
sources: 3
tags: [derivations, plasma-foundations, particle-motion, drifts]
prerequisites: "Lorentz force; [[Debye Shielding and the Plasma Frequency]] (optional)"
next: "[[Adiabatic Invariants and Magnetic Mirrors]]"
---

# Guiding-Center Drifts

**Part I, page 2** of the [[Derivations Index]] · Previous: [[Debye Shielding and the Plasma Frequency]] · Next: [[Adiabatic Invariants and Magnetic Mirrors]]

## Where we're going

A charged particle in a magnetic field does something almost boring: it circles. Add anything else (an electric field, gravity, a gradient in $|\mathbf{B}|$, a bend in the field line, a slowly changing $\mathbf{E}$) and the circle starts to **drift**. That drift is slow and steady, at right angles to *both* the push and $\mathbf{B}$.

The single organizing idea of this page is

$$\mathbf{v}_F = \frac{\mathbf{F}\times\mathbf{B}}{qB^2}.$$

Once we have that, every named drift ($\mathbf{E}\times\mathbf{B}$, gravity, $\nabla B$, curvature, polarization) is just a matter of identifying the right $\mathbf{F}$. In the ionosphere, $\mathbf{E}\times\mathbf{B}$ *is* plasma convection. In the magnetosphere, $\nabla B$ and curvature drifts *are* the ring current.

**The one assumption behind everything here:** fields change slowly on the scale of one gyration. Spatial scales must be large compared to the gyroradius, $r_L \ll L$, and time scales long compared to the gyroperiod, $\omega \ll \Omega$. We treat each particle as a **test particle**: it feels the fields but doesn't change them.

---

## 1. Gyration in a uniform field

Take uniform $\mathbf{B} = B\hat{\mathbf{z}}$ and nothing else:

$$m\frac{d\mathbf{v}}{dt} = q\,\mathbf{v}\times\mathbf{B}.$$

**First, a free result.** Dot both sides with $\mathbf{v}$. The right side is $q\,\mathbf{v}\cdot(\mathbf{v}\times\mathbf{B}) = 0$, so $\frac{d}{dt}\left(\tfrac12mv^2\right)=0$. *Magnetic fields do no work.* Remember that; it's why the drifts below come out the way they do.

The $z$-component says $\dot v_\parallel = 0$, so motion along $\mathbf{B}$ is free streaming. The perpendicular components are

$$\dot v_x = \frac{qB}{m}v_y, \qquad \dot v_y = -\frac{qB}{m}v_x.$$

Differentiate the first equation and substitute the second: $\ddot v_x = -(qB/m)^2v_x$. That's a harmonic oscillator, with the **gyrofrequency**

$$\boxed{\Omega = \frac{|q|B}{m}}$$

The solution is a circle of radius

$$\boxed{r_L = \frac{v_\perp}{\Omega} = \frac{mv_\perp}{|q|B}}$$

called the Larmor radius or gyroradius. Put the two motions together and you get a helix.

**Which way do they turn?** Solve with the initial condition $\mathbf{v}(0) = v_\perp\hat{\mathbf{y}}$ for $q>0$. You get $v_x = v_\perp\sin\Omega t$ and $v_y = v_\perp\cos\Omega t$, so the velocity rotates from $+\hat{\mathbf y}$ toward $+\hat{\mathbf x}$. Viewed with $\mathbf{B}$ pointing at you, that's clockwise. **Ions gyrate left-handed about $\mathbf{B}$, and electrons right-handed.** Either way, the current loop the gyration makes produces a magnetic moment that *opposes* $\mathbf{B}$. A plasma is **diamagnetic**.

Numbers at 300 km ($B\approx5\times10^{-5}$ T):

| | Gyroperiod | Gyroradius |
|---|---|---|
| O$^+$ | about 21 ms | a few m |
| Electron | about 0.7 µs | about 2 cm |

---

## 2. The $\mathbf{E}\times\mathbf{B}$ drift

Now add a uniform $\mathbf{E}$. Any component of $\mathbf{E}$ along $\mathbf{B}$ just accelerates the particle along the field ($m\dot v_\parallel = qE_\parallel$). That's why large-scale $E_\parallel$ is rare in space plasmas: the particles short it out. The interesting part is $\mathbf{E}_\perp$.

Here's the trick. Go to a frame moving at some constant velocity $\mathbf{v}_E$. In that frame the particle feels the electric field $\mathbf{E}' = \mathbf{E} + \mathbf{v}_E\times\mathbf{B}$ (the non-relativistic transformation). *Can we choose $\mathbf{v}_E$ so that $\mathbf{E}'_\perp = 0$?* If so, the particle in that frame just gyrates, and in the lab frame it gyrates *plus* drifts at $\mathbf{v}_E$.

Try $\mathbf{v}_E = \mathbf{E}\times\mathbf{B}/B^2$. Using $(\mathbf{E}\times\mathbf{B})\times\mathbf{B} = \mathbf{B}(\mathbf{E}\cdot\mathbf{B}) - \mathbf{E}B^2 = -\mathbf{E}_\perp B^2$,

$$\mathbf{E}' = \mathbf{E} + \frac{(\mathbf{E}\times\mathbf{B})\times\mathbf{B}}{B^2} = \mathbf{E} - \mathbf{E}_\perp = \mathbf{E}_\parallel.$$

So the perpendicular field vanishes in that frame:

$$\boxed{\mathbf{v}_E = \frac{\mathbf{E}\times\mathbf{B}}{B^2}}$$

**Look at what's missing:** no $q$, no $m$. Ions and electrons drift *together*, at the same speed and in the same direction. That means no current flows. The whole plasma simply moves.

The picture behind it: during the half of its orbit when an ion moves along $\mathbf{E}$ it speeds up and its gyroradius grows. During the other half it slows down and the gyroradius shrinks. Big arcs alternate with small arcs, and the guiding center walks sideways. An electron turns the other way *and* is accelerated the other way, so the two sign flips cancel.

> **In the ionosphere.** In the F region, ions gyrate many times between collisions with neutrals ($\Omega_i \gg \nu_{in}$), so $\mathbf{v}_E$ is the plasma convection velocity. A typical polar-cap field of 50 mV/m in a 50,000 nT field drives $v_E = 1$ km/s. This is the flow that carries [[Polar Cap Patch|patches]] and the [[Tongue of Ionization]] across the polar cap in the [[Dungey Cycle]]. It is also exactly what [[RISR-N]] and [[SuperDARN]] measure as line-of-sight ion velocity. In the E region, ion–neutral collisions interrupt the ion drift; $\Omega_i \sim \nu_{in}$ near 100–130 km. Electrons are still magnetized there and keep $\mathbf{E}\times\mathbf{B}$ drifting, so the two species separate and current flows. That's where [[Ionospheric Conductivity]] comes from.

---

## 3. The general force drift

Nothing in §2 used the fact that the force was electric. It only used a constant force $q\mathbf{E}$ perpendicular to $\mathbf{B}$. So replace $q\mathbf{E}\to\mathbf{F}$:

$$\boxed{\mathbf{v}_F = \frac{\mathbf{F}\times\mathbf{B}}{qB^2}}$$

This is the master formula. Now the charge *doesn't* cancel unless $\mathbf{F}\propto q$. Any force that is the same for ions and electrons drives them in **opposite** directions, and that **is a current**.

**Gravity drift.** With $\mathbf{F} = m\mathbf{g}$, $\mathbf{v}_g = m\,\mathbf{g}\times\mathbf{B}/(qB^2)$. For O$^+$ at 300 km this is only about 3 cm/s, which is tiny. But it is mass- and charge-dependent, so it drives a real horizontal current at the magnetic equator. That current is the seed of the equatorial Rayleigh–Taylor instability (see [[Ionospheric Instabilities]], [[Equatorial Ionosphere]]).

---

## 4. The grad-$B$ drift

Now let $|\mathbf{B}|$ vary across the field, say $B_z(x) \approx B_0 + x\,\partial B/\partial x$. The force is no longer constant, but we can still use the master formula. All we need is the **force averaged over one gyration**.

Expand around the guiding center at the origin, and use the *unperturbed* orbit as the zeroth-order path. For an ion that orbit is $x = r_L\cos\Omega t$ and $v_y = -v_\perp\cos\Omega t$. The $x$-force is

$$F_x = q\,v_yB_z(x) = q\,(-v_\perp\cos\Omega t)\left(B_0 + r_L\cos\Omega t\,\frac{\partial B}{\partial x}\right).$$

Averaged over a gyroperiod, the $B_0$ term vanishes ($\langle\cos\rangle = 0$), and the gradient term survives because $\langle\cos^2\rangle = \tfrac12$:

$$\langle F_x\rangle = -\frac{q\,v_\perp r_L}{2}\frac{\partial B}{\partial x} = -\frac{mv_\perp^2}{2B}\frac{\partial B}{\partial x}.$$

The $y$-force averages to zero, since it is proportional to $\langle\sin\cos\rangle$. Define the **magnetic moment**

$$\mu \equiv \frac{mv_\perp^2}{2B} = \frac{W_\perp}{B},$$

and the averaged force is $\langle\mathbf{F}\rangle = -\mu\nabla B$. That's just the force on a magnetic dipole $\boldsymbol\mu$ pointed *against* $\mathbf{B}$, which we already knew from the diamagnetism in §1. Feed it to the master formula:

$$\boxed{\mathbf{v}_{\nabla B} = \frac{\mu\,\mathbf{B}\times\nabla B}{qB^2} = \frac{W_\perp}{qB^3}\,\mathbf{B}\times\nabla B}$$

**The picture:** on the strong-field side of the orbit the gyroradius is smaller, and on the weak-field side it is larger. The orbit doesn't close on itself, and the guiding center creeps sideways. The sign of $q$ survives, so ions and electrons drift in opposite directions, and the drift is a current.

---

## 5. The curvature drift

Field lines in a dipole aren't straight. A particle streaming along a curved line at $v_\parallel$ has to turn with it, so in its own frame it feels a centrifugal force. Define the **curvature vector**

$$\boldsymbol\kappa \equiv (\hat{\mathbf b}\cdot\nabla)\hat{\mathbf b} = -\frac{\mathbf{R}_c}{R_c^2},$$

which points toward the center of curvature with magnitude $1/R_c$. The centrifugal force is $\mathbf{F}_{cf} = -mv_\parallel^2\,\boldsymbol\kappa$. The master formula gives

$$\boxed{\mathbf{v}_c = \frac{mv_\parallel^2}{qB}\,\hat{\mathbf b}\times\boldsymbol\kappa = \frac{2W_\parallel}{qB^4}\,\mathbf{B}\times(\mathbf{B}\cdot\nabla)\mathbf{B}}$$

The second form is [[Strangeway Ch3 Physics of Magnetized Plasmas|Strangeway]]'s Eq. 3.39. It equals the first because $\mathbf{B}\times(\mathbf{B}\cdot\nabla)\mathbf{B} = B^3\,\hat{\mathbf b}\times\boldsymbol\kappa$; the part of $(\mathbf B\cdot\nabla)\mathbf B$ along $\hat{\mathbf b}$ drops out of the cross product.

> **"Centrifugal force? Really?"** It's fair to be suspicious of a rotating-frame argument. Strangeway (§3.3.5) re-derives the same drift with no fictitious forces, by Taylor-expanding the equation of motion in a slightly bent field. He gets the identical result, and also shows that the guiding center follows the field line while the gyration stays perpendicular to it.

### Gradient and curvature together, in a vacuum field

In a curl-free field ($\nabla\times\mathbf{B} = 0$, a good approximation for the inner magnetosphere's dipole), the two drifts aren't independent. The identity $\nabla(B^2/2) = (\mathbf{B}\cdot\nabla)\mathbf{B} + \mathbf{B}\times(\nabla\times\mathbf{B})$ becomes $(\mathbf{B}\cdot\nabla)\mathbf{B} = B\nabla B$. Write the left side as $B^2\boldsymbol\kappa + B\hat{\mathbf b}(\hat{\mathbf b}\cdot\nabla B)$ and you find

$$\boldsymbol\kappa = \frac{\nabla_\perp B}{B} \qquad (\nabla\times\mathbf{B}=0).$$

The field lines bend toward the strong-field region. The two drifts then add:

$$\boxed{\mathbf{v}_{\nabla B} + \mathbf{v}_c = \frac{W_\perp + 2W_\parallel}{qB^3}\,\mathbf{B}\times\nabla B} \qquad (\nabla\times\mathbf{B}=0)$$

In [[Thorne 1993 AOS 250B Course Reader|Thorne]]'s pitch-angle form this is $\propto(\tfrac12\sin^2\alpha + \cos^2\alpha)$, his Eq. 1.22.

**In the dipole.** Ions drift **westward** and electrons **eastward**. Both carry current to the west: that's the **[[Ring Current]]**. For an equatorially mirroring particle ($W_\parallel = 0$) at distance $r = LR_E$, $|\nabla B| = 3B/r$. That gives an azimuthal drift period

$$T_D = \frac{2\pi\,qB_ER_E^2}{3\,W\,L},$$

where $B_E \approx 3\times10^{-5}$ T is the equatorial surface field. A 100 keV proton at $L=4$ goes around Earth in about **106 minutes**. Higher energy means a faster drift: drift periods scale as $1/(WL)$.

---

## 6. The polarization drift

Finally, let $\mathbf{E}_\perp$ change *slowly* in time. The particle tries to keep up with $\mathbf{v}_E(t)$, but $\mathbf{v}_E$ is now accelerating, so in the frame that follows it there's an inertial force $-m\,d\mathbf{v}_E/dt$. This is the move [[Thorne 1993 AOS 250B Course Reader|Thorne]] uses (his Eq. 1.17): add inertial forces when the drift frame accelerates. Apply the master formula:

$$\mathbf{v}_p = \frac{-m\,\dot{\mathbf{v}}_E\times\mathbf{B}}{qB^2} = -\frac{m}{qB^4}\left(\dot{\mathbf{E}}\times\mathbf{B}\right)\times\mathbf{B} = \frac{m}{qB^4}\,B^2\,\dot{\mathbf{E}}_\perp,$$

$$\boxed{\mathbf{v}_p = \frac{m}{qB^2}\frac{d\mathbf{E}_\perp}{dt}}$$

This one is along $\dot{\mathbf{E}}$, not perpendicular to it. It's mass-proportional, so the ions completely dominate. Summing over species gives the **polarization current**

$$\mathbf{j}_p = \frac{\rho}{B^2}\frac{d\mathbf{E}_\perp}{dt},$$

where $\rho$ is the mass density.

Why should we care about something so small? Because it's the **only** perpendicular current in a time-varying, collisionless plasma that carries inertia. It's the current that closes [[Alfvén Waves]] across field lines. It also lets you treat a magnetized plasma as a dielectric with $\varepsilon_\perp = 1 + \rho/(\varepsilon_0B^2) = 1 + c^2/v_A^2$, which is enormous in most space plasmas.

---

## The generalized drift (for reference)

[[Strangeway Ch3 Physics of Magnetized Plasmas|Strangeway]] §3.3.6 carries the expansion to first order in all field gradients and time derivatives at once (his Eq. 3.68). The result contains $\mathbf{v}_E$, $\nabla B$, curvature, polarization, and a few unnamed terms involving $\partial\mathbf{B}/\partial t$ and $(\mathbf{v}_E\cdot\nabla)$. His §3.7.2 then shows something important: summing these drifts over all particles **and adding the magnetization current** $\nabla\times\mathbf{M}$ from the gyration gives *exactly* the perpendicular current of MHD. The $\nabla B$-drift current cancels against part of the magnetization current. That's a warning: drift currents alone are not the plasma current. See [[Ideal MHD from Kinetic Theory]].

---

## What we assumed, and where it breaks

- **$r_L \ll L$ and $\omega\ll\Omega$.** This fails for energetic ions in thin current sheets such as the magnetotail neutral sheet (where $B\to0$; see [[Artemyev 2008 Harris Current Sheet]]). It also fails for high-frequency waves and for super-relativistic particles. Thorne notes that the guiding-center approximation fails for galactic cosmic rays in the geomagnetic field.
- **Non-relativistic.** For radiation-belt electrons, replace $m\to\gamma m$ and use momentum $p_\perp$ rather than velocity. Thorne writes every drift relativistically (his Eqs. 1.19–1.27).
- **Test particles.** Drift currents change $\mathbf{B}$, for example in the storm-time ring current. At that point you need a self-consistent (fluid or kinetic) treatment.
- **Collisionless.** Collisions destroy gyration-based drifts. In the E region this is precisely what gives the Pedersen and Hall currents.

---

## Verification

- **Sources agree.** [[Strangeway Ch3 Physics of Magnetized Plasmas|Strangeway Ch. 3]] Eqs. 3.8–3.18 (gyration, $\mathbf{E}\times\mathbf{B}$, force drift), 3.34–3.39 ($\nabla B$, curvature), 3.68–3.69 (generalized drift, vacuum-field sum). [[Thorne 1993 AOS 250B Course Reader|Thorne 1993]] Eqs. 1.10–1.27 (same results, relativistic, Gaussian units). [[Bellan 2006 Fundamentals of Plasma Physics|Bellan]] §3.5.
- **SymPy:**
  - The gyration solution satisfies the equation of motion.
  - $\mathbf{v}_E$ plus gyration satisfies the equation with uniform $\mathbf{E}$.
  - The gyro-averaged force in $B_z = B_0(1+\epsilon x)$ is exactly $\langle F_x\rangle = -\mu\,\partial B/\partial x$ and $\langle F_y\rangle = 0$.
- **Numerical test-particle integration** (SciPy, rtol $10^{-10}$):
  - **Drift period.** A 100 keV equatorial proton at $L=4$ in a pure dipole drifts westward; a quarter drift orbit took the predicted time to within 0.15%. The residual is finite-gyroradius error.
  - **Polarization drift.** For $\dot E = 10^{-3}$ V m$^{-1}$s$^{-1}$, the integrated mean drift matched $m\dot E/(qB^2)$ to 4 significant figures.
  - **Curvature identity.** $\boldsymbol\kappa_\perp = \nabla_\perp B/B$ was confirmed in a dipole field to a relative error of $2\times10^{-9}$.

## Sources

- [[Strangeway Ch3 Physics of Magnetized Plasmas]] — §3.3 (particle orbit theory, generalized drift), §3.7.2 (drift vs. MHD currents)
- [[Thorne 1993 AOS 250B Course Reader]] — Ch. 1 (charged-particle orbital dynamics, relativistic drifts)
- [[Bellan 2006 Fundamentals of Plasma Physics]] — §3.5 (drift equations)
