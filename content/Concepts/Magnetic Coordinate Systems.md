---
type: concept
status: draft
updated: 2026-10-08
sources: 1
tags: [coordinates, magnetic-coordinates, IGRF, ionosphere, magnetosphere]
---

# Magnetic Coordinate Systems

A family of coordinate systems designed to align with Earth's magnetic field rather than its rotation axis. Essential for ionospheric and magnetospheric physics because charged particle motion, current flow, and electric field mapping all follow field lines — not geographic directions.

## Why magnetic coordinates?

Ions and electrons are constrained to move along field lines; physical quantities like **E**, **J**, and $\mathbf{v}_{E\times B}$ are often constant or slowly varying along field lines. Geographic/geocentric coordinates mix field-parallel and field-perpendicular directions, making ionospheric mapping awkward.

A common but physically incorrect practice is representing a vector (e.g. **E** or **J**) in orthogonal geographic/CD components while plotting it on a QD or MA grid. This is mathematically inconsistent: vectors should be invariant with respect to the coordinate system, but this practice effectively changes them, causing systematic longitude- and hemisphere-dependent errors (Gasda & Richmond 1998; Laundal & Gjerloev 2014).

## Orthogonal systems

### Centered Dipole (CD / MAG / geomagnetic)

Best-fit single dipole to IGRF centered on Earth. $\hat{z}_{cd} = \hat{m}$ (dipole axis, positive toward geographic south in NH). IGRF-12 NH pole at $\Theta_N = 9.69°$, $\Phi_N = -72.63°$. "Geomagnetic" and "MAG" both refer to CD, but "geomagnetic" is ambiguous — it sometimes means dip latitude in the literature. CD is the simplest global magnetic frame; errors at high latitudes can reach several degrees latitude relative to IGRF-tracing methods.

### Eccentric Dipole (ED)

Best-fit dipole with center shifted $\delta \approx 576.8$ km from Earth's center (moving ~2.5 km/yr). Derived from the first 8 IGRF Gauss coefficients. More accurate than CD for conjugate-point studies; the shift Cartesian components are $\Delta x = \eta R_E$, $\Delta y = \zeta R_E$, $\Delta z = \xi R_E$.

### Dip latitude

$\lambda_{dip} = \arctan(\frac{1}{2}\tan I)$ where $I$ is magnetic inclination. Dip equator where $I = 0$. Primarily used for equatorial ionospheric phenomena (EIA, equatorial electrojet, equatorial spread-F).

### GSM (Geocentric Solar Magnetic)

$\hat{x}_{gsm}$ toward Sun; $\hat{z}_{gsm}$ is the component of $\hat{m}$ perpendicular to $\hat{x}$ in the dipole–Sun plane (toward NH); $\hat{y}_{gsm}$ toward dusk. Standard for solar wind–magnetosphere coupling: $B_z$ and $B_y$ in GSM control dayside reconnection and the ionospheric convection pattern.

### Solar Magnetic (SM)

$\hat{z}_{sm} = \hat{m}$; $\hat{x}$-$\hat{z}$ plane contains the Earth-Sun line. Used for ring current and inner magnetosphere, where the dipole axis (not the Sun direction) is the primary organizing axis.

## Non-orthogonal systems

### Quasi-Dipole (QD)

QD latitude is constant along IGRF field lines:
$$\lambda_{qd} = \pm\cos^{-1}\sqrt{\frac{R_E + h}{R_E + h_A}}$$
where $h_A$ is the apex height of the IGRF field line through the point. The grid is significantly non-orthogonal: angles between eastward and northward QD unit vectors range from ~60° to ~116° globally.

QD at $h = 0$ is identical to Modified Apex at $h_R = 0$.

**Base vectors** (Richmond 1995; Emmert et al. 2010):
- $\mathbf{g}_1 = \frac{R_E+h}{F}\cos\lambda_{qd}\nabla\phi_{qd}$ — eastward along constant $\lambda_{qd}$
- $\mathbf{g}_2 = \frac{R_E+h}{F}\nabla\lambda_{qd}$ — northward along constant $\phi_{qd}$
- $\mathbf{g}_3 = F\hat{k}$ — approximately vertical ($F = \|\mathbf{f}_1 \times \mathbf{f}_2\|$, volume factor $W = (R_E+h)^2\cos\lambda_{qd}$)

Current density in QD: $\mathbf{J} = J_{f_1}\mathbf{f}_1 + J_{f_2}\mathbf{f}_2 + J_{f_3}\mathbf{f}_3$; first two components are horizontal, third is approximately vertical. Scaled vertical current: $J_{qr} = J_{f_3}/F^2 = J_r/F$.

### Modified Apex (MA)

Introduces a reference height $h_R$ (typically 110–130 km for ionospheric applications):
$$\lambda_{ma} = \pm\cos^{-1}\sqrt{\frac{R_E + h_R}{R_E + h_A}}$$
At $r = R_E + h_R$ the MA base vectors are orthonormal for a pure dipole. The deviation parameter $D = \|\mathbf{d}_1 \times \mathbf{d}_2\|$ equals 1 for a perfect dipole at that radius.

**Base vectors** $\mathbf{d}_i$ (covariant-like, scaled for dipole orthonormality):
$$\mathbf{d}_1 = (R_E + h_R)\cos\lambda_{ma}\,\nabla\phi_{ma}$$
$$\mathbf{d}_2 = -(R_E + h_R)\sin I_{ma}\,\nabla\lambda_{ma}, \quad \sin I_{ma} = 2\sin\lambda_{ma}(4 - 3\cos^2\lambda_{ma})^{-1/2}$$
$$\mathbf{d}_3 = \frac{-\nabla V}{|\nabla V|D} \quad \text{(field-aligned)}$$

