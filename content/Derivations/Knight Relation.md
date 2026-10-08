---
type: derivation
status: draft
updated: 2026-10-07
sources: 4
tags: [derivations, aurora, field-aligned-currents, auroral-acceleration, kinetic-theory]
prerequisites: "[[Adiabatic Invariants and Magnetic Mirrors]]; [[Moment Equations from the Vlasov Equation]] §1 (Liouville)"
next: "[[Derivations Index]]"
---

# Knight Relation

**Part III (magnetosphere–ionosphere coupling)** of the [[Derivations Index]] · Builds on: [[Adiabatic Invariants and Magnetic Mirrors]]

## Where we're going

Upward field-aligned current means *downgoing electrons*. Those electrons have to come from the hot, tenuous magnetospheric plasma at the top of the field line. Here's the problem: almost all of them **mirror** before they reach the ionosphere (the loss cone is tiny; see [[Adiabatic Invariants and Magnetic Mirrors]] §2). So there's a maximum current the magnetosphere can deliver *for free*. Ask for more, and the system has to build a parallel potential drop $\Phi$ that pushes more electrons into the loss cone.

The **Knight relation** (Knight 1973) is the resulting current–voltage law, $j_\parallel(\Phi)$. It is the backbone of the quasi-static, inverted-V picture of [[Auroral Acceleration]]. We'll derive it, check every limit, and then sort out the several different-looking versions that circulate in papers (and that circulated in this wiki).

---

## 1. Setup: two effects of a converging field

Label the magnetospheric source region "$m$" (field $B_m$) and the top of the ionosphere "$I$" (field $B_I$). Define the **mirror ratio**

$$R \equiv \frac{B_I}{B_m} \gg 1.$$

On auroral field lines $R$ is of order $10$–$10^3$, depending on where the source sits.

**Effect 1: magnetic focusing.** In a steady state, $\nabla\cdot\mathbf{j}=0$. Along a thin flux tube carrying only parallel current, $j_\parallel A$ is constant, and since $A\propto1/B$, $j_\parallel/B$ is constant. Whatever current density leaves the source arrives at the ionosphere amplified by $R$:

$$j_\parallel^I = R\,j_\parallel^m.$$

**Effect 2: the mirror.** An electron starting at the source with parallel energy $\mathcal{E}_\parallel$ and perpendicular energy $\mathcal{E}_\perp$ conserves $\mu$, so $\mathcal{E}_\perp^I = R\,\mathcal{E}_\perp^m$. It also gains $e\Phi$ from the downward-accelerating potential drop. Energy conservation then gives

$$\mathcal{E}_\parallel^I = \mathcal{E}_\parallel^m + e\Phi - (R-1)\,\mathcal{E}_\perp^m.$$

The electron arrives only if $\mathcal{E}_\parallel^I > 0$:

$$\boxed{\mathcal{E}_\perp^m < \frac{\mathcal{E}_\parallel^m + e\Phi}{R-1}}$$

This is the **potential-modified loss cone**. With $\Phi = 0$ it is the ordinary loss cone. A positive $\Phi$ *widens* it: electrons that would have mirrored now get through.

> *A subtlety about where the potential sits.* We've assumed every particle that satisfies the endpoint condition actually gets through. That can fail if the combined "effective potential" $U(s) = -e\phi(s) + \mu B(s)$ has a maximum *partway* down the field line (Whipple 1977, via Gunell et al. 2013). Knight showed the current is "independent of the behaviour of the electric potential as long as this does not have a significant minimum." The *shape* of $\phi(s)$ matters for trapping particles, but not, to good approximation, for the current.

---

## 2. Count the current

Only downgoing electrons in the modified loss cone carry net current. Mirrored electrons come back up and cancel their own contribution. Use cylindrical velocity coordinates, $d^3v = v_\perp\,dv_\perp\,dv_\parallel\,d\gamma = m^{-2}\,d\mathcal{E}_\perp\,d\mathcal{E}_\parallel\,d\gamma/v_\parallel$, and take an **isotropic Maxwellian** source of density $n$ and temperature $T$:

$$f_m = n\left(\frac{m_e}{2\pi k_BT}\right)^{3/2}e^{-(\mathcal{E}_\parallel+\mathcal{E}_\perp)/k_BT}.$$

The electron number flux at the source is $\int v_\parallel f\,d^3v$ over the loss cone. Since $v_\parallel\,dv_\parallel = d\mathcal{E}_\parallel/m_e$, the factor $v_\parallel$ cancels neatly:

