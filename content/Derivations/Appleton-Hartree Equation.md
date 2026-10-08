---
type: derivation
status: draft
updated: 2026-10-08
sources: 3
tags: [derivations, ionosphere, radio-propagation, ionosonde, cold-plasma, magneto-ionic]
prerequisites: "[[Debye Shielding and the Plasma Frequency]] (plasma frequency); [[Guiding-Center Drifts]] §1 (gyration)"
next: "[[Cold-Plasma Waves]]"
---

# Appleton-Hartree Equation

**Part II (ionosphere), page 9** of the [[Derivations Index]] · Concept pages: [[HF Radio Propagation]], [[Plasma Waves]]

## Where we're going

An ionosonde sweeps frequency upward and times the echoes. At some frequency the echo from the F layer disappears: the wave punches through. That frequency, $f_oF_2$, gives the peak density directly through $f = 8.98\sqrt{n}$ Hz. But every ionogram shows **two** traces split by about 0.7 MHz: the ordinary (O) and extraordinary (X) waves. Why two, and why that splitting?

The answer is the **magneto-ionic refractive index** for radio waves in a magnetized, cold electron plasma: the Appleton (or Appleton–Hartree) formula. We'll derive it by treating the electrons as a polarizable medium, read off its cutoffs, and connect them to ionograms and HF propagation. The derivation follows [[Davies 1966 Ionospheric Radio Propagation|Davies]] §2.3.2, cross-checked against the Stix cold-plasma form in [[Bellan 2006 Fundamentals of Plasma Physics|Bellan]] §6.2.

---

## 1. Setting up

