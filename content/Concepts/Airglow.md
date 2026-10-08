---
type: concept
status: draft
updated: 2026-05-19
sources: 3
tags: [ionosphere, optics, airglow]
---

# Airglow

Faint optical emission from the upper atmosphere produced by chemical reactions and photochemical processes, as distinct from [[Aurora|auroral]] particle precipitation. Airglow can be dayglow, nightglow, or twilight glow depending on the solar illumination geometry. The most diagnostically useful channel for ionospheric F-region science is the 630.0 nm OI red line.

## 630 nm OI Red Line

### Production channels (Schunk & Nagy §8.7, Eqs 8.57–8.68)

Schunk & Nagy enumerate eight distinct O($^1$D) production channels, with rate expressions tied to the specific chemical pathway:

1. **O$_2^+$ + e dissociative recombination** (dominant nighttime): O$_2^+$ + e → O($^1$D) + O; rate $\alpha_2\cdot\beta_2^{1D}\cdot[O_2^+][e]$ where $\alpha_2 = 2.4\times10^{-7}(300/T_e)^{0.70}$ and branching fraction $\beta_2^{1D}$ ~1.1 (per Link & Cogger 1988).
2. **NO$^+$ + e dissociative recombination**: contributes a small fraction at altitudes where NO$^+$ is abundant.
3. **O$_2$ photodissociation** (dayside only): solar UV dissociates O$_2$ directly to excited products; important in upper mesosphere/lower thermosphere.
4. **Electron impact on O** (EI): O + e* → O($^1$D) + e; rate scales with superthermal electron flux; notable in auroral zones.
5. **O($^1$S) cascade**: O($^1$S) → O($^1$D) + photon (557.7 nm green line), providing a minor source.
6. **O + O + M three-body recombination**: O + O + M → O$_2$ → O($^1$D) + O; important in lower thermosphere at night.
7. **O$^+$ + e charge recombination**: very slow radiative process; negligible.
8. **Thermal O($^1$D) excitation by hot electrons**: thermal electrons above ~1000 K can excite O to $^1$D via inelastic scattering; captured by the Schunk & Nagy electron cooling rate (Eq 9.67).

**The O$_2^+$ dissociative recombination pathway dominates** at F-region altitudes at night, giving the VER formula below. On the dayside, channel 3 (O$_2$ photodissociation) becomes comparable.

The fraction of O$_2^+ + e$ reactions producing O($^1$D) is the metastable yield $\beta_{1D} \approx 1.1$ (Link & Cogger 1988).

### Loss — quenching and radiation

O($^1$D) is metastable with a radiative lifetime of $\tau \approx 110$ s. Three quenching processes compete with emission:

$$\text{O}(^1\text{D}) + \text{N}_2 \rightarrow \text{O}(^3\text{P}) + \text{N}_2 \quad\text{(rate }k_a\text{; dominant low-altitude quench)}$$
$$\text{O}(^1\text{D}) + \text{O}_2 \rightarrow \text{O}(^3\text{P}) + \text{O}_2 \quad\text{(rate }k_b\text{)}$$
$$\text{O}(^1\text{D}) + e \rightarrow \text{O}(^3\text{P}) + e \quad\text{(rate }k_c\text{)}$$

At F-region altitudes (~300 km) quenching is negligible and nearly all excited atoms emit. Below ~150 km almost all are quenched and no red-line emission reaches the ground.

### Volume emission rate (VER)

Assuming O$_2^+$ is in chemical equilibrium with $[\text{O}_2^+] = k_2[\text{O}^+][\text{O}_2]/(\alpha[e])$ (where $\alpha$ is the dissociative recombination rate and $k_2$ is the O$^+$ + O$_2$ interchange rate), the 630.0 nm VER is:

$$I_{630.0} = \frac{A_{630.0}}{A_{630.0}+A_{636.4}}\cdot\frac{A_{630.0}+A_{636.4}}{A_{630.0}+A_{636.4}+k_a[\text{N}_2]+k_b[\text{O}_2]+k_c[e]}\cdot\beta_{1D}\,\alpha\left[\text{O}_2^+\right][e]$$

which simplifies to:

$$I_{630.0} = \frac{A_{630.0}\,\beta_{1D}\,k_2[\text{O}_2]}{A_{630.0}+A_{636.4}+k_a[\text{N}_2]+k_b[\text{O}_2]+k_c[e]}[\text{O}^+]$$

The branching fraction $A_{630.0}/(A_{630.0}+A_{636.4}) = 0.76$. The second factor is the quenching survival fraction — strongly altitude-dependent because $[\text{N}_2]$ falls exponentially. At ~300 km the survival fraction $\approx 1$; at ~120 km it $\approx 0$.

### Altitude sensitivity — the Sojka ambiguity

Because both the O$_2$ production factor and the quenching survival fraction depend on neutral density, the 630 nm VER is highly sensitive to the altitude of the O$^+$ layer, not just its density. Sojka et al. (1997) demonstrated that modulating $h_{mF2}$ by $\pm 100$ km with **no change in $N_e$** changes the observed 630 nm column intensity by a **factor of four**. This has two critical implications:

