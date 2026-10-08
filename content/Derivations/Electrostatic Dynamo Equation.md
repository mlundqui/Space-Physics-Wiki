---
type: derivation
status: draft
updated: 2026-10-07
sources: 2
tags: [derivations, ionosphere, electrodynamics, dynamo, convection, field-aligned-currents]
prerequisites: "[[Pedersen and Hall Conductivity]]; [[Ideal MHD from Kinetic Theory]] §2 (∇·j = 0)"
next: "Part II continues in [[Derivations Index]]"
---

# Electrostatic Dynamo Equation

**Part II (ionosphere), page 6** of the [[Derivations Index]] · Previous: [[Frictional and Joule Heating]] · Concept page: [[Ionospheric Dynamo]]

## Where we're going

Where do ionospheric electric fields come from? There are two drivers:

- the **magnetosphere** pushes current down field lines ([[Field-Aligned Currents]]);
- the **neutral wind** pushes on ions and drags current through the conducting layer.

In either case the ionosphere must arrange an electric field so that **current is conserved**. That one requirement, $\nabla\cdot\mathbf{J} = 0$, plus the conductivity tensor, gives a single elliptic equation for the electrostatic potential: the **dynamo equation**. Solve it and you have the convection pattern that carries [[Polar Cap Patch|patches]], the electric field [[RISR-N]] measures, and the [[Joule Heating]].

This follows AOS 205B Lecture 6.2 (course notes), with every sign re-derived.

---

## 1. Two approximations

**(a) Currents close.** Take the divergence of Ampère's law, $\nabla\cdot(\nabla\times\mathbf{B}) = 0 = \mu_0\nabla\cdot\mathbf{J} + \mu_0\varepsilon_0\partial_t\nabla\cdot\mathbf{E}$. That's charge conservation. At non-relativistic speeds the displacement current drops out ([[Ideal MHD from Kinetic Theory]] §2), leaving

$$\nabla\cdot\mathbf{J} = 0.$$

Current can't pile up anywhere. It has to flow in closed loops.

**(b) Electrostatic fields.** If $\partial\mathbf{B}/\partial t\to0$, then $\nabla\times\mathbf{E} = 0$ and $\mathbf{E} = -\nabla\phi$. When is that fair? Changes in $\mathbf{E}$ propagate along $\mathbf{B}$ as Alfvén waves. "Electrostatic" means the Alfvén transit time is short compared with the timescale of interest, i.e. infinitely stiff field lines that can't bend. That fails for fast transients (minutes or less), where [[Alfvén Waves]] carry the signal.

---

## 2. The 3-D equation

Write Ohm's law from [[Pedersen and Hall Conductivity]] §3, separating the part driven by $\phi$ from everything else:

$$\mathbf{J} = \boldsymbol\sigma\cdot(-\nabla\phi) + \underbrace{\boldsymbol\sigma\cdot(\mathbf{u}_n\times\mathbf{B}) + \mathbf{J}_{\text{grav}} + \mathbf{J}_{\text{diamag}}}_{\mathbf{J}_0\ \text{(known if }\mathbf{u}_n,\mathbf{g},\nabla p\text{ are given)}}.$$

Then $\nabla\cdot\mathbf{J} = 0$ becomes

$$\boxed{\nabla\cdot(\boldsymbol\sigma\cdot\nabla\phi) = \nabla\cdot\mathbf{J}_0}$$

an inhomogeneous, linear, elliptic PDE for $\phi$. It's Poisson's equation with an anisotropic "permittivity" $\boldsymbol\sigma$, and like any elliptic problem it needs boundary conditions.

---

## 3. Two warm-up examples: polarization fields

Before the general case, build intuition with slabs. In both, a wind tries to drive current across a conductivity boundary it can't cross. Charge accumulates at the edges, and the **polarization field** that results cancels the blocked current.

**F-region slab dynamo.** Take a layer of high Pedersen conductivity (no Hall) between insulating regions, with a horizontal wind $\mathbf{u}_n$ across $\mathbf{B}$. The wind drives $\mathbf{J}_0 = \sigma_P(\mathbf{u}_n\times\mathbf{B})$ vertically, but that current can't leave the slab. So a polarization field builds up until the total current vanishes:

$$\mathbf{E}_p = -\mathbf{u}_n\times\mathbf{B},\qquad\mathbf{J} = \sigma_P(\mathbf{E}_p + \mathbf{u}_n\times\mathbf{B}) = 0.$$

