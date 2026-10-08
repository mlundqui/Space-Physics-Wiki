---
type: derivation
status: draft
updated: 2026-10-07
sources: 3
tags: [derivations, plasma-foundations, MHD, ohms-law, frozen-in]
prerequisites: "[[Moment Equations from the Vlasov Equation]]"
next: "[[MHD Wave Modes]]"
---

# Ideal MHD from Kinetic Theory

**Part I, page 5** of the [[Derivations Index]] · Previous: [[Moment Equations from the Vlasov Equation]] · Next: [[MHD Wave Modes]]

## Where we're going

We have fluid equations for *each species*. Now we add them up into a single conducting fluid, then ask what Ohm's law looks like for such a fluid. Then we watch a remarkable theorem fall out: **in a perfectly conducting plasma, the magnetic field moves with the fluid.**

By the end we'll have a closed set of equations in just four quantities, $\rho$, $\mathbf{u}$, $p$ and $\mathbf{B}$, in which $\mathbf{E}$ and $\mathbf{j}$ have disappeared as independent players. This is ideal MHD, the workhorse for the solar wind, the magnetosphere and the large-scale coupling to the ionosphere. The concept page [[MHD]] summarizes the results; this page derives them.

---

## 1. Adding up the species

Define single-fluid variables by summing over species $s$:

$$\rho = \sum_s n_sm_s, \quad \rho\mathbf{u} = \sum_s n_sm_s\mathbf{u}_s, \quad \rho_q = \sum_s n_sq_s, \quad \mathbf{j} = \sum_s n_sq_s\mathbf{u}_s.$$

Because $m_i\gg m_e$, $\mathbf{u}$ is essentially the ion velocity, while $\mathbf{j}$ is mostly carried by the *difference* between ion and electron velocities. To make the sums clean, define every species' pressure tensor relative to the common velocity $\mathbf{u}$, as [[Strangeway Ch3 Physics of Magnetized Plasmas|Strangeway]] does, and let $\mathsf{P} = \sum_s\mathsf{P}_s$.

**Mass and charge.** Multiply each species' continuity equation by $m_s$ and sum, then by $q_s$ and sum:

$$\frac{\partial\rho}{\partial t} + \nabla\cdot(\rho\mathbf{u}) = 0, \qquad \frac{\partial\rho_q}{\partial t} + \nabla\cdot\mathbf{j} = 0.$$

The first assumes no net mass source; ionization and recombination of the plasma relative to the neutrals would add one.

**Momentum.** Sum the species momentum equations. Collisions *between plasma species* cancel in the sum: Newton's third law says the momentum electrons lose to ions, the ions gain. What's left is

$$\rho\frac{D\mathbf{u}}{Dt} = -\nabla\cdot\mathsf{P} + \rho_q\mathbf{E} + \mathbf{j}\times\mathbf{B} + \rho\mathbf{g}.$$

Notice that $\sum_s n_sq_s(\mathbf{E} + \mathbf{u}_s\times\mathbf{B})$ has neatly become $\rho_q\mathbf{E} + \mathbf{j}\times\mathbf{B}$.

---

## 2. Two approximations that make it MHD

**(a) Quasi-neutrality: drop $\rho_q\mathbf{E}$.** Estimate both electromagnetic forces for a flow $u$ over a scale $L$:

- Gauss's law gives $\rho_q\sim\varepsilon_0E/L$, and in a flowing plasma $E\sim uB$.
- Ampère's law gives $j\sim B/\mu_0L$.

So

$$\frac{\rho_qE}{jB}\sim\frac{\varepsilon_0u^2B^2/L}{B^2/\mu_0L} = \frac{u^2}{c^2}.$$

The electric force on net charge is smaller than the magnetic force by $(u/c)^2$. Drop it. This isn't saying $\rho_q = 0$ exactly. It's saying the tiny charge that *is* there does nothing to the dynamics.

