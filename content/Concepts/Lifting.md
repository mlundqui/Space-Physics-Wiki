---
type: concept
status: draft
updated: 2026-05-19
sources: 3
tags: [ionosphere, transport, f-region]
---

# Lifting

Vertical raising of [[F-Layer|F-region]] plasma to higher altitudes — a central mechanism in polar-cap and storm-time ionospheric dynamics. Because O$^+$ loss is dominated by the atom-ion interchange reactions:

$$\text{O}^+ + \text{N}_2 \rightarrow \text{NO}^+ + \text{N}, \qquad \text{O}^+ + \text{O}_2 \rightarrow \text{O}_2^+ + \text{O}$$

the loss rate $L = k_1[\text{O}^+][\text{N}_2] + k_2[\text{O}^+][\text{O}_2]$ falls exponentially with altitude as molecular neutral densities decrease. Lifting plasma out of the molecular-rich lower thermosphere therefore **slows recombination** and allows density structures to persist far longer than they otherwise would.

## Mechanisms

### 1. Vertical component of $\mathbf{E}\times\mathbf{B}$ drift

The dominant storm-time lifting mechanism. The geomagnetic field in a dipole geometry is tilted such that any horizontal motion perpendicular to $\mathbf{B}$ necessarily has a vertical component. A poleward (nominally horizontal) $\mathbf{E}\times\mathbf{B}$ drift must remain perpendicular to $\mathbf{B}$, giving:

$$u_z = u_\perp \sin\theta_\text{dip}$$

where $\theta_\text{dip}$ is the local magnetic dip angle. At mid-to-high latitudes ($\theta_\text{dip} \sim 70°–80°$), poleward $\mathbf{E}\times\mathbf{B}$ speeds of ~500 m/s produce upward drift rates of ~470–490 m/s. Over the storm main phase, this can elevate $h_{mF2}$ by hundreds of km, as observed in PFISR data (Zou et al. 2013).

This mechanism is amplified during geomagnetic storms by:
- **Prompt penetrating electric fields (PPEFs):** Enhanced magnetospheric convection electric fields that penetrate to sub-auroral latitudes within minutes of southward IMF onset, before the magnetospheric shielding layer can respond.
- **Disturbance dynamo:** Storm-driven thermospheric winds that create a secondary ionospheric dynamo electric field, sustained for hours on the storm main and early recovery phases.

### 2. Neutral wind parallel projection along $\mathbf{B}$

Neutral winds with a component along $\mathbf{B}$ drag ions up or down field lines via ion-neutral friction. The parallel ion momentum equation (neglecting inertia) gives an equilibrium parallel velocity with contributions from gravity, the ambipolar electric field, and the projected neutral wind:

$$u_\parallel \sim u_n\cos\theta_\mathbf{B}$$

where $\theta_\mathbf{B}$ is the angle between the neutral wind and $\mathbf{B}$. Poleward meridional winds project upward along $\mathbf{B}$ at high latitudes (where $\mathbf{B}$ is nearly vertical), lifting the ionosphere. Equatorward winds push it down.

### 3. Ambipolar diffusion and scale height

In the absence of external forcing, the F-region plasma settles to the plasma scale height $H_p = k_B(T_e + T_i)/(m_i g)$. Elevated electron or ion temperatures (from precipitation, frictional heating, or enhanced EUV) increase $H_p$ and raise the centroid of the density profile. This is a slower process than direct $\mathbf{E}\times\mathbf{B}$ lifting.

## Temperature sensitivity of loss rates

Both $k_1$ and $k_2$ depend on the effective temperature $T_{eff}$, which accounts for frictional heating when ions drift relative to neutrals at velocity $|\mathbf{u}_i - \mathbf{u}_n|$:

$$k_1 = \begin{cases} 1.2\times10^{-12}(T_{eff}/300)^{-0.45} & T_{eff} \leq 1000\text{ K} \\ 7.0\times10^{-13}(T_{eff}/1000)^{2.12} & T_{eff} > 1000\text{ K} \end{cases}$$

