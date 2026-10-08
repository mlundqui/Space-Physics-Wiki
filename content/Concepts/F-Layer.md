---
type: concept
status: draft
updated: 2026-10-07
sources: 2
tags: [ionosphere, f-region]
---

# F-Layer

The F region of the [[Ionosphere]] — the altitude range (~150–600 km) containing the daytime electron-density peak. Conventionally subdivided into F1 (a daytime ledge near ~150–200 km) and F2 (the main peak, typically 250–400 km but varying widely with latitude, season, solar cycle, and storm conditions).

## Key Parameters

- **NmF2** — peak electron density at the F2 layer.
- **hmF2** — altitude of the F2 peak.
- **Bottomside / topside scale heights** (H_b, H_t in Epstein-style layer models) — characterize how density falls off below and above the peak.

These parameters are sufficient to describe the F-region profile for many empirical and statistical purposes.

## Chapman Layer Production

Ionization is produced by EUV/X-ray photoionization of O above ~150 km. The **Chapman production function** for a single absorber and monochromatic radiation at solar zenith angle $\chi$ (S&N Eq 9.21):

$$P_c(z,\chi) = I_\infty \eta n(z) \sigma^a \exp\!\left[-H n(z)\sigma^a \sec\chi\right]$$

This peaks at the altitude where the optical depth $\tau = Hn\sigma^a\sec\chi = 1$. At the peak:

$$P_{c,\max} = \frac{I_\infty \eta \cos\chi}{eH}$$

The peak production altitude shifts upward with increasing $\chi$ (sunrise/sunset or high latitude) and downward for shorter wavelengths (deeper penetration). The F1 ledge (~170 km) sits near the production peak of **17–91 nm EUV** photons (200C textbook Ch. 2). X-rays (1–10 nm) instead contribute to E-region production. *(Corrected 2026-10-07: this previously attributed the F1 ledge to "harder X-ray photons.")*

## F2-Layer Chemistry: Competing Production and Loss

**The F2 peak does not arise from photoionization balancing chemical loss.** In pure chemical equilibrium the O$^+$ density *increases* with altitude (below). The peak forms where the chemical loss time $1/\beta$ equals the diffusion time, $\beta(h_mF_2)\approx D/H^2$ ([[Schunk Nagy 2009 Ionospheres|S&N]] §11.4; derivation and numerical check in [[Chapman Layer]] §4–5). *(Corrected 2026-10-07: this sentence previously said the F2 peak forms where production balances chemical loss.)* The dominant loss pathway is the two-step process:

1. **Ion-atom interchange:** $\text{O}^+ + \text{N}_2 \rightarrow \text{NO}^+ + \text{N}$ (rate $k_1$, strongly $T_{eff}$-dependent)
2. **Dissociative recombination:** $\text{NO}^+ + e \rightarrow \text{N} + \text{O}$ (rate $\alpha \approx 4\times10^{-7}(300/T_e)^{0.5}$ cm$^3$ s$^{-1}$)

The effective loss rate for O$^+$ at F-region altitudes is approximately:

$$L \approx \beta n_e, \qquad \beta = k_1[N_2] + k_2[O_2]$$

Because $[N_2]$ and $[O_2]$ fall exponentially with altitude, and faster than the [O] that sets production, the chemical-equilibrium density $P/\beta$ *rises* with height, and $\beta$ decreases rapidly with altitude — this is why **lifting plasma to higher altitudes suppresses recombination** and allows density to build up. This is the central mechanism behind [[Lifting]], [[Storm-Enhanced Density|SED]], and the long lifetimes of [[Polar Cap Patch|polar cap patches]] at high altitude.

## Diffusive Equilibrium in the Topside (§5.5–5.7)

Above the F2 peak, chemical loss becomes negligible and the plasma is governed by [[Ambipolar Diffusion]] along **B**. In the topside F region, the density profile approaches diffusive equilibrium (vertical drift → 0):

