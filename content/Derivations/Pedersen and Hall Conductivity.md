---
type: derivation
status: draft
updated: 2026-10-07
sources: 3
tags: [derivations, ionosphere, conductivity, pedersen, hall, E-region, electrodynamics]
prerequisites: "[[Guiding-Center Drifts]] §2 (E×B drift); [[Plasma Diffusion Along B]] §4 (ion–neutral friction)"
next: "Part II continues in [[Derivations Index]]"
---

# Pedersen and Hall Conductivity

**Part II (ionosphere), page 4** of the [[Derivations Index]] · Concept page: [[Ionospheric Conductivity]]

## Where we're going

In the F region, ions and electrons both $\mathbf{E}\times\mathbf{B}$ drift together, so no perpendicular current flows ([[Guiding-Center Drifts]] §2). Go lower and the ions start colliding with neutrals before they finish a gyration. Now the two species move **differently**, and differential motion *is* current. The result is a tensor Ohm's law with three conductivities:

- **Pedersen** ($\sigma_P$), along $\mathbf{E}_\perp$: carried mainly by ions;
- **Hall** ($\sigma_H$), along $-\mathbf{E}\times\mathbf{B}$: carried mainly by electrons;
- **parallel** ($\sigma_\parallel$), along $\mathbf{B}$: enormous.

