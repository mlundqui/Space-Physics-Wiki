---
type: derivation
status: draft
updated: 2026-10-07
sources: 3
tags: [derivations, ionosphere, ambipolar-diffusion, scale-height, polar-wind, F-region]
prerequisites: "[[Moment Equations from the Vlasov Equation]] §4 (momentum equation); [[Chapman Layer]]"
next: "Part II continues in [[Derivations Index]]"
---

# Plasma Diffusion Along B

**Part II (ionosphere), page 3** of the [[Derivations Index]] · Previous: [[Chapman Layer]] · Concept page: [[Ambipolar Diffusion]]

## Where we're going

Above about 200 km, plasma can't move across $\mathbf{B}$ except by $\mathbf{E}\times\mathbf{B}$ drift ([[Guiding-Center Drifts]]), but it can slide freely along the field. Gravity pulls it down, pressure pushes it up, and neutrals drag on it. This page derives:

1. the **ambipolar electric field**, a tiny charge separation that ties ions and electrons together;
2. the **plasma scale height** $H_p = k_B(T_e+T_i)/m_ig$, about twice the neutral scale height;
3. the **minor-ion** result: light ions such as H$^+$ are pushed *up* by that electric field. This is the seed of the [[Polar Wind]];
4. the **ambipolar diffusion equation**, which together with chemistry fixes the F2 peak ([[Chapman Layer]] §5).

The derivation follows AOS 205B Lecture 3.2 (course notes) step by step, cross-checked against [[Schunk Nagy 2009 Ionospheres|Schunk & Nagy]] Ch. 5.

---

## 1. Start from the ion momentum equation

From [[Moment Equations from the Vlasov Equation]] §4, the ion momentum equation with collisions and chemistry is

$$\frac{\partial(m_in_i\mathbf{u}_i)}{\partial t} + \nabla\cdot\left(m_in_i\mathbf{u}_i\mathbf{u}_i + p_i\mathsf{I} + \boldsymbol\tau_i\right) = q_in_i(\mathbf{E}+\mathbf{u}_i\times\mathbf{B}) + m_in_i\mathbf{g} + \frac{\delta\mathbf{M}_i}{\delta t} + m_i\mathbf{u}_i\frac{\delta n_i}{\delta t}.$$

For the F region and topside, make four simplifications:

| Assumption | Drops | Justification |
|---|---|---|
| Steady state | $\partial_t(m_in_i\mathbf{u}_i)$ | slow evolution |
| Isotropic pressure | stress $\boldsymbol\tau_i$ | collisions keep $f$ near-Maxwellian |
| **Subsonic** flow | $m_in_iu_i^2\ll p_i$ | define $a = \sqrt{k_BT_i/m_i}$; then $p_i = m_in_ia^2$, so for $|u_i|\ll a$ the dynamic pressure is negligible. *Fails in the supersonic polar wind.* |
| Chemistry term small | $m_i\mathbf{u}_i\,\delta n_i/\delta t$ | small compared with collisional momentum transfer |

