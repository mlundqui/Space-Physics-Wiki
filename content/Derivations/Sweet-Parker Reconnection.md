---
type: derivation
status: draft
updated: 2026-10-08
sources: 3
tags: [derivations, reconnection, MHD, current-sheet, magnetopause, magnetotail]
prerequisites: "[[Ideal MHD from Kinetic Theory]] (resistive Ohm's law, magnetic Reynolds number, tension); [[MHD Wave Modes]] (Alfvén speed)"
next: "[[Dessler-Parker-Sckopke Relation]]"
---

# Sweet-Parker Reconnection

**Part III, page 6** of the [[Derivations Index]] · Builds on: [[Ideal MHD from Kinetic Theory]] · Concept pages: [[Dungey Cycle]], [[MHD]]

## Where we're going

The frozen-in theorem says field lines can't break. But the [[Dungey Cycle]] needs them to: IMF field lines connect to Earth's field at the dayside magnetopause, are dragged over the polar cap, and reconnect again in the tail. The *rate* of that reconnection sets the cross-polar-cap potential, about 200 kV during active times (200C §9.5).

Reconnection needs a place where ideal MHD fails. With resistivity alone, the only candidate is a thin current sheet. Sweet (1958) and Parker (1957) worked out how fast such a sheet can process magnetic flux, using nothing but conservation laws and order-of-magnitude estimates. Their answer is *far* too slow for space plasmas. Understanding exactly **why** it's slow is the starting point for all of modern reconnection theory.

We follow [[Velli Basics of Plasma Astrophysics|Velli]] §9.1.1 and [[Bellan 2006 Fundamentals of Plasma Physics|Bellan]] Assignment 12.7, with context from 200C Ch. 9.

---

## 1. Why resistivity needs a thin sheet

The resistive induction equation ([[Ideal MHD from Kinetic Theory]]) is

$$\frac{\partial\mathbf B}{\partial t} = \nabla\times(\mathbf u\times\mathbf B) + \eta\nabla^2\mathbf B,\qquad\eta = \frac{1}{\mu_0\sigma}\ \text{(magnetic diffusivity, m}^2/\text{s)}.$$

The ratio of the two terms over a length $\ell$ is the magnetic Reynolds number $u\ell/\eta$. Using the Alfvén speed and the global scale $L$ gives the **Lundquist number**

$$S = \frac{v_AL}{\eta}.$$

For the magnetopause, $S\sim10^{11}$–$10^{12}$ (see §4). Diffusion is utterly negligible on the global scale. The only way to make it matter is to make $\ell$ tiny: a **current sheet** of thickness $\delta\ll L$, where $\nabla^2\mathbf B\sim B/\delta^2$ is huge. Everything below is about how thin the sheet gets, and what that implies for the inflow speed.

---

## 2. The Sweet–Parker estimate

Picture a sheet of length $2L$ and thickness $2\delta$. Oppositely directed fields $\pm B_i$ are carried in from above and below at speed $u_{\rm in}$, annihilate in the sheet, and the plasma squirts out of the ends at $u_{\rm out}$ (Velli Fig. 9.7, Bellan Fig. 12.6c). Assume steady, two-dimensional, incompressible flow. Three conservation statements fix everything.

**(i) Ohm's law: inflow = diffusion.** Outside the sheet the field is frozen in, so $E = u_{\rm in}B_i$. At the center $\mathbf B\approx0$, so $E = \eta_{\rm res}J$, where $J\approx B_i/\mu_0\delta$ by Ampère's law. In steady state $E$ is uniform (since $\nabla\times\mathbf E = 0$ in 2-D), so (Velli Eq. 9.8, Bellan Eq. 12.100)

$$u_{\rm in} = \frac{\eta}{\delta}.$$

The plasma can only flow in as fast as the field diffuses across the sheet.

**(ii) Mass: what comes in goes out.** Incompressibility gives (Velli Eq. 9.9, Bellan Eq. 12.99)

$$u_{\rm in}L = u_{\rm out}\delta.$$

**(iii) Momentum: the outflow is Alfvénic.** Along the sheet, the reconnected field lines are kinked and their tension $J\times B$ slings plasma out of the ends. Balance the outflow kinetic energy against the magnetic energy released, or equivalently the force along the sheet:

$$\rho\frac{u_{\rm out}^2}{L}\sim J B_o\sim\frac{B_iB_o}{\mu_0\delta},\qquad B_o = B_i\frac{\delta}{L}\ \ (\nabla\cdot\mathbf B = 0)\quad\Longrightarrow\quad u_{\rm out}\approx v_{A,i} = \frac{B_i}{\sqrt{\mu_0\rho}}.$$

**Solve the three together** (SymPy):

