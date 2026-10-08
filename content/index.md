---
type: meta
updated: 2026-10-07
---


# Wiki Index

Catalog of every wiki page, grouped by type. The LLM updates this on every ingest. When answering a query, read this file first to locate relevant pages, then drill into them — only fall back to the raw PDFs in `Atlas/Papers/` or `Atlas/Textbooks/` when the wiki is insufficient.

## Dashboard

- dashboard — live Dataview tables: concepts by status, entity list, source bibliography, stubs needing work, recently updated. **Requires Dataview community plugin.**

## Overview

- [[overview]] — evolving research synthesis. Current synthesis after 59 sources: D/L/LD event taxonomy (Lundquist 2026 core finding); confirmed ring current → SAPS → SED → TOI → patch storm pathway; 4 patch formation mechanisms + non-classic transport; storm preconditioning; upflow density-controls-flux result; IPWM/GITM/E-CHAIM/MAGE modeling landscape; Decadal Survey ITM priorities; 7 prioritized open questions.

## Entities

- [[RISR-N]] — Resolute Bay Incoherent Scatter Radar, North Face. Polar-cap ISR, operating since 2009; volumetric 3-D patch imaging capability.
- [[AMISR]] — family of phased-array ISR instruments (RISR-N/C, PFISR, …).
- [[E-CHAIM]] — empirical climatological model ≥50°N MGLAT; sub-models for NmF2, hmF2, topside (NeQuick g=0.18), bottomside; AACGM coordinates; AE/PC/F10.7/IG12 driven.
- [[IPWM]] — Ionosphere Polar Wind Model; 3-D first-principles 8-moment ion transport; 78-cell flux-tube grid 97–8400 km; van Leer finite-volume horizontal transport.
- [[GITM]] — Global Ionosphere-Thermosphere Model; 3-D fluid simulation ~100–700 km; SED plume backtracing, patch cutting simulations.
- [[OMNI]] — NASA solar-wind and geomagnetic-index data service.
- [[pySPEDAS]] — Python heliophysics data-analysis toolkit; used to query OMNI.
- [[SuperDARN]] — global HF coherent-scatter radar network; ionospheric convection maps and HF backscatter from patch irregularities.
- [[FAST]] — Fast Auroral SnapshoT explorer (350–4175 km); auroral acceleration region; three FAC regions; dispersive Alfvén wave statistics (Chaston 2003, 2007).
- [[DMSP]] — LEO satellite constellation at 840 km; in-situ ion density, temperature, drift; hot/cold patch classification.
- [[MAGE]] — Multiscale Atmosphere Geospace Environment coupled model; GAMERA (MHD) + RCM + REMIX + TIEGCM; localized Joule heating and TAD generation.
- [[THEMIS]] — five-spacecraft NASA constellation; fluxgate magnetometers (FGM) covering 1–30 R_E; substorm onset timing; solar wind upstream monitoring.
- [[Van Allen Probes]] — twin RBSP spacecraft (2012–2019); EMFISIS instrument suite (MAG + WFR + HFR); radiation belt wave and field measurements.
- [[SAMI2]] — NRL 2-D dipole-grid ionosphere-plasmasphere model; 7 ion species; 5-moment fluid; SAMI2-PE extension adds Boltzmann-Fokker-Planck photoelectron transport (Varney 2012 thesis).
- [[Jicamarca Radio Observatory]] — world's largest ISR; Lima, Peru; dip equator; full-profile T_e/T_i mode; reference observatory for low-latitude ionospheric energetics.

## Concepts

