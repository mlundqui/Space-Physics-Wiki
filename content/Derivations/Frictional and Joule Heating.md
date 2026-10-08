---
type: derivation
status: draft
updated: 2026-10-07
sources: 3
tags: [derivations, ionosphere, joule-heating, frictional-heating, poynting-flux, thermosphere]
prerequisites: "[[Pedersen and Hall Conductivity]]; Poynting's theorem"
next: "Part II continues in [[Derivations Index]]"
---

# Frictional and Joule Heating

**Part II (ionosphere), page 5** of the [[Derivations Index]] · Previous: [[Pedersen and Hall Conductivity]] · Concept pages: [[Ion Frictional Heating]], [[Joule Heating]]

## Where we're going

At high latitude, magnetospheric electric fields drive ions through the neutral gas at up to kilometers per second. The ions rub against the neutrals, and that friction does two things:

1. It **heats the ions**, by an amount set only by the speed difference and the neutral mass. The heating is fast, so $T_i$ is almost always in steady state.
2. It **heats the neutral gas** at the rate $\sigma_P|\mathbf{E}'|^2$, which is **Joule heating**. This is the largest single energy input to the high-latitude thermosphere during storms, and it's what drives [[Traveling Atmospheric Disturbances|TADs]] and composition changes.

Then Poynting's theorem tells us where the energy comes from, and why a neutral wind can make the ionosphere a *generator* rather than a load. Following AOS 205B Lecture 8.1 (course notes), checked against [[Schunk Nagy 2009 Ionospheres|Schunk & Nagy]] and existing wiki sources.

---

## 1. Ion temperature from friction

The collisional energy exchange between Maxwellian ions $i$ and neutrals $n$ (the 5-moment collision term; S&N Ch. 4–5) is

$$\frac{\delta E_i}{\delta t} = \frac{n_im_i\nu_{in}}{m_i+m_n}\Big[3k_B(T_n - T_i) + m_n|\mathbf{u}_i - \mathbf{u}_n|^2\Big].$$

There are two pieces. **Thermal relaxation** pulls $T_i$ toward $T_n$. **Frictional heating** is proportional to the square of the relative drift: the ions are being dragged through a gas, and they turn some of that drag into random motion.

Ions have almost no heat capacity compared with the neutrals, and their collision time is short (about 1 s in the F region; [[Plasma Diffusion Along B]] §4). So they reach steady state almost immediately. Set $\delta E_i/\delta t = 0$:

$$\boxed{T_i = T_n + \frac{m_n}{3k_B}|\mathbf{u}_i - \mathbf{u}_n|^2}$$

This is S&N Eq. 5.36. The **neutral** mass sets the heating, not the ion mass, because the ion is bouncing off neutrals.

In the F region, $\kappa_i\gg1$, so ions $\mathbf{E}\times\mathbf{B}$ drift and $|\mathbf{u}_i - \mathbf{u}_n|\approx E'/B$, with $\mathbf{E}' = \mathbf{E} + \mathbf{u}_n\times\mathbf{B}$:

| $E'$ (with $B = 5\times10^{-5}$ T) | $|\mathbf{u}_i-\mathbf{u}_n|$ | $\Delta T_i$ (O, $m_n = 16$ u) |
|---|---|---|
| 25 mV/m | 0.5 km/s | about 160 K |
| 50 mV/m | 1 km/s | about 640 K |
| 100 mV/m | 2 km/s | about 2600 K |

**Why this matters for patches and the TOI.** The rate of O$^+$ + N$_2$ → NO$^+$ + N depends on the *effective* reaction temperature

$$T_{\text{eff}} = \frac{m_rT_i + m_iT_n}{m_i+m_r} + \frac{m_im_r|\mathbf{u}_i-\mathbf{u}_n|^2}{3k_B(m_i+m_r)},$$

which comes from the mean relative kinetic energy of the reacting pair. For O$^+$ + N$_2$ at 1 km/s and $T_n = 1000$ K, $T_i\approx1640$ K and $T_{\text{eff}}\approx1820$ K. That's enough to speed up O$^+$ loss sharply. Fast flow channels therefore *erode* the plasma they carry. See [[Ion Frictional Heating]] and [[Tongue of Ionization]].

---

## 2. Where the energy goes: neutral heating = Joule heating

The neutrals feel the mirror-image exchange:

$$\frac{\delta E_n}{\delta t} = \frac{n_nm_n\nu_{ni}}{m_n+m_i}\Big[3k_B(T_i - T_n) + m_i|\mathbf{u}_i - \mathbf{u}_n|^2\Big].$$

Substitute the steady-state $T_i - T_n = m_n|\Delta\mathbf{u}|^2/3k_B$. The bracket becomes $(m_n + m_i)|\Delta\mathbf{u}|^2$, and the mass factor cancels:

$$\frac{\delta E_n}{\delta t} = n_nm_n\nu_{ni}|\Delta\mathbf{u}|^2 = n_im_i\nu_{in}|\mathbf{u}_i - \mathbf{u}_n|^2,$$

