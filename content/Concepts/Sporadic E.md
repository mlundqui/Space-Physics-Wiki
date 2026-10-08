---
type: concept
status: draft
updated: 2026-05-20
sources: 1
tags: [ionosphere, e-region, sporadic-e]
---

# Sporadic E

Thin, dense ionization layers in the E region (~90–120 km altitude) that appear sporadically (unpredictably in time) against the background E-region ionosphere. They are 0.6–2 km thick and can be 5–10$\times$ denser than the surrounding E-layer plasma, producing large $f_o$Es reflections on ionosondes and significant HF and VHF radio propagation anomalies.

## Formation Mechanism: Metallic Ion Wind-Shear Convergence (S&N §11.13)

The dominant sporadic-E formation mechanism at mid-latitudes is **vertical wind-shear convergence of long-lived metallic ions** deposited by meteor ablation.

**Metallic ion source:** Meteors ablate in the 80–110 km altitude range, depositing Fe, Mg, Ca, Na, and other metallic atoms. These are quickly photoionized to Fe$^+$, Mg$^+$, Ca$^+$, Na$^+$. Metallic ions have very slow chemical loss rates (no efficient dissociative recombination pathway; only slow radiative recombination) — lifetimes of hours to days compared to minutes for O$_2^+$ and NO$^+$.

**Wind-shear convergence:** In the presence of vertical shear in the horizontal wind $u(z)$, the ion drift velocity under $\mathbf{E}\times\mathbf{B}$ and neutral drag produces a convergence altitude:
- Above the convergence altitude: eastward wind → ions drift southward and downward
- Below the convergence altitude: westward wind → ions drift northward and upward

The node of the wind shear (where the vertical ion drift reverses sign) acts as a **concentration point**. Metallic ions accumulate there on a timescale of hours. The layer thickness is set by the diffusion rate competing against the convergence rate; typical result is a layer 0.6–2 km thick.

**Ion chemistry:** Once concentrated, metallic ions can form molecular species ($\text{FeO}^+$, $\text{MgO}^+$) at low altitudes, but in the 90–110 km range the primary loss is diffusion spreading and wind-shear reversal. The long metallic ion lifetime is the key enabling factor — it allows accumulation over many wind cycles.

## Properties

| Property | Typical Value |
|---|---|
| Altitude | 90–120 km |
| Thickness | 0.6–2 km |
| Electron density | 5–10$\times$ background E-layer |
| Duration | Minutes to hours |
| Horizontal extent | ~100–1000 km along magnetic field |
| Dominant ions | Fe$^+$, Mg$^+$ (from meteors); Ca$^+$, Na$^+$ also present |

## Intermediate Layers

Distinct from narrow sporadic-E, **intermediate layers** (also §11.13) are wider (10–20 km) ionization enhancements in the 120–180 km altitude range, composed primarily of NO$^+$ and O$_2^+$ (normal E-region ions). They descend at night as the dynamo wind field changes, and are associated with the lower boundary of the F$_1$ layer. Their downward phase velocity (~1–4 km/hr) follows the pattern of atmospheric tides.

## Observational Signatures

- **Ionosondes:** Strong oblique and vertical echoes at $f_o$Es (critical frequency of sporadic-E layer); can blanketing the F region, masking the F2 trace.
- **ISR:** A thin, bright backscatter layer at E-region altitudes; the narrow vertical extent challenges ISR vertical resolution unless multi-beam or range-coded pulses are used.
- **VHF forward scatter:** When $f_o$Es > VHF frequency, single-hop propagation over 1000–2000 km distances ("sporadic-E skip").
- **GPS TEC:** Sporadic-E contributes a small, localized TEC enhancement detectable by dense receiver arrays.

## Polar and Auroral Sporadic E

At high latitudes, particle precipitation from auroral activity produces dense, structured E-region ionization that mimics sporadic-E on ionosondes. These auroral E-layers are not from wind-shear convergence of metallic ions but from direct impact ionization by precipitating electrons. They are transient, co-located with discrete auroral forms, and associated with strong field-aligned currents.

## Related Concepts

- [[F-Layer]] — sporadic-E can blank the ionosonde F-region trace
- [[Ionospheric Conductivity]] — sporadic-E layers dramatically enhance $\Sigma_P$ and $\Sigma_H$ locally
- [[Equatorial Ionosphere]] — Equatorial electrojet-related instabilities (Farley-Buneman) also produce E-region fine structure
- [[Aurora]] — auroral E-region ionization at high latitudes is functionally similar

## Sources

- [[Schunk Nagy 2009 Ionospheres]] (§11.13: metallic ion sporadic-E mechanism, wind-shear convergence, intermediate layers)
