---
type: derivation
status: draft
updated: 2026-10-08
sources: 3
tags: [derivations, shocks, bow-shock, MHD, solar-wind, conservation-laws]
prerequisites: "[[Ideal MHD from Kinetic Theory]] (conservation form); [[MHD Wave Modes]] (fast speed)"
next: "[[Chapman-Ferraro Standoff Distance]]"
---

# Rankine-Hugoniot Jump Conditions

**Part III, page 4** of the [[Derivations Index]] · Builds on: [[Ideal MHD from Kinetic Theory]], [[MHD Wave Modes]] · Previous: [[Parker Solar Wind and Spiral]]

## Where we're going

The solar wind arrives at Earth at about 400 km/s. The fastest signal the plasma can carry, the fast magnetosonic wave, travels at only about 70 km/s. So the wind can't "hear" the magnetosphere coming and smoothly divert around it. Instead it passes through a **shock**, a thin layer where it is slowed, compressed, heated and made subsonic, so that it can flow around the obstacle.

What happens *inside* a collisionless shock is a hard kinetic problem (200C Ch. 6 §6.4). But the *jumps* across it don't care. Mass, momentum, energy and magnetic flux all have to be conserved, and that alone fixes the downstream state from the upstream one. Those are the **Rankine–Hugoniot (RH) relations**. We'll derive them, solve the gas-dynamic and perpendicular cases in closed form, and find out why a shock can't compress plasma by more than a factor of 4. Sources: 200C textbook Ch. 6 §§6.2–6.3 and [[Siscoe 1983 Solar System MHD|Siscoe (1983)]] §III.

---

## 1. Conservation laws make jump conditions

Every ideal-MHD equation can be written in **conservation form**, $\partial_tQ + \nabla\cdot\mathbf F = 0$. Work in the shock rest frame, where the flow is steady, and assume the structure varies only along the shock normal $\hat{\mathbf n}$. Then $dF_n/dn = 0$. Integrating across the layer, however thin and however messy inside, gives

$$[F_n]\equiv F_n^{(2)} - F_n^{(1)} = 0.$$

Subscript 1 means upstream and 2 means downstream. Let $\ell$ label the tangential direction in the plane of $\hat{\mathbf n}$ and $\mathbf B_1$. The fluxes from [[Ideal MHD from Kinetic Theory]] then give (200C Eqs. 6.9–6.14; Siscoe Eqs. III.55–63):

$$
\begin{aligned}
&\text{mass:} && [\rho u_n] = 0\\
&\text{normal momentum:} && \left[\rho u_n^2 + p + \frac{B_\ell^2}{2\mu_0}\right] = 0\\
&\text{tangential momentum:} && \left[\rho u_nu_\ell - \frac{B_nB_\ell}{\mu_0}\right] = 0\\
&\text{energy:} && \left[\rho u_n\left(\frac{u^2}{2} + \frac{\gamma}{\gamma-1}\frac p\rho\right) + \frac{B^2u_n - (\mathbf u\cdot\mathbf B)B_n}{\mu_0}\right] = 0\\
&\nabla\cdot\mathbf B = 0: && [B_n] = 0\\
&\text{Faraday (steady):} && [\mathbf E_t] = 0\ \Rightarrow\ [u_nB_\ell - u_\ell B_n] = 0
\end{aligned}
$$

The energy flux combines the flow's kinetic energy, its **enthalpy** $\gamma p/(\gamma-1)$ (not just the internal energy; the extra $p$ is the work done by pressure), and the Poynting flux $\mathbf E\times\mathbf B/\mu_0$ with $\mathbf E = -\mathbf u\times\mathbf B$.

**Free geometric results.** Since $[B_n] = 0$ and $[\mathbf E_t] = 0$, the vectors $\mathbf B_1$, $\mathbf B_2$ and $\hat{\mathbf n}$ must lie in one plane. That's the **coplanarity theorem**, and it gives a single-spacecraft normal (200C Eq. 6.4):

$$\hat{\mathbf n} = \pm\frac{(\mathbf B_1\times\mathbf B_2)\times(\mathbf B_1 - \mathbf B_2)}{|(\mathbf B_1\times\mathbf B_2)\times(\mathbf B_1 - \mathbf B_2)|}.$$

