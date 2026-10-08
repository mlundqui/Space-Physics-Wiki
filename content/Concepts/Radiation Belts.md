---
type: concept
status: draft
updated: 2026-10-08
sources: 5
---

# Radiation Belts

Toroidal regions of energetic (keV–MeV) charged particles trapped by Earth's magnetic field via the three adiabatic invariants. Comprise the inner belt (~1–2 $R_E$; proton-dominated) and the outer belt (~3–7 $R_E$; electron-dominated), separated by the slot region (~2–3 $R_E$).

## Trapping and Adiabatic Invariants

Particles undergo three nested periodic motions; each has an associated adiabatic invariant conserved when the field changes on timescales long compared to that period:

| Motion | Period | Invariant |
|--------|--------|-----------|
| Gyration around $\mathbf{B}$ | ~µs–ms (electrons), ~0.01–1 s (protons) | $\mu = p_\perp^2/2\gamma m B$ (magnetic moment) |
| Bounce along field line | ~0.1–1 s (electrons), ~1–30 s (keV–MeV protons) | $J = \oint p_\parallel \, d\ell$ (longitudinal invariant) |
| Azimuthal drift around Earth | ~min–hours | $\Phi = \int \mathbf{B} \cdot d\mathbf{A}$ (magnetic flux) |

*(Corrected 2026-10-07: the bounce period was given as ~0.1–1 s for all particles, but that only holds for electrons. A 100 keV proton at L = 4 bounces in about 17 s; see [[Thorne 1993 AOS 250B Course Reader]] Table 6.1 and [[Adiabatic Invariants and Magnetic Mirrors]]. Gyroperiod ranges were also tightened.)*

**Loss cone**: particles whose mirror points are below ~100 km are absorbed by the atmosphere. Loss cone angle: $\sin^2\alpha_L = B_0/B_A$ where $B_0$ is the equatorial field and $B_A$ the field at the absorption altitude. For a dipole, $\sin^2\alpha_L = L^{-3}(4-3/L)^{-1/2}$, about 5° at $L=4$ and 2.5° at $L=6.6$.

## L-Shell Coordinate

McIlwain L-value: $L \approx r_0/R_E$ (equatorial crossing distance in Earth radii). Natural coordinate because $\mu = \text{const}$ and $J = \text{const}$ map to a unique $(L, B)$ surface. For a dipole field:

$$B(L,\lambda) = \frac{B_E}{L^3} \cdot \frac{(1 + 3\sin^2\lambda)^{1/2}}{\cos^6\lambda}$$

- Inner belt: $L \approx$ 1–2; protons up to ~100 MeV, electrons ~100s keV
- Slot region: $L \approx$ 2–3; depleted by wave scattering ([[Wave-Particle Interactions]])
- Outer belt: $L \approx$ 3–7; electrons up to ~MeV; highly variable with solar activity

## Ring Current

Gradient-$B$ drift of trapped particles is energy- and charge-sign dependent:
- Positive ions drift westward (gradient + curvature drift)
- Electrons drift eastward

Net westward current at $L \sim$ 3–5 is the ring current, measurable globally by the Dst/SYM-H geomagnetic index. Ring current energy ~$10^{15}$ J during moderate storms; decay timescale ~days (charge exchange with exospheric neutrals).

## Source and Loss Processes

**Sources:**
- Inward radial diffusion of outer-boundary particles (violation of $\Phi$ invariant by ULF waves)
- Local acceleration by chorus waves ([[Wave-Particle Interactions]])
- Solar energetic particle (SEP) injection

**Losses:**
- Precipitation into atmosphere (wave-induced pitch-angle scattering into loss cone)
- Charge exchange (ions)
- Magnetopause shadowing (outer boundary loss during compressions)

## Quasi-Trapped and Drift Loss Cone

Particles that drift longitudinally across a field minimum (e.g., South Atlantic Anomaly) can have local loss cone filling; these quasi-trapped particles are lost in ~1 drift orbit. "Shell splitting" occurs when drift invariant $\Phi$ is violated on timescales comparable to the drift period.

## Radiation Belt Dynamics During Storms

Geomagnetic storms produce complex, energy-dependent variations:
1. Initial dropout (magnetopause compression + ULF wave scattering)
2. Injection of ring-current ions ($L \approx$ 3–6)
3. Multi-day enhancement or depletion of outer belt electrons depending on wave environment
Whistler-mode chorus in the outer belt and EMIC waves at dusk are the dominant scattering agents.

## Related Concepts