- [[Ionosphere]] — partially ionized upper atmosphere; D/E/F regions; medium for HF propagation.
- [[F-Layer]] — F region; N_mF2 at h_mF2; Chapman production function; chemistry-transport competition; plasma scale height; diffusive equilibrium in topside.
- [[Polar Cap Patch]] — mesoscale F-region density enhancements (>~2× background) inside the polar cap; formation taxonomy, hot/cold classification, GDI instability, radio effects.
- [[Tongue of Ionization]] — planetary-scale dayside-to-nightside plasma channel; parent structure of patches; geospace plume connection.
- [[Polar Holes]] — polar cap density depletions opposite to patches; stagnant-cell and localized-loss formation.
- [[Lifting]] — vertical raising of F-region plasma; slows recombination; vertical ExB drift component in dipole; central to SED and LD-event interpretation.
- [[Dungey Cycle]] — magnetospheric convection cycle whose ionospheric projection is the two-cell polar convection pattern.
- [[Storm-Enhanced Density]] — sub-auroral storm-time F-region density enhancement; positive (lifting) vs negative (N2 expansion) storm effects; plume-feeds the TOI.
- [[High-Speed Streams]] — fast solar wind from coronal holes; CH/HSS-driven activity is geomagnetically active without strong negative Bz.
- [[Atmospheric Escape]] — Jeans escape, hydrodynamic escape, and non-thermal loss mechanisms; governs long-term atmospheric evolution.
- [[Ion Upflow]] — Type 1 (frictional) vs Type 2 (ambipolar/precipitation) O⁺ upflow; flux table; density-limited flux; links to patches, SED, NEIALs, LD events.
- [[Polar Wind]] — supersonic H⁺ outflow on open polar cap field lines; ambipolar-driven transonic solution above ~2500 km; propagating polar wind jets above patches.
- [[Ionospheric Energetics]] — EUV/photoelectron heating, elastic/inelastic cooling, and T_e/T_i/T_n profiles in the ionosphere.
- [[Ionospheric Conductivity]] — Pedersen, Hall, and parallel conductivities; height-integrated conductances Σ_P, Σ_H; κ_i parameter.
- [[Ionospheric Dynamo]] — electrostatic convection mapping, master equation, CPCP, two-cell convection pattern.
- [[Joule Heating]] — Ohmic dissipation Q_J = Σ_P|E+u_n×B|²; neutral-frame correction; dominant high-latitude thermospheric energy source.
- [[Field-Aligned Currents]] — Birkeland currents, Region 1/2 system, substorm current wedge, Knight relation for parallel acceleration.
- [[Aurora]] — particle precipitation, ionization, optical emissions, Robinson conductance parameterization, discrete vs. diffuse aurora.
- [[Ionospheric Instabilities]] — Farley-Buneman, gradient-drift, and Rayleigh-Taylor instabilities; coherent scatter, GPS scintillation, and NEIALs.
- [[NEIALs]] — Naturally Enhanced Ion Acoustic Lines; non-thermal ISR coherent scatter from auroral plasma instabilities; Type 1 (Langmuir decay) vs Type 2 (ion-ion streaming); strong magnetic aspect angle dependence.
- [[Ring Current]] — westward toroidal current in the inner magnetosphere; energetic H⁺/O⁺/electrons; gradient/curvature drifts; controls SAPS and Region-2 FAC geometry during storms.
- [[Subauroral Polarization Streams]] — SAPS; fast westward ion drift in low-conductance sub-auroral gap; primary dusk-side plasmasphere erosion and TEC trough mechanism; driven by Region-2 current closure.
- [[Equatorial Ionosphere]] — equatorial electrojet, EIA/Appleton anomaly, pre-reversal enhancement, equatorial plasma bubbles, Rayleigh-Taylor instability derivation, F₃ layer, nonmigrating tides.
- [[Ionospheric Storms]] — positive/negative phase mechanisms; SAPS→SED→TOI→patch storm pathway; PPEF effects; composition changes; storm-time TIDs.
- [[Sporadic E]] — metallic ion wind-shear convergence (Fe⁺, Mg⁺); 0.6–2 km thickness; intermediate layers; ionosonde signatures.
- [[Magnetotail]] — lobes, plasma sheet, Harris current sheet, energy storage and substorm loading/unloading.
- [[MHD]] — frozen-in flux, generalized Ohm's law, plasma β, CGL double-adiabatic, Parker spiral, Alfvén/magnetosonic wave modes.
- [[Ambipolar Diffusion]] — plasma scale height H_p = k_B(T_e+T_i)/m_i g; diffusion along B; cross-field suppression; minor ion force balance; polar wind kinematic origin.
- [[Ion Frictional Heating]] — T_i elevation from E×B ion-neutral relative drift; T_eff enhancement of O⁺ chemistry rate coefficients (×16 for 2× E-field); patch cutting mechanism.
- [[Airglow]] — 630 nm O(¹D) VER formula; Sojka factor-of-4 altitude ambiguity; airglow patches vs electron density patches.
- [[Radiation Belts]] — trapped particles, adiabatic invariants (μ,J,Φ), L-shell, ring current, inner/outer belt structure.
- [[Plasma Waves]] — whistler, chorus, EMIC, upper/lower hybrid, ion acoustic waves; cold plasma Stix formalism; two-stream instability; double layers; S&N Ch. 6 full dispersion relations.
- [[Wave-Particle Interactions]] — Landau and cyclotron resonance, pitch-angle diffusion, Fokker-Planck equation, Kennel-Petschek theory.
- [[Alfvén Waves]] — shear Alfvén mode; two-fluid derivation of kinetic ($\rho_s$) and inertial ($\lambda_e$) Alfvén waves; $E_\parallel/E_\perp$; Landau-resonant electron acceleration; propagation from plasma sheet to ionosphere; contrast with chorus.
- [[Auroral Acceleration]] — diffuse (chorus scattering) vs. monoenergetic/inverted-V (quasi-static $\Phi_\parallel$, Knight relation) vs. broadband (Alfvénic $E_\parallel$); comparison table.
- [[Synchrotron Radiation]] — relativistic electron radiation in B field; Larmor formula, beaming, synchrotron spectrum; planetary belt diagnostics.
- [[Traveling Atmospheric Disturbances]] — propagating neutral thermospheric waves from high-latitude Joule heating; equatorward propagation; constructive intersection at low latitudes; drive TIDs.
- [[Magnetic Coordinate Systems]] — eight systems reviewed: CD/MAG, ED, dip, GSM, SM, QD, MA, CGM/AACGM; non-orthogonal systems (QD/MA/AACGM) require covariant/contravariant base vectors for correct E/J/v mapping.
- [[HF Radio Propagation]] — Appleton-Hartree refractive index, Haselgrove ray tracing (HASEL), O/X modes, MUF, patch-enhanced SuperDARN backscatter, polar latitude HF scintillation.

