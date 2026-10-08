---
type: source
status: mature
updated: 2026-05-19
authors: R.E. Dickinson, J.E. Geisler
year: 1968
---

# Dickinson Geisler 1968 Thermospheric Vertical Motion

**Citation:** Dickinson, R. E., and J. E. Geisler (1968), *Vertical Motion Field in the Middle Thermosphere from Satellite Drag Densities*, Monthly Weather Review, 96(9), 606–611.

## Summary

Derives the thermospheric vertical motion field from the continuity equation applied to horizontal winds inferred from satellite drag data (Jacchia & Slowey model). The central contribution is the w = w_D + w_L decomposition: vertical motion consists of a mass-divergence component (w_D) and a pressure-surface lifting component (w_L ≈ ∂h/∂t). For planetary-scale diurnal motions, ∂h/∂t ≫ **c**·∇h, so w_L dominates. Adiabatic heating by this vertical motion is thermodynamically comparable in magnitude to direct solar radiation heating. This paper is the foundational reference for the thermospheric vertical wind coordinate ambiguity problem revisited by [[Thayer Coleman 2026 Vertical Winds]].

## Key claims

- **w = w_D + w_L decomposition**: total vertical motion at a constant pressure surface p₀ is the sum of the divergence-driven term w_D = −(1/ρ(h))div[∫_h^∞ ρ**c** dz] and the lifting term w_L = ∂h/∂t|_{p=p₀}, the rate of rise of that surface.
- For planetary-scale (diurnal) motions, ∂h/∂t ≫ **c**·∇h, so w_L ≈ ∂h/∂t dominates; w_D is the mass-divergence contribution.
- Amplitudes of total vertical motion at 300 km: ~1 m/s; decrease by a factor of ~3 going from 300 km to 150 km.
- Mean zonal-average vertical motion at 300 km: upward (rising) at high latitudes, downward near the equator, consistent with a thermally-driven mean meridional circulation.
- Diurnal adiabatic heating amplitude at 300 km (~3000 K/day) exceeds direct solar radiation heating at 30° lat. at equinox (~1000 K/day); the adiabatic cooling/heating pattern advances the phase of the thermospheric diurnal bulge by 3–4 hours relative to solar-only model predictions.
- Atmosphere is stably stratified (Γ − Γ_a < 0 throughout thermosphere): upward motion produces adiabatic cooling, downward motion produces adiabatic warming.

## Methods/data

- Horizontal winds derived from the global JS thermospheric model based on satellite drag density data (Geisler 1966); model covers 120–500 km.
- Vertical velocity computed from the depth-integrated continuity equation; zonal and meridional wind divergence contributions isolated separately.
- Results shown at 150, 200, and 300 km levels; equinox solar-minimum conditions.

## Connections

- [[Lifting]] — w_L is the pressure-surface lifting mechanism by which ionospheric F-region plasma is vertically displaced; this paper establishes the formal decomposition underpinning all thermospheric lifting discussions.
- [[Thayer Coleman 2026 Vertical Winds]] — explicitly revisits and extends the Dickinson & Geisler decomposition to address FPI airglow measurement ambiguities in the context of TIEGCM adiabatic heating.
- [[Traveling Atmospheric Disturbances]] — adiabatic heating from vertical motions modulates the thermospheric background temperature profile into which TADs propagate.
- [[Ionospheric Energetics]] — adiabatic heating from vertical motions is a second heat source (~3000 K/day) comparable in magnitude to solar EUV at 300 km.

## Open questions

- How does the decomposition behave at auroral/high-latitude scales where Joule heating produces strongly localized, large-amplitude horizontal wind divergences?
- Is w_L separable from w_D observationally using FPI vertical wind measurements alone? (This is the Thayer 2026 ambiguity problem.)
