---
type: source
status: draft
updated: 2026-05-19
authors: Alex T. Chartier, Cathryn N. Mitchell, Ethan S. Miller
year: 2018
---

# Chartier 2017 Swarm Patch Occurrence

*Annual Occurrence Rates of Ionospheric Polar Cap Patches Observed Using Swarm.* Chartier, A.T., Mitchell, C.N., & Miller, E.S. (2018). *Journal of Geophysical Research: Space Physics*, 123, 2327–2335. doi:10.1002/2017JA024811.

## Summary

Three-year analysis of patch occurrence using Swarm satellite Langmuir probe and upward-GPS data (Aug 2014–Jul 2017) reveals that patches occur more frequently around December in **both** hemispheres — not following local winter as predicted by existing formation theories. This result is produced by the absolute-test detection algorithm (D2/D3) and is missed by relative-test algorithms (D1) because of the ionospheric annual asymmetry between hemispheres.

## Key Claims

1. **December maximum in both hemispheres**: the correct result, confirmed by Langmuir probe (D1 with F_10.7-linked threshold = D3) and GPS (D2) data across Swarm A and B at 55°, 70°, and 78° MLAT cutoffs.
2. **Relative detection algorithm (D1)**: patch peak density must exceed double the 1250-km sliding-window mean; produces a **local-winter maximum in each hemisphere** (NH winter = December; SH winter = June).
3. **Absolute detection algorithm (D2/D3)**: patch peak linked to 81-day averaged F_10.7 value (×1000 as threshold in el/cm³); produces **December maximum in both hemispheres**.
4. **Root cause of algorithm discrepancy**: SH winter has extremely low background density → relative algorithm counts tiny fluctuations as patches; SH summer has high background density → large real patches fail the relative doubling test. NH annual asymmetry is less pronounced, so relative algorithm works passably there.
5. **Proposed fix (D3)**: uses absolute test tied to F_10.7 (solar-activity-scaled threshold) + Langmuir probe in-situ data (not GPS TEC) to avoid multiple-counting.
6. **Current patch formation theory is "at least incomplete"**: no mechanism predicts a December maximum in both hemispheres; Sojka et al. 1994 UT-minimum model, Lockwood & Carlson 1992 transient reconnection, and particle-precipitation mechanisms all predict enhancement during local winter solstice conditions.
7. The widely used Crowley (1996) criterion (factor-of-2 above background density) should be revised for Southern Hemisphere / high-background conditions; an absolute solar-flux-linked criterion is superior.

## Methods/Data

- Swarm A (87.4° orbit) and B (88.0° orbit); Nov 2013 launch.
- Langmuir probe: in-situ N_e, 0.5-s cadence (~10 km resolution); GPS upward TEC at 1-s cadence (~10 km).
- 3-year dataset: Aug 2014–Jul 2017; analysis separated by hemisphere, satellite, instrument type.
- Three detection algorithms: D1 (relative, after Coley & Heelis 1995), D2 (absolute, replicates NOJA/CHAMP approach), D3 (new, Langmuir + F_10.7-linked threshold).
- GPS biases estimated daily, corrected before analysis.

## Connections

- [[Polar Cap Patch]] — central observational result; definition debate
- [[DMSP]] — prior patch occurrence datasets used for comparison
- [[Tongue of Ionization]] — SED/TOI parent structure whose occurrence is also asymmetric

## Open Questions

- Physical cause of the December maximum in both hemispheres is unknown; requires a UT/longitude mechanism beyond pure local season.
- How to reconcile with the well-established UT/seasonal control of sub-cusp foF2 (Buchau et al. 1985) which does peak in local winter.