Reciprocal set: $\mathbf{e}_1 = \mathbf{d}_2 \times \mathbf{d}_3$, $\mathbf{e}_2 = \mathbf{d}_3 \times \mathbf{d}_1$, $\mathbf{e}_3 = \mathbf{d}_1 \times \mathbf{d}_2$.

**Key mapping property:** Electric field components $E_{d_1}$, $E_{d_2}$ (from $\mathbf{E} = E_{d_1}\mathbf{d}_1 + E_{d_2}\mathbf{d}_2$) are exactly constant along field lines, enabling rigorous field-line mapping of the convection electric field. Similarly drift components $v_{e_1}$, $v_{e_2}$ are constant along field lines. Magnetic field $\mathbf{B}$ component $B_{e_3}$ is also constant along field lines.

### CGM / AACGM

**Corrected Geomagnetic (CGM):** Trace the IGRF field line from point $P$ to its intersection with the centered dipole equatorial plane at height $h_{eq}$, then apply the dipole mapping to $1R_E$:
$$\lambda_{cgm} = \pm\cos^{-1}\sqrt{\frac{R_E}{R_E + h_{eq}}}$$
CGM is undefined in equatorial regions where some IGRF field lines do not reach the CD equatorial plane (shaded regions near the dip equator). The CGM equator is distinct from the dip equator.

**AACGM (Altitude-Adjusted CGM):** Mathematically identical to CGM; Shepherd (2014) implementation uses spherical harmonic fitting instead of field-line tracing, enabling fast conversion at any altitude. Earlier implementations (Gustafsson et al. 1992) used lookup tables only at $h = 0$ and introduced interpolation errors.

At high latitudes (polar cap, auroral zone), AACGM and MA (at $h_R = 0$) agree well; differences are significant only near the low-latitude boundary where AACGM becomes undefined.

Software: `aacgmv2` (Python/C/IDL, Shepherd 2014); `apexpy` (Python, Emmert et al. 2010 for MA/QD).

## Magnetic Local Time (MLT)

The recommended definition (Laundal & Richmond 2017, Eq. 93):
$$\text{MLT} = (\phi - \phi_{cd,\hat{s}})/15 + 12$$
where $\phi$ is the magnetic longitude (in CD, ED, CGM/AACGM, or QD/MA — must be stated) and $\phi_{cd,\hat{s}}$ is the CD longitude of the subsolar point. The simpler formula $\text{UT} + (\phi + \Phi_N)/15$ does not correctly place MLT = 12 at the subsolar magnetic meridian.

The MLT/latitude grid rotates relative to Earth at a seasonally varying rate: 0.94–1.10 hours MLT per UT hour (2015) because the spacing of magnetic meridians is non-uniform. Systematic differences between MLT implementations reach up to 0.25 h, sufficient to shift solar-wind–MLT correlation results by ~0.1 h per 10° IMF tilt angle.

## Secular variation

All magnetic coordinate systems evolve as Earth's internal field changes. The QD grid shifted ~2° latitude at polar regions and ~5° at mid-latitudes from 1985 to 2015. The four pole types (CD, ED, dip, QD/MA apex) drift independently and at different rates. The IGRF epoch used for conversions **must be specified** in all publications.

## Summary table

| System | Type | Basis | Primary use |
|---|---|---|---|
| CD / MAG | orthogonal | IGRF dipole moment | polar cap, general high-latitude |
| ED | orthogonal | IGRF first 8 Gauss coefficients | conjugate studies |
| Dip / DIP | orthogonal | IGRF inclination $I$ | equatorial ionosphere |
| GSM | orthogonal | dipole + Sun direction | solar wind coupling, IMF $B_z$/$B_y$ |
| SM | orthogonal | dipole + Sun direction | ring current, inner magnetosphere |
| QD | non-orthogonal | IGRF field line apex | large-scale ionospheric maps, ΔB |
| MA | non-orthogonal | IGRF field line apex + $h_R$ | E/J/v field-line mapping |
| CGM / AACGM | non-orthogonal | IGRF field line + CD equatorial plane | high-latitude data analysis |

## Related concepts

- [[Dungey Cycle]] — GSM $B_z$ controls reconnection rate and ionospheric convection
- [[Ionospheric Conductivity]] — Pedersen/Hall currents and conductances mapped in QD/MA
- [[Field-Aligned Currents]] — $J_{qr} = J_r/F$ is the scaled vertical current component in QD base vectors
- [[Ionospheric Dynamo]] — convection electric field maps along MA $\mathbf{d}_i$; systematic errors arise from using geographic vectors on magnetic grids
- [[Radiation Belts]] — McIlwain $L$; invariant latitude $\Lambda = \cos^{-1}\sqrt{1/L}$ bridges to trapped particle physics
- [[E-CHAIM]] — uses AACGM at 350 km reference altitude
- [[IPWM]] — uses a dipole-aligned coordinate ($\chi = \sin^2\theta/r$) with analogous field-line-following structure

## Derivations

- [[Dipole Field and L-Shells]] — the centered-dipole baseline (L, invariant latitude, dip angle)

## Sources

- [[Laundal Richmond 2016 Magnetic Coordinates]]