Then $\mathbf{E}_p\times\mathbf{B}/B^2 = \mathbf{u}_n$ (check: $-(\mathbf{u}_n\times\mathbf{B})\times\mathbf{B}/B^2 = \mathbf{u}_{n\perp}$). **The plasma ends up drifting with the wind.** This is the F-region dynamo. At night, when the E region (which would otherwise short out $\mathbf{E}_p$) disappears, it sets the post-sunset equatorial fields ([[Equatorial Ionosphere]]).

**Cowling channel.** Now include Hall conductivity and let the channel be bounded in $y$, with a wind along $y$ and $\mathbf{B}$ along $\hat{\mathbf{z}}$. The wind drives a Pedersen current along $x$ (allowed) and a Hall current along $y$ (blocked). A polarization field $E_p$ along $y$ builds up until $J_y = 0$:

$$0 = \sigma_Hu_nB - \sigma_PE_p\;\Rightarrow\;E_p = \frac{\sigma_H}{\sigma_P}u_nB.$$

But $E_p$ itself drives a Hall current along $x$, which adds to the Pedersen current:

$$J_x = \left(\sigma_P + \frac{\sigma_H^2}{\sigma_P}\right)u_nB\equiv\sigma_Cu_nB,\qquad\boxed{\sigma_C = \sigma_P + \frac{\sigma_H^2}{\sigma_P}}$$

The **Cowling conductivity** can be much larger than either $\sigma_P$ or $\sigma_H$ when $\sigma_H\gg\sigma_P$. That's why the **equatorial electrojet** (a natural Cowling channel, bounded above and below by the conductivity profile) carries intense eastward current in a narrow band at the dip equator.

---

## 4. Equipotential field lines: the 2-D dynamo equation

Above the E region, $\sigma_\parallel\gg\sigma_P$ by more than $10^4$ ([[Pedersen and Hall Conductivity]] §3). Take the limit $\sigma_\parallel\to\infty$, so $E_\parallel\to0$ and $\phi$ is **constant along each field line**. The problem collapses to two dimensions, $\phi(x,y)$, with $z$ along $\mathbf{B}$.

Split the divergence, $\nabla_\perp\cdot\mathbf{J}_\perp = -\partial J_\parallel/\partial s$, and integrate through the thin conducting layer from its top to its bottom. Below the ionosphere no current flows (the atmosphere is an insulator), so

$$\int\nabla_\perp\cdot\mathbf{J}_\perp\,ds = j_{\text{in}},$$

where $j_{\text{in}}$ is the field-aligned current density **flowing into the ionosphere from above**. Because $\phi$ doesn't depend on height, it comes outside the integral, and only height-integrated quantities remain:

$$\Sigma_{P,H} = \int\sigma_{P,H}\,ds,\qquad\mathbf{K}_0 = \int\boldsymbol\sigma_\perp\cdot(\mathbf{u}_n\times\mathbf{B})\,ds\quad(\text{wind-driven sheet current}).$$

With $\mathbf{J}_\perp^{\text{sheet}} = \Sigma_P\mathbf{E}_\perp - \Sigma_H\,\mathbf{E}_\perp\times\hat{\mathbf b} + \mathbf{K}_0$ and $\mathbf{E}_\perp = -\nabla_\perp\phi$, expanding the divergence (and using $\nabla\cdot(\nabla\phi\times\hat{\mathbf b}) = 0$ for a uniform $\hat{\mathbf b}$) gives

$$\boxed{\nabla_\perp\cdot(\Sigma_P\nabla_\perp\phi) - \nabla_\perp\Sigma_H\cdot(\nabla_\perp\phi\times\hat{\mathbf b}) = -j_{\text{in}} + \nabla_\perp\cdot\mathbf{K}_0}$$

Read it as **ionospheric response = −(magnetospheric driving) + (neutral-wind driving).** With $j_{\text{in}}$ defined as current *into* the ionosphere, this form holds in both hemispheres. In the north $\hat{\mathbf b}$ points down, so $j_{\text{in}} = J_{\text{FAC}}$ (positive along $\mathbf{B}$). In the south, $j_{\text{in}} = -J_{\text{FAC}}$. That is the $\mp$ in the lecture notes.

**Two features of the Hall term:**

- Hall conductance enters **only through its gradient**. With uniform $\Sigma_H$, Hall currents flow in closed loops (along equipotentials) and never connect to FACs.
- Hall gradients (auroral arcs, terminator crossings) *do* couple to FACs. This is the "E-region modification" behind feedback instabilities.

**Uniform conductance and no wind** reduce it to Poisson's equation:

$$\nabla_\perp^2\phi = -\frac{j_{\text{in}}}{\Sigma_P}.$$

That's electrostatics with $j_{\text{in}}/\Sigma_P$ playing the role of charge density over $\varepsilon_0$, and it can be solved with every trick from undergraduate E&M.

