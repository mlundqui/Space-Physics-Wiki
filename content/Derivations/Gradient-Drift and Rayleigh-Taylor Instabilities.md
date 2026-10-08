---
type: derivation
status: draft
updated: 2026-10-08
sources: 2
tags: [derivations, ionosphere, instabilities, gradient-drift, rayleigh-taylor, polar-cap-patches, equatorial-spread-F]
prerequisites: "[[Pedersen and Hall Conductivity]]; [[Electrostatic Dynamo Equation]]"
next: "Part II continues in [[Derivations Index]]"
---

# Gradient-Drift and Rayleigh-Taylor Instabilities

**Part II (ionosphere), page 7** of the [[Derivations Index]] · Previous: [[Electrostatic Dynamo Equation]] · Concept page: [[Ionospheric Instabilities]]

## Where we're going

A [[Polar Cap Patch]] drifting across the polar cap doesn't stay smooth. Its **trailing edge** breaks up into structure from tens of km down to meters, and that structure is what scintillates GPS signals. At the magnetic equator after sunset, the bottomside F layer erupts into plumes (**equatorial spread F**).

Both are the same instability. A density gradient in a plasma that carries current across $\mathbf{B}$ is unstable if the current flows the "wrong" way relative to the gradient. We'll derive:

1. the **gradient-drift instability (GDI)**, driven by an electric field (or by the plasma flowing relative to the neutrals);
2. the **Rayleigh–Taylor (RT) instability**, driven by gravity.

