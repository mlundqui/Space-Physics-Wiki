---
type: source
status: draft
updated: 2026-10-07
sources: 0
authors: C.C. Chaston, J.W. Bonnell, C.W. Carlson, J.P. McFadden, R.E. Ergun, R.J. Strangeway
year: 2003
doi: 10.1029/2002JA009420
tags: [alfven-waves, FAST, auroral-acceleration, inertial-alfven-waves, statistics]
---

# Chaston 2003 FAST Small-Scale Alfvén Waves

## Summary

A statistical [[FAST]] study (350–4175 km altitude) of Alfvén waves with transverse scales near the electron skin depth, at 0.2–20 Hz in the spacecraft frame. It is combined with a 1-D inertial-Alfvén-wave simulation (Thompson & Lysak 1996 equations). Findings:
- The waves occur **throughout the auroral oval**. They are most frequent in the **cusp** (10–13 MLT) and most intense at the **premidnight polar-cap boundary** (21–01 MLT).
- Wave Poynting flux correlates with field-aligned electron energy flux.
- **Most electron acceleration happens above FAST, at 1–2 $R_E$ altitude**, where the wave meets the $v_A$ peak. The most energetic electrons originate about 2–3 $R_E$ up.

## Key claims

- **Occurrence and intensity:**
  - Cusp events appear on nearly every cusp pass.
  - Premidnight events correlate with AE and are strongest in substorm expansion (Polar UVI).
  - Electron energy flux in polar-cap-boundary events can exceed 100 mW m⁻², enough for the brightest aurora.
- **Characteristic energies:** median up to **about 4 keV premidnight** and **about 100 eV in the cusp**. Interpreted as Landau resonance, the cusp energies imply a peak $v_A \geq 6\times10^3$ km/s above the dayside oval, at altitudes at least 3000 km.
- **Electron and wave energy flux:**
  - At FAST, downgoing electron energy flux *exceeds* wave Poynting flux, because the wave has already deposited its energy above.
  - Upgoing electron and upgoing wave energy fluxes are well correlated and comparable, consistent with Landau damping (Lysak & Lotko 1996) and acceleration by reflected waves.
- **Altitude profile:**
  - Wave $E_\perp$ and Poynting flux decrease toward lower altitude about 5× faster than reflection alone predicts, so energy is being dissipated, mainly into electrons.
  - $E_\perp/B_\perp$ stays about $V_A$ throughout.
  - No significant gain in electron energy flux is seen across the FAST altitude range, so the acceleration is mostly finished above 4175 km.
- **The $v_A$ peak and reflection** (simulation, statistical density and composition):
  - Steep $v_A$ gradients sit near **7000 km (nightside)** and about 13,000 km (dayside).
  - Only about **10%** of the nightside incident Poynting flux from 30,000 km penetrates below FAST apogee; about 50% does on the dayside, where the ionospheric scale height is larger.
  - FAST can therefore see accelerated electrons with *almost no* dissipative-scale waves present.
  - The nightside gives peak electron energies about 2× the dayside, even with 5× less Poynting flux at FAST.
- **Ionospheric Alfvén resonator (IAR)** (Lysak 1991). The cavity between the ionosphere and the $v_A$ gradient can make the field-aligned Poynting flux vary with altitude without any dissipation. It is a partial, not sufficient, explanation of the altitude trend. Lessard & Knudsen 2001 argue it can't operate for $\lambda_\perp < 2$ km and $f > 0.4$ Hz.
- **Widths.** The median current-filament width mapped to 100 km is **about 1 km** (range 100 m to more than 10 km). The simulation uses $\lambda_\perp = 2$ km.
- **Ions.** Ion heating carries an order of magnitude less energy than the wave flux, so it can't account for the wave energy lost.
- **Mode conversion.** Conversion to electrostatic modes is energetically minor: the $E$ spectrum goes as $f^{-1.52}$, consistent with Seyler's $k^{-5/3}$ inertial-AW turbulence.
- **Sources are magnetospheric, not local.** Candidates:
  - Reconnection at the open/closed boundary, whose separatrix "unfolding" acts as a compressional wave that **mode-converts to shear Alfvén waves on perpendicular $v_A$ gradients in the plasma sheet boundary layer** (Hasegawa & Chen 1975; Allan & Wright 2000)
  - Fast-flow instabilities
  - Waves generated at $\lambda_e$ or $\rho_s$ scales directly in the reconnection diffusion region (Shay 2001)
  - Polar observations at 4–6 $R_E$ (Wygant 2000) support this

## Methods/data

FAST fields (fluxgate magnetometer, electric field) and electrons. Events are selected by Alfvénic $E/B$ ratio. Statistical density and composition profiles. 1-D inertial Alfvén wave simulation in a dipole field (600 V Gaussian pulse launched at 30,000 km, $\lambda_\perp = 2$ km at the ionosphere, scaled as $B^{-1/2}$). Uses the local relations $E_\parallel/E_\perp = k_\parallel k_\perp\lambda_e^2/(1 + k_\perp^2\lambda_e^2)$ and $E_\perp/B_\perp = V_A(1 + k_\perp^2\lambda_e^2)^{1/2}$.

## Connections

- [[Alfvén Waves]] — the $v_A$ profile, where acceleration happens, the IAR, widths, sources
- [[Auroral Acceleration]] — broadband aurora energies and locations
- [[FAST]], [[Chaston 2007 DAW Auroral Acceleration Fraction]], [[Keiling 2003 Alfvén Wave Poynting Flux]]
- [[Strangeway Ch11 The Aurora]] — co-author; same FAST framework

## Open questions

- Can phase mixing of large-scale shear waves (minimum about 50 km mapped scale in Allan & Wright) actually reach the about 1 km inertial scales observed?
