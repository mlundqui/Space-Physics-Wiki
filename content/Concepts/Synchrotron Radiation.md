---
type: concept
status: draft
updated: 2026-05-13
sources: 0
---

# Synchrotron Radiation

Electromagnetic radiation emitted by relativistic charged particles ($\gamma \gg 1$) undergoing centripetal acceleration in a magnetic field. Also called magnetic bremsstrahlung. The dominant radiation mechanism for ultra-relativistic electrons in astrophysical and planetary radiation belts.

## Larmor Formula (Non-Relativistic)

For an accelerating charge, the total radiated power is:

$$P = \frac{2e^2 a^2}{3c^3}$$

Radiation pattern: dipole-like, with null along the acceleration direction and maximum perpendicular ($dP/d\Omega \propto \sin^2\theta$).

## Relativistic Synchrotron Power

For a relativistic electron ($\gamma \gg 1$) with pitch angle $\alpha$ in magnetic field $B$:

$$P_\text{syn} = 2\sigma_T c \beta^2 \gamma^2 \frac{B^2}{8\pi} \sin^2\alpha$$

where $\sigma_T = 6.65\times10^{-25}$ cm$^2$ is the Thomson cross section and $\beta = v/c$.

**Relativistic beaming:** radiation is confined to a cone of half-angle $\sim 1/\gamma$ around the instantaneous velocity vector. For ultra-relativistic electrons, an observer sees a brief pulse of radiation once per gyration cycle.

## Synchrotron Spectrum

The radiated power spectrum $P(\nu)$ peaks at the critical frequency:

$$\nu_c \propto \gamma^2 \frac{\Omega_e}{2\pi} \propto \gamma^2 \frac{eB}{mc}$$

For a power-law electron energy distribution $N(E) \propto E^{-n}$, the synchrotron spectrum is also a power law: $P(\nu) \propto \nu^{-(n-1)/2}$. This is the standard radio source spectrum used in astrophysics.

## Cherenkov Radiation

Related mechanism: a particle moving through a dielectric medium at $v > c/n(\omega)$ emits coherent radiation at the Cherenkov angle $\cos\theta_C = c/(nv)$. Analogous to a Mach cone in supersonic flow. Connected to the Landau resonance condition $\omega = k_z v_z$ in a dispersive medium.

## Planetary Applications

**Jupiter:** $B \approx 1$ G at the magnetic equator; electrons at ~15 MeV trapped in the Jovian radiation belts emit decimeter-wavelength synchrotron emission detectable from Earth. Intensity and spatial structure infer the Jovian magnetic moment and relativistic particle populations.

**Earth (Starfish artificial belt):** The 1962 Starfish Prime nuclear detonation at ~400 km altitude injected MeV electrons into an artificial radiation belt. Synchrotron emission was detected; decay time $\tau_{1/2} \sim 60$ days from wave-particle scattering losses.

**General diagnostic:** synchrotron brightness $\propto N_\text{rel} B^2$; the brightness spectral index gives the electron spectral index $n$. Combined with polarization (which traces field geometry), provides remote sensing of relativistic electron populations and magnetic fields in planets, pulsars, and AGN jets.

## Energy Loss

The synchrotron energy loss rate follows directly from $P_\text{syn}$:

$$\frac{dE}{dt} = -P_\text{syn} \propto -\gamma^2 B^2 \sin^2\alpha$$

This gives a loss timescale $\tau_\text{syn} = E/(dE/dt) \propto 1/(\gamma B^2)$. For MeV electrons in Earth's outer belt ($B \sim 0.1$–$0.3$ G at $L \sim 4$): $\tau_\text{syn} \sim$ months to years — typically longer than wave-particle scattering timescales, so synchrotron loss is rarely the dominant loss mechanism in Earth's belts.

## Related Concepts

- [[Radiation Belts]] — relativistic electrons in Earth's and Jupiter's belts emit synchrotron radiation
- [[Wave-Particle Interactions]] — wave scattering usually dominates over synchrotron loss for radiation belt electrons

## Sources

Seeded from AOS 250B course materials (Thorne 1993 course reader, Chapter 2).
