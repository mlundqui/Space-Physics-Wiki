---
type: derivation
status: draft
updated: 2026-10-08
sources: 3
tags: [derivations, plasma-waves, cold-plasma, whistler, Stix, dispersion]
prerequisites: "[[Guiding-Center Drifts]] (polarization and E×B drifts); [[Appleton-Hartree Equation]] (electron-only version)"
next: "[[Dipole Field and L-Shells]]"
---

# Cold-Plasma Waves

**Part III, page 8** of the [[Derivations Index]] · Builds on: [[Appleton-Hartree Equation]], [[Guiding-Center Drifts]] · Concept pages: [[Plasma Waves]], [[Wave-Particle Interactions]]

## Where we're going

The [[Appleton-Hartree Equation]] gave the refractive index for HF radio waves, with only electrons moving. Below a few kHz, the ions join in, and a whole zoo of waves appears: whistlers, chorus, hiss, EMIC waves, lower-hybrid waves, Alfvén waves. Remarkably, *all* of them are branches of one dispersion relation, the **cold-plasma dispersion relation** in Stix's notation.

We'll build the dielectric tensor from single-particle motion, get the dispersion relation, organize it by cutoffs and resonances, and then pull out the whistler, including why its tone falls and why it stays within 19.5° of $\mathbf B$. We follow [[Bellan 2006 Fundamentals of Plasma Physics|Bellan]] Ch. 6 (§§6.1–6.6), with the Stix (1962) notation it adopts, and cross-check against [[Thorne 1993 AOS 250B Course Reader|Thorne's 250B reader]] for magnetospheric applications.

---

## 1. Each species is a driven oscillator

Take a uniform $\mathbf B_0 = B_0\hat{\mathbf z}$, a cold plasma (so no pressure) and small fields $\propto e^{i\mathbf k\cdot\mathbf x - i\omega t}$. The linearized momentum equation for species $\sigma$ is $-i\omega m_\sigma\tilde{\mathbf v}_\sigma = q_\sigma(\tilde{\mathbf E} + \tilde{\mathbf v}_\sigma\times\mathbf B_0)$. Solving for $\tilde{\mathbf v}_\sigma$ (Bellan Eq. 6.7):

$$\tilde{\mathbf v}_\sigma = \frac{iq_\sigma}{\omega m_\sigma}\left[\tilde E_z\hat{\mathbf z} + \frac{\tilde{\mathbf E}_\perp}{1 - \omega_{c\sigma}^2/\omega^2} - \frac{i\omega_{c\sigma}}{\omega}\frac{\hat{\mathbf z}\times\tilde{\mathbf E}}{1 - \omega_{c\sigma}^2/\omega^2}\right],\qquad\omega_{c\sigma} = \frac{q_\sigma B_0}{m_\sigma}\ \text{(signed)}.$$

The three terms are old friends from [[Guiding-Center Drifts]], now at finite frequency:

- **Parallel quiver.** Along $\mathbf B$ the particle doesn't feel the field, so it moves exactly as in an unmagnetized plasma.
- **Generalized polarization drift.** For $\omega\ll\omega_c$ this is $m\dot{\mathbf E}_\perp/qB^2$, and it resonates at $\omega = \omega_c$.
- **Generalized $\mathbf E\times\mathbf B$ drift.** For $\omega\ll\omega_c$ this is $\mathbf E\times\mathbf B/B^2$.

Sum $n_\sigma q_\sigma\tilde{\mathbf v}_\sigma$ over species to get the current, and put it into Ampère's law as a dielectric tensor, $\nabla\times\mathbf B = c^{-2}\partial_t(\overleftrightarrow{K}\cdot\mathbf E)$ (Bellan Eqs. 6.10–6.12):

$$\overleftrightarrow{K} = \begin{pmatrix}S & -iD & 0\\ iD & S & 0\\ 0 & 0 & P\end{pmatrix},\quad S = 1 - \sum_\sigma\frac{\omega_{p\sigma}^2}{\omega^2 - \omega_{c\sigma}^2},\quad D = \sum_\sigma\frac{\omega_{c\sigma}\omega_{p\sigma}^2}{\omega(\omega^2 - \omega_{c\sigma}^2)},\quad P = 1 - \sum_\sigma\frac{\omega_{p\sigma}^2}{\omega^2}.$$