- [[Wave-Particle Interactions]] — scattering into loss cone drives precipitation; local acceleration drives flux enhancements
- [[Synchrotron Radiation]] — relativistic electrons emit detectable radio emission (Jupiter's radiation belts; Starfish artificial belt)
- [[Dungey Cycle]] — drives radial transport and sets outer boundary condition

## Observational Constraints from Van Allen Probes

The [[Van Allen Probes]] mission (2012–2019) provided the first comprehensive in-situ wave and field measurements of the radiation belts. Key findings from the EMFISIS instrument suite ([[Kletzig 2013 EMFISIS]], [[Kletzig 2023 EMFISIS Science]]):

- Outward ULF-driven radial diffusion during storm main phase is a significant outer belt loss mechanism (electrons transported to magnetopause boundary for permanent loss).
- Local chorus acceleration at L ~ 5 produces post-storm outer belt flux enhancements; inward radial diffusion and local acceleration are complementary rather than competing.
- EMIC waves drive rapid (minutes–hours) precipitation of relativistic electrons (E > ~2 MeV) at L > 3 during storm main phase — rate too fast for diffusive models.
- Slot region (L ~ 2–3) is controlled by plasmaspheric hiss, scattering electrons on hour–day timescales.
- Van Allen Probe magnetometer calibration procedure: [[Vasquez 2020 Van Allen Probe FGM Calibration]].

## Quantitative loss rates at L < 4

[[Claudepierre 2022 Radiation Belt Losses]] performs a comprehensive quasilinear Fokker-Planck analysis of electron loss processes (30 keV–4 MeV) at L < 4 during geomagnetically quiet times. Key findings:

- **Coulomb energy drag is critical at $L \leq 2$**: ionization energy loss by collisions with thermal plasma must be included; omitting it produces factor-of-several errors in predicted lifetimes.
- **Plasmaspheric density model choice dominates uncertainty**: different empirical density models change predicted e-folding lifetimes by orders of magnitude at the same (L, E).
- **Lightning-generated whistlers (LGW)** improve agreement with observed Van Allen Probe decay timescales at $L \approx 1.8$–3.2; including them closes a systematic model–observation gap.
- **Drift-loss-cone correction** (using realistic vs. dipole field geometry) can significantly modify theoretical lifetimes at large L.
- The model matches observed Van Allen Probe e-folding times across most of L = 1–4 when all processes are included.

The loss hierarchy at L < 4 is: hiss + LGW (main pitch-angle diffusion) + Coulomb drag (energy loss at low L) + VLF transmitters (minor but non-negligible).

## K-P Flux Limiting: Observational Confirmation

The Kennel-Petschek self-limiting process (see [[Wave-Particle Interactions]]) has now been directly confirmed observationally. [[Olifer 2023 KP Self-Limiting Precipitation]] used a superposed epoch analysis of 70 geomagnetic storms (Van Allen Probes + POES): dawn-side substorm injections drive 54 keV electron fluxes above the K-P limit, exciting chorus wave growth that rapidly restores fluxes to the asymptotic level (~$5\times10^3$ cm$^{-2}$ s$^{-1}$ sr$^{-1}$ keV$^{-1}$ at $L\approx4.5$); the dusk-side remains capped at or below the K-P limit throughout. This confirms that the K-P limit sets the entire pitch-angle distribution shape, not just an equatorial boundary condition. [[Summers 2009 Relativistic KP Limit]] provides the fully relativistic theoretical framework: marginal stability (wave convective gain over a growth length) replaces Kennel 1966's wave-reflection criterion; observed Earth fluxes at L=5–10 lie slightly below the relativistic limit, consistent with self-regulation. Uranus and Jupiter also satisfy the relativistic K-P limit within observational uncertainties.

## Derivations

- [[Quasilinear Diffusion]] — pitch-angle diffusion and loss-cone lifetimes
- [[Kennel-Petschek Limit]] — self-limiting trapped flux
- [[Adiabatic Invariants and Magnetic Mirrors]] — derivation of $\mu$, $J$, $\Phi$, mirror force, dipole loss cone, bounce and drift periods
- [[Guiding-Center Drifts]] — gradient and curvature drifts that form the ring current
- [[Dipole Field and L-Shells]] — L, invariant latitude, mirror ratios
- [[Cold-Plasma Waves]] — whistler-mode and EMIC branches

## Sources

Seeded from AOS 250B course materials (Thorne 1993 course reader).
- [[Kletzig 2013 EMFISIS]]
- [[Kletzig 2023 EMFISIS Science]]
- [[Claudepierre 2022 Radiation Belt Losses]]
- [[Olifer 2023 KP Self-Limiting Precipitation]]
- [[Summers 2009 Relativistic KP Limit]]