Everything in high-latitude electrodynamics (closure of field-aligned currents, [[Joule Heating]], the [[Ionospheric Dynamo]], electrojets, [[Subauroral Polarization Streams|SAPS]]) runs through this tensor. The derivation follows AOS 205B Lecture 6.1 (course notes), checked against [[Kelley Earth's Ionosphere|Kelley]] §2.2 and [[Schunk Nagy 2009 Ionospheres|Schunk & Nagy]] §5.11.

---

## 1. Momentum balance for each species

Take the steady, perpendicular-dominated momentum equation for species $s$ (ions $i$, electrons $e$), keeping only the electromagnetic and frictional forces. Pressure and gravity add the "general drifts" of §5.

$$0 = q_s(\mathbf{E} + \mathbf{u}_s\times\mathbf{B}) - m_s\nu_{sn}(\mathbf{u}_s - \mathbf{u}_n).$$

**How big are the terms?** For an O$^+$ ion moving at 10 m/s in $5\times10^{-5}$ T, the magnetic acceleration $(q/m)uB$ is about 3000 m s$^{-2}$, some 300 times gravity. In the F region, collisions are negligible next to it, and you recover $\mathbf{E} = -\mathbf{u}\times\mathbf{B}$, the pure $\mathbf{E}\times\mathbf{B}$ drift, with no current.

**Go to the neutral frame.** The friction depends on $\mathbf{u}_s - \mathbf{u}_n$, so shift to a frame moving with the wind. There the electric field is $\mathbf{E}' = \mathbf{E} + \mathbf{u}_n\times\mathbf{B}$, and with $\mathbf{u}'_s = \mathbf{u}_s - \mathbf{u}_n$:

$$\frac{q_s}{m_s}\left(\mathbf{E}' + \mathbf{u}'_s\times\mathbf{B}\right) = \nu_{sn}\mathbf{u}'_s.$$

The neutral wind therefore enters *only* through $\mathbf{u}_n\times\mathbf{B}$. That is the seed of the [[Ionospheric Dynamo]].

---

## 2. Solve for the velocity: the mobility tensor

Put $\mathbf{B} = B\hat{\mathbf{z}}$ and define the **signed** gyrofrequency $\Omega_s = q_sB/m_s$ (negative for electrons). The equation is linear in $\mathbf{u}'_s$, and writing it as a matrix and inverting gives

$$\mathbf{u}'_s = \boldsymbol{\mu}_s\cdot\mathbf{E}',\qquad \boldsymbol{\mu}_s = \frac{q_s}{m_s}\begin{pmatrix}\dfrac{\nu}{\nu^2+\Omega_s^2} & \dfrac{\Omega_s}{\nu^2+\Omega_s^2} & 0\\[2mm] -\dfrac{\Omega_s}{\nu^2+\Omega_s^2} & \dfrac{\nu}{\nu^2+\Omega_s^2} & 0\\[2mm] 0 & 0 & \dfrac1\nu\end{pmatrix}.$$

Here $\nu = \nu_{sn}$ is the total collision frequency with all neutral species. The **diagonal** (Pedersen) mobility moves particles *along* $\mathbf{E}_\perp$. The **off-diagonal** (Hall) mobility moves them *across* it.

Everything is controlled by one dimensionless number per species:

$$\boxed{\kappa_s = \frac{\Omega_s}{\nu_{sn}}}$$

that is, gyrations per collision. Apply $\mathbf{E}' = E\hat{\mathbf{y}}$. The velocity makes an angle $\psi$ with $\mathbf{E}$, given by $\tan\psi = \mu_H/\mu_P = \kappa_s$:

| $\kappa$ | Motion | Picture |
|---|---|---|
| $\kappa\ll1$ | along $\mathbf{E}$ ($\psi\to0$) with mobility $q/m\nu$ | collisions win; particle is dragged straight by $\mathbf{E}$ |
| $\kappa = 1$ | at 45° | each species' Pedersen mobility peaks here |
| $\kappa\gg1$ | along $\mathbf{E}\times\mathbf{B}$ ($\psi\to90°$) at $E/B$ | gyration wins; pure $\mathbf{E}\times\mathbf{B}$ drift |

**Where are the crossovers?** Electrons are about $10^4$ times more magnetized than ions at the same altitude ($\Omega_e/\Omega_i\sim m_i/m_e$, while $\nu_{en}$ and $\nu_{in}$ differ far less), so the electrons cross over much lower. [[Kelley Earth's Ionosphere|Kelley]] (Fig. 2.5; equatorial, $B = 0.25$ G, $\nu_e = \nu_{en} + \nu_{ei}$) gives $|\kappa_e| = 1$ near **75 km** and $\kappa_i = 1$ near **130 km**.

> *Discrepancy flagged.* The AOS 205B notes give $\kappa_i = 1$ at 120–140 km, which agrees with Kelley. They give $|\kappa_e| = 1$ at about 90 km, which does not. The crossing heights depend on $B$ and on the collision-frequency model. A stronger $B$ (e.g. 0.5 G at high latitude) doubles $\kappa$ and lowers the crossing altitude. I'm citing Kelley's value with its stated conditions. The 90 km figure in the notes should be checked against the model used in lecture.

Between those two heights, roughly 75–130 km, **ions are collision-dominated but electrons are magnetized**. That's the E-region "dynamo layer," where the two species separate and current flows.

---

## 3. The conductivity tensor

The current is $\mathbf{J} = \sum_sn_sq_s\mathbf{u}_s$. By quasi-neutrality, $\sum_sn_sq_s = 0$, so the $\mathbf{u}_n$ terms cancel: **a wind with no electric field drives no current in its own frame, only through $\mathbf{u}_n\times\mathbf{B}$.** Then

$$\mathbf{J} = \boldsymbol\sigma\cdot(\mathbf{E} + \mathbf{u}_n\times\mathbf{B}),\qquad \boldsymbol\sigma = \sum_sn_sq_s\boldsymbol\mu_s = \begin{pmatrix}\sigma_P & -\sigma_H & 0\\ \sigma_H & \sigma_P & 0\\ 0&0&\sigma_\parallel\end{pmatrix}.$$

For one singly charged ion species plus electrons, written with $\kappa$:

$$\boxed{\sigma_P = \frac{n e}{B}\left(\frac{\kappa_i}{1+\kappa_i^2} + \frac{|\kappa_e|}{1+\kappa_e^2}\right),\qquad \sigma_H = \frac{n e}{B}\left(\frac{\kappa_e^2}{1+\kappa_e^2} - \frac{\kappa_i^2}{1+\kappa_i^2}\right),\qquad \sigma_\parallel = ne^2\left(\frac{1}{m_i\nu_{in}} + \frac{1}{m_e\nu_e}\right)}$$

These are Kelley Eqs. 2.38–2.39 and S&N Eqs. 5.117–5.118. Using $\kappa^2/(1+\kappa^2) = 1 - 1/(1+\kappa^2)$, the Hall conductivity can also be written

$$\sigma_H = \frac{ne}{B}\left(\frac{1}{1+\kappa_i^2} - \frac{1}{1+\kappa_e^2}\right).$$

The coordinate-free form is

$$\mathbf{J} = \sigma_\parallel E'_\parallel\hat{\mathbf b} + \sigma_P\mathbf{E}'_\perp - \sigma_H\,\mathbf{E}'_\perp\times\hat{\mathbf b}.$$

> **Sign conventions.** Kelley and the AOS 205B notes write the Hall term as $-\sigma_H\mathbf{E}'\times\hat{\mathbf b}$. Schunk & Nagy (Eq. 5.116) write $+\sigma_H\,\hat{\mathbf b}\times\mathbf{E}'$. These are identical, since $\hat{\mathbf b}\times\mathbf{E} = -\mathbf{E}\times\hat{\mathbf b}$. With either, $\sigma_H > 0$ and **the Hall current flows opposite to $\mathbf{E}\times\mathbf{B}$**. It's the magnetized electrons $\mathbf{E}\times\mathbf{B}$-drifting while the collisional ions lag behind, and a negative charge moving one way is a current the other way.

### Reading the formulas

- **Pedersen current is carried by ions.** The ion term $\kappa_i/(1+\kappa_i^2)$ peaks at $\kappa_i = 1$. The electron term is tiny above about 90 km because $|\kappa_e|\gg1$. S&N Eq. 5.119 drops it entirely: "the electrons contribute to the Hall current, but not to the Pedersen current."
- **Hall current needs $\kappa_e\gg1$ *and* $\kappa_i\lesssim1$.** It lives in a narrow layer, peaking lower than $\sigma_P$ (around 105–110 km vs. 120–130 km in the notes' sketch), and needs high density. As Kelley puts it, $\sigma_H$ "is important only in a narrow height range where three conditions are met: $\kappa_e\gg1$, $\kappa_i<1$, and $n$ is large."
- **F region** ($\kappa_i\gg1$): $\sigma_H\to0$ and $\sigma_P\to nm_i\nu_{in}/B^2$ (Kelley Eq. 2.40b). There is still a small Pedersen conductivity, proportional to the ion–neutral collision rate. It's what lets the F region carry Pedersen current and feel frictional drag, and it's why F-region conductance matters for SAPS and patches.
- **Parallel conductivity** is dominated by electrons and is enormous: $\sigma_\parallel/\sigma_P > 10^4$ above 130 km (Kelley). Field lines are nearly equipotentials, which is why $\mathbf{E}_\perp$ maps between the ionosphere and the magnetosphere (until the [[Knight Relation]] regime, where it doesn't).

### Height-integrated conductances

Because $\sigma_\parallel$ is so large, $\mathbf{E}_\perp$ is nearly constant along a field line through the thin conducting layer. Integrating over height gives the conductances

$$\Sigma_{P,H} = \int\sigma_{P,H}\,dz\quad(\text{siemens}),\qquad \mathbf{J}_\perp^{\text{(sheet)}} = \Sigma_P\mathbf{E}'_\perp - \Sigma_H\,\mathbf{E}'_\perp\times\hat{\mathbf b}.$$

These are the quantities that couple to the magnetosphere through [[Field-Aligned Currents]], $j_\parallel = \nabla_\perp\cdot\mathbf{J}_\perp^{\text{(sheet)}}$, and that set the [[Joule Heating]] rate $\Sigma_PE'^2$.

---

## 4. Worked check: the ion and electron velocity triangle

Apply $\mathbf{E}' = E\hat{\mathbf{y}}$ with $\mathbf{B}$ out of the page. The electrons, with $|\kappa_e|\gg1$, go almost straight along $\mathbf{E}\times\mathbf{B} = +\hat{\mathbf{x}}$. The ions, with $\kappa_i\sim1$, go at about 45° between $\mathbf{E}$ and $\mathbf{E}\times\mathbf{B}$. The current $\propto\mathbf{u}_i - \mathbf{u}_e$ then has:

- a $+\hat{\mathbf{y}}$ component: **Pedersen**, along $\mathbf{E}$;
- a $-\hat{\mathbf{x}}$ component: **Hall**, against $\mathbf{E}\times\mathbf{B}$.

This is the sketch on Lecture 6.1 p. 9, and SymPy confirms $J_x = -\sigma_HE_y$ with $\sigma_H > 0$ whenever $\kappa_e > \kappa_i$.

---

## 5. Beyond $\mathbf{E}$: gravity and pressure-gradient currents

Replace $(q/m)\mathbf{E}'$ by the *total* force per unit mass,

$$\mathbf{a}_s = \frac{q_s}{m_s}\mathbf{E}' + \mathbf{g} - \frac{\nabla p_s}{n_sm_s},$$

and the same matrix (call it $\boldsymbol\gamma_s = (m_s/q_s)\boldsymbol\mu_s$) gives the general drift

$$\mathbf{u}_s = \mathbf{u}_n + \boldsymbol\mu_s\cdot\mathbf{E}' + \boldsymbol\gamma_s\cdot\mathbf{g} - \mathbf{D}_s\cdot\left(\frac{\nabla n_s}{n_s} + \frac{\nabla T_s}{T_s}\right),\qquad \mathbf{D}_s = \frac{k_BT_s}{m_s}\boldsymbol\gamma_s.$$

This is the collisional generalization of the force drift $\mathbf{F}\times\mathbf{B}/qB^2$ from [[Guiding-Center Drifts]] §3. The current splits into electric, gravity-driven and diamagnetic parts (Lecture 6.1, "General Currents"). The gravity current is what drives equatorial Rayleigh–Taylor ([[Ionospheric Instabilities]]). Its $\kappa\gg1$ limit is the gravity drift $m\mathbf{g}\times\mathbf{B}/qB^2$.

---

## What we assumed, and where it breaks

- **Steady state and no inertia.** Fine on timescales longer than $1/\nu_{in}$ and $1/\Omega_i$ (seconds or less in the E region).
- **Single ion species.** For mixtures, sum over ions with their own $\kappa_j$ and number densities.
- **Electron–ion collisions neglected in the perpendicular terms.** Kelley includes $\nu_{ei}$ in $\kappa_e$ for his figure and notes the effect is minor above 100 km.
- **Collision frequencies depend on temperature.** Strong $\mathbf{E}$ fields raise $T_i$ by frictional heating, which changes $\nu_{in}$ and also changes the chemistry (O$^+$ + N$_2$ is faster; see [[Ion Frictional Heating]]). Electron heating by Farley–Buneman waves changes $\nu_{en}$.
- **Linear response.** Coherent waves and instabilities (Farley–Buneman, gradient drift) can add anomalous conductivity.

---

## Verification

- **Sources agree.**
  - Momentum balance, mobility tensor, $\kappa$, limits, conductivity tensor, Hall sign, general drifts and currents: AOS 205B Lecture 6.1 (course notes).
  - [[Kelley Earth's Ionosphere|Kelley]] §2.2, Eqs. 2.37–2.40 and Figs. 2.5–2.6 (κ crossover heights, $\sigma_P$ F-region limit, Hall-layer conditions, $\sigma_0/\sigma_P$).
  - [[Schunk Nagy 2009 Ionospheres|S&N]] Eqs. 5.116–5.120 (same tensor; Hall written as $\hat{\mathbf b}\times\mathbf{E}$; electrons carry no Pedersen current).
  - Agrees with the formulas already on [[Ionospheric Conductivity]].
- **SymPy.**
  - Solving the 3×3 force balance reproduces the mobility tensor exactly.
  - Summing species gives the boxed $\sigma_P$ and $\sigma_H$ in κ form, with the antisymmetric off-diagonal $\sigma_{xy} = -\sigma_H$.
  - $\kappa/(1+\kappa^2)$ is maximal at $\kappa = 1$.
  - The $\kappa_i\gg1$ limit is $\sigma_P\to nm_i\nu_{in}/B^2$.
  - $J_x = -\sigma_HE_y$, so the Hall current runs opposite to $\mathbf{E}\times\mathbf{B}$.
- **Unresolved:** the $|\kappa_e| = 1$ height (Kelley about 75 km vs. lecture notes about 90 km); see §2.

## Sources

- AOS 205B Lecture 6.1, *Ionospheric Ohm's Law* (`Atlas/Courses/AOS 205B/Lecture6_1_OhmsLaw.pdf`) — course notes, primary derivation
- [[Kelley Earth's Ionosphere]] — §2.2 (conductivity tensor, κ profiles, Figs. 2.5–2.6)
- [[Schunk Nagy 2009 Ionospheres]] — §5.11 (Eqs. 5.111–5.121, perpendicular and parallel currents)
