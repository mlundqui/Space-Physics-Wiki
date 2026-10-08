---
type: derivation
status: draft
updated: 2026-10-08
sources: 3
tags: [derivations, dipole, L-shell, magnetosphere, geometry, coordinates]
prerequisites: "none (magnetostatics)"
next: "[[Derivations Index]]"
---

# Dipole Field and L-Shells

**Part III, page 9** of the [[Derivations Index]] · Used by: [[Adiabatic Invariants and Magnetic Mirrors]], [[Dessler-Parker-Sckopke Relation]], [[Polar Wind Transonic Outflow]], [[Chapman-Ferraro Standoff Distance]], [[Cold-Plasma Waves]] · Concept page: [[Magnetic Coordinate Systems]]

## Where we're going

Almost every page in this track quietly uses the same handful of dipole facts:

- $r = L\cos^2\lambda$;
- $|\nabla B|/B = 3/r$ at the equator;
- flux tubes widen as $r^3$ near the pole;
- $B_{\rm foot}/B_{\rm eq}$ is huge.

This page collects them in one place and derives each one. It is short and geometric, but it is the coordinate system of the inner magnetosphere and the high-latitude ionosphere. Sources: 200C textbook Ch. 7 §7.2 and [[Schunk Nagy 2009 Ionospheres|S&N]] §11.1, with [[Thorne 1993 AOS 250B Course Reader|Thorne]] for curvature.

---

## 1. The field

Near the Earth, the field is a curl-free potential field from internal sources (Gauss; 200C Eq. 7.1). Its leading multipole is a dipole:

$$\Phi_m = \frac{B_ER_E^3\cos\theta}{r^2},\qquad\mathbf B = -\nabla\Phi_m = \frac{B_ER_E^3}{r^3}\left(2\cos\theta\,\hat{\mathbf r} + \sin\theta\,\hat{\boldsymbol\theta}\right),\qquad|\mathbf B| = \frac{B_ER_E^3}{r^3}\sqrt{1 + 3\cos^2\theta}.$$

Here $\theta$ is magnetic colatitude and $B_E$ is the surface equatorial field (S&N Eqs. 11.1–11.3; 200C Eq. 7.2). SymPy confirms $\nabla\cdot\mathbf B = 0$. As written, the moment points along $+\hat{\mathbf z}$. **Earth's actual moment points roughly south**, so the field points *down* in the northern hemisphere. Flip the overall sign for Earth; magnitudes are unaffected.

> **Why sources quote different moments.** 200C gives $7.8\times10^{15}$ T m$^3$ ($30.2\ \mu$T $R_E^3$, epoch around 2007). S&N quote $7.9\times10^{15}$ in the text and $8.06\times10^{15}$ in Table 2.4 ($B_E = 31.1\ \mu$T). Older texts give $8.0\times10^{15}$. The dipole is weakening by about 0.1%/yr (200C §7.2.2), so these are different **epochs**, not errors. The same goes for the tilt: 11.5° (S&N; the 1850–1960 value) vs. 10.2° (200C; 2007).

**The dip angle.** The field makes an angle $I$ with the horizontal, where $\tan I = B_r/B_\theta = 2\cot\theta = 2\tan\lambda$ (S&N Eqs. 11.5–11.7; $\lambda$ is magnetic latitude). That's why F-region plasma diffusing along $\mathbf B$ moves vertically at a rate scaled by $\sin^2 I$ ([[Plasma Diffusion Along B]]), and why the equatorial ionosphere, where $I = 0$, is so different ([[Equatorial Ionosphere]]).

---

## 2. Field lines and $L$

A field line is everywhere tangent to $\mathbf B$: $dr/(r\,d\theta) = B_r/B_\theta = 2\cot\theta$. Integrating gives (SymPy; 200C Eq. 7.6; S&N Eq. 11.9)

$$r = r_0\sin^2\theta\qquad\Longleftrightarrow\qquad\boxed{r = LR_E\cos^2\lambda},$$

where $L$ is the equatorial crossing distance in Earth radii. Setting $r = R_E$ gives the **invariant latitude** at the footpoint:

$$\cos^2\Lambda = \frac1L,\qquad\Lambda = \arccos L^{-1/2}.$$

$L = 4$ maps to 60° and $L = 10$ to 71.6° (200C §7.2.1). The auroral oval near 65–70° corresponds to $L\approx6$–9, and the RISR-N polar-cap field lines near 80° map to $L > 30$. Those are open in practice: the dipole formula labels them, but the field line goes into the tail, not to the conjugate point.

**Along a field line**, $|B|$ grows toward the footpoint:

$$\frac{B(\lambda)}{B_{\rm eq}} = \frac{\sqrt{1 + 3\sin^2\lambda}}{\cos^6\lambda},\qquad B_{\rm eq} = \frac{B_E}{L^3}.$$

| $L$ | $\Lambda$ | Field-line length (foot to foot) | $B_{\rm foot}/B_{\rm eq}$ |
|---|---|---|---|
| 2 | 45.0° | 3.4 $R_E$ | 13 |
| 4 | 60.0° | 9.0 $R_E$ | 115 |
| 6.6 (GEO) | 67.1° | 16.2 $R_E$ | 541 |
| 10 | 71.6° | 25.6 $R_E$ | 1920 |

The huge mirror ratio is why the loss cone at large $L$ is only a few degrees ([[Adiabatic Invariants and Magnetic Mirrors]] §2).

---

## 3. Gradients, curvature and flux tubes

**Equatorial gradient and curvature.** At the equator, SymPy gives

