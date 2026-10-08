---
type: concept
status: draft
updated: 2026-10-08
sources: 1
tags: [radio, HF, propagation, ray-tracing, SuperDARN]
---

# HF Radio Propagation

High-frequency (HF, 3–30 MHz) radio waves refract in the ionosphere due to the plasma refractive index. The geometric optics (ray tracing) approximation is valid for HF because the wavelength (~10–100 m) is much shorter than ionospheric scale lengths (~km). The ionosphere is therefore simultaneously a medium enabling HF propagation (over-the-horizon radar, shortwave communications, [[SuperDARN]]) and a source of disturbances (skip fading, scintillation, Doppler shift) when density structures like [[Polar Cap Patch|patches]] are present.

## Appleton-Hartree Refractive Index

The refractive index $\mu$ for HF in a magnetized plasma is given by the Appleton-Hartree equation (including Earth's magnetic field):

$$\mu^2 = 1 - \frac{2X(1-X)}{2(1-X) - Y^2\sin^2\beta \pm \sqrt{Y^4\sin^4\beta + 4Y^2(1-X)^2\cos^2\beta}}$$

where $X = 8.06\times10^{-5}N/f^2$ (N = electron density in cm$^{-3}$, f = frequency in MHz). *(Corrected 2026-10-08 from $8.06\times10^{-6}$. Check: $N=10^6$ cm$^{-3}$ must give $X=1$ at $f = 8.98$ MHz.)*, Y = f_H/f (gyrofrequency-to-wave ratio), $\beta$ = angle between wave normal and **B**. The ± selects the **ordinary (O) and extraordinary (X) modes** — they propagate at different phase velocities and have different polarizations.

Neglecting **B**: $\mu^2 = 1 - X = 1 - f_p^2/f^2$. Wave reflection occurs at the critical height where $\mu = 0$, i.e., f = f_p (the plasma frequency). This gives the **critical frequency** foF2 and the **Maximum Usable Frequency** (MUF) = foF2 · sec($\theta_i$), where $\theta_i$ is the ray incidence angle at the reflection height.

## Haselgrove Ray Tracing

Ray trajectories in a 3-D ionosphere are governed by the Haselgrove equations (ODEs for position **x** and wave normal direction **u**):

$$\frac{dx_i}{d\tau} = Ju_i - Kv_i, \qquad \frac{du_i}{d\tau} = L\frac{\partial X}{\partial x_i} + \sum_j\!\left(Ku_j + Mv_j\right)\frac{\partial(Yv_j)}{\partial x_i}$$

where J, K, L, M are combinations of X, Y, and the Appleton-Hartree discriminant. The HASEL subroutine ([[Coleman 1992 Ionospheric Ray Tracing]]) implements this via an adaptive Runge-Kutta-Fehlberg integrator with a 9-component state vector: position (3), wave normal (3), phase path P, group path P', and ionospheric Doppler shift Δf. The ionosphere can be represented analytically, as Chapman-layer parameters on a geographic grid, or as height-sample arrays.

## SuperDARN and Backscatter Geometry

[[SuperDARN]] transmits HF pulses at 8–20 MHz that must refract to near-perpendicularity with the geomagnetic field **B** to satisfy the **Bragg condition** for coherent backscatter from field-aligned decametre-scale irregularities. Ray tracing is required to determine which combinations of radar frequency, elevation angle, and ionospheric density structure achieve this geometry.

**Patch-enhanced backscatter:** Dense [[Polar Cap Patch|patches]] (factor 2–10$\times$ background $N_e$) locally refract HF rays more strongly than the surrounding ionosphere. Patches appear as enhanced-backscatter regions in SuperDARN range-time-intensity (RTI) plots; one-to-one spatial correspondence between RTI backscatter and 630-nm airglow patches has been confirmed observationally.

## Signal Disturbances at Polar Latitudes

Patches and the gradient-drift instability irregularities within them cause:
- **Amplitude scintillation** (S4 index): random multipath fading of HF and VHF signals
- **Phase scintillation** ($\sigma_\phi$): rapid phase fluctuations degrading GPS timing accuracy
- **Doppler spread:** spectral broadening of reflected HF signals, impairing ionosonde and OTH radar target discrimination

The 2024 Decadal Survey ([[Decadal Survey 2024]]) identifies ionospheric HF signal propagation disturbance forecasting as an explicit space weather focus area, with a target operational outcome of 1-hour forecasts.

## Related Concepts

- [[Ionospheric Instabilities]] — gradient-drift instability generates the field-aligned irregularities that produce HF backscatter
- [[Polar Cap Patch]] — primary HF propagation disturbers at polar latitudes
- [[SuperDARN]] — global HF coherent-scatter radar network using this physics

## Derivations

- [[Appleton-Hartree Equation]] — derivation, Stix cross-check, O/X cutoffs, $f_xF_2\approx f_oF_2+f_H/2$

## Sources

- [[Coleman 1992 Ionospheric Ray Tracing]]