The names are Stix's mnemonics: **S**um, **D**ifference, **P**arallel. They become clear when you rotate to circular components:

$$R\equiv S + D = 1 - \sum_\sigma\frac{\omega_{p\sigma}^2}{\omega(\omega + \omega_{c\sigma})},\qquad L\equiv S - D = 1 - \sum_\sigma\frac{\omega_{p\sigma}^2}{\omega(\omega - \omega_{c\sigma})}.$$

$R$ blows up at the **electron** cyclotron frequency (recall $\omega_{ce} < 0$ with signed charge). $L$ blows up at the **ion** cyclotron frequency. **R**ight-handed waves resonate with electrons and **L**eft-handed waves with ions ("Lion", as Bellan puts it).

---

## 2. The dispersion relation

Faraday plus Ampère give $\mathbf n\times(\mathbf n\times\mathbf E) + \overleftrightarrow K\cdot\mathbf E = 0$, with $\mathbf n = c\mathbf k/\omega$. Put $\mathbf n$ in the $x$–$z$ plane at angle $\theta$ to $\mathbf B_0$:

$$\begin{pmatrix}S - n^2\cos^2\theta & -iD & n^2\sin\theta\cos\theta\\ iD & S - n^2 & 0\\ n^2\sin\theta\cos\theta & 0 & P - n^2\sin^2\theta\end{pmatrix}\begin{pmatrix}E_x\\E_y\\E_z\end{pmatrix} = 0.$$

Setting the determinant to zero gives (SymPy confirms the expansion; Bellan Eqs. 6.47–6.48):

$$\boxed{An^4 - Bn^2 + C = 0},\qquad\begin{aligned}A &= S\sin^2\theta + P\cos^2\theta\\ B &= RL\sin^2\theta + PS(1 + \cos^2\theta)\\ C &= PRL\end{aligned}$$

using $S^2 - D^2 = RL$. The discriminant is $B^2 - 4AC = (RL - SP)^2\sin^4\theta + 4P^2D^2\cos^2\theta\ge0$ (Bellan Eq. 6.50; SymPy). So $n^2$ is always **real**. Each mode either propagates ($n^2 > 0$) or is evanescent ($n^2 < 0$). There's no growth or damping without collisions or kinetic effects.

**The Stix tan² form** isolates the angle (SymPy-verified):

$$\tan^2\theta = -\frac{P(n^2 - R)(n^2 - L)}{(Sn^2 - RL)(n^2 - P)}.$$

It immediately gives the two principal directions:

| Direction | Modes | Notes |
|---|---|---|
| $\theta = 0$ (parallel) | $n^2 = R$ (right circular), $n^2 = L$ (left circular) | Also $P = 0$, an electrostatic plasma oscillation |
| $\theta = 90°$ (perpendicular) | $n^2 = P$ (**O-mode**), $n^2 = RL/S$ (**X-mode**) | Matches [[Appleton-Hartree Equation]] with ions dropped |

---

## 3. Cutoffs and resonances

From the $An^4 - Bn^2 + C$ form:

- **Cutoffs** ($n\to0$, reflection) occur where $C = 0$, i.e. $P = 0$, $R = 0$ or $L = 0$. These are independent of $\theta$.
- **Resonances** ($n\to\infty$, absorption) occur where $A = 0$, i.e. $\tan^2\theta = -P/S$. These depend on direction, so a resonance at $\theta = 0$ needs $R$ or $L\to\infty$ (cyclotron), and at $\theta = 90°$ needs $S = 0$ (**hybrid**).

Electron-only cutoffs (SymPy) and hybrid resonances (Bellan Eqs. 6.38–6.40):

$$\omega_P = \omega_{pe},\qquad\omega_{R,L} = \pm\frac{|\omega_{ce}|}{2} + \sqrt{\frac{\omega_{ce}^2}{4} + \omega_{pe}^2},\qquad\omega_{UH}^2 = \omega_{pe}^2 + \omega_{ce}^2,\qquad\omega_{LH}^2 = \omega_{ci}^2 + \frac{\omega_{pi}^2}{1 + \omega_{pe}^2/\omega_{ce}^2}.$$

