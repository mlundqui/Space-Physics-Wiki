---
type: concept
status: draft
updated: 2026-05-20
sources: 2
---

# Equatorial Ionosphere

The ionosphere within ~±20° magnetic latitude of the dip equator, where the near-horizontal magnetic field geometry creates unique electrodynamic phenomena not seen at other latitudes.

## Equatorial Electrojet (EEJ)

An intense eastward current in the E region (~100–115 km) along the magnetic dip equator. Driven by the tidal dynamo wind-driven $\mathbf{E}\times\mathbf{B}$ drift combined with the Cowling conductivity enhancement.

**Cowling conductivity**: when the horizontal magnetic field prevents vertical current flow ($\sigma_0$ in the vertical direction is blocked by the horizontal $\mathbf{B}$), the Hall current from the Pedersen flow sets up a polarization electric field. This induces an additional Pedersen current aligned eastward, effectively enhancing the total eastward conductivity:

$$\sigma_C = \sigma_P + \frac{\sigma_H^2}{\sigma_P} \approx \frac{\sigma_H^2}{\sigma_P} \quad \text{(dominant term)}$$

The EEJ current is ~100–300 mA/m (integrated), driving 100–200 nT magnetic perturbations at the surface. The EEJ reverses to a westward counter-electrojet (CEJ) during disturbed times or with some tidal forcings.

## Equatorial Ionization Anomaly (EIA / Appleton Anomaly)

The fountain effect: dayside $\mathbf{E}\times\mathbf{B}$ upward drift at the equator (driven by eastward zonal electric field $\mathbf{E}_y$ and northward $\mathbf{B}$) lifts plasma to the topside F region, where it diffuses down both legs of the field lines under gravity and ambipolar diffusion, depositing enhanced NmF2 at ~±15° magnetic latitude.

- Plasma "crests" in NmF2 flanking the equatorial trough
- Strongest during solar maximum and in the afternoon sector (~14–18 LT)
- The pre-reversal enhancement (PRE) of the zonal electric field (see below) strengthens the EIA crests

## Pre-Reversal Enhancement (PRE)

Near sunset, the F-region zonal electric field briefly strengthens (eastward spike) before reversing to westward for the nighttime. Driven by E-region conductance gradient at the terminator: the day-night conductance asymmetry creates a wind-driven dynamo that concentrates eastward flow in the F region.

Consequence: upward $\mathbf{E}\times\mathbf{B}$ drift at the dip equator after sunset drives Rayleigh-Taylor instability growth (see [[Ionospheric Instabilities]]) and initiates equatorial plasma bubbles.

## Equatorial Plasma Bubbles (EPBs) / Equatorial Spread-F (ESF)

After sunset, the bottomside F-layer develops an inverted density gradient (depleted D/E regions below dense F-region plasma). The Rayleigh-Taylor instability drives depleted plasma "bubbles" that rise through the F region, creating radar-detectable spread-F and GPS scintillation.

- Strongest activity: September equinox in the American sector; March equinox in the Asian sector
- PRE amplitude is the primary trigger: large PRE → high probability of ESF
- Bubble plumes can reach the topside F layer (~1000 km altitude)

## Rayleigh-Taylor Instability (§11.12)

The gravitational Rayleigh-Taylor (R-T) instability drives equatorial plasma bubbles and spread-F when the bottomside F layer has an inverted density gradient (dense plasma above depleted E/D region). Pre-reversal enhancement at dusk raises the F layer to high altitude (~400–500 km), sharpening the gradient and maximizing growth rates.

**Setup:** Consider the bottomside F layer with vertical density gradient $\partial n_0/\partial z$ (positive = increasing upward = stable; negative for bottomside). In the neutral reference frame, the gravitational drift of ions is:

$$u_{i0} = \frac{g}{\omega_{ci}} \hat{e}_y \qquad (\text{westward; Eq 11.79})$$

This drift carries ions but not electrons, setting up a charge separation that is the seed for the instability.

**Linearized transport** (Eqs 11.80–11.86): perturbing the ion continuity and momentum equations with $n_1 = n_0 e^{ik_y y}$ (horizontal wavenumber $K = k_y$) and solving for the electric field and velocity perturbations yields the dispersion relation (S&N Eq 11.87):

$$\omega = \frac{1}{2} K u_{i0} \pm \left[\frac{1}{4}K^2 u_{i0}^2 - \frac{g}{n_0}\frac{\partial n_0}{\partial z}\right]^{1/2}$$

**Instability condition:** When $\frac{g}{n_0}\frac{\partial n_0}{\partial z} < 0$ (i.e., $\partial n_0/\partial z < 0$; density decreasing upward = bottomside), the discriminant is imaginary and the mode grows. Growth rate $\gamma \approx \sqrt{-g(\partial n_0/\partial z)/n_0}$.