**(b) Drop the displacement current.** In Ampère's law, $\varepsilon_0\partial\mathbf{E}/\partial t$ compared with $\nabla\times\mathbf{B}$ is again of order $u^2/c^2$ for slow, non-relativistic flows. So

$$\nabla\times\mathbf{B} = \mu_0\mathbf{j}, \qquad\text{and therefore}\qquad \nabla\cdot\mathbf{j}=0.$$

That second statement is a big deal for the ionosphere. Currents can't pile up charge anywhere. If perpendicular currents diverge, the difference *must* flow along $\mathbf{B}$, and that's where [[Field-Aligned Currents]] come from.

---

## 3. Magnetic pressure and tension

With Ampère's law in hand, eliminate $\mathbf{j}$ from the force. A vector identity gives

$$\mathbf{j}\times\mathbf{B} = \frac{(\nabla\times\mathbf{B})\times\mathbf{B}}{\mu_0} = \underbrace{\frac{(\mathbf{B}\cdot\nabla)\mathbf{B}}{\mu_0}}_{\text{tension}} - \underbrace{\nabla\left(\frac{B^2}{2\mu_0}\right)}_{\text{magnetic pressure}}.$$

The magnetic field acts on the plasma like an isotropic pressure $B^2/2\mu_0$, plus a tension along curved field lines. Write $(\mathbf{B}\cdot\nabla)\mathbf{B} = B^2\boldsymbol\kappa + \hat{\mathbf b}\,\partial_s(B^2/2)$, where $\boldsymbol\kappa$ is the field-line curvature from [[Guiding-Center Drifts]] §5. The parallel piece of the tension *exactly cancels* the parallel piece of the pressure gradient. That makes sense: $\mathbf{j}\times\mathbf{B}$ can't push along $\mathbf{B}$. What's left is a tension $B^2\boldsymbol\kappa/\mu_0$ that tries to straighten bent field lines, like a plucked string. That string-like restoring force is what makes [[Alfvén Waves]] possible.

The ratio of thermal to magnetic pressure is the plasma beta,

$$\beta = \frac{p}{B^2/2\mu_0}.$$

In the F region $\beta\approx4\times10^{-5}$ (for $n = 10^{12}$ m$^{-3}$, $T_e+T_i = 3000$ K, $B = 5\times10^{-5}$ T), so the geomagnetic field is utterly rigid there. In the solar wind $\beta\sim1$.

---

## 4. The generalized Ohm's law

The momentum equation brought in $\mathbf{j}\times\mathbf{B}$, but we still need a relation between $\mathbf{E}$ and the flow. That comes from the **electron** momentum equation. Electrons are light, so they respond almost instantly, and their equation acts as a constraint:

$$m_en\frac{d\mathbf{u}_e}{dt} = -\nabla p_e - ne(\mathbf{E} + \mathbf{u}_e\times\mathbf{B}) + \mathbf{R}_{ei}.$$

There are two ingredients:

- **Friction.** Collisional drag against the ions is $\mathbf{R}_{ei} = -m_en\nu_{ei}(\mathbf{u}_e - \mathbf{u}_i) = (m_e\nu_{ei}/e)\,\mathbf{j}$, using $\mathbf{j} = ne(\mathbf{u}_i - \mathbf{u}_e)$.
- **Electron velocity.** With $\mathbf{u}\approx\mathbf{u}_i$, we have $\mathbf{u}_e = \mathbf{u} - \mathbf{j}/ne$.

Substitute both and solve for $\mathbf{E}$:

$$\boxed{\mathbf{E} + \mathbf{u}\times\mathbf{B} = \underbrace{\eta\,\mathbf{j}}_{\text{resistive}} + \underbrace{\frac{\mathbf{j}\times\mathbf{B}}{ne}}_{\text{Hall}} - \underbrace{\frac{\nabla p_e}{ne}}_{\text{electron pressure}} + \underbrace{\frac{m_e}{ne^2}\frac{\partial\mathbf{j}}{\partial t}}_{\text{electron inertia}}}, \qquad \eta = \frac{m_e\nu_{ei}}{ne^2}.$$

