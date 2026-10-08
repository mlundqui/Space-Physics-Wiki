---
type: concept
status: mature
updated: 2026-10-07
sources: 3
---

# Ionospheric Energetics

The balance of heating and cooling processes that set the electron ($T_e$), ion ($T_i$), and neutral ($T_n$) temperature profiles in the ionosphere. $T_e > T_i > T_n$ in the F region under typical daytime conditions.

## Photoionization and Solar EUV (Schunk & Nagy Ch. 9)

**Chapman production function:** For a single absorber and monochromatic radiation at solar zenith angle $\chi$, the ionization production rate is:
$$P_c(z,\chi) = I_\infty \eta n(z) \sigma^a \exp[-H n(z) \sigma^a \sec\chi]$$
This peaks at the altitude $z_{max}$ where $\tau = Hn\sigma^a\sec\chi = 1$. At the peak: $P_c(z_{max}) = I_\infty \eta \cos\chi / (eH)$. The production rate increases toward the equator (decreasing $\chi$) and shifts upward with increasing $\chi$.

**EUVAC solar flux model:** Uses 37 wavelength intervals from 5–105 nm. Solar-activity scaling via:
$$I_i = F74113_i\left[1 + A_i(P - 80)\right], \qquad P = (F_{10.7} + \langle F_{10.7}\rangle)/2$$
Ionization frequencies (Table 9.2): for O, solar minimum $2.44\times10^{-7}$ s$^{-1}$, solar maximum $6.35\times10^{-7}$ s$^{-1}$ — a factor ~2.6 solar-cycle variation. The same factor modulates O$^+$ production rates and thus the polar wind H$^+$ flux.

**Photoelectron production rate** (Eq 9.24): altitude-, energy-, and zenith-angle-dependent, integrating over neutral species $s$, ion states $l$, and wavelengths up to the ionization threshold $\lambda_{si}$:
$$P_e(E,\chi,z) = \sum_l\sum_s n_s(z)\int_0^{\lambda_{si}} I_\infty(\lambda)\exp[-\tau(\lambda,\chi,z)]\sigma_s^i(\lambda)p_s(\lambda,E_l)\,d\lambda$$
where $p_s$ is the branching ratio for ion state $l$ at ionization energy $E_l$.

## Heating Sources

**Electrons:**
- **Photoelectron heating (dominant F-region source):** Primary ionization deposits ~10–20 eV in photoelectrons. The heating rate of thermal electrons from superthermal photoelectrons (S&N Eq 9.49):
$$Q_e(z) = \int_{E_T}^\infty \Phi_e(z,E)\left(\frac{dE}{dz}\right)_e dE$$
where $\Phi_e$ is the photoelectron flux and $(dE/dz)_e = \Sigma_e$ is the electron-electron stopping cross section (Eq 9.40). Ion heating primary source is *thermal electrons*, not photoelectrons, because the high photoelectron velocity gives a small Coulomb cross section.
- **EUV / solar UV photoionization**: produces photoelectrons with excess energy = $h\nu - E_{threshold}$. He II 30.4 nm (the strongest EUV line) carries 40.8 eV per photon. Ionizing ground-state O (13.6 eV) with it leaves a photoelectron of about 27 eV (less for excited O$^+$ states). *(Corrected 2026-10-07: this previously gave the photoelectron energy as ~41 eV, which is the photon energy.)*
- **Joule / ion frictional heating**: at high latitudes, elevated $T_i$ → $T_e$ energy transfer via Coulomb collisions; see [[Ion Frictional Heating]] and [[Joule Heating]]

**Ions:**
- Elastic collisions with hot electrons (electron → ion heat transfer)
- Ion frictional heating from ion-neutral collisions when $\mathbf{v}_i \neq \mathbf{v}_n$ (important in E-region; also drives [[Joule Heating]])
- Wave heating and Coulomb collisions

**Neutrals:**
- Ion-neutral frictional heating transfers momentum and energy to the thermosphere

## Cooling Processes

**Electrons — rotational excitation (dominant low altitude):**
$$L_e(N_2) = 3.5\times10^{-14}\,n_e n(N_2)(T_e - T_n)/T_e^{1/2} \quad\text{(Eq 9.50)}$$
$$L_e(O_2) = 5.2\times10^{-15}\,n_e n(O_2)(T_e - T_n)/T_e^{1/2} \quad\text{(Eq 9.51)}$$

**Electrons — vibrational excitation (important 200–400 km for T_e > 1000 K):**
N$_2$ vibration (10 vibrational levels; Eq 9.58) — complex temperature-dependent expression using polynomial coefficients (Tables 9.3–9.5).
O$_2$ vibration (Eq 9.60) — significant for $T_e > 2000$ K.

**Electrons — atomic oxygen processes (important F region and above):**
O fine structure (Eq 9.65): $L_e(O) = n_e n(O) D^{-1}\{S_{10}[1-\exp(98.9/T_e-98.9/T_n)] + S_{20}[\cdots] + S_{21}[\cdots]\}$; important when $T_e > T_n$ by ~hundreds of K.
O($^1$D) excitation (Eq 9.67): $L_e(O(^1D)) = 1.57\times10^{-12}\,n_e n(O)\exp[d(T_e-3000)/(3000T_e)]\cdot[\exp(-22713(T_e-T_n)/(T_eT_n))-1]$; significant above ~300 km.

**Electrons — high altitude:**
Coulomb collisions with ions (from 5-moment energy exchange term, Eq 4.124c) become dominant above ~400 km where neutral density is low. At high latitude, Figure 9.17 shows the electron cooling budget at 50° magnetic latitude (winter, medium solar activity, Kp=6): N$_2$ rotation dominates below 150 km; N$_2$ vibration peaks near 200 km; O fine structure and O($^1$D) excitation dominate 200–400 km; Coulomb collisions (e–i) become the leading term above ~500 km.