> **Two lower-hybrid formulas.** The full form reduces to $\omega_{LH}\approx\sqrt{|\omega_{ce}|\omega_{ci}}$ only when $\omega_{pe}\gg|\omega_{ce}|$ (dense plasma), and to $\omega_{LH}\approx\omega_{pi}$ when $\omega_{pe}\ll|\omega_{ce}|$.
> - **F region** ($f_{pe}/f_{ce}\approx6$): full 8.07 kHz vs. dense 8.17 kHz, so the shortcut is fine.
> - **$L = 4$ outside the plasmapause** ($n = 10$ cm$^{-3}$, $f_{pe}/f_{ce}\approx2$): full 286 Hz vs. dense 316 Hz, an 11% error.
> - **Auroral density cavity** ($f_{pe} < f_{ce}$): the shortcut fails outright.

**Numbers** at $L = 4$ in the plasmasphere ($B = 484$ nT, $n = 10^3$ cm$^{-3}$):

| Frequency | Value |
|---|---|
| $f_{ce}$ | 13.6 kHz |
| $f_{pe}$ | 284 kHz |
| $f_{UH}$ | 284 kHz |
| $f_R$ | 291 kHz |
| $f_L$ | 277 kHz |
| $f_{LH}$ | 316 Hz |
| Whistler "nose" | 3.4 kHz (see §4) |

Every magnetospheric wave band lives somewhere in this ordering. **Chorus** and **hiss** are whistler-mode waves between $f_{LH}$ and $f_{ce}$. **EMIC** waves are on the $L$ branch below $f_{ci}$. **AKR** is on the R-X branch above $f_R$ ([[Plasma Waves]]).

**The CMA diagram** (Clemmow–Mullaly–Allis; Bellan §6.2.7) maps the cutoff and resonance surfaces in the plane $(\omega_{pe}^2/\omega^2,\ \omega_{ce}^2/\omega^2)$. Between those boundaries, the topology of each mode's wave-normal surface stays the same. It is the "periodic table" of cold-plasma waves.

---

## 4. The whistler

Take $\omega_{ci}\ll\omega < |\omega_{ce}|\cos\theta$ and $\omega_{pe}\gg|\omega_{ce}|$, which holds in the ionosphere and plasmasphere. The ions and the "1" from the displacement current drop out of the $R$-branch, and for $\theta = 0$:

$$n^2\approx\frac{\omega_{pe}^2}{\omega(|\omega_{ce}| - \omega)}\quad\Longrightarrow\quad k = \frac{\omega_{pe}}{c}\sqrt{\frac{\omega}{|\omega_{ce}| - \omega}}.$$

**Group velocity and the falling tone.** Differentiating (SymPy):

$$v_g = \frac{d\omega}{dk} = \frac{2c}{\omega_{pe}|\omega_{ce}|}\,\omega^{1/2}\left(|\omega_{ce}| - \omega\right)^{3/2}.$$

For $\omega\ll|\omega_{ce}|$, $v_g\propto\sqrt\omega$. Lightning launches all frequencies at once, so the high ones arrive first and the tone falls. That's Storey's (1953) explanation. The travel time along a path is the Eckersley law, $t\propto\omega^{-1/2}$ (Bellan Eqs. 6.80–6.86, which uses a stationary-phase argument).

The group velocity **peaks** at

$$\omega_{\rm nose} = \frac{|\omega_{ce}|}{4}\qquad\text{(SymPy: }dv_g/d\omega = 0\text{)}.$$

Frequencies just above *and* below the nose arrive later than the nose itself. A whistler recorded at high latitude therefore has a "nose" shape on a spectrogram. Since $f_{\rm nose}\approx f_{ce,\rm eq}/4$ at the equatorial crossing, nose whistlers measure the **$L$-shell** of the path, and their dispersion measures the **equatorial density**. This was how the plasmapause was discovered (Carpenter 1963; historical note, not from the vault sources).

**Guidance: the Storey angle.** In the low-frequency limit, $n^2\approx\omega_{pe}^2/(\omega|\omega_{ce}|\cos\theta)$, so $n\propto(\cos\theta)^{-1/2}$. The ray (group velocity) direction deviates from $\mathbf k$ by $\tan\delta = -\frac1n\frac{dn}{d\theta} = -\tfrac12\tan\theta$. Maximizing the angle between the ray and $\mathbf B$, $\theta - \arctan(\tfrac12\tan\theta)$, over $\theta$ gives