$$n(z) \approx n_0 \exp\!\left(-\int \frac{m_i g + \frac{d}{dz} k_B(T_e+T_i)}{k_B(T_e+T_i)}\,dz\right)$$

*(Corrected 2026-10-07: same sign error as on [[Ambipolar Diffusion]]. The temperature-gradient term enters with a plus sign.)*

The effective scale height is the **plasma scale height**:

$$H_p = \frac{k_B(T_e + T_i)}{m_i g}$$

For O$^+$ at $T_e = T_i = 1000$ K: $H_p \approx 110$ km — twice the neutral O scale height because the ambipolar electric field supports the ions against gravity.

## Nighttime Decay and Maintenance

After sunset the photoionization source disappears. F-region O$^+$ decays via the same $k_1[N_2]$ and $k_2[O_2]$ loss reactions, but because the F2 peak is at ~300 km where $[N_2]$ and $[O_2]$ are already small, the decay timescale is long (~hours). The density typically falls by a factor of 3–10 from afternoon maximum to post-midnight minimum under quiet conditions.

**Conjugate photoelectron maintenance:** During polar night, the F region can be sustained at significant density by photoelectrons arriving along field lines from the sunlit conjugate hemisphere. These superthermal electrons ionize O and heat the thermal electrons, maintaining an ionized layer even in total darkness. This is directly relevant to polar cap patch formation during winter months.

## F-Layer Lifting

The F2 peak height $h_{mF2}$ is set by the competition among:
- Downward diffusion (ambipolar)
- Upward $E\times B$ drift
- Neutral wind divergence along field lines
- Ion-neutral drag (from meridional neutral wind $u_n$)

Raising $h_{mF2}$ moves the plasma into a region of lower neutral density, reducing the effective loss coefficient $\beta$ and allowing $N_mF2$ to grow (or persist longer). The [[Lifting]] mechanism is the primary way polar cap plasma attains densities 2–10$\times$ the background.

## Topside vs Bottomside Asymmetry

The topside scale height is set by $H_p$ (plasma scale, ambipolar diffusion); the bottomside scale height is set by the chemistry-transport competition and is typically steeper. In ISR observations, the topside can be fit with an $\alpha$-Chapman form, $n_m\exp[\tfrac12(1-y-e^{-y})]$, and the bottomside is often fit with a different scale height or an Epstein-layer form. *(Corrected 2026-10-07: the sech$^2$ profile was previously attributed to the α-Chapman layer. sech$^2$ is the Epstein-layer shape; the α-Chapman shape is given above, see [[Chapman Layer]] §3.)*

## Sporadic Layers

Thin, dense ionization layers (a few km thick) can form within or below the E region due to metallic ion wind-shear convergence — see [[Sporadic E]]. Occasional F-region thin layers also form from gravity wave breaking or plasma instabilities.

## Related Concepts

- [[Lifting]] — what raises hmF2; suppresses recombination
- [[Ambipolar Diffusion]] — governs topside density profile; sets plasma scale height
- [[Ionospheric Energetics]] — Te and Ti set Hp and diffusion rates
- [[Polar Cap Patch]] — F-region density structures studied via NmF2 and hmF2 anomalies
- [[Tongue of Ionization]] — continuous band of elevated F-region density entering the polar cap
- [[Ionospheric Storms]] — storm-time lifting, SAPS-driven SED, negative phase from O/N$_2$ depletion
- [[Sporadic E]] — thin dense layers in the E region

## Derivations

- [[Chapman Layer]] — production function, α-Chapman layer, β-type chemistry, and the F2-peak condition (verified numerically)

## Sources

- [[Schunk Nagy 2009 Ionospheres]] (Ch. 9 §9.3: Chapman production function Eq 9.21; Ch. 8 Table 8.3: ion-atom interchange rates; Ch. 5 §5.5–5.7: ambipolar diffusion, plasma scale height)
- [[Lundquist Varney 2026]]
