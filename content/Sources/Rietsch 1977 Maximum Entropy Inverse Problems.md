---
type: source
status: draft
updated: 2026-05-19
authors: E. Rietsch
year: 1977
---

# Rietsch 1977 Maximum Entropy Inverse Problems

*The Maximum Entropy Approach to Inverse Problems: Spectral Analysis of Short Data Records and Density Structure of the Earth.* Rietsch, E. (1977). *Journal of Geophysics*, 42, 489–506.

## Summary

Tutorial-style paper applying Jaynes' (1968) maximum entropy principle to two underdetermined geophysical inverse problems: (1) estimating the power spectrum from a finite set of autocovariance function values (maximum entropy spectrum), and (2) determining the density structure of a spherically symmetric Earth from its mass, radius, and moment of inertia. In both cases, the available information is expressed as linear constraints on the unknown probability distribution, and the maximum entropy principle selects the least-biased distribution consistent with those constraints. The MEM power spectrum recovered is shown to be identical to the standard Burg maximum entropy spectrum.

## Key Claims

1. **Maximum entropy principle** (Jaynes 1968): among all probability distributions consistent with known constraints, choose the one that maximizes $H(\mathbf{p}) = -\sum p_k \ln p_k$ — the least informative distribution beyond what is constrained.
2. **MEM power spectrum**: derived from the autocovariance function of a band-limited time series using a finite number of lag values; the expectation value of the derived probability distribution reproduces the Burg MEM spectrum exactly.
3. **Earth density inversion**: from mass $M$, radius $R$, and moment of inertia $I$, the maximum entropy probability distribution for density as a function of depth is computed; the result agrees well with the Bullen (1975) Earth density model.
4. **Both problems are linear functional constraints**: the formalism is general — any set of known linear functionals of the unknown function can be handled within the same maximum entropy framework.

## Methods/Data

Analytical. Entropy maximization using Lagrange multipliers. Two example applications: spectral estimation and planetary density inversion.

## Connections

- [[Varney 2021 ISR Probability]] — probabilistic foundations of ISR analysis; maximum entropy is a related inverse-problem methodology used in spectral estimation
- [[HF Radio Propagation]] — spectral estimation methods relevant to ISR and radar signal processing

## Open Questions

- Non-linear constraints (e.g., positivity alone) require iterative entropy maximization; the linear case treated here does not cover all practical geophysical inversions.