**Ions:**
- Elastic Coulomb collisions with electrons transfer electron thermal energy to ions (5-moment Eq 4.124c); the main ion heating mechanism at all but the highest latitudes
- Ion-neutral elastic collisions provide the dominant *cooling* of ions in the E and lower F region; this energy goes to neutrals (the Joule heating channel)
- Ion frictional heating (from high-speed convection) can reverse the usual $T_e > T_i > T_n$ ordering, driving $T_i$ well above $T_e$ in fast-convection regions; see [[Ion Frictional Heating]]

## Temperature Profiles

- **D region** (~60–90 km): $T_e \approx T_i \approx T_n$; high collision frequency forces tight coupling
- **E region** (~90–150 km): $T_e$ begins to separate; $T_i$ still $\approx T_n$
- **F region** (~150–1000 km): $T_e \gg T_n$; $T_i$ intermediate; classic elevated electron temperature layer
- **Topside**: $T_e$, $T_i$, $T_n$ all increase with altitude following the solar EUV gradient; $T_e$ can reach 3000–5000 K at solar maximum

## Heating Efficiency

Fraction of photoelectron energy converted to electron gas heat. Remaining fraction goes into: inelastic losses (N$_2$ excitation, ionization by superthermal electrons), escape along field lines.

$\eta \sim 0.05$ at low altitudes (mostly lost to N$_2$), increasing toward $\eta \sim 0.4$–$0.5$ in the topside F region.

## Airglow Connection

Inelastic collisions that excite metastable states (O($^1$D) at 630 nm, O$_2$ dayglow) produce [[Airglow]] emissions. The 630 nm emission rate (VER) is proportional to the quench-rate-limited O($^1$D) production rate.

## Related Concepts

- [[Ionospheric Conductivity]] — $T_e$ and $T_i$ affect collision frequencies
- [[Joule Heating]] — dominant high-latitude energy source; feeds back into $T_i$ and $T_n$
- [[Airglow]] — optical signature of inelastic cooling
- [[Ionosphere]] — parent concept

## Photoelectron Transport and the Nonlocal Heating Problem

In the low-latitude topside ionosphere, the primary source of electron heating is **not** locally produced photoelectrons — it is photoelectrons generated in the dense F-regions (~200–400 km) and transported upward along magnetic field lines. [[Varney 2012 Thesis]] establishes this through SAMI2-PE, a model extending [[SAMI2]] with a full Boltzmann-Fokker-Planck solver for the photoelectron distribution function $\Phi(\ell, \mathcal{E}, \mu)$.

**Key physics:**
- Photoelectrons are produced by EUV photons (brightest line: He II 30.4 nm → 41 eV photoelectrons). At high altitudes the neutral density is too low for significant local production.
- Transport to the topside is governed by parallel streaming, the magnetic mirror force (which preferentially allows high-$\mu$ electrons to escape), and energy loss via Coulomb collisions with thermal electrons ($L(\mathcal{E})$).
- The heating rate at topside altitudes is thus a nonlocal integral over the production and loss of photoelectrons across the entire conjugate field line — sensitive to N_e distributions in both F-regions.

**Why SAMI2 fails at low latitudes:** SAMI2's empirical heating parameter $C_{qe}$ assumes a fixed attenuation of the local heating rate. Because the real process is nonlocal, no single $C_{qe}$ can correctly reproduce T_e at all altitudes simultaneously. SAMI2-PE eliminates this failure, reproducing JRO T_e to within ~30% throughout the day (reference day March 25, 2009).

**T_e feedback mechanism:** Neutral winds and $E\times B$ drifts set F-region N_e via the fountain effect, meridional wind lifting/lowering, and recombination altitude. Reduced F-region N_e allows more photoelectrons to escape to the topside (fewer thermal electrons to absorb energy en route), increasing the topside heating rate per thermal electron. The net result: lower F-region N_e → higher topside T_e, lower topside thermal energy density. This is the mechanism by which climatological uncertainties in winds (±factor of 2) or electric fields (±25%) drive >30% errors in topside T_e.

**Equatorial arc shadows:** In the afternoon, the EIA arcs at ±15° MLAT absorb photoelectrons transiting between hemispheres, creating local minima in the upward flux. These manifest as a T_e inflection near 800 km in the afternoon — a directly observable signature of nonlocal transport geometry.

**N($^2$D) quenching (lower F-region):** At ~240 km, quenching of metastable N($^2$D) by NO$^+$ is the dominant electron heat source, changing T_e by >50% relative to no-quenching runs. This process scales with neutral NO density, which is poorly constrained by current empirical models.

**Day-to-day variability (open problem):** JRO observations on 6 consecutive quiet days (July 8–13, 2008) show ~500 K day-to-day T_e differences at 1370 km. SAMI2-PE with climatological drivers is nearly identical from day to day. Day-to-day variations in the $E\times B$ vertical drift (estimable from ΔH magnetometer data) and meridional neutral winds (not yet measurable without an ionosonde chain off-equator) are the leading candidates.

## Related Concepts (added)

- [[Ion Frictional Heating]] — direct ion heating mechanism at high latitudes; can exceed photoelectron contribution locally
- [[Airglow]] — O($^1$D) excitation is both a cooling channel for electrons and the production channel for 630 nm emission

## Derivations

- [[Chapman Layer]] — derivation of the Chapman production function and α-Chapman layer

## Sources

- [[Schunk Nagy 2009 Ionospheres]] (Ch. 9: photoionization, photoelectron transport, electron/ion heating and cooling rates)
- [[Varney 2012 Thesis]] (nonlocal photoelectron transport at low latitudes)
- AOS 205B course materials