1. A [[Polar Cap Patch|patch]] raised to anomalously high altitude via [[Lifting]] will appear *dim* in 630 nm even if its electron density is 2–3$\times$ the background — the airglow signature is suppressed by the reduced quenching and production efficiency at high altitude.
2. A patch at normal altitude will appear *bright* relative to a lifted patch of equal density.

The [[Lundquist Varney 2026]] L-type events (lifted, not necessarily dense) are therefore predicted to be dim or invisible in all-sky airglow surveys, even when present in the polar cap.

## Airglow patches vs electron density patches

Not equivalent categories:

| Event type | Electron density patch? | Airglow patch? |
|---|---|---|
| Dense, normal altitude | Yes | Yes (bright) |
| Dense, highly lifted | Yes | Possibly not (dim) |
| Normal density, altitude anomaly | No | Possibly yes (altitude-modulated brightness) |
| Hot patch (precipitation) | Yes | Bright (+ impact excitation) |

Ground-based airglow surveys therefore have a systematic selection bias against lifted structures, and an airglow-based patch catalog is **not interchangeable** with an electron density patch catalog. Comparison between [[RISR-N]] volumetric images and simultaneous all-sky 630 nm data is needed to calibrate this bias.

## 557.7 nm Green Line

Produced by the O($^1$S) $\rightarrow$ O($^1$D) transition (Figure 1.8 in Varney 2026 PatchesChapter). Radiative lifetime $\tau \approx 0.91$ s — two orders of magnitude shorter than the red line. The short lifetime prevents accumulation; green-line emission responds to nearly instantaneous local conditions rather than integrating a tall column. Primarily an E-region and lower thermosphere diagnostic rather than an F-region one.

## PMAFs and airglow patches

Poleward moving auroral forms (PMAFs) produce bright 630 nm enhancements at the dayside cusp from soft precipitation depositing energy at F-region altitudes. The precipitation creates ionisation that can persist for hours after the PMAF moves through. This newly created plasma then convects poleward as an airglow patch — technically a [[Polar Cap Patch|hot patch]] seeded by local production. Hosokawa et al. observed faint red-line enhancements propagating poleward from the brighter PMAF arcs, identifying these as ionisation patches seeded by the PMAF precipitation.

## Diagnostic use

- **Ground-based all-sky imagers at 630 nm:** Cameras at Resolute Bay, Longyearbyen, South Pole, and other polar sites detect [[Polar Cap Patch|patches]] and the [[Tongue of Ionization|TOI]] as brightness enhancements. Field of view typically ~1000 km diameter from 250 km altitude emission layer.
- **Inversion to $N_e$:** Under known $T_e$, neutral density profile, and absence of precipitation, the VER formula above can be inverted to $[\text{O}^+]$. Requires independent knowledge of $h_{mF2}$ (from ISR or ionosonde) to constrain the quenching survival fraction.
- **Dayglow:** Much brighter than nightglow due to direct UV photodissociation and photoelectron impact excitation. Key dayglow channels include OI 130.4 nm, 557.7 nm O($^1$S), and N$_2$ LBH UV bands.

## Related concepts

- [[F-Layer]] — VER peaks near $h_{mF2}$
- [[Polar Cap Patch]] — detected via 630 nm; distinction between airglow and electron density patches
- [[Lifting]] — $h_{mF2}$ changes modulate VER by a factor of four for fixed $N_e$
- [[Aurora]] — shares 630 nm wavelength via soft precipitation impact excitation; distinct from airglow chemistry
- [[Ionospheric Energetics]] — elevated $T_e$ modifies O$_2^+$ recombination rate and thus VER

## Excitation pathways beyond direct ionization

[[Gerard 1980 Optical F-region Processes]] establishes that polar F-region optical emission involves multiple excitation channels beyond direct precipitating-particle impact:

- **O$^+$($^2$P) and O$^+$($^2$D):** measured by Atmosphere Explorer C; excited via charge exchange with N$_2$ and by photoelectron impact; transitions contribute to 630 nm and 636 nm doublet lines.
- **N($^2$D):** excited by ion-atom interchange and dissociative recombination; but transported horizontally by neutral winds and $E\times B$ drifts by hundreds of km before emitting, complicating its use as a local production diagnostic.
- **O($^1$D) 630 nm:** primary nighttime source is dissociative recombination of O$_2^+$ (as in the standard VER formula); daytime source is additionally thermal electron impact, partially offset by N$_2$ and O quenching.

Quenching by atomic O is critical at F-region altitudes: whether excited states radiate or are collisionally de-excited depends sensitively on [O], which has significant latitudinal and storm-time variability.

## Sources

- [[Schunk Nagy 2009 Ionospheres]] (§8.7: O($^1$D) production channels Eqs 8.57–8.74; §9.7 Eq 9.67: O($^1$D) electron cooling rate)
- Varney 2026 PatchesChapter
- [[Gerard 1980 Optical F-region Processes]]
- [[Zou 2021 Polar Cap Density Structure Advances]]
