---
type: derivation
status: draft
updated: 2026-10-08
sources: 3
tags: [derivations, ionosphere, polar-wind, ion-outflow, transonic-flow, IPWM]
prerequisites: "[[Plasma Diffusion Along B]] (ambipolar field, minor ions); [[Moment Equations from the Vlasov Equation]] (momentum equation)"
next: "[[Parker Solar Wind and Spiral]]"
---

# Polar Wind Transonic Outflow

**Part II (ionosphere), page 8** of the [[Derivations Index]] · Builds on: [[Plasma Diffusion Along B]] · Concept page: [[Polar Wind]]

## Where we're going

On open polar-cap field lines nothing caps the ionosphere from above. [[Plasma Diffusion Along B]] showed that the ambipolar electric field pushes light ions *up* (H$^+$ feels a net upward force about 7 times its weight in an O$^+$ plasma). Once plasma starts flowing upward along a diverging flux tube, a new question appears: **does it stay subsonic, or does it break through to supersonic outflow, the way the solar wind does?**

This page derives the **Mach-number equation** and shows that it has a critical point. The only solution that goes supersonic must pass smoothly through $M = 1$ at a specific radius, exactly as in a de Laval rocket nozzle or Parker's solar wind. Following [[Schunk Nagy 2009 Ionospheres|Schunk & Nagy]] §5.8 and §12.16, with the 200C textbook Ch. 2 §2.12.1 as a second source.

---

## 1. Momentum and continuity along a flux tube

The assumptions are S&N's (a)–(f): a single ion species, ambipolar flow ($n_i = n_e$, $u_i = u_e$), isothermal, steady, stationary neutrals, and no stress, heat flow or centrifugal terms. Unlike [[Plasma Diffusion Along B]], we **keep the inertial term** $n_im_iu\,du/dr$, because that's what matters once the flow is fast.

The ion momentum equation along $\mathbf{B}$, with the ambipolar field $eE_\parallel = -(1/n)\,d(nk_BT_e)/dr$ substituted, is (S&N Eq. 5.80)

$$n m_i u\frac{du}{dr} + k_B(T_e+T_i)\frac{dn}{dr} + n m_i g = -n m_i\nu_{in}u.$$

Divide by $nm_i$ and introduce the **ion-acoustic speed**

$$V_S = \sqrt{\frac{k_B(T_e+T_i)}{m_i}}.$$

The electron temperature appears because the electrons push on the ions through $E_\parallel$:

$$u\frac{du}{dr} + \frac{V_S^2}{n}\frac{dn}{dr} + g = -\nu_{in}u.$$

**Continuity** in a flux tube of cross-section $A(r)$, with no sources or sinks, is $\frac{1}{A}\frac{d}{dr}(Anu) = 0$. Flux conservation then fixes how density falls as the flow speeds up and the tube widens:

$$\frac{1}{n}\frac{dn}{dr} = -\frac{1}{u}\frac{du}{dr} - \frac{1}{A}\frac{dA}{dr}.$$

Since $B\propto1/A$ and a dipole near the pole has $B\propto r^{-3}$, $A\propto r^3$.

---

## 2. The Mach-number equation

Substitute the density gradient and collect the $du/dr$ terms. With $M = u/V_S$:

$$(u^2 - V_S^2)\frac{1}{u}\frac{du}{dr} = \frac{V_S^2}{A}\frac{dA}{dr} - g - \nu_{in}u,$$

$$\boxed{\frac{dM}{dr} = \frac{M}{M^2-1}\left(\frac{1}{A}\frac{dA}{dr} - \frac{g}{V_S^2} - \frac{\nu_{in}}{V_S}M\right)}$$

This is S&N Eq. 5.87, and it has the same structure as the 200C text's Eq. 2.87. Read it like a nozzle:

- **Prefactor $M/(M^2-1)$:** negative for subsonic flow, positive for supersonic flow, and singular at $M = 1$.
- **The bracket** is the competition between the pushes:
  - area divergence $\frac1A\frac{dA}{dr} = 3/r$, which accelerates the flow (it acts like a pressure drop);
  - gravity, which decelerates it;
  - friction, which also decelerates it.

At low altitude, gravity and friction win: the bracket is negative, and with a negative prefactor $dM/dr > 0$. The flow speeds up. Higher up, $\nu_{in}\to0$ and $g\propto r^{-2}$ falls faster than $3/r$, so **the bracket changes sign**. What happens next depends on where the flow is at that moment:

- if it's still subsonic, $dM/dr$ turns negative and the flow decelerates again (**breeze**, S&N Fig. 5.4 curve B);
- if it's exactly sonic **where the bracket vanishes**, it passes smoothly through $M = 1$ and keeps accelerating (**the transonic wind**, curve A).

Any other way of reaching $M = 1$ makes $dM/dr$ infinite, which is unphysical. So the supersonic solution is unique. It is the **critical solution**, and the pressure difference between the ionosphere and the magnetospheric "sink" decides which branch nature picks (S&N §5.8).

> **De Laval nozzle.** In a rocket nozzle, subsonic gas accelerates in a *converging* section ($dA/dr < 0$, so the bracket is negative with negative prefactor) and passes $M = 1$ at the throat. It then keeps accelerating in the *diverging* section (positive bracket, positive prefactor). In the polar wind, gravity and friction play the role of the converging section.

---

## 3. The sonic point

For the collisionless case ($\nu_{in} = 0$), the bracket vanishes where