The left side is the electric field *in the frame moving with the plasma*. Each term on the right is a way for that field to be nonzero. **How big is each one relative to $uB$?**

| Term | Ratio to $uB$ | Matters when… |
|---|---|---|
| resistive | $1/R_m$, with $R_m = \mu_0uL/\eta$ | collisions are frequent or scales are tiny |
| Hall | $(v_A/u)(d_i/L)$, with $d_i = c/\omega_{pi}$ | $L\lesssim d_i$ |
| electron pressure | $(c_s/u)(\rho_s/L)$, with $c_s = \sqrt{k_BT_e/m_i}$ and $\rho_s = c_s/\Omega_i$ | $L\lesssim\rho_s$ (the kinetic-Alfvén scale) |
| electron inertia | $\sim(d_e/L)^2$ | $L\lesssim d_e = c/\omega_{pe}$ |

*(All four ratios use $j\sim B/\mu_0L$ and $\partial_t\sim u/L$. The Hall estimate uses $B/\mu_0ne = v_Ad_i$, an exact identity, and the pressure estimate uses $k_BT_e/eB = c_s\rho_s$. Inertial lengths: F region, O$^+$ at $10^{12}$ m$^{-3}$: $d_i\approx0.9$ km, $d_e\approx5$ m. Solar wind: $d_i\approx100$ km. Plasma sheet: $d_i\approx400$ km, $d_e\approx10$ km.)*

On large scales in a collisionless plasma, every term on the right is negligible:

$$\boxed{\mathbf{E} + \mathbf{u}\times\mathbf{B} = 0}$$

This is the **ideal Ohm's law**. Compare [[Guiding-Center Drifts]] §2: it says $\mathbf{u}_\perp = \mathbf{E}\times\mathbf{B}/B^2$, the $\mathbf{E}\times\mathbf{B}$ drift again. The fluid and particle pictures agree. The small terms are where the interesting physics hides:

- Electron inertia and electron pressure give the inertial and kinetic [[Alfvén Waves]] their $E_\parallel$.
- The Hall term structures reconnection.
- In the ionosphere, collisions with *neutrals* (not included here) replace this Ohm's law with the anisotropic Pedersen/Hall form of [[Ionospheric Conductivity]].

---

## 5. The frozen-in theorem

Take the curl of the ideal Ohm's law and use Faraday's law, $\partial\mathbf{B}/\partial t = -\nabla\times\mathbf{E}$:

$$\boxed{\frac{\partial\mathbf{B}}{\partial t} = \nabla\times(\mathbf{u}\times\mathbf{B})}$$

That's the **induction equation**. Keep the resistive term and you get an extra $(\eta/\mu_0)\nabla^2\mathbf{B}$: field diffusion, which competes with advection in the ratio $R_m$.

### Part 1: flux through a moving loop is conserved

Take any closed loop $C$ whose points move with the fluid, and the flux $\Phi = \int_S\mathbf{B}\cdot d\mathbf{A}$ through it. The flux changes for two reasons:

1. $\mathbf{B}$ changes in time: $\int\partial_t\mathbf{B}\cdot d\mathbf{A}$.
2. The loop moves. In time $dt$, each element $d\boldsymbol\ell$ sweeps out area $\mathbf{u}\,dt\times d\boldsymbol\ell$, adding flux $\mathbf{B}\cdot(\mathbf{u}\times d\boldsymbol\ell)\,dt = -(\mathbf{u}\times\mathbf{B})\cdot d\boldsymbol\ell\,dt$. (The swept surface plus the old and new caps form a closed surface, and $\nabla\cdot\mathbf{B} = 0$ guarantees the bookkeeping is consistent.)

So