$$\boxed{\frac{u_{\rm in}}{v_A} = \frac{\delta}{L} = S^{-1/2}}$$

The dimensionless **reconnection rate** $M_A = u_{\rm in}/v_A$, which is also $E/v_AB_i$, falls like $S^{-1/2}$. A larger $S$ means a better conductor, which means a *thinner* sheet ($\delta = LS^{-1/2}$). But mass conservation forces everything through that thin nozzle, so the inflow *slows*. The geometry, not the resistivity alone, is the bottleneck.

**Energy budget.** The Poynting flux into the sheet is $4L\cdot u_{\rm in}B_i^2/\mu_0$. The kinetic energy flux out is $4\delta\cdot\tfrac12\rho u_{\rm out}^3$. Using the scalings above, their ratio is exactly $\tfrac12$ (SymPy). **Half the magnetic energy becomes bulk flow, and half becomes Ohmic heat.**

---

## 3. An exact solution that shows the balance $u_{\rm in}\delta\sim\eta$

The estimate in §2(i) is order-of-magnitude. It's worth seeing that the balance is real, using a case that can be solved exactly. Take the stagnation-point flow $\mathbf u = (\alpha x, -\alpha y)$ carrying $B_x(y)$ toward $y = 0$. The steady induction equation becomes

$$\eta B_x'' + \alpha(yB_x)' = 0\quad\Longrightarrow\quad B_x(y) = \frac{2C}{\sqrt{2\alpha\eta}}\,D\!\left(y\sqrt{\frac{\alpha}{2\eta}}\right),$$

where $D(s) = e^{-s^2}\int_0^se^{t^2}dt$ is **Dawson's function**. SymPy confirms it satisfies the ODE.

This is the classic annihilation solution (a version of Sonnerup–Priest), and it shows the physics directly:

- **Far away**, $B_x\to C/(\alpha y)$. The field is carried in frozen, $u_yB_x = $ const, so the flux delivered is fixed.
- **Near $y = 0$** the field is destroyed in a layer whose edge (the $|B_x|$ peak) sits at $\delta = 1.31\sqrt{\eta/\alpha}$.
- At that edge, $u_{\rm in}\delta/\eta = \alpha\delta^2/\eta = 1.71$, which is order unity. That's exactly the Sweet–Parker balance $u_{\rm in}\approx\eta/\delta$.

What this solution *lacks* is the finite length $L$ and the outflow constraint. Its outflow $\alpha x$ grows without limit, which is why it can reconnect at any rate. Sweet–Parker adds the finite $L$, and that's what throttles the rate.

---

## 4. Numbers: why Sweet–Parker fails in space

Use Spitzer diffusivity $\eta\approx5.2\times10^{-5}\ln\Lambda/(\mu_0T_e^{3/2})$ m$^2$/s with $T_e$ in eV and $\ln\Lambda = 20$. That's a standard textbook form, used here only for orders of magnitude.

| Setting | $\eta$ | $v_A$ | $S$ | Sweet–Parker rate | Time to reconnect $L$ |
|---|---|---|---|---|---|
| Solar loop, $L = 10^4$ km, 50 eV (Bellan 12.7k) | 2.3 m²/s | 1000 km/s | $4\times10^{12}$ | $5\times10^{-7}$ | ~240 days |
| Magnetopause, $L = 1\,R_E$, $n = 10$ cm⁻³, $B = 30$ nT | 2.3 m²/s | 210 km/s | $6\times10^{11}$ | $1\times10^{-6}$ | ~270 days |
| Magnetotail, $L = 10\,R_E$, $n = 0.3$ cm⁻³, $B = 20$ nT, 500 eV | 0.07 m²/s | 800 km/s | $7\times10^{14}$ | $4\times10^{-8}$ | ~70 years |

Observed: solar flares release energy in **minutes**, and substorms in about **an hour**. The Dungey cycle needs a dayside rate of order $E\approx0.1v_AB$ (the commonly cited normalized rate; not derived in the vault sources) (a 200 kV polar-cap potential needs 0.2 MWb/s of reconnected flux, 200C §9.5). Sweet–Parker is too slow by a factor of $10^4$–$10^6$. This is the **reconnection rate problem**.

---

## 5. Why published rates differ, and what fixes the problem

**Factor-of-order-unity variants of Sweet–Parker.** Velli §9.1.1 redoes step (iii) with the pressure gradient along the sheet. Cross-sheet pressure balance makes the central pressure $P_c = P_i + B_i^2/2\mu_0$. Adding that to the tension gives

$$u_{\rm out}^2 = 2v_{A,i}^2 + \frac{2(P_i - P_o)}{\rho}\qquad\text{(Velli Eq. 9.12)}.$$