$$\frac{p}{r_c} = \frac{GM_E}{r_c^2V_S^2}\quad\Longrightarrow\quad r_c = \frac{GM_E}{p\,V_S^2},\qquad p = \begin{cases}3 & \text{polar dipole flux tube}\\2 & \text{radial (Parker solar wind)}\end{cases}$$

The equation also has an exact integral (verified by SymPy) for $A\propto r^3$:

$$\frac{M^2}{2} - \ln M = 3\ln r + \frac{GM_E}{V_S^2r} + C.$$

The transonic solution is the one whose constant $C$ makes $M = 1$ at $r = r_c$. The $p = 2$ version of this integral is Parker's 1958 solar-wind solution (see [[Parker 1958 Solar Wind]]).

**Numbers** (single-ion, isothermal, collisionless model):

| Ion | $T_e+T_i$ | $V_S$ | Sonic radius $r_c$ |
|---|---|---|---|
| O$^+$ | 3000 K | 1.2 km/s | 13.5 $R_E$ |
| O$^+$ | 6000 K | 1.8 km/s | 6.7 $R_E$ |
| H$^+$ | 3000 K | 5.0 km/s | 0.84 $R_E$ (below the surface) |
| H$^+$ | 6000 K | 7.0 km/s | 0.42 $R_E$ (below the surface) |

The table makes a physical point:

- **O$^+$ at ordinary ionospheric temperatures is gravitationally bound.** Its sonic point lies many Earth radii out, so it can't develop a thermal wind on its own. Getting O$^+$ out needs extra energy: transverse heating, Poynting flux, or wave–particle heating ([[Atmospheric Escape]], [[Zou 2021 SED Ion Upflow]]). This is S&N's "classical polar wind with gravitationally bound O$^+$."
- **For H$^+$, gravity is nearly irrelevant.** The collisionless "sonic radius" is below the surface. So the subsonic-to-supersonic transition is set by the **friction term** ($\nu_{in}$, mainly H$^+$–O$^+$ collisions), which dies off with altitude. In the real polar wind, H$^+$ is also a *minor* ion in an O$^+$-dominated plasma, so the O$^+$ ambipolar field pushes it upward even harder ([[Plasma Diffusion Along B]] §3). Both effects favor supersonic H$^+$, which is what S&N's full models give, with transonic flow and Mach number about 1.2 near 1400 km in one case (S&N Fig. 12.50).

**The escape flux is production-limited.** In the full model, H$^+$ is made by O$^+$ + H ⇌ H$^+$ + O charge exchange. In steady state the escape flux can't exceed the column production, so as the topside pressure is lowered, the H$^+$ flux **saturates**, with a magnitude proportional to $[\text{O}^+][\text{H}]/[\text{O}]$ (S&N Fig. 12.52). For a 20 km/s escape velocity, S&N's model gives $8.5\times10^7$ cm$^{-2}$ s$^{-1}$.

---

## What we assumed, and where it breaks

- **Isothermal, single ion, no stress or heat flow.** The real polar wind becomes collisionless and anisotropic, with $T_\parallel\neq T_\perp$ and heat flux. Early hydrodynamic models kept a Navier–Stokes stress term *precisely because it removes the $M = \pm1$ singularity* (S&N §12.16). Modern models use 8- to 16-moment, kinetic or PIC approaches; [[IPWM]] uses 8-moment equations ([[Blelly Schunk 1993 Moment Comparison]]).
- **Steady flow along a fixed flux tube.** The polar wind convects horizontally across the polar cap in about the same time it takes to flow out, so the conditions are never steady (S&N §12.16).
- **No centrifugal acceleration, wave heating, photoelectrons or hot magnetospheric electrons.** All of these enhance outflow (S&N's list of "non-classical" processes).

---

## Verification

- **Sources agree.**
  - Momentum equation, continuity with $A\propto r^3$, Mach equation, singularity, breeze vs. wind branches, de Laval analogy: [[Schunk Nagy 2009 Ionospheres|S&N]] §5.8, Eqs. 5.80–5.87, Fig. 5.4.
  - The same equation in the 200C textbook Ch. 2 §2.12.1 (Eqs. 2.82–2.87), which notes its resemblance to the solar-wind equation.
  - Full-model behavior (transonic Mach 1.17 at 1400 km; flux saturation; gravitationally bound O$^+$): S&N §12.16, Figs. 12.50–12.52.
- **SymPy.**
  - The Mach equation follows exactly from momentum plus flux-tube continuity.
  - Sonic radii $GM/(pV_S^2)$ for $p = 2, 3$.
  - The integral of motion is exactly conserved along the collisionless ODE.
- **Numerical.** The sonic-radius table above.
- **Interpretive (mine, not stated by the sources):** the explicit sonic-radius table and the conclusion that the collisionless H$^+$ sonic point lies below the surface. This follows directly from the verified formula, and it is consistent with S&N's statement that O$^+$ is gravitationally bound while H$^+$ escapes.

## Sources

- [[Schunk Nagy 2009 Ionospheres]] — §5.8 (supersonic ion outflow, Mach equation), §12.16 (polar wind: hydrodynamic models, transonic solutions, flux limiting)
- 200C textbook Ch. 2 §2.12.1, *High-speed outflow* (`Atlas/Texts/Textbooks/200C Textbook/Ch2_UpperAtmosphereIonosphere.pdf`)
- [[Parker 1958 Solar Wind]] — the $A\propto r^2$ analogue