$$\psi_{\max} = 19.47°\ (19°28'),\ \text{reached at}\ \theta = 54.7°\qquad\text{(numerical)}.$$

So **every** low-frequency whistler ray stays within about 19.5° of the field line, whatever its wave-vector direction. That's why lightning whistlers are ducted to the conjugate hemisphere, and it matches the "within ~19.5°" statement on [[Plasma Waves]].

**Low-frequency limit: Alfvén waves.** For $\omega\ll\omega_{ci}$, $R\approx L\approx S\approx1 + c^2/v_A^2$ and $|P|\to\infty$. The two roots become $n^2 = S$ (fast/compressional) and $n^2\cos^2\theta = S$ (shear Alfvén). Without the displacement-current "1", these are exactly the [[MHD Wave Modes]] (Bellan §6.2.4). MHD is the low-frequency, long-wavelength corner of cold-plasma theory.

---

## What we assumed, and where it breaks

- **Cold.** There are no thermal effects, so no Landau or cyclotron damping, and nothing happens at the resonances themselves (where $n\to\infty$ and the wavelength reaches the gyroradius). Near resonances you need kinetic theory: Bernstein waves, ECH waves ([[Plasma Waves]]), [[Landau Damping]] and cyclotron resonance ([[Quasilinear Diffusion]]).
- **Uniform plasma.** Real propagation uses the local $n(\mathbf x,\omega)$ in ray tracing. Cutoff and resonance *surfaces* become reflection and absorption *layers* (Bellan §6.2.2).
- **No collisions.** Collisions give complex $n$ (cf. $Z$ in [[Appleton-Hartree Equation]]).
- **Relativity.** For AKR, the relativistic mass shift moves the R-X cutoff and cyclotron resonance. That's what lets the cyclotron maser work below the nonrelativistic $f_{ce}$ ([[Strangeway Ch11 The Aurora|Strangeway Ch. 11]]).

---

## Verification

- **Sources agree.**
  - Species velocity response, the $S$/$D$/$P$ tensor, $R$ and $L$, $An^4 - Bn^2 + C$, positive discriminant, parallel/perpendicular modes, hybrid resonances, CMA diagram, whistler and Eckersley dispersion: [[Bellan 2006 Fundamentals of Plasma Physics|Bellan]] §§6.1–6.6, Eqs. 6.7–6.86.
  - The same discriminant written as $F^2 = (RL - PS)^2\sin^4\theta + 4P^2D^2\cos^2\theta$: [[Thorne 1993 AOS 250B Course Reader|Thorne]] Eq. 4.24.
  - Electron-only $R$, $L$, $P$ cutoffs and the O/X structure: the same as [[Davies 1966 Ionospheric Radio Propagation|Davies]] via [[Appleton-Hartree Equation]], numerically equal to $10^{-11}$ there.
  - Magnetospheric wave bands (chorus, hiss, EMIC) on the whistler and $L$ branches: [[Thorne 1993 AOS 250B Course Reader|Thorne]] and [[Plasma Waves]].
  - AKR relativistic cutoff: [[Strangeway Ch11 The Aurora|Strangeway Ch. 11]].
- **SymPy.**
  - Determinant $= An^4 - Bn^2 + C$.
  - Bellan's discriminant identity, Eq. 6.50.
  - Stix $\tan^2\theta$ form equivalent to the determinant.
  - Electron cutoffs $\omega_{R,L}$.
  - Whistler $v_g$ and the nose at $|\omega_{ce}|/4$.
- **Numerical.**
  - Stix roots satisfy the full $3\times3$ determinant for 2000 random $(S, D, P, \theta)$ (maximum residual $7\times10^{-16}$).
  - Storey angle 19.47° at $\theta = 54.7°$.
  - Frequency table.
  - Lower-hybrid full vs. dense-limit comparison.

## Sources

- [[Bellan 2006 Fundamentals of Plasma Physics]] — Ch. 6 (cold plasma waves in a magnetized plasma)
- [[Thorne 1993 AOS 250B Course Reader]] — magnetospheric wave modes
- [[Strangeway Ch11 The Aurora]] — AKR and the relativistic R-X cutoff
- [[Appleton-Hartree Equation]] — the electron-only, collisional special case