$$\Gamma = \frac{2\pi}{m_e^2}\,n\left(\frac{m_e}{2\pi k_BT}\right)^{3/2}\int_0^\infty d\mathcal{E}_\parallel\int_0^{(\mathcal{E}_\parallel+e\Phi)/(R-1)}d\mathcal{E}_\perp\;e^{-(\mathcal{E}_\parallel+\mathcal{E}_\perp)/k_BT}.$$

Do the inner integral, $k_BT\left[1 - e^{-(\mathcal{E}_\parallel+e\Phi)/(R-1)k_BT}\right]$, then the outer one. The second term gives $k_BT\,\frac{R-1}{R}\,e^{-e\Phi/(R-1)k_BT}$. Collecting the prefactors, $n(m_e/2\pi k_BT)^{3/2}\cdot2\pi(k_BT)^2/m_e^2 = n\sqrt{k_BT/2\pi m_e}$, so

$$\Gamma = n\sqrt{\frac{k_BT}{2\pi m_e}}\left[1 - \frac{R-1}{R}\,e^{-e\Phi/(R-1)k_BT}\right].$$

Multiply by $e$ (current) and by $R$ (focusing) to get the ionospheric current density:

$$\boxed{j_\parallel = j_0\left[R - (R-1)\exp\!\left(-\frac{e\Phi}{(R-1)\,k_BT}\right)\right], \qquad j_0 = e\,n\sqrt{\frac{k_BT}{2\pi m_e}}}$$

$j_0$ is the one-way **thermal current** of the source: the downgoing electron flux through a plane in a Maxwellian, times $e$. (It is sometimes called the "Bohm current" in course notes.) Strangeway writes the same result as $j_0R\{1 - (1 - 1/R)\exp[\cdots]\}$, which is identical.

The relation inverts cleanly, giving the voltage needed to drive a given current:

$$e\Phi = (R-1)\,k_BT\,\ln\!\left(\frac{R-1}{R - j_\parallel/j_0}\right).$$

---

## 3. The limits: where all the published forms come from

Let $x = e\Phi/k_BT$.

| Regime | Result | Meaning |
|---|---|---|
| $x = 0$ | $j_\parallel = j_0$ | the most current the magnetosphere supplies *without* a potential drop |
| $x \ll R-1$ (expand the exponential) | $j_\parallel \approx j_0\left(1 + x - \dfrac{x^2}{2(R-1)}+\dots\right) \to j_0\left(1+\dfrac{e\Phi}{k_BT}\right)$ | **linearized Knight**; also the exact $R\to\infty$ limit |
| $1 \ll x \ll R-1$ | $j_\parallel \approx K\Phi$, with $K = \dfrac{j_0e}{k_BT} = \dfrac{e^2n}{\sqrt{2\pi m_ek_BT}}$ | **"Ohmic" form** with Knight conductance $K$. The offset $j_0$ is negligible. |
| $x \gg R-1$ | $j_\parallel \to Rj_0$ | **saturation**: the whole source hemisphere is in the loss cone, and more voltage buys nothing |

So $j = K\Phi$ and $j = j_0(1 + e\Phi/k_BT)$ are *both correct*, in different regimes. They differ only by whether the zero-voltage offset $j_0$ is kept. The linear form is attractive because it looks like Ohm's law along the field: the magnetosphere acts as a conductance $K$ in series with the ionospheric Pedersen conductance. Global MHD models use the linear limit to estimate precipitation energy, since they can't compute $\Phi$ themselves ([[Strangeway Ch11 The Aurora|Strangeway Ch. 11]]). Fridman & Lemaire (1980) found the current proportional to the potential drop for parameters typical of the upward-current region.

**Numbers.** For a plasma-sheet-like source with $n = 1$ cm$^{-3}$ and $k_BT = 1$ keV: $j_0 = 0.85$ µA m$^{-2}$ and $K = 8.5\times10^{-10}$ S m$^{-2}$. An upward current of a few µA m$^{-2}$ (typical of discrete arcs) therefore needs $j_\parallel/j_0$ of a few, i.e. $e\Phi$ of a few keV for large $R$. That is just the energy of inverted-V electrons.

---

## 4. Why published current–voltage relations differ

They all share the same skeleton, $j = R\,e\int_{\text{loss cone}}v_\parallel f\,d^3v$, and differ in what goes into it:

1. **Which limit is quoted** (§3). This accounts for the $K\Phi$ vs $j_0(1+e\Phi/kT)$ vs full-form discrepancy.
2. **The source distribution.** Kappa (suprathermal-tail) distributions give modified but qualitatively similar relations (Pierrard 1996; Pierrard et al. 2007, cited in Gunell et al. 2013). Anisotropic sources change the effective $j_0$.
3. **Additional populations.** Knight's form includes only magnetospheric electrons. Ionospheric electrons, backscattered and secondary electrons, and upgoing ions all modify the net current. They matter most in *downward*-current regions, where the relation doesn't apply anyway.
4. **Steady state.** The relation is time-stationary. Vlasov simulations of a whole auroral flux tube (Gunell et al. 2013) find that the potential forms a thin double layer at about 1 $R_E$ plus an extended region above it, and still recover currents that "match Knight's relation reasonably well."

> **Wiki correction (2026-10-07).** Two forms that circulated in this wiki were dimensionally wrong:
> - $J = \frac{n_em_e\Omega_e}{k_BT_e}\left(\frac{e\Phi}{2\pi}\right)^{1/2}$, which has no source.
> - $K = n_e\left(\frac{e}{2\pi m_ek_BT_e}\right)^{1/2}$.
>
> Both have been replaced on [[Field-Aligned Currents]] and [[Aurora]]. The correct conductance is $K = e^2n_e/\sqrt{2\pi m_ek_BT_e}$, in units of A m$^{-2}$ V$^{-1}$ = S m$^{-2}$.

---

## What we assumed, and where it breaks

- **Isotropic Maxwellian source; collisionless adiabatic motion** ($\mu$ and energy conserved). Wave–particle scattering, or a $\mu$-violating field geometry, breaks it.
- **Monotonic potential with no significant minimum.** Otherwise particle access isn't determined by the endpoints alone (§1).
- **Upward current only.** Downward-current (return-current) regions are carried by upgoing ionospheric electrons and need a different treatment ([[Auroral Acceleration]]).
- **Quasi-static.** In the Alfvénic regime, $E_\parallel$ is carried by dispersive [[Alfvén Waves]], and there's no single $\Phi$.
- **Current from the source side only.** The ionosphere is treated as a perfect absorber.

---

## Verification

- **Sources agree:**
  - Full relation, $j_0$ and limits: AOS 205B Lecture 10.1 (course notes, Knight relation) and [[Strangeway Ch11 The Aurora|Strangeway Ch. 11]] Eqs. 11.32–11.33. Both give the same functional form, the same $j_0 = en\sqrt{k_BT/2\pi m_e}$ and the same saturation at $Rj_0$. The lecture gives the same Knight conductance $e^2n/\sqrt{2\pi m_ek_BT}$.
  - Literature context: Gunell et al. (2013) for Knight's profile-independence statement, Fridman & Lemaire's linearity, kappa extensions and the Vlasov-simulation agreement.
- **Numerical:**
  - Direct 2-D quadrature of the loss-cone flux integral reproduced the closed form to 4 decimals for $R = 3, 10, 100$ and $e\Phi/k_BT = 0$–$100$.
  - A Monte Carlo test ($2\times10^6$ Maxwellian electrons, each mapped with $\mu$ and energy conservation) agreed to within 0.3%, which is the sampling noise.
  - The $R\to\infty$ limit equals $j_0(1+x)$; the inversion formula round-trips; and $K = j_0e/k_BT$ was confirmed in SI units.
- **Not from original papers:** Knight (1973) and Fridman & Lemaire (1980) were not read directly. Their content here is via Gunell et al. (2013).

## Sources

- [[Strangeway Ch11 The Aurora]] — §11.5, Knight relation Eqs. 11.32–11.33 and the MHD-model use of the linear limit
- AOS 205B Lecture 10.1, *Knight Relation* — course notes (`Atlas/Courses/AOS 205B/Lecture10_1_KnightRelation.pdf`), full derivation and Knight conductance
- Gunell, H., J. De Keyser, E. Gamby, I. Mann (2013), Vlasov simulations of parallel potential drops, *Ann. Geophys.*, 31, 1227–1240, [doi:10.5194/angeo-31-1227-2013](https://doi.org/10.5194/angeo-31-1227-2013) (open access; not in vault)
- Knight, S. (1973), Parallel electric fields, *Planet. Space Sci.*, 21, 741–750. Cited via Gunell et al.; not in vault.
- Fridman, M., and J. Lemaire (1980), *J. Geophys. Res.*, 85, 664–670, doi:10.1029/JA085iA02p00664. Cited via Gunell et al.; not in vault.
