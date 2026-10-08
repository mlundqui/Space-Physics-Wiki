---
type: entity
status: draft
updated: 2026-05-19
sources: 2
tags: [instrument, mission, radiation-belts, inner-magnetosphere]
---

# Van Allen Probes

NASA twin-spacecraft mission dedicated to understanding the dynamics of Earth's radiation belts. Originally named Radiation Belt Storm Probes (RBSP); renamed after launch. Launched August 30, 2012; final data collection 2019. Orbited between 1.1 and 5.5 R_E on highly elliptical 9-hour orbits, repeatedly traversing the inner and outer radiation belts and the slot region at all local times.

## EMFISIS Instrument Suite

The Electric and Magnetic Field Instrument Suite and Integrated Science (EMFISIS) is the primary wave and magnetic field instrument; described by [[Kletzig 2013 EMFISIS]] (instrument) and [[Kletzig 2023 EMFISIS Science]] (post-mission science):

| Component | Measurement | Range |
|-----------|-------------|-------|
| MAG (DC fluxgate) | Background B vector | DC to ~10 Hz; 64 vectors/s |
| WFR (waveform receiver) | Full-vector E and B waves | 10 Hz – 12 kHz |
| HFR (high-freq receiver) | Single electric component | 10 kHz – 500 kHz |

MAG calibration: [[Vasquez 2020 Van Allen Probe FGM Calibration]] (ensemble daily spin-tone method).

WFR provides the first full 3-D vector (E and B) wave measurements in the inner magnetosphere — enabling wave-normal analysis (WNA) for polarization, ellipticity, and Poynting flux.

## Key Scientific Results

- **ULF/radial diffusion:** Outward radial diffusion during storm main phase transports outer-belt electrons to the magnetopause for permanent loss; inward diffusion + local acceleration together explain post-storm outer belt recoveries at L ~ 5.
- **Chorus acceleration:** Substorm-injected electrons drive chorus waves (0.2–0.6 $\Omega_e$) outside the plasmapause; local cyclotron acceleration produces MeV enhancement events.
- **Hiss-controlled slot region:** Plasmaspheric hiss (100 Hz–2 kHz, inside plasmapause) scatters electrons into the loss cone over hours–days; maintains the slot between inner and outer belt.
- **EMIC precipitation:** Proton ring current drives EMIC waves at dusk; causes rapid (minutes–hours) precipitation of multi-MeV electrons at L > 3 during storm main phase.
- **Plasma density:** HFR upper hybrid line provides the most accurate inner-magnetosphere density, independent of and superior to particle detectors at high densities.

## Relevance to High-Latitude Ionosphere

Van Allen Probes constrain the ring current injection geometry that drives [[Subauroral Polarization Streams|SAPS]], which in turn drives [[Storm-Enhanced Density|SED]] formation and [[Polar Cap Patch]] occurrence (see [[Bao 2023 Geospace Plume MAGE]]). EMIC wave environments connect to auroral precipitation patterns and NEIALs at high latitudes.

## See Also

- [[THEMIS]] — companion mission covering magnetotail and solar wind; upstream IMF monitoring
- [[MAGE]] — coupled geospace model linking ring current (EMIC → radiation belt) to ionospheric response

## Sources

- [[Kletzig 2013 EMFISIS]]
- [[Kletzig 2023 EMFISIS Science]]