$$\frac{|\nabla B|}{B} = \frac3r,\qquad\kappa = |\hat{\mathbf b}\cdot\nabla\hat{\mathbf b}| = \frac3r\ \ (R_c = r/3;\ \text{Thorne Ch. 1}).$$

These two factors of 3 are the "3" in the equatorial ∇B drift and in the [[Dessler-Parker-Sckopke Relation]] ($v_D = 3W_\perp/qBr$). Because $B\propto r^{-3}$, the product $Br^3$ is constant on the equator, and the DPS result doesn't depend on where the particles are.

**Flux-tube cross-section.** Since $BA$ = const along a tube, $A\propto r^3/\sqrt{1 + 3\cos^2\theta}$. Differentiating along $\hat{\mathbf b}$ gives (S&N Eq. 11.12; SymPy)

$$\frac1A\frac{dA}{ds} = \frac{9\cos\theta + 15\cos^3\theta}{r(1 + 3\cos^2\theta)^{3/2}}\xrightarrow{\theta\to0}\frac3r.$$

That's the $A\propto r^3$ used for the polar wind ([[Polar Wind Transonic Outflow]]). The tube flares faster than spherical expansion, $A\propto r^2$ ([[Parker Solar Wind and Spiral]]).

**Flux-tube volume.** The volume per unit magnetic flux is $V = \int ds/B$. With $ds = LR_E\cos\lambda\sqrt{1 + 3\sin^2\lambda}\,d\lambda$, the square roots cancel (SymPy):

$$\frac{ds}{B} = \frac{L^4R_E}{B_E}\cos^7\lambda\,d\lambda\quad\Longrightarrow\quad V\approx\frac{32}{35}\frac{L^4R_E}{B_E}.$$

The integral runs between the footpoints; it gives $0.913$ at $L = 4$ and $0.894$ at $L = 2$, against the large-$L$ limit $32/35 = 0.914$. The **$L^4$** scaling is why a fixed number of ions per flux tube gives a density falling as about $L^{-4}$, roughly the observed plasmasphere profile. The same $V$ enters the standard interchange-stability criterion through $pV^{5/3}$ (stated here, not derived).

**Flux through the polar cap.** The flux crossing the surface poleward of invariant latitude $\Lambda$ is $\Phi = \int B_r\,dA = 2\pi R_E^2B_E\cos^2\Lambda = 2\pi R_E^2B_E/L$:

| Polar-cap boundary | Open flux |
|---|---|
| 80° | 0.24 GWb |
| 75° | 0.53 GWb |
| 70° | 0.92 GWb |

This converts a polar-cap boundary latitude into open flux, which is the budget the [[Dungey Cycle]] adds to and subtracts from. Note the sensitivity: moving the boundary by 5° changes the open flux by a factor of about 2.

---

## What we assumed, and where it breaks

- **Centered, untilted dipole.** The real internal field has significant higher multipoles: the South Atlantic Anomaly is the weak-field region where radiation-belt particles reach the atmosphere (200C §7.2.2). IGRF spherical harmonics (200C Eqs. 7.7–7.10) and apex or AACGM coordinates ([[Laundal Richmond 2016 Magnetic Coordinates]]) handle this properly.
- **No external currents.** Beyond about 5–6 $R_E$, magnetopause, tail and ring currents distort the field. The dayside is compressed, the nightside stretched. McIlwain's $L$ and Roederer's $L^*$ generalize $L$ as a drift-shell label rather than an equatorial distance ([[Adiabatic Invariants and Magnetic Mirrors]] §3).
- **Closed field lines.** Poleward of the oval, field lines are open. "$L$" there is just a label for the latitude via $\cos^2\Lambda = 1/L$.

---

## Verification

- **Sources agree.**
  - Potential, components, magnitude, field-line equation, flux-tube $(1/A)\,dA/ds$, dip-angle relations: [[Schunk Nagy 2009 Ionospheres|S&N]] §11.1, Eqs. 11.1–11.12.
  - The same dipole formulas, $r = L\cos^2\lambda$, invariant latitude and its 60°/71.6° examples, moment and tilt history: 200C textbook Ch. 7 §§7.2–7.2.2, Eqs. 7.1–7.10.
  - Curvature radius $R_c = r/3$: [[Thorne 1993 AOS 250B Course Reader|Thorne]] Ch. 1 ("In a pure dipole field $R_c\sim R/3$").
- **SymPy.**
  - $\mathbf B = -\nabla\Phi_m$ and $|\mathbf B|$.
  - $\nabla\cdot\mathbf B = 0$.
  - The field-line ODE solution.
  - Equatorial $|\nabla B|/B = \kappa = 3/r$.
  - S&N Eq. 11.12 and its polar limit $3/r$.
  - $ds/B\propto\cos^7\lambda$, and $\int_0^{\pi/2}\cos^7\lambda\,d\lambda = 16/35$.
- **Numerical.**
  - The $L$ table (invariant latitude, length, mirror ratio).
  - Flux-tube volume vs. 32/35.
  - Open flux vs. polar-cap latitude.
  - Moment consistency ($30.2\ \mu$T $R_E^3 = 7.81\times10^{15}$ T m$^3$).

## Sources

- [[Schunk Nagy 2009 Ionospheres]] — §11.1 (dipole magnetic field)
- 200C textbook Ch. 7 §7.2 (`Atlas/Texts/Textbooks/200C Textbook/Ch7_Solar-Wind_Interaction_with_Magnetized_ObstaclesJLcomm_CTR.pdf`)
- [[Thorne 1993 AOS 250B Course Reader]] — dipole curvature
- [[Laundal Richmond 2016 Magnetic Coordinates]] — beyond the dipole
