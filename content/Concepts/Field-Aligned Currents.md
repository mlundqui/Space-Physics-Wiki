---
type: concept
status: draft
updated: 2026-10-08
sources: 4
---

# Field-Aligned Currents

Electric currents flowing along geomagnetic field lines that electrically couple the magnetosphere to the ionosphere. Also called Birkeland currents. They are the primary mechanism by which magnetospheric stresses (driven by solar wind interaction) are transmitted to the high-latitude ionosphere and thermosphere.

## Region 1 and Region 2 Systems

The large-scale FAC system consists of two concentric rings at auroral latitudes:

- **Region 1 (outer)**: ~70–75° magnetic latitude; current flows into the ionosphere on the dawn side, out on the dusk side (sense reverses for southward IMF). Connected to the magnetopause/boundary layer at high altitudes.
- **Region 2 (inner)**: ~65–70°; opposite sense to Region 1; connected to the partial ring current in the inner magnetosphere. Returns the current back upward to close the circuit.

The two-cell [[Ionospheric Dynamo|convection pattern]] is driven and sustained by the divergence of the FAC system closing through horizontal Pedersen currents.

## Current Continuity

At the ionosphere:

$$\nabla_\perp \cdot \mathbf{J}_\perp = -J_\parallel$$

Divergence of horizontal (Pedersen + Hall) currents must equal the FAC density. This gives the master equation of the [[Ionospheric Dynamo]].

## Substorm Current Wedge

During magnetospheric substorms, disruption of the near-Earth cross-tail current diverts current into the ionosphere as a localized FAC "wedge" centered near midnight:
- Downward FAC on the dusk flank, upward on the dawn flank of the disruption region
- Drives the auroral substorm bulge electrojet
- Corresponds to dipolarization of the field in the magnetotail

## Parallel Electric Fields and Acceleration

Where $J_\parallel$ cannot be carried by thermal particle populations (low density on magnetospheric field lines), a parallel electric field $E_\parallel$ develops to accelerate electrons or ions to carry the current. For an isotropic Maxwellian source this is the Knight (1973) relation:

$$j_\parallel = j_0\left[R - (R-1)\exp\!\left(-\frac{e\Phi}{(R-1)k_BT}\right)\right], \qquad j_0 = en\sqrt{\frac{k_BT}{2\pi m_e}}, \qquad R = \frac{B_I}{B_m}$$

Its limits are $j_0$ at $\Phi=0$; $j_0(1+e\Phi/k_BT)$ for $e\Phi\ll(R-1)k_BT$; $K\Phi$ with $K = e^2n/\sqrt{2\pi m_ek_BT}$ for $1\ll e\Phi/k_BT\ll R-1$; and saturation at $Rj_0$. Full derivation, verification and the reasons published forms differ: [[Knight Relation]].

*(Corrected 2026-10-07: this section previously gave $J_\parallel = \frac{n_em_e\Omega_e}{k_BT_e}(e\Phi/2\pi)^{1/2}$. That expression is not dimensionally a current density and has no source.)*

The accelerated electrons produce discrete auroral arcs (see [[Aurora]]).

**Three auroral current regions** ([[Strangeway Ch11 The Aurora]], from FAST):
1. **Upward current / inverted-V.** Carried by electrons accelerated through a quasi-static potential.
2. **Downward return current.** Carried by upgoing ionospheric electrons. It empties the ionosphere ("black aurora") and is not exactly balanced locally.
3. **Alfvénic region.** Small-scale up and down currents that largely cancel. Here $E/b \approx v_A$ instead of $1/(\mu_0\Sigma_P)$, and the currents are carried by dispersive [[Alfvén Waves]]. This is the M-I system "not yet in large-scale equilibrium."

**Waves as energy carriers.** Large-scale quasi-static FACs are **not the only** electromagnetic energy carrier into the auroral zone. Alfvén-wave Poynting flux at 25,000–38,000 km traces the whole oval and can supply about 30–35% of auroral luminosity. In one event it exceeded FAC-associated Poynting flux by 1–2 orders of magnitude ([[Keiling 2003 Alfvén Wave Poynting Flux]]). Monoenergetic (inverted-V) precipitation statistically tracks the Region 1 system ([[Newell 2009 Global Precipitation Budget]]).

Strangeway's form, $j = j_0(B_I/B_m)\{1 - (1 - B_m/B_I)\exp[\cdots]\}$, is algebraically identical to the one above. The thermal current is $j_0 \approx 0.85$ µA m⁻² at 1 cm⁻³ and 1 keV. The forms previously flagged as conflicting are reconciled on [[Knight Relation]]: they are different limits of one relation. See also [[Auroral Acceleration]].

## Observational Signatures

- Magnetometer deflections at ground or in space (AMPERE satellite network provides near-real-time FAC maps)
- Electron/ion pitch-angle distributions: field-aligned beams signal FAC-driven particle acceleration
- ISR observations of elevated $T_e$ along auroral arcs (Joule heating and electron precipitation)

## Related Concepts

- [[Ionospheric Dynamo]] — FACs are the source term in the master equation
- [[Joule Heating]] — Pedersen currents driven by FACs dissipate energy
- [[Aurora]] — discrete aurora marks regions of upward FAC (downward electron beam)
- [[Dungey Cycle]] — source of the Region 1 FAC system

## Relationship to particle precipitation

[[Xiong 2020 FACs Precipitation DMSP]] provides a direct statistical comparison of DMSP-derived FAC magnitudes and simultaneous precipitating particle energy fluxes using magnetometer + SSJ/5 spectrometer data sorted by IMF $B_y$:

- **Region 2 current maxima are co-located with particle energy flux peaks** at both dusk and dawn sides for southward IMF — the downward R2 current correlates spatially with the electron precipitation peak in the auroral band.
- **Region 1 is displaced ~3.5° equatorward from the precipitation peak** on the dawn side — a systematic spatial offset between the current maximum and the ionization peak.
- **FAC peaks bracket the precipitation zone**: the statistical auroral band lies *between* the R1 and R2 maxima, enclosed by the current sheets on either side.
- **Particle precipitation energy flux near R1 is lower than near R2** despite R1 typically carrying larger field-aligned currents — suggesting that the current near R1 is carried by accelerated electrons rather than diffuse precipitation.

These relationships are consistent with the picture that R2 currents close through diffuse precipitation in the auroral oval, while R1 currents are associated with more structured (discrete arc) precipitation at the boundary.

## Derivations

- [[Knight Relation]] — full kinetic derivation of the upward-current current–voltage relation
- [[Ideal MHD from Kinetic Theory]] — why $\nabla\cdot\mathbf{j}=0$ forces diverging perpendicular currents along $\mathbf{B}$
- [[MHD Wave Modes]] — the shear Alfvén wave as the carrier of $j_\parallel$
- [[Magnetotail]] — cross-tail current and the substorm current wedge (concept page)

## Sources

Seeded from AOS 205B course materials.
- [[Xiong 2020 FACs Precipitation DMSP]]
- [[Strangeway Ch11 The Aurora]]
- [[Keiling 2003 Alfvén Wave Poynting Flux]]
- [[Newell 2009 Global Precipitation Budget]]
