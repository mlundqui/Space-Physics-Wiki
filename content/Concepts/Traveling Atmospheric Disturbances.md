---
type: concept
status: draft
updated: 2026-05-20
sources: 2
tags: [thermosphere, neutral-atmosphere, waves, TADs, TIDs]
---

# Traveling Atmospheric Disturbances

Propagating perturbations in thermospheric neutral density, temperature, and wind. TADs are the neutral atmospheric analog of traveling ionospheric disturbances (TIDs); the two are mechanistically coupled — TADs drive TIDs via neutral wind momentum transfer to plasma through ion-neutral collisions.

## Physical nature

TADs are large-scale thermospheric gravity waves launched primarily at high latitudes during geomagnetically active periods. They are not electrodynamic; they are neutral fluid waves in the thermosphere. The restoring force is buoyancy (stratification of the neutral atmosphere), and the propagation speed is near or slightly below the local adiabatic sound speed at F-region altitudes (~500–800 m/s at 300–400 km).

TADs propagate equatorward from their high-latitude sources, and in some cases continue past the equator into the opposite hemisphere. They perturb the neutral density along satellite orbits (CHAMP, GRACE) and the plasma density and drift along ISR beam paths.

## Generation

The dominant source is geomagnetic-storm-time [[Joule Heating]] at high latitudes. Localized, impulsive Joule heating deposits energy rapidly into the thermosphere, expanding the gas and launching a gravity-wave-like pulse. Key finding from [[Pham 2022 TADs]]: the **spatial distribution** of Joule heating matters more than its total power. Mesoscale, localized heating (as occurs in reality and in physics-based coupled models like [[MAGE]]) generates TADs with correct amplitudes and propagation. Spatially broad, smooth empirical Joule heating (Weimer 2005 specification in standalone TIEGCM) generates TADs with incorrect properties.

Additional sources: particle precipitation heating at the cusp (direct soft electron precipitation, Alfvén wave thermospheric heating), substorm current wedge Joule heating, and in principle any impulsive high-latitude heat source.

## Propagation and observation

TADs propagate at acoustic-gravity wave speeds, generally equatorward. Propagation times from the high-latitude generation region to mid-low latitudes are ~1–6 hr, depending on source latitude and wave speed.

Because the satellite intercepts a moving TAD at a specific time and location, the observed density enhancement depends on both when and where the TAD was generated. Correctly simulating a single CHAMP or GRACE density peak requires:
1. Generating the TAD at the correct time and location
2. Propagating it at the correct speed and amplitude
3. Having the TAD arrive at the satellite's position at the correct time

This strict constraint explains why empirical models systematically fail and why physics-based coupled models are necessary.

## Constructive intersection at low latitudes

When TADs generated in opposite (northern and southern) hemispheres simultaneously propagate equatorward toward the equatorial region, they can overlap and interfere constructively, producing density enhancements larger than either TAD alone. This mechanism explains why large density peaks at low latitudes are sometimes observed away from any obvious local energy source. [[Pham 2022 TADs]] traces two specific CHAMP density enhancements to exactly this intersection mechanism.

## Relation to TIDs

Neutral wind perturbations carried by TADs drag plasma along field lines and in the perpendicular direction (via collisions), creating correlated electron density perturbations at F-region altitudes — these are TIDs. Large-scale TIDs (LSTIDs, scale >1000 km, speed ~300–700 m/s) are the ionospheric manifestation of large-scale TADs. The LSTID-like oscillations in $h_{mF2}$ observed at Eglin AFB during the May 2024 storm ([[Themens 2024 May Storm]]) are consistent with TAD-driven plasma displacement (2 hr period, 150–300 km amplitude).

## Observational detection

- **CHAMP/GRACE accelerometers:** Neutral density at ~400 km mapped to a reference altitude; density peaks along the satellite track are the primary TAD observational dataset.
- **ISR hmF2 time series:** LSTID-like oscillations in peak height reveal TAD-driven plasma motion.
- **Ionosondes:** foF2 and hmF2 oscillations; the LSTID-like modulations are visible if the ionosonde is in the TAD path.

## Gravity Wave Theory Foundation (S&N §10.4)

TADs are the large-scale limit of atmospheric gravity waves — buoyancy-driven oscillations in a stratified atmosphere. The fundamental frequency scale is the **Brunt-Väisälä (buoyancy) frequency**:

$$\omega_b^2 = \frac{g^2}{c_s^2}\!\left[\gamma - 1 + \frac{1}{H}\frac{\partial H}{\partial z}\right]$$

where $c_s = \sqrt{\gamma k_B T/m}$ is the acoustic speed and $H = k_B T/(mg)$ is the neutral scale height. In an isothermal atmosphere: $\omega_b^2 = g(\gamma-1)/(c_s^2/\gamma) = g/H_s$ where $H_s = c_s^2/(\gamma g)$ is the scale height. $\omega_b$ is the maximum frequency for vertically propagating gravity waves; acoustic waves propagate above the acoustic cutoff $\omega_a = c_s/(2H)$.

**AGW dispersion relation** (S&N Eq 10.37):

$$\omega^2 = \omega_a^2 + k_\perp^2 c_s^2\frac{\omega^2 - \omega_b^2}{\omega^2 - \omega_a^2}$$

where $k_\perp$ is the horizontal wavenumber. For $\omega_b < \omega < \omega_a$: evanescent (no real vertical $k$); for $\omega < \omega_b$: internal gravity waves (upward propagating, downward phase velocity); for $\omega > \omega_a$: acoustic waves.

**TAD parameters:**
- Period: ~0.5–3 hours (between $2\pi/\omega_a$ and $2\pi/\omega_b$)
- Horizontal wavelength: ~500–3000 km
- Phase speed: ~300–800 m/s equatorward
- Amplitude grows with altitude as $\propto e^{z/2H}$ (density decrease)

**Wind filtering:** Gravity waves are Doppler-shifted by the background wind $\mathbf{U}$. A wave with horizontal phase speed $c$ is absorbed (critical level absorption) where $c = \mathbf{U}\cdot\hat{k}$. This selective filtering by the time-varying background thermospheric wind shapes the spectrum of TADs that reach low latitudes, and can cause a TAD generated equatorward to reflect or be absorbed before reaching its target.

## Ionospheric Manifestation (TIDs)

Large-scale TADs (period > 1 hour, horizontal wavelength > 1000 km) manifest as **Large-Scale TIDs (LSTIDs)** in the ionosphere. The neutral wind perturbation $\delta u_n$ drives a $\mathbf{u}_n \times \mathbf{B}$ electric field that displaces plasma along inclined field lines, moving $h_{mF2}$ up or down. The amplitude of the $N_e$ perturbation depends on the ratio $\delta u_n / \nu_{in}$ (neutral forcing relative to ion-neutral coupling) and the local recombination rate.

## Sources

- [[Pham 2022 TADs]]
- [[Schunk Nagy 2009 Ionospheres]] (§10.4: Brunt-Väisälä frequency, AGW dispersion relation Eq 10.37, wind filtering/critical levels; §11.15: gravity wave seeding of R-T instability, nonmigrating tides)