Now project along the field. Let $\hat{\mathbf b}$ point *upward* along $\mathbf{B}$ (that's $-\mathbf{B}/B$ in the northern hemisphere), $s$ be distance along it, and $I$ be the dip angle. The magnetic force has no parallel component. Gravity gives $\hat{\mathbf b}\cdot\mathbf{g} = -g\sin I$, and $d/ds = \sin I\,d/dz$ for a horizontally stratified ionosphere.

---

## 2. Collisionless first: the ambipolar field and the plasma scale height

Drop collisions for the moment. Then the **ion** equation along $\mathbf{B}$ is

$$\frac{dp_i}{ds} = en_iE_\parallel - m_in_ig\sin I.$$

To find $E_\parallel$, look at the **electrons**. Their equation is the same with $q = -e$ and $m_e$ instead of $m_i$. Since $m_e\to0$, the electrons feel essentially no gravity:

$$\frac{dp_e}{ds} = -en_eE_\parallel\quad\Longrightarrow\quad\boxed{E_\parallel = -\frac{1}{en_e}\frac{dp_e}{ds}}$$

This is the **ambipolar electric field**. Picture it this way:

- Light, hot electrons try to float off. Gravity barely holds them, and their pressure pushes them up.
- A tiny charge separation forms: electrons slightly above, ions slightly below.
- That separation produces an upward $E_\parallel$ that **holds the electrons down and lifts the ions up**, until both species move together.

How tiny is "tiny"? It is of order $\varepsilon_0E/eL$, a fractional imbalance of $10^{-12}$ or less ([[Strangeway Ch3 Physics of Magnetized Plasmas|Strangeway]] §3.4.3 makes the same estimate for the magnetosphere).

Substitute into the ion equation with $n_i = n_e = n$:

$$\frac{d}{ds}(p_i + p_e) = -m_ing\sin I.$$

The $\sin I$ cancels on converting to $z$. **The plasma is in hydrostatic balance as if it were a single gas** with total pressure $p_i + p_e$ and mass $m_i$ per ion. For constant temperatures,

$$\boxed{n(z) = n(z_0)\exp\!\left(-\frac{z-z_0}{H_p}\right),\qquad H_p = \frac{k_B(T_e+T_i)}{m_ig}}$$

Compare the neutral scale height $H_n = k_BT_n/m_ng$. With $T_e = T_i = T_n$, $H_p = 2H_n$: the electrons' pressure, transmitted through $E_\parallel$, effectively **halves the ions' weight**. In the daytime F region $T_e > T_i$, so the plasma scale height is larger still:

| $T_e$, $T_i$ (K) | $H_p$ (O$^+$, $g = 9.0$ m s$^{-2}$) | $H_n$ (O, $T_n = T_i$) |
|---|---|---|
| 1000, 1000 | 115 km | 57 km |
| 2000, 1000 | 172 km | 57 km |
| 3000, 1500 | 258 km | 86 km |

*(The concept page [[Ambipolar Diffusion]] quotes "~110 km" for the first case. That's consistent with $g\approx9.5$ m s$^{-2}$; the value depends on which altitude's $g$ you use.)*

With temperature gradients, the exact diffusive-equilibrium profile is

$$n(z) = n_0\exp\!\left(-\int\frac{m_ig + \frac{d}{dz}k_B(T_e+T_i)}{k_B(T_e+T_i)}dz\right).$$

The **plus** sign means a rising plasma temperature makes density fall *faster*. *(This sign was wrong on [[Ambipolar Diffusion]] and [[F-Layer]]; both were corrected 2026-10-07.)*

---

## 3. Minor ions and the birth of the polar wind

Now add a **minor** ion $j$ (density $n_j\ll n_e$, mass $m_j$, charge $q_j$) that feels the *same* $E_\parallel$. That field is set by the major ion and the electrons; the minor ion is too sparse to change it. Its equation is

$$k_BT_j\frac{dn_j}{dz} = q_jn_jE_\parallel/\sin I - m_jn_jg.$$

The major-ion layer has $d\ln n_e/dz = -1/H_p$, so $eE_\parallel/\sin I = k_BT_e/H_p$ for constant $T_e$. Then

$$\frac{1}{H_j} = \frac{m_jg}{k_BT_j} - \frac{q_j}{e}\frac{T_e}{T_j}\frac{1}{H_p}.$$

The first term is the minor ion's own weight. The second is the ambipolar lift, which is set by the **major** ion's mass through $H_p$. Take all temperatures equal and singly charged ions:

$$\frac{1}{H_j} = \frac{g}{k_BT}\left(m_j - \frac{m_i}{2}\right).$$

**If $m_j < m_i/2$, the scale height is negative: the minor ion's density increases with altitude.** For H$^+$ in an O$^+$ plasma:

$$H_{\text{H}^+} = -\frac17\,\frac{k_BT}{m_pg}.$$

The upward electric force on a proton is $m_ig/2 = 8m_pg$, eight times its weight. This is S&N's Eq. 5.79 result ("net upward force for $m_\ell < m_i/2$"). It's why H$^+$ eventually takes over as the major ion at high altitude (the protonosphere), and on open polar field lines it's what accelerates H$^+$ to supersonic outflow: the [[Polar Wind]].

> *Subtlety.* In this static solution, H$^+$ just increases exponentially, which can't continue forever. Once H$^+$ is no longer minor, it contributes to $E_\parallel$ and the assumption fails. On open field lines the static solution doesn't exist at all, and the outflow becomes supersonic. Then the dropped $m_in_iu_i^2$ term matters, and you need transonic (Parker-wind-like) equations: S&N Ch. 12; [[IPWM]]; [[Blelly Schunk 1993 Moment Comparison]].

---

## 4. Turning collisions back on: ambipolar diffusion

In the F region, ions collide with neutrals. The collisional momentum transfer is

$$\frac{\delta\mathbf{M}_i}{\delta t} = -\sum_nm_in_i\nu_{in}(\mathbf{u}_i - \mathbf{u}_n).$$

Keep it in the parallel ion equation, use the same $E_\parallel$, and solve for the field-aligned ion flux:

$$\boxed{n_iu_{i\parallel} = -D_a\left[\frac{dn_i}{ds} + n_i\frac{d\ln(T_e+T_i)}{ds} + \frac{n_i\sin I}{H_p}\right] + n_iu_{n\parallel},\qquad D_a = \frac{k_B(T_e+T_i)}{m_i\sum_n\nu_{in}}}$$

Every term is a *push* on the plasma:

- density gradient (diffuse from high to low);
- temperature gradient;
- gravity;
- the neutral wind, which **drags the plasma along $\mathbf{B}$ at the wind's parallel speed**.

That last term is how a meridional wind lifts or lowers the F layer. An equatorward wind blows plasma *up* the inclined field lines; see [[Chapman Layer]] §5 and [[Lifting]].

$D_a$ is the **ambipolar diffusion coefficient**: the ion diffusion coefficient with the electron temperature added. Electrons, held to the ions by $E_\parallel$, effectively donate their pressure to the ions. Since $\nu_{in}\propto n_{\text{neutral}}$, $D_a$ grows exponentially with altitude.

**Order of magnitude at about 300 km.** S&N Table 4.5 gives the O$^+$–O resonant charge-exchange collision frequency as $\nu_{in} = 3.67\times10^{-11}\,n(\text{O})\,T_r^{1/2}(1 - 0.064\log_{10}T_r)^2$ s$^{-1}$, with $n$ in cm$^{-3}$ and $T_r = (T_i+T_n)/2$.

- For $n(\text{O}) = 10^9$ cm$^{-3}$ and $T_r = 1000$ K: $\nu_{in}\approx0.8$ s$^{-1}$.
- With $T_e + T_i = 3000$ K: $D_a\approx2\times10^6$ m² s$^{-1}$.
- The diffusion time across one O scale height (50 km) is $H^2/D_a\approx20$ min.

That's the timescale that competes with the chemical lifetime $1/\beta$ to set the F2 peak.

**The ambipolar diffusion equation.** Put the flux into the continuity equation (no perpendicular divergence):

$$\frac{\partial n_i}{\partial t} + \frac{\partial}{\partial s}\left(n_iu_{i\parallel}\right) = P - \beta n_i.$$

That's a second-order parabolic PDE with sources. It has no general closed form, but it's straightforward numerically (e.g. Crank–Nicolson; Lecture 3.2). Its limits are the whole story of the F region:

| Region | Balance | Profile |
|---|---|---|
| Low altitude | $P = \beta n$ (chemistry) | $n = P/\beta$, *rising* with height |
| High altitude | $\partial_s(nu_\parallel) = 0$; zero flux ⇒ hydrostatic | $e^{-z/H_p}$, *falling* |
| Near the peak | excess production carried away by divergent flux | peak where $\beta\approx D/H^2$ ([[Chapman Layer]] §5) |
| Night ($P = 0$) | $\partial_tn = -\partial_s(nu) - \beta n$ | decays over hours. O$^+$ formed near 300 km diffuses down to about 200 km before being lost to O$^+$ + N$_2$. |

---

## What we assumed, and where it breaks

- **Subsonic, isotropic, collision-dominated.** Fails in the topside polar cap, where H$^+$ (and, during upflow, O$^+$) becomes supersonic and anisotropic. Use the 8-, 13- or 16-moment equations there ([[Moment Equations from the Vlasov Equation]] §5).
- **Single major ion.** Multi-ion mixtures need the full coupled set, including ion–ion friction (S&N §5.7).
- **No thermal diffusion.** S&N show that heat-flow collision terms correct $D_a$ by a factor $(1-\Delta_{in})^{-1}$ (their Eq. 5.165), which matters in the upper F region.
- **No perpendicular transport.** $\mathbf{E}\times\mathbf{B}$ drift moves whole flux tubes, as in convection and patch transport. This page is only the along-$\mathbf{B}$ part.

---

## Verification

- **Sources agree.**
  - Ambipolar field, $H_p$, minor-ion scale height, $D_a$, diffusion equation and limits: AOS 205B Lecture 3.2 (course notes), every step re-derived.
  - Same results: [[Schunk Nagy 2009 Ionospheres|Schunk & Nagy]] Eqs. 5.54–5.63 ($D_a = 2kT_p/m_i\nu_{in}$, $T_p = (T_e+T_i)/2$, which is identical), Eq. 5.59 ($H_p$), Eq. 5.79 (minor-ion condition $m_\ell < m_i/2$), Eq. 11.59 (vertical form with $\sin^2I$, wind and $\mathbf{E}\times\mathbf{B}$ terms), and Table 4.5 ($\nu_{in}$).
  - The 200C textbook Ch. 2 §2.12 gives the same minor-ion momentum balance (Eqs. 2.82–2.86).
- **SymPy.**
  - Solving the collisional parallel momentum balance gives exactly the boxed flux, including $+n_iu_{n\parallel}$.
  - Minor-ion $1/H_j = (g/k_BT)(m_j - m_i/2)$, so $H_{\text{H}^+} = -k_BT/(7m_pg)$.
- **Numerical.** Scale heights in the table, $\nu_{in}$, $D_a$ and the diffusion time were computed from the S&N formula.

## Sources

- AOS 205B Lecture 3.2, *Ambipolar Electric Fields and Ambipolar Diffusion* (`Atlas/Courses/AOS 205B/Lecture3_2_AmbipolarDiffusion.pdf`) — course notes, primary derivation
- [[Schunk Nagy 2009 Ionospheres]] — §5.5–5.7 (ambipolar diffusion, plasma scale height, minor ions), §11.4 (F2 diffusion equation), Table 4.5 (collision frequencies)
- 200C textbook Ch. 2 §2.12.1 (`Atlas/Texts/Textbooks/200C Textbook/Ch2_UpperAtmosphereIonosphere.pdf`) — high-speed light-ion outflow
