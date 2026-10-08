---
type: source
status: draft
updated: 2026-05-19
authors: B. Larson, A.V. Koustov, D.R. Themens, R.G. Gillies
year: 2023
---

# Larson 2023 E-CHAIM vs RISR

*Ionospheric electron density over Resolute Bay according to E-CHAIM model and RISR radar measurements.* Larson, B., Koustov, A.V., Themens, D.R., & Gillies, R.G. (2023). *Advances in Space Research*, 71, 2759–2769. doi:10.1016/j.asr.2023.01.017.

## Summary

Statistical comparison of E-CHAIM model electron density predictions against RISR-N and RISR-C observations at Resolute Bay across seasons (2014–2019), covering all altitudes from E region to topside. First comprehensive evaluation of E-CHAIM as a complete profile model against in-situ ISR data deep in the polar cap.

## Key Claims

1. **E-CHAIM/RISR ratio ≈ 1 near the F2 peak in all seasons except winter** — the model is well calibrated at the density maximum.
2. **E-CHAIM underestimates topside and bottomside by ~10–20%** across most conditions.
3. **Bottomside underestimates are largest in summer and equinoctial nighttime**.
4. **Topside underestimates are strongest in autumn nighttime**.
5. **Model fails to predict the highest observed peak densities** and the **largest hmF2 values** — it misses the extreme end of the distribution.
6. **Model overestimates the middle F layer during dawn hours in autumn**.
7. **Winter data too sparse** (very few RISR beams above 45° elevation meet quality thresholds) to draw conclusions.
8. Broader ratio distributions (larger variability) for spring, autumn, and summer nighttime reflect genuine ionospheric variability that the climatological model cannot capture.

## Methods/Data

- RISR World Day mode (11 beams); only beams above 45° elevation used; relative error < 50%.
- Data restricted to 100–500 km altitude; 5-min integration.
- Calibration: RISR calibrated to CADI ionosonde (foF2, hmF2 median ratio → calibration constant); iterated to convergence.
- Seasons defined: spring (Feb–Apr), summer (May–Jul), autumn (Sep–Oct), winter (January only; no Nov/Dec data).
- E-CHAIM version used anchors F2 peak parameters as spherical cap harmonics; topside uses NeQuick g=0.18; bottomside uses semi-Epstein parameterization.

## Connections

- [[E-CHAIM]] — direct validation of E-CHAIM predictions
- [[RISR-N]] — primary observational dataset
- [[AMISR]] — both RISR-C (dominant after 2016) and RISR-N used

## Open Questions

- Whether RISR data used during E-CHAIM development biased these validation results (model used some RISR data for topside fitting but not bottomside).
- Larger ISR database with better winter and nighttime coverage would improve validation confidence.
- New E-CHAIM features (auroral precipitation E-region, FIRI-2018 below E peak) not fully evaluated here.