**Assumptions** (Davies' list):

- a plane, monochromatic wave;
- a neutral, uniform medium in a uniform $\mathbf{B}_0$;
- **only electrons respond** (ions are too heavy at HF);
- a **cold** plasma (no thermal motion);
- an electron collision frequency $\nu$ independent of energy;
- free-space magnetic permeability.

Let the wave travel along axis 1, $\propto e^{i(\omega t - kx_1)}$ in Davies' sign convention, with $\mathbf{B}_0$ in the 1–3 plane at angle $\theta$ to $\mathbf{k}$. Define the dimensionless **magneto-ionic parameters**:

$$X = \frac{\omega_{pe}^2}{\omega^2},\qquad Y = \frac{\omega_{ce}}{\omega},\qquad Y_L = Y\cos\theta,\quad Y_T = Y\sin\theta,\qquad Z = \frac{\nu}{\omega}.$$

$X$ measures how dense the plasma is relative to the wave frequency, $Y$ how strongly magnetized it is, and $Z$ how collisional.

**Maxwell's equations.** Treat the electrons as a polarization $\mathbf{P} = -ne\boldsymbol\xi$, where $\boldsymbol\xi$ is the electron displacement, so $\mathbf{D} = \varepsilon_0\mathbf{E} + \mathbf{P}$. Davies stresses that you must choose either polarization *or* conduction current, never both. For a plane wave:

- $\nabla\cdot\mathbf{D} = 0$ gives $D_1 = 0$: **$\mathbf{D}$ is transverse**, but $\mathbf{E}$ and $\mathbf{P}$ can have longitudinal parts.
- The curl equations give, with $n = ck/\omega$,

$$n^2 = 1 + \frac{P_2}{\varepsilon_0E_2} = 1 + \frac{P_3}{\varepsilon_0E_3}.$$

So everything reduces to finding the medium's response $P/E$. The **wave polarization** is $R = P_3/P_2 = E_3/E_2$.

**The electron equation of motion** includes the wave field, the Lorentz force from $\mathbf{B}_0$ (the wave's own $\mathbf{B}$ is a $v/c$ correction and is dropped) and collisional friction:

$$m\ddot{\boldsymbol\xi} = -e\mathbf{E} - e\dot{\boldsymbol\xi}\times\mathbf{B}_0 - m\nu\dot{\boldsymbol\xi}.$$

Multiply by $-ne$, replace time derivatives with $i\omega$, and write it in terms of $\mathbf{P}$. The result is the **constitutive relations**, three linear equations linking $\varepsilon_0X\mathbf{E}$ to $\mathbf{P}$ through $Z$, $Y_L$ and $Y_T$ (Davies Eqs. 2.69).

---

## 2. Solving: a quadratic for the polarization, then the index

Use $D_1 = 0$ (so $\varepsilon_0E_1 = -P_1$) to eliminate the longitudinal components. Then take a combination of the transverse equations that cancels $E$, using $P_2/E_2 = P_3/E_3$. What remains is a **quadratic for the polarization** (Davies Eq. 2.72):

$$Y_LR^2 - \frac{iY_T^2}{1 - X - iZ}R + Y_L = 0,$$

$$R = \frac{i}{Y_L}\left[\frac{Y_T^2}{2(1-X-iZ)}\mp\sqrt{\frac{Y_T^4}{4(1-X-iZ)^2} + Y_L^2}\right].$$

**Two roots means two characteristic waves.** A magnetized plasma propagates only two polarizations, and they generally have different refractive indices. Feeding $R$ back into $n^2 = 1 + P_2/\varepsilon_0E_2$ gives

$$\boxed{n^2 = 1 - \frac{X}{1 - iZ - \dfrac{Y_T^2}{2(1-X-iZ)}\pm\sqrt{\dfrac{Y_T^4}{4(1-X-iZ)^2} + Y_L^2}}}$$

The **+** sign is the **ordinary (O)** wave and the **−** sign the **extraordinary (X)** wave (Davies' convention, valid for $X < 1$). Davies notes that Hartree's proposed Lorentz-polarization correction is not supported by theory or experiment, so the "Hartree" in the name is historical.

**Check against general plasma theory.** For collisionless electrons, this must agree with the cold-plasma dispersion relation written in Stix's $R$, $L$, $P$, $S$ notation (Bellan Ch. 6):

$$An^4 - Bn^2 + C = 0,\qquad R = 1-\frac{X}{1-Y},\ L = 1-\frac{X}{1+Y},\ P = 1-X.$$

I checked this numerically. Over 20,000 random $(X, Y, \theta)$, the two roots of the Appleton formula match the two Stix roots to $10^{-11}$. Appleton–Hartree is just the cold-plasma dispersion relation, rearranged for radio propagation.

---

## 3. Cutoffs: why ionograms have two traces

A vertically incident wave reflects where $n = 0$ (Davies §2.3.3: at reflection the ray turns horizontal, $n_r = \sin\theta_0$, which is 0 for normal incidence). Setting $n^2 = 0$ with $Z = 0$:

| Wave | Reflection condition | In frequency |
|---|---|---|
| **O** (+) | $X = 1$ | $f = f_{pe}$, independent of $\mathbf{B}$ |
| **X** (−), $f > f_H$ | $X = 1 - Y$ | $f(f - f_H) = f_{pe}^2$ |
| **X** (−), $f < f_H$ | $X = 1 + Y$ | $f(f + f_H) = f_{pe}^2$ |

These are Davies Eqs. 2.80–2.81. The O-wave reflects exactly where the plasma frequency matches, as if the field weren't there. The X-wave reflects at a lower density, at a level that depends on the field's *strength* but not its direction.

**Consequences:**

- **$f_oF_2$ measures $N_mF_2$ directly:** $N_mF_2 = f_oF_2^2/80.6$ m$^{-3}$ with $f$ in Hz (from $f_{pe} = 8.98\sqrt{n}$; [[Debye Shielding and the Plasma Frequency]] §1).
- **The X trace is shifted up.** Its penetration frequency satisfies $f_x(f_x - f_H) = f_{oF_2}^2$, so $f_xF_2\approx f_oF_2 + f_H/2$. With $f_H\approx1.4$ MHz (high latitude) and $f_oF_2 = 9$ MHz, $f_xF_2 = 9.73$ MHz. The trace separation of about 0.7 MHz is half the gyrofrequency.
- **Absorption** enters through $Z$. It's largest where $\nu$ is large (the D region) and near $Y\approx1$, the gyro-resonance at about 1.4 MHz. That's why low HF frequencies are absorbed during daytime and during polar-cap absorption events ([[HF Radio Propagation]]).

**Limits worth knowing:**

- $Y\to0$ (no field): $n^2 = 1 - X$ for both waves. This is the unmagnetized result.
- $\theta = 0$ (along $\mathbf{B}$): $n^2 = 1 - X/(1\pm Y)$. These are circularly polarized waves, and the $1 - X/(1-Y)$ branch at $\omega\ll\omega_{ce}$ is the **whistler** ([[Plasma Waves]]).
- $\theta = 90°$: the O-wave has $n^2 = 1 - X$ exactly. This matches the "Ordinary mode" entry on [[Plasma Waves]].

---

## What we assumed, and where it breaks

- **Cold plasma.** Thermal effects matter near resonances (upper hybrid, gyro-harmonics). Those are kinetic topics.
- **Electrons only.** Fine at HF. At VLF/ELF the ions matter (ion-cyclotron and lower-hybrid physics).
- **Energy-independent collisions.** The Sen–Wyller formulation generalizes this (Davies §2.3.4).
- **Uniform medium.** Real propagation uses the local index with ray tracing (WKB, Snell's law in a stratified medium; [[Coleman 1992 Ionospheric Ray Tracing]]) or full-wave solutions near reflection.

---

## Verification

- **Sources agree.**
  - Assumptions, constitutive relations, polarization quadratic, O/X reflection conditions: [[Davies 1966 Ionospheric Radio Propagation|Davies]] §2.3.2–2.3.3, Eqs. 2.59–2.81.
  - Cold-plasma $S$, $D$, $P$ and $R$, $L$ cutoffs and resonances: [[Bellan 2006 Fundamentals of Plasma Physics|Bellan]] §6.2.
  - O-mode $n^2 = P$ cutoff at $\omega_{pe}$: consistent with [[Plasma Waves]].
- **Numerical.** The Appleton formula vs. the Stix quartic roots over 20,000 random cases (collisionless, electrons only): maximum relative difference $7.6\times10^{-12}$. Also the $f_xF_2$ example.
- **SymPy.** The zeros of $n^2$ are $X = 1$ and $X = 1\pm Y$. SymPy finds all three in the combined numerator; the assignment of each to a branch follows Davies.
- **Not reproduced step by step:** the algebra from the constitutive relations to the polarization quadratic (Davies Eqs. 2.69–2.72). It is cited from Davies and validated indirectly by the agreement with Stix.

## Sources

- [[Davies 1966 Ionospheric Radio Propagation]] — §2.3 (magneto-ionic theory; derivation and properties of the Appleton formula)
- [[Bellan 2006 Fundamentals of Plasma Physics]] — Ch. 6 (cold-plasma waves; Stix $S$, $D$, $P$; cutoffs and resonances)
- [[Coleman 1992 Ionospheric Ray Tracing]] — application to HF ray tracing