using momentum symmetry, $n_nm_n\nu_{ni} = n_im_i\nu_{in}$. **All the frictional work ends up in the neutrals.** The ions are just a conduit. Summed over ion species:

$$\frac{\delta E_n}{\delta t} = \sum_in_im_i\nu_{in}|\mathbf{u}_i - \mathbf{u}_n|^2\qquad\text{(frictional heating rate).}$$

**Now bring in the mobility tensor** from [[Pedersen and Hall Conductivity]] §2. With $\mathbf{E}'\perp\mathbf{B}$, $\mathbf{u}_i - \mathbf{u}_n = \boldsymbol\mu_i\cdot\mathbf{E}'$, and since the tensor is a rotation times a scale,

$$|\mathbf{u}_i-\mathbf{u}_n|^2 = (\mu_P^2+\mu_H^2)|\mathbf{E}'|^2 = \frac{q^2}{m_i^2}\frac{1}{\nu_{in}^2+\Omega_i^2}|\mathbf{E}'|^2.$$

Therefore

$$n_im_i\nu_{in}|\Delta\mathbf{u}|^2 = n_iq\cdot\frac{q}{m_i}\frac{\nu_{in}}{\nu_{in}^2+\Omega_i^2}|\mathbf{E}'|^2,$$

and that prefactor is exactly the ion Pedersen conductivity. When electron–neutral collisions are negligible (electron Pedersen term $\approx0$, true above about 90 km):

$$\boxed{\frac{\delta E_n}{\delta t} = \sigma_P|\mathbf{E}'|^2 = \sigma_P|\mathbf{E} + \mathbf{u}_n\times\mathbf{B}|^2}$$

That's the **ionospheric Joule heating** equation. Two things to notice:

- **Only $\sigma_P$ appears.** Hall current flows perpendicular to $\mathbf{E}'$, so it does no work. (Formally, $(\mathbf{E}'\times\hat{\mathbf b})\cdot\mathbf{E}' = 0$.)
- **It's $\mathbf{E}'$, the field in the neutral frame, not $\mathbf{E}$.** A neutral wind that co-moves with the plasma ($\mathbf{u}_n = \mathbf{E}\times\mathbf{B}/B^2$) gives $\mathbf{E}' = 0$ and **no heating**, however big $\mathbf{E}$ is. After hours of strong convection, ion drag spins up the neutrals and Joule heating drops. This is the "flywheel" effect.

Height-integrated, $Q_J = \Sigma_P|\mathbf{E}'|^2$ in W m$^{-2}$. For $\Sigma_P = 10$ S and $E' = 50$ mV/m, that's 25 mW m$^{-2}$, a moderate-to-active level.

---

## 3. Poynting's theorem: where the energy comes from

Dot Faraday's law with $\mathbf{B}/\mu_0$ and Ampère's law with $\mathbf{E}/\mu_0$, subtract, and use $\nabla\cdot(\mathbf{E}\times\mathbf{B}) = \mathbf{B}\cdot\nabla\times\mathbf{E} - \mathbf{E}\cdot\nabla\times\mathbf{B}$:

$$\frac{\partial}{\partial t}\left(\frac{\varepsilon_0E^2}{2} + \frac{B^2}{2\mu_0}\right) + \nabla\cdot\mathbf{S} = -\mathbf{J}\cdot\mathbf{E},\qquad\mathbf{S} = \frac{\mathbf{E}\times\mathbf{B}}{\mu_0}.$$

This is exact, with no approximations. $\mathbf{J}\cdot\mathbf{E} > 0$ means a **load** (field energy is removed, as in a resistor). $\mathbf{J}\cdot\mathbf{E} < 0$ means a **generator** (field energy is created, as in a battery).

**Circuit analogy** (Lecture 8.1). In a battery–resistor circuit, $\mathbf{S}$ flows through the space *between* the wires, from battery to resistor. The magnetosphere–ionosphere Region-1 system has the same shape:

- **Generator:** the magnetopause and boundary layer ($\mathbf{J}\cdot\mathbf{E} < 0$), driven by the solar wind.
- **Transmission:** field-aligned currents ([[Field-Aligned Currents]]); Poynting flux flows down the field lines.
- **Load:** the ionosphere ($\mathbf{J}\cdot\mathbf{E} > 0$).

**Only the perturbation field carries energy down.** Split $\mathbf{B} = \mathbf{B}_0 + \delta\mathbf{B}$, where $\nabla\times\mathbf{B}_0 = 0$ (the geomagnetic field) and $\nabla\times\delta\mathbf{B} = \mu_0\mathbf{J}$. For an electrostatic $\mathbf{E}$ ($\nabla\times\mathbf{E} = 0$), both $\mathbf{E}\times\mathbf{B}_0$ terms drop out of $\nabla\cdot\mathbf{S}$. They also have no component along $\mathbf{B}_0$. So the energy-carrying Poynting flux is