This fails for exactly parallel or perpendicular shocks, where $\mathbf B_1\parallel\mathbf B_2$.

**Classification** (Siscoe §III):

- $u_n = 0$, $B_n\neq0$: **contact discontinuity**. Only the density and temperature jump; the pressure stays continuous.
- $u_n = 0$, $B_n = 0$: **tangential discontinuity**. Only total pressure $p + B^2/2\mu_0$ is continuous. These are common in the solar wind.
- $u_n\neq0$: **shocks**. These dissipate flow energy into heat.

> Every one of these conservation laws also holds with *nothing* changing. So every jump equation has the trivial root "upstream = downstream". Factoring it out is always the first algebraic step below.

---

## 2. The gas-dynamic shock (and the parallel shock)

Set $\mathbf B = 0$, or equivalently take a **parallel** shock with $\mathbf B\parallel\hat{\mathbf n}$. In that case the magnetic terms drop out identically and the field passes through unchanged (Siscoe III.82). Tangential momentum and mass give $[u_\ell] = 0$, so slide along the shock until $u_\ell = 0$.

Normalize with $\rho_1 = u_1 = 1$ and write $p_1 = 1/(\gamma M_1^2)$, where $M_1 = u_1/c_{s1}$ is the upstream **sonic Mach number**. Let $y = u_2/u_1$. Eliminating $\rho_2 = 1/y$ and $p_2 = 1 + p_1 - y$ from the energy equation gives (SymPy-factored)

$$(y - 1)\left[(\gamma+1)M_1^2y - (\gamma-1)M_1^2 - 2\right] = 0.$$

The trivial root is $y = 1$. The **shock** root is (Siscoe III.74–76):

$$\boxed{\frac{u_2}{u_1} = \frac{\rho_1}{\rho_2} = \frac{\gamma-1}{\gamma+1} + \frac{2}{(\gamma+1)M_1^2}},\qquad \frac{p_2}{p_1} = \frac{2\gamma M_1^2 - (\gamma-1)}{\gamma+1}.$$

Read off what it means:

- **Maximum compression.** As $M_1\to\infty$, $\rho_2/\rho_1\to(\gamma+1)/(\gamma-1) = 4$ for $\gamma = 5/3$. No matter how hard you hit it, a shock compresses by **at most 4**. The pressure has no limit; it grows as $M_1^2$. So a strong shock mostly **heats**: the energy that can't go into compression goes into temperature.
- **Strong-shock temperature.** Downstream, $p_2/\rho_2\to2(\gamma-1)u_1^2/(\gamma+1)^2 = \tfrac{3}{16}u_1^2$ for $\gamma = 5/3$ (Siscoe III.77). For 400 km/s solar wind with $p = 2nk_BT$, that's $T_2\approx1.8\times10^6$ K.
- **Downstream is subsonic.** $M_2^2 = [(\gamma-1)M_1^2 + 2]/[2\gamma M_1^2 - (\gamma-1)] < 1$ whenever $M_1 > 1$ (Siscoe III.78). It tends to 1/5 for strong shocks. That's the point of the shock: subsonic flow can carry pressure signals and bend around the obstacle.
- **Entropy picks the direction.** The adiabatic "constant" $p/\rho^\gamma$ rises across the shock only if $M_1 > 1$. For $\gamma = 5/3$ it is 1.04× at $M_1 = 1.5$, 1.76× at $M_1 = 3$, and 0.999× at $M_1 = 0.9$. A rarefaction shock with $M_1 < 1$ would *lower* entropy, which is forbidden. Only compressive shocks from supersonic flow exist.

---

## 3. The perpendicular MHD shock

Now take $\mathbf B\perp\hat{\mathbf n}$, so $B_n = 0$, $B_\ell = B$. This is the cleanest MHD case, and it applies approximately on the **quasi-perpendicular** side of the bow shock ($\theta_{Bn} > 45°$). For a 45° Parker-spiral IMF, the subsolar point itself sits at $\theta_{Bn}\approx45°$. Tangential momentum again gives $[u_\ell] = 0$, and the frozen-in condition $[u_nB] = 0$ means

