---
type: source
status: draft
updated: 2026-05-13
authors: Laundal, Richmond
year: 2017
tags: [magnetic-coordinates, coordinate-systems, IGRF, QD, AACGM, apex-coordinates, ionosphere, magnetosphere]
---

# Laundal & Richmond 2017 — Magnetic Coordinate Systems

## Summary

Comprehensive review and standardization reference for the magnetic coordinate systems used in space physics. Covers eight systems: Centered Dipole (CD), Eccentric Dipole (ED), local magnetic/dip, Geocentric Solar Magnetic (GSM), Solar Magnetic (SM), Quasi-Dipole (QD), Modified Apex (MA), and Corrected Geomagnetic/AACGM. The non-orthogonal systems (QD, MA, CGM/AACGM) receive extended treatment including covariant/contravariant base vectors and how to decompose ionospheric electrodynamic quantities (**E**, **J**, **v**, $\Delta\mathbf{B}$) without introducing coordinate-system-dependent errors. The paper argues that "geomagnetic" and "magnetic" terminology is ambiguous in the literature and calls for precision in specifying which system is used and at which IGRF epoch.

## Key claims

- **Centered Dipole (CD / MAG):** $\hat{z}_{cd} = \hat{m}$ (dipole moment direction, pointing toward geographic south in NH). IGRF-12 NH pole at $\Theta_N = 9.69°$, $\Phi_N = -72.63°$. "Geomagnetic" has historically referred to CD but is ambiguous (sometimes means dip latitude in the literature).
- **Eccentric Dipole (ED):** Best-fit dipole shifted $\delta \approx 576.8$ km from Earth center, moving ~2.5 km/yr; computed from the first 8 IGRF Gauss coefficients ($\Delta x = \eta R_E$, $\Delta y = \zeta R_E$, $\Delta z = \xi R_E$).
- **Dip latitude:** $\lambda_{dip} = \arctan(\frac{1}{2}\tan I)$ where $I$ is magnetic inclination. Dip equator where $I = 0$.
- **GSM:** $\hat{x}_{gsm}$ toward Sun; $\hat{z}_{gsm}$ is the component of $\hat{m}$ perpendicular to $\hat{x}$ in the dipole-Sun plane (toward NH); $\hat{y}_{gsm}$ toward dusk. Standard for solar wind coupling: $B_z$ and $B_y$ in GSM control reconnection and ionospheric convection.
- **Solar Magnetic (SM):** $\hat{z}_{sm} = \hat{m}$; $\hat{x}$-$\hat{z}$ plane contains the Earth-Sun line. Used for ring current and inner magnetosphere.
- **Quasi-Dipole (QD):** $\lambda_{qd} = \pm\cos^{-1}\sqrt{(R_E+h)/(R_E+h_A)}$; constant along IGRF field lines. Grid angles between east and north QD unit vectors range from ~60° to ~116° — significantly non-orthogonal. QD at $h = 0$ equals MA at $h_R = 0$.
- **Modified Apex (MA):** $\lambda_{ma} = \pm\cos^{-1}\sqrt{(R_E+h_R)/(R_E+h_A)}$ where $h_R$ is a reference height (typically 110–130 km). At $r = R_E + h_R$ the base vectors $\mathbf{d}_i$ are orthonormal for a pure dipole. $D = \|\mathbf{d}_1 \times \mathbf{d}_2\|$ measures deviation from dipolar; $D = 1$ for a perfect dipole at $r = R_E + h_R$.
- **CGM / AACGM:** Trace the IGRF field line to the CD equatorial plane at height $h_{eq}$; map to $1R_E$ with dipole formula: $\lambda_{cgm} = \pm\cos^{-1}\sqrt{R_E/(R_E+h_{eq})}$. Undefined in equatorial regions where field lines do not cross the CD equatorial plane. Very similar to MA at $h_R = 0$ at high latitudes. Shepherd (2014) AACGM implementation uses spherical harmonics for conversion at any altitude.
- **Decomposing E in MA:** $\mathbf{E} = E_{d_1}\mathbf{d}_1 + E_{d_2}\mathbf{d}_2$; scalar components $E_{d_i}$ are constant along field lines, enabling exact ionospheric field-line mapping. Similarly $v_{e_1}$, $v_{e_2}$ (drift components in the $\mathbf{e}_i$ basis) are constant along field lines.
- **Coordinate mismatch error:** Using CD or local magnetic base vectors on QD/MA grids is mathematically unsound — vectors should be invariant with respect to the coordinate system, but this practice effectively changes them, causing systematic longitude- and hemisphere-dependent errors (Gasda & Richmond 1998; Laundal & Gjerloev 2014).
- **MLT ambiguity:** The simple formula $\text{MLT} = \text{UT} + (\phi + \Phi_N)/15$ does not place MLT = 12 at the correct magnetic longitude of the subsolar point. Recommended: $\text{MLT} = (\phi - \phi_{cd,\hat{s}})/15 + 12$ where $\phi_{cd,\hat{s}}$ is the CD longitude of the subsolar point. Systematic differences between MLT implementations reach up to 0.25 h, sufficient to distort IMF-tilt correlation studies.
- **Secular variation:** QD grid shifted ~2° latitude at polar and ~5° at midlatitudes from 1985 to 2015. IGRF epoch must be stated for all coordinate conversions. The four pole types (CD, ED, dip, QD/MA apex) drift independently.
- **Invariant latitude:** $\Lambda = \cos^{-1}\sqrt{1/L}$ from McIlwain's $L$ parameter; reduces to CGM for a dipole field; valid where $L \geq 1$.

## Methods / data

Analytical derivations throughout; figures use IGRF-12 (Thébault et al. 2015, $N_{max} = 13$, 195 coefficients). Code: apexpy (Python wrapper for Emmert et al. 2010 MA/QD code) and aacgmv2 (Shepherd 2014, C/IDL/Python). Subsolar point algorithm given in Appendix C (accurate to 0.01° lat / 0.025° lon for years 1601–2100).

## Connections

- [[Magnetic Coordinate Systems]] — this source is the primary reference for the concept page
- [[E-CHAIM]] — uses AACGM at 350 km reference altitude for its coordinate system
- [[IPWM]] — uses a dipole-aligned coordinate ($q^2 = \chi = \sin^2\theta/r$); distinct from QD/MA but field-line-following philosophy is analogous
- [[Ionospheric Dynamo]] — E and J decomposition in MA base vectors; Gasda & Richmond (1998) errors arise from using geographic vectors on QD/MA grids
- [[Field-Aligned Currents]] — scaled vertical current density $J_{qr} = J_{f_3}/F^2 = J_r/F$ in QD base vectors; field-aligned current maps conveniently in $\mathbf{e}_3$ direction
- [[Radiation Belts]] — McIlwain $L$ and invariant latitude $\Lambda$ link trapped particle physics to the magnetic coordinate framework
- [[Dungey Cycle]] — GSM $B_z$ and $B_y$ are the standard descriptors of solar wind–magnetosphere coupling
- [[Ionospheric Conductivity]] — Pedersen/Hall current decomposition and mapping along field lines requires MA/QD base vectors

## Open questions

- IPWM uses $\chi = \sin^2\theta/r$ — how does this compare to QD or MA, and are there analogous vector decomposition subtleties when comparing IPWM output to observations in AACGM or QD?
- How sensitive are RISR-N–derived ion drift vectors to the choice of coordinate system (QD vs MA vs local magnetic)?
- AACGM is undefined in low-latitude/equatorial regions — what coordinate system is used by E-CHAIM or other models in those regions?