$$\mathbf{S}' = \frac{\mathbf{E}\times\delta\mathbf{B}}{\mu_0},\qquad S'_\parallel = \frac{(\mathbf{E}\times\delta\mathbf{B})\cdot\hat{\mathbf b}}{\mu_0}.$$

This is what DMSP and SuperDARN-based Poynting-flux estimates compute ([[Perry 2021 SuperDARN Poynting Flux]], [[Thayer Semeter 2004 Energy Flux]]).

### Splitting the load: heat vs. wind

In the Earth frame, write $\mathbf{E} = \mathbf{E}' - \mathbf{u}_n\times\mathbf{B}$:

$$\boxed{\mathbf{J}\cdot\mathbf{E} = \underbrace{\mathbf{J}\cdot\mathbf{E}'}_{\sigma_P|\mathbf{E}'|^2\ \text{(heat)}} + \underbrace{\mathbf{u}_n\cdot(\mathbf{J}\times\mathbf{B})}_{\text{work on the neutral wind}}}$$

- The first term is always ≥ 0. Electromagnetic energy becomes **heat**, which raises $T_n$, causes upwelling and changes composition.
- The second term can have **either sign**.
  - $\mathbf{u}_n\cdot(\mathbf{J}\times\mathbf{B}) > 0$: the ion-drag force speeds up the wind, so electromagnetic energy becomes neutral **kinetic energy**.
  - $\mathbf{u}_n\cdot(\mathbf{J}\times\mathbf{B}) < 0$: the wind does work against $\mathbf{J}\times\mathbf{B}$, generating electromagnetic energy. That's the **neutral-wind dynamo** ([[Ionospheric Dynamo]]).

Globally, about 94% of the incoming Poynting flux goes to Joule heat and about 6% to neutral kinetic energy (Lu et al. 1995, as summarized on [[Joule Heating]]). Locally the split can be very different.

---

## What we assumed, and where it breaks

- **Maxwellian, isotropic ions.** For $E'\gtrsim40$ mV/m, the F-region ion distribution becomes anisotropic and even toroidal, with $T_{i\perp}\neq T_{i\parallel}$. S&N §5.13 covers ion stress, and §11.4 and Ch. 12 give the 40 mV m$^{-1}$ threshold, where the ion drift exceeds the neutral thermal speed. See also [[Ion Frictional Heating]]. ISR $T_i$ then depends on the look angle ([[Incoherent Scatter Spectrum]]).
- **Electron Pedersen term neglected.** Fine above about 90 km. Below that, include $\nu_{en}$.
- **Mean fields only.** Sub-grid variability of $\mathbf{E}$ adds heating, $\langle\sigma_P E'^2\rangle > \sigma_P\langle E'\rangle^2$. This is the well-known underestimate in global models.
- **Electron heating** by Farley–Buneman turbulence in strong-field E regions is a separate channel that is not captured here.

---

## Verification

- **Sources agree.**
  - Energy-exchange terms, $T_i$ result, neutral heating = $\sigma_P|\mathbf{E}'|^2$, Poynting's theorem, the $\mathbf{S}'$ decomposition, and the $\mathbf{J}\cdot\mathbf{E}$ split: AOS 205B Lecture 8.1 (course notes).
  - [[Schunk Nagy 2009 Ionospheres|S&N]] Eq. 5.36 ($T_i = T_n + m_n|\Delta\mathbf{u}|^2/3k$) and §5.13 (anisotropy).
  - The existing [[Joule Heating]] page (Thayer & Semeter 2004 framework) gives the same decomposition.
  - $T_{\text{eff}}$ matches [[Ion Frictional Heating]] and was re-derived here from the mean relative kinetic energy.
- **SymPy.**
  - Steady $T_i$.
  - Neutral heating reduces exactly to $n_nm_n\nu_{ni}|\Delta\mathbf{u}|^2$.
  - $n_im_i\nu_{in}|\boldsymbol\mu\cdot\mathbf{E}'|^2 = \sigma_{P,\text{ion}}|\mathbf{E}'|^2$.
  - $\mathbf{J}\cdot\mathbf{E} = \mathbf{J}\cdot\mathbf{E}' + \mathbf{u}_n\cdot(\mathbf{J}\times\mathbf{B})$ holds for arbitrary vectors.
- **Numerical.** $\Delta T_i$ table, $T_{\text{eff}}$ example and the Joule example were computed.

## Sources

- AOS 205B Lecture 8.1, *Joule Heating* (`Atlas/Courses/AOS 205B/Lecture8_1_JouleHeating.pdf`) — course notes, primary derivation
- [[Schunk Nagy 2009 Ionospheres]] — Eq. 5.36 (frictional ion temperature), §5.13 (anisotropy)
- [[Thayer Semeter 2004 Energy Flux]] — Poynting-flux framework for M–I energy transfer (via [[Joule Heating]])
- [[Perry 2021 SuperDARN Poynting Flux]] — observational Poynting-flux estimation
