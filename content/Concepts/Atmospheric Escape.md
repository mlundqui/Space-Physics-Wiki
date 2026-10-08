---
type: concept
status: draft
updated: 2026-10-07
sources: 4
---

# Atmospheric Escape

Loss of neutral or ionized gas from a planetary atmosphere to space. Governs long-term atmospheric evolution and the balance between planetary outgassing and loss.

## Escape Velocity and Jeans Parameter

The **escape velocity** at the exobase (critical level $r_c$, where mean-free-path equals scale height; ~500 km on Earth):

$$v_{esc} = \left(\frac{2GM}{r_c}\right)^{1/2}$$

The **Jeans parameter** $\lambda_c = m v_{esc}^2 / (2kT)$ measures the ratio of gravitational binding energy to thermal energy. Jeans escape is significant only when $\lambda \lesssim 10$; for $\lambda > 15$ escape is exponentially suppressed.

| Species | $T_{exo}$ (K) | $\lambda_c$ (Earth) | Status |
|---|---|---|---|
| H | ~1000 | ~8 | Readily escapes (Jeans) |
| He | ~1000 | ~32 | Slow Jeans escape |
| O | ~1000 | ~128 | Jeans-trapped; non-thermal only |

## Jeans Thermal Escape (S&N §10.10)

**Jeans escape flux** (S&N Eq 10.84): the flux of exobase particles with upward velocity $> v_{esc}$ in a Maxwellian distribution:

$$\Gamma_{esc} = \frac{n(r_c) v_{mp}}{2\sqrt{\pi}}(1 + \lambda_c)\, e^{-\lambda_c}$$

where $v_{mp} = \sqrt{2kT/m}$ is the most-probable speed. The exponential $e^{-\lambda_c}$ makes the escape flux extremely sensitive to $T_{exo}$: a factor-of-2 increase in $T$ can raise $\Gamma_{esc}$ by many orders of magnitude for heavy species.

For H at Earth ($\lambda \approx 8$): $\Gamma_{esc} \approx 10^8$ cm$^{-2}$ s$^{-1}$ — a slow but geologically significant drain. The solar EUV-heating of the exosphere thus controls the long-term water-loss history of terrestrial planets.

## Exospheric Density — Liouville Theorem

Above the exobase, collisions are rare and particles travel on ballistic Keplerian trajectories. Liouville's theorem: $f(r,v) = f(r_c,v_c)$ (S&N Eq 10.87) — the distribution function is constant along a trajectory. Integrating over the occupied phase-space volume at radius $r$ gives the exospheric density (S&N Eq 10.98):

$$n(r) = n(r_c)\, e^{-E(1-y)}\!\left[1 - (1-y^2)^{1/2}\, e^{-Ey^2/(1+y)}\right]$$

where $E = mv_{ce}^2/(2kT)$ and $y = r_c/r$. This replaces the simple barometric exponential above the exobase; the Liouville density falls off more slowly because the escaping tail of the distribution thins the exosphere preferentially.

## Hydrodynamic Escape

Bulk sonic-to-supersonic outflow driven by intense EUV heating when $\lambda \lesssim 1$–2. Treated as a fluid Parker-type transonic solution; can carry heavier species ("blow-off"). Likely dominated early-Earth H escape during the Hadean. Not active at present-day Earth but important for close-in exoplanets and early solar system conditions.

## Non-Thermal Escape Mechanisms (S&N §10.10–10.11)

### Photochemical Escape (Dissociative Recombination)

$$\text{O}_2^+ + e \rightarrow \text{O}^* + \text{O}^* \quad (v \sim 5\text{–}7 \text{ km/s})$$

The exothermic dissociation imparts ~5 km/s to each O atom — exceeding the escape velocity at Mars (~5 km/s) but below Earth's 11 km/s. Photochemical escape is the **dominant O escape mechanism at Mars** and dominates at Venus during solar maximum. Monte Carlo calculations track superthermal O atoms and compute the fraction reaching escape speed against collisional energy loss.