So $u_{\rm out}$ ranges from $\sqrt2\,v_A$ (equal end pressures) downward. A high downstream pressure chokes the outflow and *raises* the rate as $v_A/u_{\rm out}\cdot S^{-1/2}$. These are $O(1)$ corrections. The $S^{-1/2}$ scaling, which is what matters, is untouched.

**Fast reconnection.** These go beyond this page, so they're summarized rather than derived:

- **Petschek (1964).** Shrink the diffusion region to a tiny segment and let **slow-mode shocks** standing off its corners do most of the energy conversion. Velli gives the maximum rate as $\propto(\ln S)^{-1}$, and quotes a split of 3/5 kinetic and 2/5 heat for $\gamma = 5/3$. The commonly quoted coefficient, $\pi/(8\ln S)\approx0.01$–0.015 for the cases in the table, is Petschek's, not in the vault sources, and is shown for scale only. Velli notes that resistive MHD simulations reproduce Petschek only with *localized anomalous* resistivity.
- **Hall / collisionless reconnection.** When $\delta$ shrinks to the ion inertial length $d_i = c/\omega_{pi}$, ions decouple from the field and electrons carry it. The Hall term in [[Ideal MHD from Kinetic Theory|generalized Ohm's law]] brings in whistler dynamics, Velli §9.1.2 says only that this is faster than Sweet–Parker. The widely quoted normalized rate of about 0.1, roughly independent of $S$, comes from the collisionless-reconnection simulation literature, not from the vault sources. That's the regime of the magnetopause and magnetotail.
- **Plasmoid instability.** A Sweet–Parker sheet at high $S$ is itself tearing-unstable (Velli Fig. 9.8 shows it at $S\approx10^5$; the often-quoted threshold $S\sim10^4$ is from the literature, not the vault), at a rate that *increases* with $S$. It breaks into chains of islands, and no laminar sheet thinner than an aspect ratio of about $S^{1/3}$ can survive (Velli §9.2). Even resistive MHD then reconnects fast.

---

## What we assumed, and where it breaks

- **Incompressible, steady, 2-D.** Compressibility changes the factors. Real reconnection is often bursty: flux transfer events at the magnetopause, and substorm onset in the tail.
- **Collisional resistivity.** Space plasmas are collisionless, so $\eta$ is anomalous or replaced by electron inertia and pressure-tensor effects. The $S$ values above are a measure of how poorly collisions alone could do the job, not a prediction.
- **Antiparallel fields.** A **guide field** (a component along the current) and asymmetric inflow (magnetosheath vs. magnetosphere at the dayside magnetopause) both modify the rate. The Dungey-cycle dependence on IMF clock angle comes from this.

---

## Verification

- **Sources agree.**
  - The three conservation relations and $u_{\rm in}/v_A = \delta/L = S^{-1/2}$: [[Velli Basics of Plasma Astrophysics|Velli]] §9.1.1, Eqs. 9.8–9.11 (Gaussian units, converted here), and [[Bellan 2006 Fundamentals of Plasma Physics|Bellan]] Assignment 12.7, Eqs. 12.99–12.101.
  - Pressure-corrected outflow, Petschek summary, plasmoid aspect ratio: Velli Eq. 9.12, §9.1.2, §9.2.
  - Dungey-cycle rate, 200 kV, 0.2 MWb/s: 200C textbook §9.5. Sweet/Petschek context: §9.6.1.
- **SymPy.**
  - Solution of the Sweet–Parker system.
  - $B_o/B_i = S^{-1/2}$.
  - Energy split exactly 1/2.
  - The Dawson-function annihilation solution satisfies the steady induction ODE exactly.
- **Numerical.**
  - Dawson peak at $s = 0.924$, giving $\delta = 1.31\sqrt{\eta/\alpha}$ and $u_{\rm in}\delta/\eta = 1.71$.
  - Far-field $sD(s)\to\tfrac12$.
  - The $S$ and time-scale table.
- **Flagged.**
  - The Spitzer prefactor $5.2\times10^{-5}$ Ω m eV$^{3/2}$ is from memory of standard textbooks (not cross-checked in the vault) and is used only for orders of magnitude.
  - Petschek's $\pi/8\ln S$ coefficient is not in the vault sources.

## Sources

- [[Velli Basics of Plasma Astrophysics]] — Ch. 9 (Sweet–Parker, Petschek, tearing and plasmoid instability)
- [[Bellan 2006 Fundamentals of Plasma Physics]] — Ch. 12, Assignment 12.7 (Sweet–Parker via merging current loops)
- 200C textbook Ch. 9, *Solar wind–magnetosphere coupling* (`Atlas/Texts/Textbooks/200C Textbook/Ch9_SolarWindMagnetosphereCoupling.pdf`)