$$\frac{B_2}{B_1} = \frac{\rho_2}{\rho_1}\equiv X,$$

so **the field is compressed exactly as much as the plasma** (Siscoe III.89). Put the magnetic pressure $B^2/2\mu_0$ into the momentum equation and the Poynting flux $B^2u/\mu_0$ into the energy equation. Then eliminate $p_2$. After factoring out $X = 1$ (SymPy):

$$\boxed{(2-\gamma)X^2 + \left[(\gamma-1)M_A^2 + \gamma(1+\beta_1)\right]X - (\gamma+1)M_A^2 = 0}$$

Here $M_A = u_1/v_{A1}$ and $\beta_1 = 2\mu_0p_1/B_1^2$. This quadratic has exactly one positive root, the physical one; it is Siscoe's Eq. III.90 written for the compression rather than the velocity ratio. Checks:

- **$B\to0$** ($M_A\to\infty$ at fixed sonic Mach $M_1$): it reduces to the gas-dynamic $X = (\gamma+1)M_1^2/[(\gamma-1)M_1^2 + 2]$.
- **$M_A\to\infty$** at fixed $\beta$: $X\to(\gamma+1)/(\gamma-1) = 4$, the same ceiling (Siscoe III.93).
- **Shock vanishes** ($X = 1$) exactly when $M_A^2 = 1 + \gamma\beta_1/2$, i.e. when $u_1 = \sqrt{v_A^2 + c_s^2}$, the perpendicular **fast-mode speed** ([[MHD Wave Modes]]). A perpendicular shock is a steepened fast wave and needs a fast Mach number above 1. Checked numerically for $\beta = 0, 0.5, 2$.

**The field stiffens the plasma.** At a given Mach number, magnetic pressure resists compression, so $X$ is smaller than in the gas-dynamic case. Equivalently, more of the flow energy has to come out as heat.

**Earth's bow shock, typical numbers.** With $n = 5$ cm$^{-3}$, $V = 400$ km/s, $B = 5$ nT and $T = 10^5$ K:

| Quantity | Value |
|---|---|
| $v_A$ | 49 km/s |
| $c_s$ | 52 km/s |
| $v_f$ | 72 km/s |
| $M_A$ | 8.2 |
| $M_{ms}$ (fast Mach) | 5.6 |
| $\beta_1$ | 1.4 |

The perpendicular shock then gives:

- $X = 3.6$ (just below the ceiling of 4);
- $B_2 = 18$ nT;
- $u_2 = 112$ km/s;
- $T_2 = 1.7\times10^6$ K (150 eV), a **17-fold** heating.

This is the hot, dense, slow **magnetosheath** plasma that pushes on the magnetopause ([[Chapman-Ferraro Standoff Distance]]).

---

## 4. Oblique shocks (stated, verified, not derived step by step)

For general $\theta_{Bn}$, the tangential field and velocity both jump. Solving the tangential-momentum and induction equations together gives (200C, below Eq. 6.14b; verified by SymPy)

$$\frac{B_{2\ell}}{B_{1\ell}} = \frac{b - 1}{b - y},\qquad\frac{u_{2\ell}}{u_{1n}} = \frac{\sqrt{bc}\,(y-1)}{b - y},$$

with $y = u_{2n}/u_{1n}$, $b = B_n^2/\mu_0\rho_1u_{1n}^2$ and $c = B_{1\ell}^2/\mu_0\rho_1u_{1n}^2$. The energy equation then becomes a **quartic** in $y$ with the trivial root $y = 1$. Its remaining cubic has up to three physical roots: the **fast, intermediate and slow** shocks, one per MHD wave mode. The fast shock is the bow shock.

Notice the singularity at $y = b$, i.e. when the downstream normal flow equals the normal Alfvén speed. That's the root of the **switch-on shock** behavior near $\theta_{Bn}\approx0$ at low $\beta$, where a tangential field appears downstream out of nothing (200C §6.4.1).