$$T_{eff} \approx T_n + \frac{1}{3k_B}\left(m_b + \frac{m_i(m_r-m_b)}{m_i+m_r}\right)|\mathbf{u}_i - \mathbf{u}_n|^2$$

Large $\mathbf{E}\times\mathbf{B}$ drifts relative to neutrals therefore accelerate loss even while the vertical drift component is lifting the plasma. This coupling creates the "cutting" mechanism for [[Polar Cap Patch|patches]]: fast convection channels simultaneously lift plasma (via $u_z$) and cut TOIs (via $T_{eff}$-accelerated $L$).

## Lifting failure: thermospheric expansion

Joule heating during major storms expands the neutral thermosphere outward, pushing N$_2$ and O$_2$ to higher altitudes relative to the O$^+$ layer. This is *de*-lifting in effect — it brings molecular neutrals up to where the ions are, increasing $L$ and offsetting or overwhelming the positive vertical drift effect. The May 2024 superstorm ([[Themens 2024 May Storm]]) is the canonical counter-example: massive N$_2$ upwelling through Joule heating (O/N$_2$ depleted 50%; $T_n$ increased 50%) annihilated high-latitude F-region plasma at ESR and PFISR through accelerated recombination, suppressing [[Polar Cap Patch|polar cap patches]] entirely on Day 2 of the storm despite comparable geomagnetic forcing. F-region recovery to pre-storm conditions required ~3 days.

The same storm shows that positive lifting can be extreme when it does operate: during the initial storm phase on Day 1, midlatitude $h_{mF2}$ at Eglin AFB rose by ~300 km in ~1 hr, ultimately reaching 630 km — well above the quiet-time F-region peak of ~300 km — with LSTID-like oscillations of 150–300 km amplitude and ~2 hr period superimposed. SED-origin patches at ESR (78°N) also had peak heights exceeding 475 km, the radar's operational ceiling. This is the observational upper bound on lifting magnitudes in realistic storm conditions.

## Connection to the L/D/LD classification

The [[Lundquist Varney 2026]] L/D/LD event taxonomy is a separation of polar cap plasma by Lagrangian altitude history:
- **D events (Dense, not lifted):** Transported plasma at normal altitudes. Loss is occurring at normal rates.
- **L events (Lifted, not dense):** O$^+$ raised to high altitude at some earlier point; density has partially decayed away during the transport, but the elevated $h_{mF2}$ signature remains.
- **LD events (Lifted and dense):** Rarest; plasma that has maintained both anomalous altitude and anomalous density throughout the polar cap transit. Plausible [[Storm-Enhanced Density|SED]] remnants.

The variability of parallel ion fluxes along the 3-D Lagrangian flux-tube trajectories is identified as an open problem for understanding which events become LD vs L.

## Thermospheric origin of the lifting mechanism

The w = w_D + w_L decomposition for thermospheric vertical motion was established by [[Dickinson Geisler 1968 Thermospheric Vertical Motion]]. Vertical motion at a constant-pressure surface $p_0$ consists of:
- **w_D**: driven by horizontal mass divergence — $\int\rho$**c** dz depth-integrated divergence above the surface
- **w_L $\approx \partial h/\partial t$**: the rate at which the pressure surface itself rises or falls

For planetary-scale diurnal motions, $\partial h/\partial t \gg$ **c**·$\nabla h$ so w_L dominates; amplitudes are ~1 m/s at 300 km. Adiabatic heating by w_L is thermodynamically significant (diurnal component ~3000 K/day at 300 km, comparable to solar radiation heating ~1000 K/day). The Thayer & Coleman (2026) ambiguity — whether FPI vertical wind measurements capture w_L or w_D — traces directly to this decomposition. At auroral latitudes where Joule heating drives large, localized horizontal wind divergences, w_D may become significant relative to w_L, complicating the interpretation of FPI data as purely F-region lifting signals.

## Sources

- [[Lundquist Varney 2026]]
- Varney 2026 PatchesChapter
- [[Themens 2024 May Storm]]
- [[Dickinson Geisler 1968 Thermospheric Vertical Motion]]