$$\frac{d\Phi}{dt} = \int_S\frac{\partial\mathbf{B}}{\partial t}\cdot d\mathbf{A} - \oint_C(\mathbf{u}\times\mathbf{B})\cdot d\boldsymbol\ell = -\int_S\nabla\times(\mathbf{E}+\mathbf{u}\times\mathbf{B})\cdot d\mathbf{A},$$

using Faraday and Stokes. If the ideal Ohm's law holds, the integrand vanishes and **$d\Phi/dt = 0$ for every loop moving with the fluid.**

### Part 2: field lines connect the same fluid elements

Expand the curl (using $\nabla\cdot\mathbf{B}=0$):

$$\nabla\times(\mathbf{u}\times\mathbf{B}) = (\mathbf{B}\cdot\nabla)\mathbf{u} - (\mathbf{u}\cdot\nabla)\mathbf{B} - \mathbf{B}(\nabla\cdot\mathbf{u}),$$

so $D\mathbf{B}/Dt = (\mathbf{B}\cdot\nabla)\mathbf{u} - \mathbf{B}(\nabla\cdot\mathbf{u})$. Now use continuity, $D\rho/Dt = -\rho\nabla\cdot\mathbf{u}$, and the $\nabla\cdot\mathbf{u}$ terms cancel:

$$\boxed{\frac{D}{Dt}\left(\frac{\mathbf{B}}{\rho}\right) = \left(\frac{\mathbf{B}}{\rho}\cdot\nabla\right)\mathbf{u}}$$

Compare a material line element $d\boldsymbol\ell$ joining two nearby fluid particles. Its far end moves at $\mathbf{u} + (d\boldsymbol\ell\cdot\nabla)\mathbf{u}$, so $D(d\boldsymbol\ell)/Dt = (d\boldsymbol\ell\cdot\nabla)\mathbf{u}$. **Same equation.** If $\mathbf{B}/\rho$ and $d\boldsymbol\ell$ start parallel, they stay parallel forever. Two fluid elements on the same field line stay on the same field line.

> **Two cautions from [[Strangeway Ch3 Physics of Magnetized Plasmas|Strangeway]] (§3.6.4), worth taking seriously.**
> 1. *The field is frozen to the fluid,* not the other way round. The flow changes the field; "plasma tied to field lines" mixes up cause and effect.
> 2. *Moving field lines are a bookkeeping device.* You can measure plasma velocity, but there's no measurement of a field line's velocity. A uniform field "moving" produces no force on anything.
>
> His example: magnetospheric corotation is not "imposed" by field lines being equipotentials. It is imposed by currents whose $\mathbf{j}\times\mathbf{B}$ force accelerates the plasma, driven by the rotating, collisionally coupled ionosphere.

**Where it breaks:** wherever the right side of the generalized Ohm's law matters, meaning thin current sheets at the magnetopause and in the tail. There, field lines "reconnect": plasma on one field line ends up on another. Reconnection is what lets the solar wind drive the [[Dungey Cycle]].

---

## 6. The closed set

Replace $\mathbf{j}$ using Ampère, replace $\mathbf{E}$ using the ideal Ohm's law, assume isotropic pressure, close the energy equation adiabatically ($\nabla\cdot\mathbf{q}=0$; see [[Moment Equations from the Vlasov Equation]] §5), and drop gravity:

$$
\begin{aligned}
&\frac{\partial\rho}{\partial t} + \nabla\cdot(\rho\mathbf{u}) = 0\\
&\rho\frac{D\mathbf{u}}{Dt} = -\nabla\left(p + \frac{B^2}{2\mu_0}\right) + \frac{(\mathbf{B}\cdot\nabla)\mathbf{B}}{\mu_0}\\
&\frac{\partial\mathbf{B}}{\partial t} = \nabla\times(\mathbf{u}\times\mathbf{B}), \qquad \nabla\cdot\mathbf{B}=0\\
&\frac{D}{Dt}\left(p\rho^{-\gamma}\right) = 0, \qquad \gamma = 5/3
\end{aligned}
$$