### Charge Exchange

$$\text{H}^+_{hot} + \text{H} \rightarrow \text{H}^+ + \text{H}_{hot} \qquad \text{(S\&N Eq 10.85)}$$
$$\text{H}^+_{hot} + \text{O} \rightarrow \text{O}^+ + \text{H}_{hot} \qquad \text{(Eq 10.86)}$$

Ring-current H$^+$ (~keV) charge-exchanges with exospheric neutrals, producing superthermal H atoms that travel ballistically and partially escape. Contributes to Earth's **hydrogen corona** and the IMAGE ENA halo.

### Ion Sputtering

Precipitating solar wind ions (at Mars, where there is no global magnetic field) undergo elastic scattering with atmospheric atoms, producing collision cascades. A fraction of recoil neutrals escapes. Ion sputtering rates at Mars: ~$10^{23}$–$10^{24}$ O/s during major solar events.

## Hot Atom Coronae

Superthermal O produced by dissociative recombination and charge exchange populates a **hot oxygen corona** extending well above the exobase — detected at Venus by Pioneer Venus UV spectrometer (density ~$10^4$ cm$^{-3}$ at 200 km above exobase). Earth and Mars also have hot-O coronae; their density and vertical extent depend on solar EUV flux and storm activity.

## Polar Wind (Ionized Escape)

H$^+$ and O$^+$ flow supersonically outward on open polar field lines — the [[Polar Wind]]. Not strictly thermal escape but governed by similar physics (ambipolar electric field plays the role of temperature pressure). H$^+$ escape rates ~$3\times10^8$ cm$^{-2}$ s$^{-1}$ (quiet); O$^+$ escape rates reach ~$10^{25}$ ions/s during storm main phase (DE-1 statistics in S&N §12.17). This ionized outflow feeds the magnetosphere and constitutes an ongoing depletion of the ionospheric inventory.

## Auroral Ion Outflow (Wave-Driven)

Energetic O⁺ outflow from the auroral zone is largely wave-driven, by transverse ion heating that forms **ion conics** ([[Strangeway Ch11 The Aurora]]).
- Dispersive [[Alfvén Waves]] contain **15–34%** of energetic ion outflow at FAST altitudes (40–50% near the cusp and premidnight), rising with activity. The total is about $2.5\times10^{24}$ s⁻¹ at FAST altitude near solar minimum ([[Chaston 2007 DAW Auroral Acceleration Fraction]]).
- Broadband (Alfvénic) aurora supplies the most soft (<1 keV) electron energy flux, which heats the F region. It is therefore the likely main driver of outflow in active times ([[Newell 2009 Global Precipitation Budget]]).
- The dayside boundary layers dominate precipitating *number* flux and ion conics.

See [[Auroral Acceleration]].

## Key Parameters (Earth)

| Species | $T_{exo}$ (K) | $\lambda_c$ | Dominant escape path |
|---|---|---|---|
| H | ~1000 | ~8 | Jeans + charge exchange |
| He | ~1000 | ~32 | Jeans (slow) |
| O | ~1000 | ~128 | Photochemical; ion polar wind |

## Related Concepts

- [[Polar Wind]] — ionized escape on polar open field lines; related by same ambipolar physics
- [[Ionospheric Energetics]] — $T_e$ sets the Jeans parameter $\lambda$; EUV heating drives exospheric temperatures
- [[Equatorial Ionosphere]] — O$_2^+$ produced in F region is the precursor for photochemical O escape

## Sources

- [[Schunk Nagy 2009 Ionospheres]] (§10.10: escape velocity, Jeans flux Eq 10.84, Liouville exospheric density Eqs 10.87–10.98; §10.11: hot O corona, Monte Carlo methods; Ch. 2 §2.4–2.6: comparative planetary escape)
- AOS 205B course materials
- [[Chaston 2007 DAW Auroral Acceleration Fraction]]
- [[Newell 2009 Global Precipitation Budget]]
- [[Strangeway Ch11 The Aurora]]
