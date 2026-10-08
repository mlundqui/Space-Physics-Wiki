---
type: source
status: draft
updated: 2026-05-19
authors: Hu Sun, Zhijun Hua, Jiaen Ren, Shasha Zou, Yuekai Sun, Yang Chen
year: 2020
---

# Sun 2020 TEC Matrix Completion

*Matrix Completion Methods for the Total Electron Content Video Reconstruction.* Sun, H., et al. (2020). Submitted to *Annals of Applied Statistics*. University of Michigan (Statistics + Space Sciences).

## Summary

Statistical/computational paper proposing VISTA (Video Imputation with SoftImpute, Temporal smoothing, and Auxiliary data), a matrix completion algorithm for reconstructing missing values in Madrigal GPS TEC maps. Madrigal 5-minute TEC maps have ~75% missing values over ocean areas (no GNSS receivers); even after median filtering, ~50% of the global map is missing. VISTA extends SoftImpute-ALS matrix completion to account for spatial smoothness, temporal consistency, and auxiliary data constraints, outperforming existing spherical-harmonics-based methods for preserving mesoscale TEC features (equatorial plasma bubbles, high-latitude structures).

## Key Claims

1. **~50% of Madrigal TEC maps are missing** (primarily over oceans); standard IGS spherical harmonic global maps smooth out mesoscale features critical for ionospheric science.
2. **VISTA algorithm** combines: SoftImpute low-rank matrix factorization (nuclear norm minimization) + temporal smoothing penalty ($\ell_1$ TV regularization) + auxiliary data incorporation (IGS maps as initial estimate).
3. **Mesoscale TEC structures are preserved**: numerical tests on simulated data with realistic missingness patterns show VISTA outperforms prior methods (Candès, SoftImpute-ALS) in recovering equatorial plasma bubbles and high-latitude TEC patches.
4. **TEC maps are reformulated in MLT coordinates** so the noon meridian is fixed across time steps; this makes the missingness pattern quasi-stationary and stabilizes the temporal component.
5. **General algorithm**: the VISTA framework can be applied to other spatiotemporal reconstruction problems beyond TEC.

## Methods/Data

- Data: Madrigal Database (GPS + GLONASS dual-frequency; >5000 receivers; 5-min cadence; $1°\times1°$ resolution).
- Matrix completion: minimization of $H(M) = \frac{1}{2}\|P_\Omega(X - M)\|_F^2 + \lambda\|M\|_*$ (nuclear norm); solved iteratively via SVD.
- Validation: simulated missing data experiments + comparison against IGS global TEC maps (no missing values).

## Connections

- [[Polar Cap Patch]] — high-latitude TEC structures (patches) are among the mesoscale features VISTA aims to recover; directly relevant to patch statistics and occurrence studies
- [[Tongue of Ionization]] — large-scale TEC structures that GPS surveys rely on detecting
- [[David 2016 TEC Survey]] — uses the same Madrigal TEC database that VISTA reconstructs

## Open Questions

- Performance during geomagnetic storms when TEC structures are most extreme and most scientifically interesting.
- Whether VISTA-reconstructed maps are suitable for polar-cap patch occurrence studies where ground receiver density is especially low.
