---
type: source
status: draft
updated: 2026-05-13
sources: 1
authors: Varney
year: 2021
---

# Varney 2021 — Probability Theory for Incoherent Scatter Radar

## Summary

Lecture notes (13 pp) developing the probabilistic foundations of incoherent scatter radar signal processing. Covers random variables, complex random processes, the autocorrelation function (ACF) and power spectral density, and the covariance/pseudo-covariance framework for complex vectors. The central result is that ISR lag-product estimates are Gaussian-distributed by the central limit theorem, enabling maximum-likelihood (or Bayesian) parameter estimation from measured ACFs.

## Key claims

- ISR scattered voltages are modeled as complex, zero-mean, stationary random processes: $V = V_R + jV_I$ with $\langle V \rangle = 0$, so the information is entirely in the second-order statistics.
- The ACF is $R_V(\tau) = \langle V(t)V^*(t-\tau)\rangle$; the power spectral density is its Fourier transform $S_V(\omega) = \int R_V(\tau)e^{-j\omega\tau}d\tau$, which is real and non-negative (Wiener-Khinchin theorem), and satisfies $\int S_V\,d\omega = R_V(0) = \langle|V|^2\rangle$ (total power).
- For a real random vector $\mathbf{X}$, the covariance matrix is $K_X = E\{(\mathbf{X}-\bar{\mathbf{X}})(\mathbf{X}-\bar{\mathbf{X}})^T\}$; for complex vectors the Hermitian conjugate replaces the transpose: $K_X = E\{(\mathbf{X}-\bar{\mathbf{X}})(\mathbf{X}-\bar{\mathbf{X}})^H\}$.
- The pseudo-covariance $\tilde{K}_X = E\{(\mathbf{X}-\bar{\mathbf{X}})(\mathbf{X}-\bar{\mathbf{X}})^T\}$ (non-conjugate transpose) captures the correlation between $V_R$ and $V_I$; for a proper complex Gaussian process it vanishes, simplifying the likelihood function used in ISR fitting.
- By the central limit theorem, averages of many independent lag products converge to Gaussian distributions; this justifies using a Gaussian likelihood for ISR spectral fitting even though individual lag products are not Gaussian.

## Methods / data

Lecture slides — pedagogical derivations, no observational data. Motivation is ISR signal processing (RISR-N, PFISR, etc.) but the probability framework applies to any radar receiving thermal scatter.

## Connections

- [[RISR-N]] — primary instrument context; RISR-N ACF estimation and fitting is the motivating application
- [[AMISR]] — general AMISR fitting pipeline uses these probabilistic foundations
- [[F-Layer]] — ISR fitted parameters ($N_e$, $T_e$, $T_i$, $v_{los}$) from which F-region structure is derived

## Open questions

- When does the proper-complex assumption (zero pseudo-covariance) break down in practice, and what bias does it introduce in fitted ISR parameters?
- How does the Gaussian approximation perform for short integration times where relatively few lag-product samples are averaged?