They turn out to be one formula with one substitution. The derivation follows AOS 205B Lecture 10.2 (course notes), checked against [[Kelley Earth's Ionosphere|Kelley]] Ch. 4 and Ch. 6.

---

## 1. The physical picture

Take a high-density slab in the F region with a uniform field $\mathbf{E}_0$ in the neutral frame. The whole slab $\mathbf{E}\times\mathbf{B}$-drifts at $\mathbf{u}_0 = \mathbf{E}_0\times\hat{\mathbf b}/B$. Ripple one edge with a small sinusoidal perturbation.

Because Pedersen conductivity is proportional to density, the Pedersen current $\sigma_P\mathbf{E}_0$ is larger inside the ripples that bulge into the slab than in those that bulge out. The current can't diverge, so **charge piles up on the ripple flanks**, and that charge creates a perturbation field $\delta\mathbf{E}$. Its $\delta\mathbf{E}\times\mathbf{B}$ drift either:

- pushes the depleted fingers further *into* the slab and the dense fingers further *out*, so the ripple **grows** (the trailing edge); or
- pushes them back, so the ripple **flattens** (the leading edge).

---

## 2. Equations

The F region has $\kappa_i\gg1$ ([[Pedersen and Hall Conductivity]] §2), so:

- **ions** $\mathbf{E}\times\mathbf{B}$-drift: $\mathbf{u} = \mathbf{E}\times\hat{\mathbf b}/B$ (Hall terms neglected in the F region);
- **current** is Pedersen: $\mathbf{J} = \sigma_P\mathbf{E}$, with $\sigma_P\propto n$.

Then there are two conservation laws:

$$\frac{\partial n}{\partial t} + \nabla\cdot(n\mathbf{u}) = 0\quad(\text{ions}),\qquad\nabla\cdot\mathbf{J} = 0\quad(\text{charge}).$$

**Linearize.** Write $n = n_0 + \delta n$, $\mathbf{E} = \mathbf{E}_0 - \nabla\delta\phi$, with relative perturbation $n_1 = \delta n/n_0$ and gradient vector $\mathbf{G} = \nabla n_0/n_0$, which points toward higher density. The zeroth-order equations require $(\nabla+\mathbf{G})\cdot\mathbf{u}_0 = 0$ and $(\nabla+\mathbf{G})\cdot\mathbf{E}_0 = 0$. Using those, the first-order equations become

$$\frac{\partial n_1}{\partial t} + \mathbf{u}_0\cdot\nabla n_1 + (\nabla+\mathbf{G})\cdot\delta\mathbf{u} = 0,\qquad \mathbf{E}_0\cdot\nabla n_1 + (\nabla+\mathbf{G})\cdot\delta\mathbf{E} = 0.$$

The second equation says the perturbed Pedersen current $\sigma_P^0n_1\mathbf{E}_0$ must be balanced by the polarization current $\sigma_P^0\delta\mathbf{E}$.

**Fourier transform** (local approximation: $\mathbf{G}$ treated as constant over a wavelength), with everything $\propto e^{i(\mathbf{k}\cdot\mathbf{r}-\omega t)}$, $\delta\mathbf{E} = -i\mathbf{k}\,\delta\phi$, $\delta\mathbf{u} = \delta\mathbf{E}\times\hat{\mathbf b}/B$. The current equation gives the potential the density perturbation creates:

$$\delta\phi_k = \frac{-i\,(\mathbf{k}\cdot\mathbf{E}_0)}{k^2 - i\,\mathbf{k}\cdot\mathbf{G}}\,n_k.$$

Substitute into continuity, using $\mathbf{k}\cdot(\mathbf{k}\times\hat{\mathbf b}) = 0$:

$$\omega = \mathbf{k}\cdot\mathbf{u}_0 - \frac{\mathbf{G}\cdot(\mathbf{k}\times\hat{\mathbf b})}{B}\,\frac{\delta\phi_k}{n_k}.$$

The exact result, verified by SymPy, is

$$\omega_r = \mathbf{k}\cdot\mathbf{u}_0 - \frac{\left[\mathbf{G}\cdot(\mathbf{k}\times\hat{\mathbf b})\right](\mathbf{k}\cdot\mathbf{E}_0)(\mathbf{k}\cdot\mathbf{G})}{B\left[k^4 + (\mathbf{k}\cdot\mathbf{G})^2\right]},\qquad \gamma = \frac{\left[\mathbf{G}\cdot(\mathbf{k}\times\hat{\mathbf b})\right](\mathbf{k}\cdot\mathbf{E}_0)\,k^2}{B\left[k^4 + (\mathbf{k}\cdot\mathbf{G})^2\right]}.$$

**Short-wavelength limit** ($kL\gg1$, the natural regime for the local approximation):

$$\boxed{\gamma\approx\frac{\left[\mathbf{G}\cdot(\mathbf{k}\times\hat{\mathbf b})\right](\mathbf{k}\cdot\mathbf{E}_0)}{B\,k^2}}$$

The wave is unstable when $\mathbf{G}\cdot(\mathbf{k}\times\hat{\mathbf b})$ and $\mathbf{k}\cdot\mathbf{E}_0$ have the **same sign**.

### The most unstable geometry

Take $\mathbf{k}\parallel\mathbf{E}_0$. Then $\mathbf{k}\times\hat{\mathbf b}$ points along $\mathbf{u}_0$, and

$$\boxed{\gamma = \mathbf{u}_0\cdot\mathbf{G} = \frac{E_0}{BL}\quad\text{when the gradient points along the drift}}$$

with $L = 1/|\mathbf{G}|$. This is Kelley's Eq. 6.16a, $\gamma = E'/BL$.

- **Trailing edge:** the density *increases* in the direction of drift, $\mathbf{G}\parallel\mathbf{u}_0$. **Unstable.**
- **Leading edge:** $\mathbf{G}$ is antiparallel to $\mathbf{u}_0$. **Stable.**

**Numbers for a patch.** A patch drifting at $E_0/B = 500$ m/s with a 50 km trailing-edge gradient gives $\gamma = 10^{-2}$ s$^{-1}$, an e-folding time of about 100 s. That is fast compared with the roughly 1 hour it takes a patch to cross the polar cap. This is why trailing edges are reliably structured.

> **Frame matters.** $\mathbf{E}_0$ here is the field in the **neutral** frame, $\mathbf{E}' = \mathbf{E} + \mathbf{u}_n\times\mathbf{B}$. Equivalently, $\mathbf{u}_0$ is the plasma drift *relative to the neutral wind*. A patch that drifts along with the wind isn't GDI-unstable, whatever its speed over the ground. Neutral wind can also drive the instability by itself (Kelley Ch. 6).

---

## 3. Rayleigh–Taylor: same instability, gravity as the driver

Gravity also pushes current across $\mathbf{B}$. With $\kappa_i\gg1$, ions gravity-drift at $(\mathbf{g}\times\hat{\mathbf b})/\Omega_i$, and electrons essentially don't drift, so there's a current

$$\mathbf{J}_g = \frac{nm_i}{B}\,\mathbf{g}\times\hat{\mathbf b}.$$

In the F region, $\sigma_P = nm_i\nu_{in}/B^2$ (Kelley Eq. 2.40b), so this current is exactly

$$\mathbf{J}_g = \sigma_P\,\mathbf{E}_g,\qquad\mathbf{E}_g\equiv\frac{B}{\nu_{in}}\,\mathbf{g}\times\hat{\mathbf b}.$$

Gravity acts **like an effective electric field** in the current equation, proportional to density through $\sigma_P$ just as $\sigma_P\mathbf{E}_0$ was. It doesn't move the plasma as a whole (the Doppler term $\mathbf{k}\cdot\mathbf{u}_0$ is unchanged), so the growth rate is the GDI result with $\mathbf{E}_0\to\mathbf{E}_0 + \mathbf{E}_g$.

**Equatorial geometry.** $\hat{\mathbf b}$ points north and horizontal, $z$ is up, $\mathbf{g} = -g\hat{\mathbf z}$, and $\mathbf{E}_g$ points **east**. On the bottomside the density increases upward, $\mathbf{G} = \hat{\mathbf z}/L$. For $\mathbf{k}$ east–west:

$$\boxed{\gamma_{RT} = \frac{g}{\nu_{in}L}}\qquad\text{and, with an eastward }E_0:\qquad\gamma = \frac1L\left(\frac{E_0}{B} + \frac{g}{\nu_{in}}\right)$$

These are Kelley Eq. 4.16 and the "generalized Rayleigh–Taylor" form. Kelley (p. 150) generalizes "by replacing $g/\nu_{in}$ with $g/\nu_{in} + E'_{x0}/B$ … where $E'_{x0}$ is the zonal component of the electric field in the neutral frame," noting that an eastward field "drives a Pedersen current to the east," parallel to the gravity-driven current.

This is literally a heavy fluid sitting on top of a light one. The bottomside is unstable, and the topside, where density decreases upward, is stable. Two things make the post-sunset equator the worst case:

- the **pre-reversal enhancement** raises the layer, where $\nu_{in}$ is small and $g/\nu_{in}$ is large;
- the **eastward $E$** adds to the gravity term.

See [[Equatorial Ionosphere]].

---

## What we assumed, and where it breaks

- **No E-region loading.** If field lines connect to a conducting E region (sunlit, or under aurora), the polarization charge leaks away through E-region Pedersen current. The growth rate is reduced by about $\Sigma_P^F/(\Sigma_P^F + \Sigma_P^E)$. This "E-region shorting" is why patches structure more easily in the dark polar cap. Kelley discusses E-region loading and shorting qualitatively (Ch. 4 p. ~151; Ch. 10). The specific factor $\Sigma_P^F/(\Sigma_P^F+\Sigma_P^E)$ is the standard flux-tube-integrated form from the literature, quoted here without derivation and **not checked against a vault source**.
- **Local approximation** ($kL\gg1$), no diffusion. Cross-field diffusion adds $-k^2D_\perp$ (Kelley Eq. 4.26), which stabilizes the smallest scales.
- **Linear theory.** Real patch edges reach the nonlinear stage and cascade to small scales. That cascade is the source of the multi-scale irregularity spectrum seen by beacons and RISR-N ([[RISR-N]], beacon conjunctions).
- **$\kappa_i\gg1$, no Hall terms.** Fine in the F region. In the E region, the Hall terms and electron dynamics give the gradient-drift *and* Farley–Buneman instabilities, which are a separate topic.

---

## Verification

- **Sources agree.**
  - Linearized continuity and current closure, $\delta\phi_k$, the dispersion relation, the short-wavelength growth rate, and the trailing/leading-edge criterion: AOS 205B Lecture 10.2 (course notes).
  - [[Kelley Earth's Ionosphere|Kelley]] Eq. 6.16a ($\gamma = E'/BL$), Eqs. 4.15–4.16 ($\gamma = g/L\nu_{in}$), the generalized RT substitution $g/\nu_{in}\to g/\nu_{in} + E_{x0}/B$, and Eq. 4.26 (diffusive damping).
- **SymPy.**
  - Exact $\omega_r$ and $\gamma$, without the short-wavelength approximation, solved from the linearized system.
  - $\gamma = \mathbf{u}_0\cdot\mathbf{G}$ for $\mathbf{k}\parallel\mathbf{E}_0$.
  - The gravity current equals $\sigma_P\mathbf{E}_g$ with $\sigma_P = nm_i\nu_{in}/B^2$.
  - $\gamma_{RT} = g/(\nu_{in}L)$ in equatorial geometry, with $\mathbf{E}_g$ pointing east.
- **Not verified in vault sources:** the explicit E-region loading factor $\Sigma_P^F/(\Sigma_P^F+\Sigma_P^E)$. Kelley discusses loading qualitatively, but I did not find this exact expression there.

## Sources

- AOS 205B Lecture 10.2, *Gradient Drift Instability* (`Atlas/Courses/AOS 205B/Lecture10_2_Instabilities.pdf`) — course notes, primary derivation
- [[Kelley Earth's Ionosphere]] — Ch. 4 (Rayleigh–Taylor, Eqs. 4.14–4.26), Ch. 6 (high-latitude gradient drift, Eq. 6.16a), Ch. 10