**Physical picture:** Depleted plasma pushed upward by a perturbation is lighter than surrounding denser plasma — gravity continues pushing it upward while denser plasma falls. The $E\times B$ drift of the bubbles feeds back positively. The process non-linearly evolves to magnetic-field-aligned bubble plumes reaching the topside.

**Observational consequence:** Radar spread-F on equatorial ISRs, GPS scintillation on transionospheric links, airglow depletions visible in 630 nm all-sky cameras.

## F$_3$ Layer (§11.14)

When the $E\times B$ upward drift at the magnetic equator is very strong (dusk, high solar activity), plasma that constitutes the F$_2$ layer lifts above ~500 km, and a new F$_2$ layer forms below by continued O$^+$ photoionization. The original lifted layer persists as the **F$_3$ layer** at higher altitude — an anomalous secondary maximum.

- Observed at both geographic hemispheres; most pronounced at dusk in American/Asian sectors during solar maximum
- F$_3$ density can exceed $10^6$ cm$^{-3}$; it eventually diffuses down both field-line legs as the $E\times B$ reverses at night

**He$^+$ layer:** At solar maximum and high altitude (~750–1200 km near the magnetic equator), helium ions can comprise up to ~50% of the ion density, forming a distinct layer above the O$^+$ F$_2$ peak. This arises because He$^+$ has a lighter mass and longer scale height; the He$^+$ abundance is thus an indicator of the extent of ionospheric ion energization.

## Tides and Nonmigrating Tides (§11.15)

Semi-diurnal (12 hr) tidal modes dominate the lower thermosphere wind field, driven by both solar heating (migrating, wavenumber-2) and tropospheric latent-heat release (nonmigrating modes). The **wavenumber-4 longitudinal structure** in TEC (~20% peak-to-trough variation) is a nonmigrating tide signature — four longitude sectors of enhanced density wrap around the globe at the magnetic equator. This structure is reproduced by global models when tidal forcing from the Whole Atmosphere Community Climate Model (WACCM) is included.

Tidal winds at E-region altitudes (~110 km) drive the ionospheric dynamo (ion-drag, $\mathbf{u}_n \times \mathbf{B}$ electromotive force), modulating the equatorial electric field and thus the vertical $E\times B$ drift with tidal period. The semi-diurnal tide can modulate the vertical drift by ±5–10 m/s, shifting the F$_2$ peak height and the EIA crest latitude.

**Gravity wave seed perturbations:** Convective sources in the troposphere and mesosphere generate small-amplitude gravity waves that propagate upward and grow in amplitude. At F-region altitudes, these waves can seed R-T instability where the background gradient is already unstable. The correlation of plasma bubble activity with tropical deep convection is attributed to this seeding mechanism.

## Fountain Effect Connection to Polar Cap

Plasma lifted by the EIA eventually supplies the sub-auroral and mid-latitude ionosphere. The [[Tongue of Ionization]] that feeds [[Polar Cap Patch|polar cap patches]] during active times traces partly back to mid-latitude density enhancements, which themselves owe to the fountain effect + [[Storm-Enhanced Density]].

## Related Concepts

- [[Ionospheric Conductivity]] — Cowling conductivity drives the EEJ
- [[Ionospheric Instabilities]] — Rayleigh-Taylor and Farley-Buneman active at equator
- [[Ambipolar Diffusion]] — diffusion along slanted field lines carries plasma away from equator
- [[Ionospheric Storms]] — PPEF superfountain; storm-time R-T suppression or enhancement
- [[Ionosphere]] — parent concept

## Storm-Time PPEF Superfountain

During extreme geomagnetic storms, **prompt penetrating electric fields (PPEFs)** reach the equatorial ionosphere before the magnetospheric shielding system can respond (~tens of minutes). [[Tsurutani 2013 PPEF Ionosphere Comment]] documents the 30 October 2003 Halloween superstorm: a PPEF of ~4 mV/m drove an anomalous upward $E\times B$ drift at the dip equator, intensifying and poleward-displacing EIA crests from ±10° MLAT to ±22–30° MLAT with TEC reaching ~210–270 TECu (CHAMP data). SAMI2 model simulations reproduce the displacement only with the PPEF included. The superfountain effect is thus the equatorial counterpart of sub-auroral [[Lifting]]: both suppress recombination by raising plasma to altitudes where [N$_2$] and [O$_2$] are depleted. Enhanced mid-latitude TEC from PPEF superfountain events can subsequently be advected poleward into the polar cap via the [[Storm-Enhanced Density|SED]] → [[Tongue of Ionization|TOI]] pathway during the same storm.

## Sources

- [[Schunk Nagy 2009 Ionospheres]] (§11.12: R-T instability derivation Eqs 11.79–11.87; §11.14: F$_3$ layer, He$^+$ layer; §11.15: tides, nonmigrating tides, gravity wave seeding)
- [[Tsurutani 2013 PPEF Ionosphere Comment]]
- AOS 205B course materials