## Derivations

Griffiths-style derivations of core results with commentary between steps. SI units; each page records its verification. Reading path: [[Derivations Index]].

- [[Derivations Index]] — curriculum and reading order; planned and flagged derivations
- [[Debye Shielding and the Plasma Frequency]] — $\omega_p$ from linearized cold fluid; $\lambda_D$ from Boltzmann response and Poisson; $\lambda_D\omega_{pe}=v_{th}$; plasma parameter
- [[Guiding-Center Drifts]] — gyration; master drift $\mathbf{F}\times\mathbf{B}/qB^2$; $\mathbf{E}\times\mathbf{B}$, gravity, $\nabla B$, curvature, polarization drifts; dipole drift period
- [[Adiabatic Invariants and Magnetic Mirrors]] — $\mu$ (betatron and mirror proofs), mirror force, dipole loss cone, $J$ and bounce period, $\Phi$, timescale hierarchy
- [[Moment Equations from the Vlasov Equation]] — Boltzmann/Vlasov; general moment equation; continuity, momentum, energy; closure table (cold → 8/13/16-moment)
- [[Ideal MHD from Kinetic Theory]] — single-fluid sums; quasi-neutrality; magnetic pressure and tension; generalized Ohm's law with ordering; frozen-in theorem (both parts)
- [[MHD Wave Modes]] — linearized MHD matrix; shear Alfvén, fast and slow dispersion; pressure phase; naming conventions
- [[Landau Damping]] — linearized Vlasov–Poisson; Landau contour; weak-damping rate and its textbook variants checked against exact $Z$-function roots; ion-acoustic damping
- [[Quasilinear Diffusion]] — 1-D QL theory (plateau, conservation, factor-2 wave energy, verified numerically); cyclotron resonance; bounce-averaged pitch-angle diffusion; weak and strong diffusion lifetimes
- [[Knight Relation]] — kinetic $j_\parallel(\Phi)$ for upward FACs; $j_0$, $K = e^2n/\sqrt{2\pi m_ek_BT}$; reconciles the wiki's three conflicting forms
- [[Kennel-Petschek Limit]] — self-limiting trapped electron flux; SI derivation; KP vs Summers values; strong vs weak diffusion
- [[Incoherent Scatter Spectrum]] — dressed-particle spectrum (Swartz & Farley / Varney 2012); ion and plasma lines; $T_e/T_i$, composition, drift; theory variants
- [[Chapman Layer]] — production function, α-Chapman layer, β-type loss, F2-peak condition $\beta\approx D/H_{\rm O}^2$ (numerically verified)
- [[Plasma Diffusion Along B]] — ambipolar field, plasma and minor-ion scale heights, ambipolar diffusion equation (after AOS 205B Lecture 3.2 and S&N Ch. 5)
- [[Pedersen and Hall Conductivity]] — mobility tensor, κ = Ω/ν, conductivity tensor (Pedersen/Hall/parallel), Hall-sign conventions, conductances, general drifts (after AOS 205B Lecture 6.1)
- [[Frictional and Joule Heating]] — frictional $T_i$, $T_{\rm eff}$, neutral heating $=\sigma_P|\mathbf{E}'|^2$, Poynting theorem and M–I energy flow, heat vs. ion-drag work (after AOS 205B Lecture 8.1)
- [[Electrostatic Dynamo Equation]] — current closure → dynamo PDE; Cowling channel; height-integrated 2-D form (sign verified both hemispheres); convection and arc examples (after AOS 205B Lecture 6.2)
- [[Gradient-Drift and Rayleigh-Taylor Instabilities]] — GDI (patch trailing edges, γ = E′/BL) and RT (equatorial spread F, γ = g/ν_in L) as one instability; exact dispersion verified (after AOS 205B Lecture 10.2, Kelley Ch. 4, 6)
- [[Polar Wind Transonic Outflow]] — Mach equation along a flux tube (S&N §5.8), critical solution, sonic radii, O$^+$ bound vs H$^+$ escape, flux limiting
- [[Appleton-Hartree Equation]] — magneto-ionic refractive index (Davies §2.3), O/X cutoffs, ionogram splitting; verified against Stix to 1e-11
- [[Parker Solar Wind and Spiral]] — static-corona argument; transonic Mach equation (A ∝ r²); Lambert-W solution; Parker 1958 speeds reproduced; spiral as exact ideal-MHD solution; spiral-angle conventions
- [[Rankine-Hugoniot Jump Conditions]] — pillbox jumps; coplanarity and de Hoffmann–Teller; gas-dynamic and perpendicular MHD shocks; 4× limit; flags 200C Eq. 6.15 erratum
- [[Chapman-Ferraro Standoff Distance]] — image dipole; stagnation factor K ≈ 0.88; $R_{mp}\propto(\rho u^2)^{-1/6}$, a = 2.44; agrees with Shue 1998 within 0.3 R_E; bow-shock standoff
- [[Sweet-Parker Reconnection]] — $S^{-1/2}$ rate from three conservation laws; exact Dawson annihilation solution; why SP fails in space; Petschek/Hall/plasmoid summary
- [[Dessler-Parker-Sckopke Relation]] — drift (−3) and magnetization (+1) fields; ΔB/B₀ = −(2/3)W/W_mag; Dst ↔ ring-current energy; Earth-induction factor
- [[Cold-Plasma Waves]] — Stix dielectric tensor; $An^4-Bn^2+C$; cutoffs/resonances; lower-hybrid limits; whistler $v_g$, nose $f_{ce}/4$, Storey 19.47°
- [[Dipole Field and L-Shells]] — dipole field and field lines; invariant latitude; 3/r gradient and curvature; flux-tube area and $L^4$ volume; open flux vs polar-cap boundary