> **Erratum in 200C Eq. 6.15.** I derived the quartic independently and compared it with the textbook's. The $y^4$, $y^3$ and $y^2$ coefficients agree (up to an overall sign). The $y^1$ and $y^0$ coefficients do not. The correct quartic, in the textbook's sign convention, is the printed one **plus $2c(y - 1)$**: the $y$ coefficient gains $+2c$ and the constant loses $2c$, leaving $-(bc + b^2 + 2ab^2d)$.
>
> Two independent checks show the printed form is wrong:
> 1. In the perpendicular limit it doesn't reproduce the compressions from §3 (residuals of 0.05–0.19 where 0 is required).
> 2. For an oblique test case ($a = 0.05$, $b = 0.08$, $c = 0.15$, $\gamma = 5/3$), a brute-force root-find of the six conservation equations gives $y = 0.4852$. The corrected quartic has that as a root; the printed one does not.
>
> The textbook's errata sheet doesn't list this. One of its entries also says the tangential velocity is unchanged across a shock. That holds for gas-dynamic, parallel and perpendicular shocks, but **not** for oblique MHD shocks, as the $u_{2\ell}$ formula above shows (the test case gives $u_{2\ell}/u_{1n} = 0.14$).

**De Hoffmann–Teller frame.** For an oblique shock you can slide along the shock surface at $\mathbf V_{HT} = \hat{\mathbf n}\times(\mathbf u_1\times\mathbf B_1)/(\hat{\mathbf n}\cdot\mathbf B_1)$ until the flow is parallel to $\mathbf B$ on both sides. Then $\mathbf E = 0$, and particle energy is conserved in that frame (200C §6.3). This frame is the natural one for shock-reflected ions and foreshock beams.

---

## What we assumed, and where it breaks

- **Isotropic pressure, fixed $\gamma$.** With $p_\parallel\neq p_\perp$ there is one more unknown than there are equations. The RH relations alone can't tell you how the heat splits between parallel and perpendicular (Siscoe §III), so it has to come from kinetics or observation.
- **Single fluid.** RH gives the *total* heating but not how it divides between ions and electrons. At Earth's bow shock, ions are heated much more than electrons (200C §6.7 discussion).
- **Planar and steady.** Real quasi-parallel shocks are reforming and turbulent, and the foreshock upstream is full of reflected ions and waves (200C §§6.8–6.9). RH applies to averages taken far enough on each side.
- **Collisionless dissipation.** RH requires dissipation but doesn't supply it. In collisionless plasmas it comes from wave–particle interactions and ion reflection. Above a **critical Mach number**, resistivity alone can't supply the dissipation, and the shock becomes "supercritical" with an overshoot (200C §6.6).

---

## Verification

- **Sources agree.**
  - Conservation-form jumps, coplanarity normal, de Hoffmann–Teller frame: 200C textbook Ch. 6 §§6.2–6.3, Eqs. 6.1–6.26.
  - Gas-dynamic shock, $M_2 < 1$, entropy, parallel and perpendicular cases, the 4× limit: [[Siscoe 1983 Solar System MHD|Siscoe]] §III, Eqs. III.67–93.
  - The 4× limit at $\theta_{Bn} = 90°$ for $\gamma = 5/3$: also 200C Fig. 6.4 discussion.
- **SymPy.**
  - Gas-dynamic energy equation factored as $(y-1)\times$(shock root), giving $u_2/u_1$, $p_2/p_1$ and $M_2^2$ exactly as in Siscoe.
  - Strong-shock $p_2/\rho_2 = 2(\gamma-1)u_1^2/(\gamma+1)^2$.
  - Perpendicular quadratic.
  - Oblique $B_{2\ell}$ and $u_{2\ell}$ matching 200C.
  - Oblique quartic: discrepancy with 200C Eq. 6.15 located in the $c$ terms.
- **Numerical.**
  - Entropy ratios.
  - The $X = 1$ fast-mode threshold for three values of $\beta$.
  - Brute-force solve of the full oblique system (residual $2\times10^{-12}$).
  - The bow-shock numbers above.

## Sources

- 200C textbook Ch. 6, *Collisionless shocks* (`Atlas/Texts/Textbooks/200C Textbook/Ch6_Collisionless_Shocks.pdf`), and errata (`Textbook Changes.pdf`)
- [[Siscoe 1983 Solar System MHD]] — §III (MHD discontinuities and shocks)
- [[Ideal MHD from Kinetic Theory]] — conservation form of the MHD equations
