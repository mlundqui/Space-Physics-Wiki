---
type: meta
status: draft
updated: 2026-10-08
tags: [derivations, index]
---

# Derivations Index

This is the reading path through the wiki's derivation pages. Each page derives one core result from first principles, with commentary between the steps. The tone follows Griffiths: say what we're about to do, do it, then stop and ask what it means. Concept pages (e.g. [[MHD]], [[Radiation Belts]]) stay short and link here for the full derivation.

**How to read these pages.** The parts build on each other, so going in order is best, but every page lists its prerequisites at the top. The equations are in standard LaTeX and render the same in Obsidian (MathJax) and on the web (KaTeX). Units are **SI throughout**. Where a source uses Gaussian units, the page says so and converts.

**How these pages are checked.** No derivation goes in unless:

1. Its main results agree across at least two independent sources in the vault.
2. Its algebra has been checked symbolically (SymPy) or numerically (test-particle integration, quadrature) wherever that's possible.

Each page ends with a **Verification** section that records exactly what was checked. Anything not yet checked is labeled as such.

---

## Part I — Plasma foundations

| # | Page | Core results |
|---|---|---|
| 1 | [[Debye Shielding and the Plasma Frequency]] | $\lambda_D$, $\omega_{pe}$, plasma parameter $N_D$ |
| 2 | [[Guiding-Center Drifts]] | gyration, $\mathbf{E}\times\mathbf{B}$, general force drift, $\nabla B$, curvature and polarization drifts |
| 3 | [[Adiabatic Invariants and Magnetic Mirrors]] | $\mu$, mirror force, loss cone, $J$ and bounce period, $\Phi$ and drift period |
| 4 | [[Moment Equations from the Vlasov Equation]] | Vlasov equation, general moment equation, continuity/momentum/energy, closure problem |
| 5 | [[Ideal MHD from Kinetic Theory]] | single-fluid equations, generalized Ohm's law, frozen-in theorem, magnetic pressure and tension |
| 6 | [[MHD Wave Modes]] | shear Alfvén, fast and slow magnetosonic dispersion relations |

### Kinetic extensions

| # | Page | Core results |
|---|---|---|
| 7 | [[Landau Damping]] | Vlasov–Poisson dispersion; Landau contour; $\gamma\propto\hat f_0'(\omega/k)$; Maxwellian rate and why textbook forms differ; ion-acoustic damping |
| 8 | [[Quasilinear Diffusion]] | QL velocity diffusion and plateau; conservation laws; cyclotron resonance; bounce-averaged pitch-angle diffusion; weak vs strong diffusion |

## Part II — Ionosphere

| # | Page | Core results |
|---|---|---|
| 1 | [[Incoherent Scatter Spectrum]] | dressed-particle / fluctuation–dissipation spectrum; ion line, plasma line; what ISR measures; why ISR theories differ |
| 2 | [[Chapman Layer]] | Beer–Lambert, optical depth; production peak at τ = 1; universal $e^{1-X-e^{-X}}$ shape; α-Chapman layer; β-type chemistry; F2-peak condition $\beta\approx D/H^2$ (verified numerically) |
| 3 | [[Plasma Diffusion Along B]] | ambipolar $E_\parallel$; plasma scale height; minor-ion (H$^+$) upward force; ambipolar diffusion coefficient and equation; wind-induced drift |
| 4 | [[Pedersen and Hall Conductivity]] | mobility tensor; κ crossover; σ_P, σ_H, σ_∥; Hall-sign conventions; conductances; gravity and diamagnetic currents |
| 5 | [[Frictional and Joule Heating]] | $T_i = T_n + m_n|\Delta u|^2/3k$; $T_{\rm eff}$; neutral heating $=\sigma_P|\mathbf{E}'|^2$; Poynting's theorem; $\mathbf{E}\times\delta\mathbf{B}$ flux; heat vs. wind work |
| 6 | [[Electrostatic Dynamo Equation]] | ∇·J = 0 → elliptic equation for φ; F-region slab dynamo; Cowling conductivity; equipotential 2-D form with conductances; arcs, two-cell convection, conjugate coupling |
| 7 | [[Gradient-Drift and Rayleigh-Taylor Instabilities]] | linearized continuity and current closure; exact dispersion; γ = E′/BL (trailing edge unstable); gravity as effective field → γ = g/ν_in L; generalized RT |
| 8 | [[Polar Wind Transonic Outflow]] | Mach-number equation; critical point and transonic solution; de Laval analogy; sonic radius $GM/pV_S^2$; O$^+$ bound vs H$^+$ escaping; flux limiting |
| 9 | [[Appleton-Hartree Equation]] | magneto-ionic index from Maxwell plus electron motion; O/X waves; cutoffs X = 1, 1 ± Y; $f_xF_2$; matches Stix cold-plasma theory |

*Part II core complete.* Candidates: ionogram virtual/true height; chemistry rate equations; thermal balance ($T_e$).

## Part III — Sun, solar wind, magnetosphere

| # | Page | Core results |
|---|---|---|
| 1 | [[Knight Relation]] | kinetic current–voltage relation; $j_0$, Knight conductance $K$; limits and reconciliation of published forms |
| 2 | [[Kennel-Petschek Limit]] | self-limiting trapped flux $J^*\propto L^{-4}$; reflection vs convective-gain criteria; why published limits differ |
| 3 | [[Parker Solar Wind and Spiral]] | static corona impossible; transonic Mach equation and critical point; Lambert-W solution; Parker spiral; why 43°/45°/47° at 1 AU all appear |
| 4 | [[Rankine-Hugoniot Jump Conditions]] | conservation-law jumps; coplanarity; gas-dynamic and perpendicular shocks; 4× compression limit; entropy; oblique quartic (200C Eq. 6.15 erratum) |
| 5 | [[Chapman-Ferraro Standoff Distance]] | image dipole (×2); stagnation-pressure factor $K\approx0.88$; $R_{mp}\propto(\rho u^2)^{-1/6}$; comparison with Shue 1998; bow-shock standoff |
| 6 | [[Sweet-Parker Reconnection]] | $u_{in}/v_A = \delta/L = S^{-1/2}$; energy split; exact annihilation solution; why SP is too slow; Petschek, Hall, plasmoids |
| 7 | [[Dessler-Parker-Sckopke Relation]] | drift (−3) + magnetization (+1) fields; $\Delta B/B_0 = -\tfrac23 W/W_{mag}$; why 4.0 vs 2.8×10¹³ J/nT |
| 8 | [[Cold-Plasma Waves]] | Stix $S,D,P$ and $R,L$; $An^4 - Bn^2 + C$; cutoffs and resonances; full vs dense-limit lower hybrid; whistler group velocity, nose at $f_{ce}/4$, Storey angle 19.5° |
| 9 | [[Dipole Field and L-Shells]] | field and field lines; invariant latitude; $\lvert\nabla B\rvert/B=\kappa=3/r$; flux-tube area and volume ($\propto L^4$); open flux vs polar-cap latitude |

*Part III core complete (2026-10-08).* Candidates: Weber–Davis wind, MHD Kelvin–Helmholtz instability, radial diffusion, ionospheric chemistry and thermal balance.