## People

- [[Michael Lundquist]] — user; PhD student, UCLA AOS.
- [[Roger Varney]] — advisor; UCLA AOS.

## Sources

- [[Lundquist Varney 2026]] — *A Statistical Survey of F2 Layer Peak Properties in the Polar Cap Ionosphere Observed by RISR-N.* Lundquist & Varney, JGR Space Physics, 2026. The wiki's first ingested source.
- Varney 2026 PatchesChapter — *Polar Cap Patches and High-Latitude Plasma Density Structures.* Varney, book chapter, 2026. Comprehensive review of patch physics, formation, instabilities, and radio consequences.
- [[Varney 2014 IPWM Supplement]] — *Supplemental Details on IPWM.* Varney, Wiltberger, Lotko, 2014. Equations, coordinate system, and numerical implementation of the 3-D IPWM.
- [[Varney 2021 ISR Probability]] — *Probability Theory for Incoherent Scatter Radar.* Varney, 2021 (lecture notes). Probabilistic foundations of ISR signal processing; ACF, PSD, complex covariance.
- [[Themens 2018 ECHAIM Primer]] — *The Empirical Canadian High Arctic Ionospheric Model (E-CHAIM) Primer.* Themens et al., 2018. User manual for E-CHAIM covering architecture, modes, error flags.
- [[David 2016 TEC Survey]] — *Polar Cap Patches and the Tongue of Ionization: A Survey of GPS TEC Maps from 2009 to 2015.* David et al., GRL 2016. 7-year observational confirmation of UT/seasonal patch dependence; rules out non-solar plasma sources.
- [[Zou Ridley 2015 GITM Backtracer]] — *Modeling of the Evolution of the SED Plume during the 24–25 October 2011 Geomagnetic Storm.* Zou & Ridley, book chapter 2015. GITM backtracer showing multi-sector plasma origins and hmF2–TEC origin diagnostic.
- [[Thayer Semeter 2004 Energy Flux]] — *The Convergence of Magnetospheric Energy Flux in the Polar Atmosphere.* Thayer & Semeter, JASTP 2004. Poynting flux framework; energy partitioning (94% Joule heat); EM vs KE vs VUV budget.
- [[Thayer Coleman 2026 Vertical Winds]] — *Resolving Thermospheric Vertical Wind Ambiguities and Energy Processes.* Thayer & Coleman, Front. Astron. Space Sci. 2026. Divergent vs lifting wind decomposition; FPI airglow ambiguity; TIEGCM adiabatic heating.
- [[Foster 2020 Geospace Plume]] — *Multi-Point Observations of the Geospace Plume.* Foster et al., book chapter 2020. Unified picture of SED→plasmaspheric plume→magnetopause reconnection; 17 March 2015 storm case.
- [[Zou 2021 SED Ion Upflow]] — *Impact of Storm-Enhanced Density on Ion Upflow Fluxes During Geomagnetic Storms.* Zou et al., Front. Astron. Space Sci. 2021. Type 1/2 upflow classification; density as rate-limiting control; peak flux 3×10^14 m⁻² s⁻¹ when SED meets cusp precipitation.
- [[Themens 2024 May Storm]] — *The High Latitude Ionospheric Response to the Major May 2024 Geomagnetic Storm: A Synoptic View.* Themens et al., GRL 2024. Extreme SED lifting (hmF2 to 630 km); IT preconditioning suppresses Day-2 patches; Sporadic-E at SAPS boundary; NEIALs at PFISR.
- [[Pham 2022 TADs]] — *Thermospheric Density Perturbations Produced by Traveling Atmospheric Disturbances During August 2005 Storm.* Pham et al., JGR 2022. MAGE vs WEIMER; localized Joule heating structure drives TAD generation; bi-hemispheric TAD intersection explains low-latitude density peaks.
- [[Blelly Schunk 1993 Moment Comparison]] — *A Comparative Study of the Time-Dependent Standard 8-, 13- and 16-Moment Transport Formulations of the Polar Wind.* Blelly & Schunk, Ann. Geophysicae 1993. Standard model overestimates F₂ peak by ×6; 8-moment optimal; 13-moment unstable in collisionless regime.
- [[Laundal Richmond 2016 Magnetic Coordinates]] — *Magnetic Coordinate Systems.* Laundal & Richmond, Space Sci Rev 2017. Reference definitions for CD, ED, dip, GSM, SM, QD, MA, CGM/AACGM; base vectors for non-orthogonal systems; MLT definition; secular variation.
- [[Akbari 2014 NEIAL Aspect Angle]] — *Aspect Angle Dependence of Naturally Enhanced Ion Acoustic Lines.* Akbari & Semeter, JGR Space Physics 2014. PFISR multibeam; Type 1 vs Type 2 NEIAL classification; Type 2 vanish at > 2° from **B** above F-region peak.
- [[Bao 2023 Geospace Plume MAGE]] — *The Relation Among the Ring Current, Subauroral Polarization Stream, and the Geospace Plume.* Bao et al., JGR Space Physics 2023. MAGE simulation of 31 March 2001 superstorm; electrodynamic linkage of plasmaspheric and ionospheric plumes; ring current → SAPS → plume causality.
- [[Dickinson Geisler 1968 Thermospheric Vertical Motion]] — *Vertical Motion Field in the Middle Thermosphere from Satellite Drag Densities.* Dickinson & Geisler, MWR 1968. Foundational w = w_D + w_L decomposition; adiabatic heating comparable to solar radiation; parent paper for Thayer 2026 ambiguity problem.
- [[Coleman 1992 Ionospheric Ray Tracing]] — *A General Purpose Ionospheric Ray Tracing Procedure.* Coleman, DSTO 1993. HASEL FORTRAN subroutine; Haselgrove ODEs; Appleton-Hartree; RKF integration; HF propagation and SuperDARN ray-path modeling.
- [[Auster 2007 THEMIS FGM]] — *The THEMIS Fluxgate Magnetometer.* Auster et al., SSR 2008. THEMIS FGM instrument description; 0.01 nT sensitivity; substorm onset measurements.
- [[Vasquez 2020 Van Allen Probe FGM Calibration]] — *Flight Calibration of the Van Allen Probe Magnetometers.* Vasquez et al., ApJS 2020. Spin-based flight calibration for RBSP/EMFISIS magnetometer; bias, gains, orthogonality, alignment.
- [[Kletzig 2013 EMFISIS]] — *EMFISIS on RBSP.* Kletzig et al., SSR 2013. Instrument description for MAG + WFR + HFR on Van Allen Probes; radiation belt science objectives.
- [[Kletzig 2023 EMFISIS Science]] — *EMFISIS: Science, Data, and Usage Best Practices.* Kletzig et al., SSR 2023. Post-mission science synthesis; ULF/chorus/hiss/EMIC results; WNA and density data guidance.
- [[Parker 1958 Solar Wind]] — *Dynamics of the Interplanetary Gas and Magnetic Fields.* Parker, ApJ 1958. Foundational solar wind prediction; transonic outflow from hot corona; Parker spiral; parent of polar wind concept.
- [[Lundquist 1951 Flux Rope Stability]] — *On the Stability of Magneto-Hydrostatic Fields.* Lundquist, Phys Rev 1951. Force-free cylindrical flux rope (Lundquist field); kink instability criterion; foundational for CME and magnetotail flux rope physics.
- [[Pierrard 2001 Solar Wind Electrons]] — *Core, Halo and Strahl Electrons in the Solar Wind.* Pierrard et al., Astrophys Space Sci 2001. Three-component electron VDF; kinetic Fokker-Planck model; strahl halo isotropy problem.
- [[Davies 1966 Ionospheric Radio Propagation]] — classic HF propagation text; §2.3 magneto-ionic theory.
- [[Decadal Survey 2024]] — *The Next Decade of Discovery in Solar and Space Physics.* National Academies, 2024. Community priorities 2024–2033; GDC/DYNAMIC top ITM mission; HF propagation forecast; DASHI ground-based priority. Reviewed by Varney.
- [[Crowley 1993 Critical Review Patches Blobs]] — *A Critical Review of Patches and Blobs.* Crowley, Radio Science 1996. Foundational patch/blob taxonomy; patch ≥2×background ≥100 km inside polar cap; blob subtypes; source = dayside solar EUV via cusp/throat.
- [[Bahcivan 2010 Initial RISR-N Observations]] — *Initial RISR-N Observations.* Bahcivan et al., GRL 2010. First RISR-N science: Bz ≥5 nT threshold; 25–75 min delays; altitudinally smooth profiles = solar-produced; ~25 km substructures.
- [[Zou 2021 Polar Cap Density Structure Advances]] — *Advances in Polar Cap Density Structures.* Zou et al., Geophysical Monograph 260 Ch.4, 2021. Te ~380K lower in patches; downward ion fluxes at 840 km; RISR-C −42% dayside→nightside; hot patch mechanisms; 630nm formula.
- [[Gilles 2018 RISR SuperDARN Velocity Comparison]] — *RISR-N/SuperDARN Velocity Comparison.* Gilles et al., Radio Science 2018. SuperDARN ~75–85% of RISR before refractive-index correction; agree after; E-region contamination in daytime SuperDARN.
- [[Larson 2023 E-CHAIM vs RISR]] — *E-CHAIM Validation against RISR-N.* Larson et al., Adv Space Res 2023. Ratio ~1 at F2 peak; underestimates topside/bottomside ~10–20%; fails at extreme densities and hmF2.
- [[Foster 2004 Multiradar TOI]] — *Multi-Radar Observations of the Tongue of Ionization.* Foster et al., JGR 2005. 20 Nov 2003 super-storm; SED>150 TECu; complete SED→TOI chain; F-peak >1.5×10^12 m^-3; O+ upflow >10^13 m^-2 s^-1.
- [[Zhang 2016 Patch Transport Beyond Classic]] — *Polar Cap Patch Transport Beyond Classic.* Zhang et al., JGR Space Physics 2016. SAPS segmentation → patch stagnation in lobe reverse convection cell during northward IMF → rapid decay.
- [[Chartier 2017 Swarm Patch Occurrence]] — *Swarm Patch Occurrence Statistics.* Chartier et al., JGR Space Physics 2018. December maximum in BOTH hemispheres from all 3 Swarm satellites; annual ionospheric asymmetry; current theory "at least incomplete."
- [[Diaz Pena 2021 Auroral Heating Patches]] — *Auroral Heating Hot Patch Mechanism.* Diaz Peña et al., JGR Space Physics 2021. RISR-N volumetric imaging + GEMINI; hot patch from auroral E-region heating + upward diffusion, not direct F-region ionization.
- [[Milan Grocott 2021 High Latitude Convection]] — *High-Latitude Convection and the Dungey Cycle.* Milan & Grocott, Geophysical Monograph 260 Ch.2, 2021. ECPC model; CPCP 30–100 kV; R1/R2 FACs; substorm cycle embedded in Dungey cycle.
- [[Albarran 2023 N+ Polar Wind MAGE]] — *N+ in the Polar Wind: HIDRA in MAGE.* Albarran et al., JGR Space Physics 2024. HIDRA = IPWM successor; N+ chemistry bug fixed (rate 100× too high); N+ ~10–14% O+ quiet-time; 50–100% storm-time. Varney PI.
- [[Kennel 1966 Limit Stably Trapped Fluxes]] — *Limit on Stably Trapped Particle Fluxes.* Kennel & Petschek, JGR 1966. Original K-P limit paper; self-regulating wave-particle feedback; strong vs weak diffusion; electrons >40 keV near limit at L ≤ 12.
- [[Perry 2021 SuperDARN Poynting Flux]] — *SuperDARN Radar Poynting Flux Model.* Perry et al., Radio Science 2022. Saskatoon SuperDARN Poynting flux profile by ray tracing; great-circle validated via CASSIOPE/RRI; E vs F region echo discrimination.
- [[Xiong 2020 FACs Precipitation DMSP]] — *FACs and Precipitation: DMSP Statistics.* Xiong et al., Earth Planets Space 2020. R2 co-located with particle flux peaks; R1 displaced ~3.5° from dawn-side precipitation; FAC peaks bracket auroral zone.
- [[Claudepierre 2022 Radiation Belt Losses]] — *Radiation Belt Electron Loss at L < 4.* Claudepierre et al., JGR Space Physics 2022. Coulomb drag critical at L ≤ 2; LGW improves agreement at L≈1.8–3.2; plasmaspheric density model dominates uncertainty.
- [[Gerard 1980 Optical F-region Processes]] — *Optical F-Region Processes in the Polar Atmosphere.* Gérard, book chapter 1980. O+(2P)/(2D), N(2D), O(1D) excitation/quenching from AE-C; N(2D) transport displaces morphology by hundreds of km.
- [[Agapitov 2011 THEMIS Chorus Waves]] — *Forward and Reflected Chorus Waves Captured by THEMIS.* Agapitov et al., Ann. Geophys. 2011. Reflected chorus attenuation 10-30×; 10% frequency shift; ray tracing confirms equatorial source at L≥8.
- [[Olifer 2023 KP Self-Limiting Precipitation]] — *Intense Electron Precipitation from K-P Self-Limiting.* Olifer et al., GRL 2023. 70 storms superposed epoch; K-P flux capping drives intense precipitation; dawn-side injections exceed K-P limit; asymptotic flux ~5×10^3 cm^-2 s^-1 sr^-1 keV^-1 at L=4.5.
- [[Summers 2009 Relativistic KP Limit]] — *Limit on Stably Trapped Particle Fluxes in Planetary Magnetospheres.* Summers, Tang & Thorne, JGR 2009. Fully relativistic K-P extension; marginal stability replaces wave-reflection criterion; compared to Earth, Jupiter, Uranus observations.
- [[Treumann 2002 Auroral Electrodynamics]] — *Auroral Plasma Physics, Chapter 6: Electrodynamics of Auroral Forms.* Treumann et al., Space Sci Rev 2002. Discrete arcs, WTS, Omega Bands, Auroral Streamers, polar cap aurora; FAC closure through Pedersen/Hall conductance.
- [[Artemyev 2008 Harris Current Sheet]] — *Evolution of a Harris Current Sheet in an Electric Field.* Artemyev, Moscow Univ. Phys. Bull. 2008. Vlasov-Maxwell simulation; CS compression to ion Larmor radius; charge separation and ambipolar field; substorm tail thinning.
- [[Carlson 2001 FAST Plasma Instrument]] — *Electron and Ion Plasma Experiment for FAST.* Carlson et al., Space Sci Rev 2001. FAST satellite plasma analyzer; 360° FOV; 4 eV–32 keV; sub-second time resolution; auroral particle acceleration and wave-particle interactions.
- [[Rietsch 1977 Maximum Entropy Inverse Problems]] — *Maximum Entropy Approach to Inverse Problems.* Rietsch, J. Geophys. 1977. MEM spectrum from autocovariance; Earth density inversion; linear constraint formalism; equivalent to Burg MEM.
- [[Sun 2020 TEC Matrix Completion]] — *Matrix Completion Methods for TEC Video Reconstruction.* Sun et al., submitted to Ann. Appl. Stats. 2020. VISTA algorithm reconstructs missing Madrigal TEC maps (~50% missing); preserves mesoscale structures; temporal smoothing + auxiliary data.
- [[Tsurutani 2013 PPEF Ionosphere Comment]] — *Comment on Rishbeth et al. (2010).* Tsurutani et al., Ann. Geophys. 2013. PPEF superfountain effect explains displaced EIA peaks (±22–30° MLAT, 270 TECu) during Halloween 2003 superstorm; SAMI2 confirmation.
- [[Gallardo-Lacourt 2018 STEVE Statistics]] — *A Statistical Analysis of STEVE.* Gallardo-Lacourt et al., JGR Space Physics 2018. 28 events; STEVE ~20 km wide, >2000 km long; sub-auroral; occurs ~1 hr after substorm onset; not conventional particle precipitation.
- [[Varney 2012 Thesis]] — *Photoelectron Transport and Energy Balance in the Low-Latitude Ionosphere.* Varney, Cornell PhD dissertation, 2012. Develops SAMI2-PE; establishes nonlocal topside T_e heating mechanism; validates against JRO full-profile T_e data.
- [[Schunk Nagy 2009 Ionospheres]] — *Ionospheres: Physics, Plasma Physics, and Chemistry* (2nd ed.). Schunk & Nagy, Cambridge University Press, 2009. Primary graduate textbook: full moment hierarchy (13-moment/bi-Maxwellian), simplified transport, O⁺ chemistry tables, EUVAC photoionization, electron/ion cooling rates, high-latitude ionosphere, polar wind kinetics, energetic ion outflow.
- [[Kelley Earth's Ionosphere]] — *The Earth's Ionosphere* (2nd ed.). Ch. 2 §2.2: mobility and conductivity tensors, κ crossover heights.
- [[Bellan 2006 Fundamentals of Plasma Physics]] — Graduate plasma text (vault PDF possibly a 2004 pre-print). Used for Debye shielding, Vlasov/moments, MHD, drifts and invariants, MHD waves.
- [[Siscoe 1983 Solar System MHD]] — MHD chapter in *Solar-Terrestrial Physics* (Reidel). Firehose and mirror instability thresholds (MHD vs kinetic); MHD discontinuities and shocks (§III); stagnation-point MHD.
- [[Velli Basics of Plasma Astrophysics]] — Chiuderi & Velli, Springer 2015 (Gaussian units). Ch. 9 reconnection: Sweet–Parker, pressure-corrected outflow, Petschek, Hall, plasmoid instability.
- [[Strangeway Ch3 Physics of Magnetized Plasmas]] — EPSS 200C textbook Ch. 3. Particle drifts, invariants, Vlasov → moments → MHD, generalized Ohm's law, frozen-in theorem, MHD waves, drift/MHD current equivalence.
- [[Thorne 1993 AOS 250B Course Reader]] — UCLA AOS 250B reader (Gaussian, relativistic). Orbital dynamics, invariants, bounce/drift periods, loss cone, Table 6.1 periods.
- [[Strangeway Ch11 The Aurora]] — *The Aurora* (EPSS 200C textbook Ch. 11; Strangeway, likely Russell/Luhmann/Strangeway 2016). Three FAST auroral current regions; Knight relation derivation; AKR; Alfvén aurora $E_\parallel$ from generalized Ohm's law (inertial and kinetic).
- [[Sivadas 2020 Thesis Energetic Precipitation]] — *Remote Sensing of Energetic Electron Precipitation.* Sivadas, Boston University PhD dissertation, 2020. PFISR max-entropy spectra validated with THEMIS; review of auroral forms and precipitation mechanisms; diffuse aurora from chorus; KAW trapping in the plasma sheet; D-region conductance dominates during substorm expansion.
- [[Hasegawa Chen 1976 KAW Mode Conversion]] — *Kinetic Processes in Plasma Heating by Resonant Mode Conversion of Alfvén Wave.* Hasegawa & Chen, Phys. Fluids 1976 (PPPL report copy). Origin of the KAW: the MHD Alfvén-resonance singularity is resolved by finite ρ_i and ρ_s into mode conversion; ω² = k∥²v_A²[1 + k⊥²ρ_i²(3/4 + T_e/T_i)]; electron Landau heating for β < 0.1. Lab-plasma context.
- [[Kletzing 1994 KAW Electron Acceleration]] — *Electron Acceleration by Kinetic Alfvén Waves.* Kletzing, JGR 1994. Wave-front E∥ of an inertial Alfvén pulse; Fermi reflection to about 2× the Alfvén speed (about 0.65–1 keV near 7000 km); electrons arrive before the fields.
- [[Lysak Lotko 1996 Kinetic Alfvén Dispersion]] — *On the Kinetic Dispersion Relation for Shear Alfvén Waves.* Lysak & Lotko, JGR 1996. Full kinetic KAW dispersion; inertial/kinetic boundary at β = m_e/m_i (about 4–5 R_E); Landau damping weak unless k⊥ρ_s or k⊥λ_e ≥ 1; hot ions suppress damping.
- [[Chaston 2003 FAST Small-Scale Alfvén Waves]] — *Properties of Small-Scale Alfvén Waves and Accelerated Electrons from FAST.* Chaston et al., JGR 2003. DAWs throughout the oval (cusp most frequent, premidnight most intense); acceleration at 1–2 R_E above FAST; v_A profile and reflection; about 1 km widths.
- [[Keiling 2003 Alfvén Wave Poynting Flux]] — *The Global Morphology of Wave Poynting Flux: Powering the Aurora.* Keiling et al., Science 2003. Polar 25,000–38,000 km; Alfvén Poynting flux traces the auroral oval and can supply about 30–35% of auroral luminosity.
- [[Chaston 2007 DAW Auroral Acceleration Fraction]] — *How Important Are Dispersive Alfvén Waves for Auroral Particle Acceleration?* Chaston et al., GRL 2007. FAST: DAWs carry 25–39% of electron energy deposition and 15–34% of energetic ion outflow; dominant near the cusp and premidnight when active.
- [[Newell 2009 Global Precipitation Budget]] — *Diffuse, Monoenergetic, and Broadband Aurora: The Global Precipitation Budget.* Newell, Sotirelis & Wing, JGR 2009. DMSP 11-yr classification; diffuse 71–84% of energy; broadband 6→13% but ×8 with driving and 28% of number flux.
- [[Thorne 2010 Chorus Diffuse Aurora]] — *Scattering by Chorus Waves as the Dominant Cause of Diffuse Auroral Precipitation.* Thorne et al., Nature 2010. CRRES + Fokker–Planck at L = 5: chorus (not ECH) scatters the injected 0.1–50 keV population in about 1 hr; pancake distributions.
- [[Artemyev 2015 KAW Electron Trapping]] — *Electron Trapping and Acceleration by Kinetic Alfvén Waves in the Inner Magnetosphere.* Artemyev, Rankin & Blanco, JGR 2015. E∥ + mirror-force trapping accelerates up to about 100 eV electrons to several keV at L = 6–9; pitch-angle collapse; field-aligned beams may drive whistlers.