That's eight equations in eight unknowns ($\rho$, $p$, three components of $\mathbf{u}$, three of $\mathbf{B}$). $\mathbf{E}$ and $\mathbf{j}$ are now *derived* quantities: $\mathbf{E} = -\mathbf{u}\times\mathbf{B}$ and $\mathbf{j} = \nabla\times\mathbf{B}/\mu_0$. Strangeway calls this the "**B, u** paradigm."

Even so, $\mathbf{E}$ and $\mathbf{j}$ remain the natural variables at the ionospheric boundary, where Pedersen and Hall conductivities connect them.

---

## What we assumed, and where it breaks

- **Slow, non-relativistic flow** ($u\ll c$): needed to drop $\rho_q\mathbf{E}$ and the displacement current.
- **Scales $\gg d_i$, $\rho_i$; frequencies $\ll\Omega_i$**: needed to drop the Hall, pressure and inertia terms. These break in current sheets, in kinetic/inertial Alfvén waves, and in whistler-mode physics.
- **Isotropic pressure**: collisionless plasmas often have $p_\parallel\neq p_\perp$. See CGL on [[MHD]].
- **Fully ionized, no neutrals**: false in the ionosphere. Ion–neutral collisions add drag to the momentum equation and turn the scalar Ohm's law into the Pedersen/Hall conductivity tensor; this will be derived in Part II.
- **Fluid localization**: see [[Moment Equations from the Vlasov Equation]].

---

## Verification

- **Sources agree:**
  - Single-fluid summation: [[Strangeway Ch3 Physics of Magnetized Plasmas|Strangeway]] Eqs. 3.107–3.127.
  - Quasi-neutrality estimate $u^2/c^2$: Strangeway Eq. 3.139.
  - Generalized Ohm's law: Strangeway Eqs. 3.132–3.137 and [[Bellan 2006 Fundamentals of Plasma Physics|Bellan]] §2.5.3.
  - Frozen-in theorem, both parts: Strangeway Eqs. 3.140–3.158 and Bellan §2.5.4.
  - Pressure/tension split: Strangeway Eq. 3.159 and Bellan Eq. 4.65.
  - [[Schunk Nagy 2009 Ionospheres]] Ch. 7 gives the same MHD set.
- **SymPy:**
  - $(\nabla\times\mathbf{B})\times\mathbf{B} = (\mathbf{B}\cdot\nabla)\mathbf{B} - \nabla(B^2/2)$ for an arbitrary field.
  - $\nabla\times(\mathbf{u}\times\mathbf{B}) = (\mathbf{B}\cdot\nabla)\mathbf{u} - (\mathbf{u}\cdot\nabla)\mathbf{B} - \mathbf{B}\nabla\cdot\mathbf{u} + \mathbf{u}\nabla\cdot\mathbf{B}$ for arbitrary fields.
  - The algebra giving $D(\mathbf{B}/\rho)/Dt = (\mathbf{B}/\rho\cdot\nabla)\mathbf{u}$.
  - $D(p\rho^{-5/3})/Dt = 0$.
- **Numerical:** $B/(\mu_0ne) = v_Ad_i$, checked to 9 significant figures. Inertial lengths and $\beta$ computed in Python.
- **Scaling only:** the ordering table gives order-of-magnitude estimates, not exact results. The identities they rest on ($B/\mu_0ne = v_Ad_i$, $k_BT_e/eB = c_s\rho_s$, $m_e/\mu_0ne^2 = d_e^2$) are exact.

## Sources

- [[Strangeway Ch3 Physics of Magnetized Plasmas]] — §3.5.3 (single-fluid MHD), §3.6 (displacement current, generalized Ohm's law, frozen-in theorem, B–u paradigm)
- [[Bellan 2006 Fundamentals of Plasma Physics]] — §2.5 (MHD continuity, motion, Ohm's law, frozen-in flux)
- [[Schunk Nagy 2009 Ionospheres]] — Ch. 7 (MHD)