---

## 5. Worked pictures

**Auroral arc (north, uniform Σ).** An arc sits on **upward** FAC ($j_{\text{in}} < 0$), so $\Sigma_P\nabla\cdot\mathbf{E} = j_{\text{in}} < 0$, and **$\mathbf{E}$ points into the arc**. Pedersen current flows along $\mathbf{E}$ into the arc and feeds the upward FAC. The return (downward) current region next to it has diverging $\mathbf{E}$. The Hall currents circulate around each FAC sheet without connecting to it. This matches Lecture 6.2's sketch.

**Two-cell polar convection (north).** Region 1 FACs flow down on the dawn side and up on the dusk side ([[Field-Aligned Currents]]). So $\phi$ has a **maximum on the dawn side** and a **minimum on the dusk side**, and $\mathbf{E}$ points dawn→dusk across the polar cap. Plasma $\mathbf{E}\times\mathbf{B}$-drifts along equipotentials:

- antisunward over the polar cap;
- sunward at lower latitudes on both flanks.

With $\mathbf{B}$ pointing down, the flow circulates **counterclockwise around the dawn potential maximum** and **clockwise around the dusk minimum**, viewed from above the north pole. The **cross-polar-cap potential** is $\Phi_{\text{PC}} = \phi_{\max} - \phi_{\min}$.

**Mid-latitude conjugate coupling.** On closed field lines, both footpoints share $\phi$, and with no magnetospheric diversion the FAC leaving one hemisphere enters the other. Adding the two hemispheres' equations:

$$\nabla_\perp\cdot\left[(\boldsymbol\Sigma^N + \boldsymbol\Sigma^S)\cdot\nabla_\perp\phi\right] = \nabla_\perp\cdot(\mathbf{K}_0^N + \mathbf{K}_0^S).$$

Winds in **either** hemisphere set the field in **both**, weighted by both hemispheres' conductances.

---

## What we assumed, and where it breaks

- **Electrostatic** ($\partial_t\mathbf{B}\approx0$). Fails for transients faster than about an Alfvén bounce time; the response then propagates as Alfvén waves.
- **Equipotential field lines** ($\sigma_\parallel\to\infty$). Fails where $E_\parallel$ develops: the auroral acceleration region ([[Knight Relation]]). There the magnetospheric and ionospheric potentials decouple.
- **Thin-shell, height-integrated.** Fine for the E region. The F-region dynamo needs the vertical structure (§3).
- **Uniform $\hat{\mathbf b}$, flat geometry.** Real calculations use magnetic apex coordinates and a spherical shell ([[Magnetic Coordinate Systems]]).

---

## Verification

- **Sources agree.** Lecture 6.2 (course notes) gives every step: $\nabla\cdot\mathbf{J} = 0$, the electrostatic limit, the 3-D elliptic equation, the slab dynamo, the Cowling channel, the equipotential reduction, conductances, the tensor-free form, Poisson's limit, the arc and two-cell examples, and conjugate coupling. The Cowling conductivity and slab dynamo are standard textbook results ([[Kelley Earth's Ionosphere|Kelley]] Ch. 3, not re-read here).
- **SymPy.**
  - With $\mathbf{J} = \Sigma_P\mathbf{E} - \Sigma_H\,\mathbf{E}\times\hat{\mathbf b}$ and $\mathbf{E} = -\nabla\phi$, the identity $\nabla\cdot(\Sigma_P\nabla\phi) - \nabla\Sigma_H\cdot(\nabla\phi\times\hat{\mathbf b}) = -\nabla\cdot\mathbf{J}_\perp$ holds for arbitrary $\phi$, $\Sigma_P$ and $\Sigma_H$, with $\hat{\mathbf b} = \mp\hat{\mathbf{z}}$ (both hemispheres).
  - Cowling: $J_x/(u_nB) = \sigma_P + \sigma_H^2/\sigma_P$.
  - Northern-hemisphere $\mathbf{E}\times\mathbf{B}$ around a potential maximum is counterclockwise viewed from above.
- **By hand.** Arc convergence sign; slab-dynamo drift equals the wind.
- **Errors found on the concept page [[Ionospheric Dynamo]]** (corrected there, 2026-10-07): the master equation had an overall sign error for "downward" $J_\parallel$, and the dawn and dusk cell rotation senses were reversed.

## Sources

- AOS 205B Lecture 6.2, *Electrostatic Dynamo Theory* (`Atlas/Courses/AOS 205B/Lecture6_2_DynamoTheory.pdf`) — course notes, primary derivation
- [[Kelley Earth's Ionosphere]] — Ch. 3 (electric-field generation, mapping, electrojet); cross-reference only
