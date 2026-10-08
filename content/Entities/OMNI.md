---
type: entity
status: stub
updated: 2026-05-12
sources: 1
tags: [data-product, solar-wind, nasa]
---

# OMNI

NASA Space Physics Data Facility data service providing time-aligned, propagated solar-wind and geomagnetic-index measurements. Solar-wind values are propagated from upstream monitors (e.g. L1) to Earth's bow shock; the propagation methodology is reviewed in Weimer & King (2008).

## Common parameters

- Solar wind: speed, density, temperature, dynamic pressure.
- IMF: Bx, By, Bz; clock angle; IEF Ey.
- Geomagnetic indices: AE, AU, AL, SYM-H, Kp, F10.7.

## Caveats

- **AE post-2020 is not in OMNI** — researchers fall back to alternative AE products. [[Lundquist Varney 2026]] uses the UCLA ELFIN proxy AE database for that period.
- The 5–15 min ionospheric response time after an IMF turning (Yu & Ridley 2009) means OMNI-tagged conditions are best interpreted as causal drivers via a look-back window, not as instantaneous proxies, for events immediately following IMF turnings.

## Tooling

Typically queried via [[pySPEDAS]] for time-series alignment with ground-based or in-situ datasets.

## Sources

- [[Lundquist Varney 2026]]
