---
type: meta
updated: 2026-05-20
---

# Wiki Log

Append-only chronological record of wiki operations. Each entry is prefixed `## [YYYY-MM-DD] <op> | <title>` so the file is grep-able:

```
grep "^## \[" log.md | tail -5
```

Operations: `init`, `ingest`, `query`, `lint`, `refactor`.

---

## [2026-05-12] init | wiki scaffolding

Created `Atlas/Wiki/` with `index.md`, `log.md`, and stub `overview.md`. Schema (page conventions, ingest/query/lint workflows, citation format) documented in the root `CLAUDE.md` under "Research wiki". Subfolders `Entities/`, `Concepts/`, `People/`, `Sources/` will be created on first ingest. Scope: research papers (`Atlas/Papers/`) and textbooks (`Atlas/Textbooks/`); courses and journals are out of scope.

## [2026-05-12] ingest | Lundquist & Varney 2026 — F-Region Peak Survey at RISR-N

First substantive ingest. Source: `Atlas/Papers/Read Papers/Lundquist 2026 - A Statistical Survey of F2 Layer Peak Properties in the Polar Cap Ionosphere Observed by RISR‐N.pdf` (18 pp, JGR Space Physics 2026, doi:10.1029/2025JA034676).

Created 16 pages:

- **Sources/** — `Lundquist Varney 2026.md`
- **Entities/** — `RISR-N.md`, `AMISR.md`, `E-CHAIM.md`, `OMNI.md`, `pySPEDAS.md`
- **Concepts/** — `Ionosphere.md`, `F-Layer.md`, `Polar Cap Patch.md`, `Tongue of Ionization.md`, `Lifting.md`, `Dungey Cycle.md`, `Storm-Enhanced Density.md`, `High-Speed Streams.md`
- **People/** — `Michael Lundquist.md`, `Roger Varney.md`

Updated `overview.md` from stub to a 1-source synthesis: polar-cap F-region density structures separate statistically into D (classical patch population) vs L (a previously-unidentified, CH/HSS-driven, lifted-but-not-dense population) vs rare LD (plausibly SED-related). Updated `index.md` with all new pages.

User redirects applied during this ingest (worth carrying into the schema as we go): prefer **broader** concept pages over narrow paper-specific ones; rename `F2 Layer` → `F-Layer`; drop obscure technical concepts (Epstein model) — the source-page body is the right home for that detail.

Pages explicitly *not* spun up this round (would clutter): `NEIALs`, `HF propagation / MUF`, `Ion upflow`, `IRI / PyIRI`, `ELFIN`, `AE/AU/AL indices`, `SYM-H`, `Lifted/Dense/LD events` taxonomy. Re-evaluate on future ingests centered on those topics.

## [2026-05-12] ingest | AOS 205B + AOS 250B course-seeded concept pages

Source material: AOS 205B (ionospheric physics, Schunk-style; ~16 lecture PDFs) and AOS 250B (magnetospheric plasma physics, Thorne 1993 course reader, 126 pp). Both courses read in full across prior and this session; concept pages written in a consolidated pass after completing all reading.

Created 16 concept pages:

- **Concepts/** (ionospheric, from AOS 205B) — `Atmospheric Escape.md`, `Polar Wind.md`, `Ionospheric Energetics.md`, `Ionospheric Conductivity.md`, `Ionospheric Dynamo.md`, `Joule Heating.md`, `Field-Aligned Currents.md`, `Aurora.md`, `Ionospheric Instabilities.md`, `Equatorial Ionosphere.md`, `Ambipolar Diffusion.md`, `Airglow.md`
- **Concepts/** (magnetospheric, from AOS 250B) — `Radiation Belts.md`, `Plasma Waves.md`, `Wave-Particle Interactions.md`, `Synchrotron Radiation.md`

Updated `index.md` with all 16 new pages.

`overview.md` not updated — course material enriches concept depth but does not shift the research-level synthesis (which is still based on [[Lundquist Varney 2026]]). The new concept pages substantially extend the wiki's coverage of the high-latitude ionosphere and inner magnetosphere, providing a foundation for future paper ingests.

Pages explicitly deferred: `Kinetic Theory` (standalone — detail lives in `Wave-Particle Interactions` and `Plasma Waves`), `Plasmapause` (mentioned in passing; spin up when a plasmasphere-focused paper is ingested).

## [2026-05-13] ingest | Thayer Coleman 2026, Foster 2020 — thermospheric vertical winds, geospace plume

Sources: `Atlas/Papers/Read Papers/Thayer 2026 - Baroclinic Lifitng Derivation.pdf` (15 of 15 pp, Frontiers; note: filename is misleading — paper is about vertical wind coordinate ambiguities, not ionospheric lifting), `Atlas/Papers/Read Papers/Foster 2020 - Multi‐Point Observations of the Geospace Plume.pdf` (10 pp, book chapter).

Created 2 new pages:

- **Sources/** — `Thayer Coleman 2026 Vertical Winds.md` (divergent vs lifting wind decomposition; FPI airglow ambiguity; TIEGCM adiabatic heating), `Foster 2020 Geospace Plume.md` (unified geospace plume: SED→plasmaspheric plume→magnetopause; 17 March 2015 storm)

No existing pages updated (Thayer 2026 content is thermosphere-specific, not directly additive to existing ionospheric concept pages; Foster 2020 extends Tongue of Ionization and SED pages but the new connections are captured in the source page links). Index updated with 2 new entries.

## [2026-05-13] ingest | David 2016, Zou Ridley 2015, Thayer Semeter 2004 — GPS TEC patch survey, GITM SED backtracer, magnetospheric energy flux

Sources: `Atlas/Papers/Read Papers/David 2016 - Polar cap patches and the tongue of ionization A survey of GPS TEC maps from 2009 to 2015.pdf` (7 pp, GRL), `Atlas/Papers/Read Papers/Zou Ridley 2015 - GITM Backtracer.pdf` (9 pp, book chapter), `Atlas/Papers/Read Papers/Thayer Semeter 2004 - The convergence of magnetospheric energy flux in the polar atmosphere.pdf` (10 of 18 pp, JASTP).

Created 5 new pages:

- **Sources/** — `David 2016 TEC Survey.md`, `Zou Ridley 2015 GITM Backtracer.md`, `Thayer Semeter 2004 Energy Flux.md`
- **Entities/** — `GITM.md` (Global Ionosphere-Thermosphere Model; 3-D fluid model ~100–700 km; SED plume backtracing)

Updated 3 existing pages:

- **Concepts/Polar Cap Patch.md** — added observational confirmation paragraph to UT/seasonal section (David 2016 Madrigal TBR confirms Sojka 1994 prediction; winter hole rules out non-solar sources); sources now 3.
- **Concepts/Joule Heating.md** — added full Poynting flux framework section (Poynting's theorem, neutral-wind frame decomposition, 94% Joule heat global partition, EM vs VUV energy budget comparison, aeronomic consequences); added Thayer Semeter 2004 to sources.
- **index.md** — added GITM entity + 3 new source entries.

`overview.md` not updated — these sources add mechanism-level depth (TEC confirmation of source mechanism, SED plasma origins, energy budget framework) but do not shift the high-level research synthesis.

## [2026-05-13] ingest | Varney 2014, Varney 2021, Themens 2018 — IPWM supplement, ISR probability, E-CHAIM primer

Three short technical papers ingested in a single batch.

Sources: `Atlas/Papers/Read Papers/Varney 2014 - Supplemental Details on IPWM.pdf` (10 pp), `Atlas/Papers/Read Papers/Varney 2021 - Probability Theory for Incoherent Scatter Radar.pdf` (13 pp lecture notes), `Atlas/Papers/Read Papers/Themens 2018 - The Empirical Canadian High Arctic Ionospheric Model (E- CHAIM) Primer.pdf` (25 pp user manual).

Created 4 new pages:

- **Sources/** — `Varney 2014 IPWM Supplement.md`, `Varney 2021 ISR Probability.md`, `Themens 2018 ECHAIM Primer.md`
- **Entities/** — `IPWM.md` (3-D Ionosphere Polar Wind Model; 8-moment equations, dipole-aligned flux tubes 97–8400 km, van Leer horizontal transport)

Updated 2 existing pages:

- **Entities/E-CHAIM.md** — upgraded stub→draft; added full sub-model table (NmF2/hmF2/topside/bottomside), AACGM coordinate system, driving indices, operational modes (Default/Satellite/Map), complete error flag table (A–J), acknowledgement text; sources now 2.
- **index.md** — added IPWM entity, updated E-CHAIM description, added 3 new source entries.

`overview.md` not updated — these sources add implementation depth (model internals, signal processing theory) without shifting the research-level synthesis.

## [2026-05-13] ingest | Blelly & Schunk 1993 — 8-, 13- and 16-Moment Transport Formulations of the Polar Wind

Source: `Atlas/Papers/Read Papers/Blelly 1992 - 8 13 and 16moment transport formulations of the polar wind.pdf` (27 pp in scan, Ann. Geophysicae 11, 443–469, 1993). Foundational comparative study of polar wind moment hierarchies; H$^+$ and O$^+$ from 200–8600 km; steady-state and dynamic (density depletion) comparison.

Created 1 new page:

- **Sources/** — `Blelly Schunk 1993 Moment Comparison.md`

Updated 3 existing pages:

- **Concepts/Polar Wind.md** — added moment hierarchy table and key quantitative results (propagation speeds, H⁺ supersonic, O⁺ downflow regions, ionospheric composition, electron temperature behavior); sources: 0→1.
- **Entities/IPWM.md** — added explanation of why 8-moment was chosen (×6 standard-model error, 13-moment collisionless instability); sources: 1→2.
- **index.md** — added Blelly Schunk 1993 source entry.

`overview.md` not updated — this is a theoretical methods paper underlying IPWM; does not shift the research synthesis.

## [2026-05-13] ingest | Pham 2022 — Thermospheric Density Perturbations by TADs During August 2005 Storm

Source: `Atlas/Papers/Read Papers/Pham 2022 - Thermospheric Density Perturbations Produced by Traveling Atmospheric Disturbances During.pdf` (14 pp, JGR Space Physics 2022, doi:10.1029/2021JA030071). MAGE coupled geospace model vs empirical WEIMER-driven TIEGCM; CHAMP and GRACE neutral density at ~400 km; August 24, 2005 storm (Dst$_\text{min}$ -170 nT).

Created 3 new pages:

- **Sources/** — `Pham 2022 TADs.md`
- **Entities/** — `MAGE.md` (Multiscale Atmosphere Geospace Environment; GAMERA + RCM + REMIX + high-res TIEGCM)
- **Concepts/** — `Traveling Atmospheric Disturbances.md` (TADs: high-latitude Joule heating source, equatorward propagation, bi-hemispheric constructive intersection, TID connection)

Updated 2 existing pages:

- **Concepts/Joule Heating.md** — added "Localization matters for TAD generation" section with MAGE vs WEIMER quantitative comparison (647 GW vs 1429 GW; R² improvement factor ~2); updated sources count 0→2; added Pham 2022 TADs to sources.
- **index.md** — added MAGE entity, TADs concept, Pham 2022 source entries.

`overview.md` not updated — TAD mechanism adds thermospheric physics depth but does not shift the ionospheric research synthesis.

## [2026-05-13] ingest | Themens 2024 — High Latitude Ionospheric Response to the May 2024 Geomagnetic Storm

Source: `Atlas/Papers/Read Papers/Themens 2024 - The High Latitude Ionospheric Response to the Major May 2024 Geomagnetic Storm A Synoptic View.pdf` (11 pp, GRL 2024, doi:10.1029/2024GL111677). Multi-instrument synoptic study of the May 10–11, 2024 superstorm (Dst$_\text{min}$ -412 nT, first Kp 9 storm since 2003). Instruments: Madrigal TEC, ESR, PFISR, Eglin AFB ionosonde, OMNI, TIMED GUVI.

Created 1 new page:

- **Sources/** — `Themens 2024 May Storm.md`

Updated 4 existing pages:

- **Concepts/Storm-Enhanced Density.md** — replaced stub counter-example with quantified preconditioning section: $h_{mF2}$ to 630 km on Day 1, O/N$_2$ depleted 50% by Day 2, F2-layer absent at ESR/PFISR, 3-day recovery; RISR-N attribution corrected to ESR/PFISR; sources: 3→4.
- **Concepts/Lifting.md** — added quantified lifting magnitudes (300 km in 1 hr, LSTID-like oscillations 150–300 km, patches >475 km at ESR) and lifting failure section expanded with preconditioning context; RISR-N attribution corrected to ESR/PFISR; sources: 2→3.
- **Concepts/Polar Cap Patch.md** — corrected storm suppression sentence (RISR-N → ESR/PFISR, prose updated, wiki link added); sources: 3→4.
- **index.md** — added Themens 2024 source entry.

`overview.md` not updated — storm suppression / preconditioning deepens mechanism understanding but does not shift the high-level research synthesis.

## [2026-05-13] ingest | Zou 2021 — SED Impact on Ion Upflow Fluxes During Geomagnetic Storms

Source: `Atlas/Papers/Read Papers/Zou 2021 - Impact of storm-enhanced density on Ion Upflow Fluxes During Geomagnetic Storms.pdf` (18 pp, Front. Astron. Space Sci. 2021, doi:10.3389/fspas.2021.746429). March 6–7, 2016 CIR storm case study; multi-instrument (VISTA TEC, SuperDARN, AMPERE, DMSP F15, PFISR, TIMED GUVI).

Created 1 new page:

- **Sources/** — `Zou 2021 SED Ion Upflow.md`

Updated 3 existing pages:

- **Concepts/Storm-Enhanced Density.md** — replaced brief ion upflow stub with full Type 1/Type 2 classification table, flux magnitudes, negative storm phase density-controls-flux finding; sources: 2→3.
- **Entities/DMSP.md** — added storm-time ion upflow observations section with Type 1/2 comparison table, SED topside density value, downward flow observation at sub-auroral latitudes; sources: 1→2.
- **index.md** — added Zou 2021 source entry.

`overview.md` not updated — this source adds mechanism-level depth on the upflow/SED coupling but does not shift the research-level synthesis (still anchored in [[Lundquist Varney 2026]]).

## [2026-05-13] ingest | Laundal & Richmond 2016 — Magnetic Coordinate Systems

Source: `Atlas/Papers/Read Papers/Laundal 2016 - MagneticCoordinateSystems.pdf` (33 pp, Space Sci Rev 206, 27–59, 2017, doi:10.1007/s11214-016-0275-y). Review and standardization reference for all magnetic coordinate systems used in space physics.

Created 2 new pages:

- **Sources/** — `Laundal Richmond 2016 Magnetic Coordinates.md` (definitions of CD/ED/dip/GSM/SM/QD/MA/CGM/AACGM; base vectors; MLT; secular variation; coordinate mismatch error)
- **Concepts/** — `Magnetic Coordinate Systems.md` (summary table, key definitions for all eight systems, base vector formulas for MA and QD, MLT recommendation, secular variation warning)

No existing pages updated — this is foundational methodology material. Concept pages that use coordinate terminology (Ionospheric Dynamo, Field-Aligned Currents, E-CHAIM) would benefit from cross-links on future lint pass. Updated `index.md` with both new entries.

`overview.md` not updated — coordinate methodology does not shift the research-level synthesis.

## [2026-05-13] ingest | Varney 2026 — Polar Cap Patches and High-Latitude Plasma Density Structures

Source: `Atlas/Papers/Read Papers/Varney 2026 - PatchesChapter.pdf` (~45 pp including references; book chapter by Roger Varney, UCLA AOS). Comprehensive review of polar cap patch physics, formation mechanisms, instabilities, and radio propagation consequences.

Created 3 new pages:

- **Sources/** — `Varney 2026 PatchesChapter.md`
- **Concepts/** — `Polar Holes.md`
- **Entities/** — `SuperDARN.md`, `DMSP.md`

Substantially updated 6 existing pages:

- **Concepts/Polar Cap Patch.md** — complete rewrite to `mature`; added full formation taxonomy (variable convection / scooping / cutting / local production), O$^+$ transport theory, $D$-parameter UT/seasonal dependence, hot/cold patch classification table, subauroral blobs, GDI growth rate derivation, radio propagation effects, and ion upflow/polar wind jet connection.
- **Concepts/Tongue of Ionization.md** — added geospace plume connection, OCB crossing physics, transit timescale (~1–2 hr), SED connection, segmentation mechanism taxonomy.
- **Concepts/Storm-Enhanced Density.md** — added positive vs negative storm-effect framework, PPEF and disturbance dynamo, vertical ExB derivation, May 2024 superstorm as suppression counter-example, ion upflow preconditioning.
- **Concepts/Lifting.md** — added full $u_z = u_\perp\sin\theta_\text{dip}$ derivation, $T_{eff}$-dependent rate coefficients $k_1$/$k_2$ (with piecewise formulas), thermospheric expansion as negative case, coupling to cutting mechanism.
- **Concepts/Airglow.md** — added full VER formula (Eq 1.27–1.30 from chapter), Sojka et al. factor-of-4 altitude ambiguity, airglow vs electron density patch distinction table, PMAF airglow patch seeding.
- **Entities/RISR-N.md** — added volumetric 3-D imaging section (Dahlgren et al. 2012) and CERTO beacon scintillation conjunction section (Lamarche et al. 2020).

Updated `index.md` with all new/updated pages. `overview.md` not updated — this source enriches mechanism depth for existing concepts but does not shift the research-level synthesis (still anchored in [[Lundquist Varney 2026]]).

## [2026-05-19] ingest | Akbari 2014, Bao 2023 — NEIAL aspect angle dependence; ring current/SAPS/geospace plume MAGE simulation

Sources: `Atlas/Papers/Read Papers/Akbari 2014 - Aspect angle dependence of naturally enhanced ion acoustic lines.pdf` (9 pp, JGR Space Physics 2014), `Atlas/Papers/Read Papers/Bao 2023 - The Relation Among the Ring Current, Subauroral Polarization Stream, and the Geospace Plume MAGE Simulation of the 31 March 2001 Super Storm.pdf` (20 pp, JGR Space Physics 2023).

Created 5 new pages:

- **Sources/** — `Akbari 2014 NEIAL Aspect Angle.md`, `Bao 2023 Geospace Plume MAGE.md`
- **Concepts/** — `NEIALs.md` (Type 1/2 classification, aspect angle sensitivity, PFISR observations), `Ring Current.md` (toroidal inner-magnetosphere current, gradient/curvature drifts, controls SAPS), `Subauroral Polarization Streams.md` (SAPS; dusk-side plasmasphere erosion; TEC trough; driven by Region-2 FAC in low-conductance sub-auroral gap)

Updated 3 existing pages:

- **Concepts/Ionospheric Instabilities.md** — added NEIALs section (Type 1/2, aspect angle dependence, PFISR context); sources: 0→1.
- **Entities/MAGE.md** — added Bao 2023 application section (geospace plume, SAPS, ring current causality, DMSP validation, model limitations); sources: 1→2.
- **Concepts/Storm-Enhanced Density.md** — added SAPS and geospace plume section with Bao 2023 (electrodynamic linkage, no mass exchange required, ring current → SAPS → SED causal chain); sources: 4→5.

Also created `Atlas/Wiki/dashboard.md` — Dataview-based live query dashboard (requires Dataview community plugin). Added dashboard entry to `index.md`.

`overview.md` not updated — these sources add inner magnetosphere and coherent scatter depth but do not shift the research-level synthesis.

## [2026-05-19] ingest | Dickinson 1968, Coleman 1992, Auster 2007, Vasquez 2020, Kletzig 2013, Kletzig 2023, Parker 1958, Lundquist 1951, Pierrard 2001, Decadal Survey 2024 — batch ingest of all remaining Read Papers

Sources: 10 papers/documents processed. Varney 2023 PRISM Grant (.docx) skipped (not readable as PDF).

Created 13 new pages:

- **Sources/** — `Dickinson Geisler 1968 Thermospheric Vertical Motion.md` (w_D/w_L decomposition; adiabatic heating; parent of Thayer 2026), `Coleman 1992 Ionospheric Ray Tracing.md` (HASEL; Haselgrove ODEs; Appleton-Hartree; HF ray tracing), `Auster 2007 THEMIS FGM.md` (THEMIS FGM instrument description), `Vasquez 2020 Van Allen Probe FGM Calibration.md` (RBSP magnetometer flight calibration), `Kletzig 2013 EMFISIS.md` (EMFISIS instrument description), `Kletzig 2023 EMFISIS Science.md` (post-mission science synthesis; ULF/chorus/hiss/EMIC), `Parker 1958 Solar Wind.md` (foundational solar wind; transonic outflow; Parker spiral), `Lundquist 1951 Flux Rope Stability.md` (force-free cylindrical field; kink instability), `Pierrard 2001 Solar Wind Electrons.md` (core/halo/strahl VDF; kinetic Fokker-Planck), `Decadal Survey 2024.md` (2024–2033 heliophysics priorities; GDC/DYNAMIC; DASHI; HF propagation)
- **Entities/** — `THEMIS.md` (five-spacecraft constellation; FGM; substorm onset), `Van Allen Probes.md` (RBSP/EMFISIS; radiation belt waves and fields)
- **Concepts/** — `HF Radio Propagation.md` (Appleton-Hartree; Haselgrove ray tracing; MUF; SuperDARN backscatter geometry; patch-driven scintillation)

Updated 6 existing pages:

- **Concepts/Lifting.md** — added "Thermospheric origin of the lifting mechanism" section with Dickinson w_D/w_L decomposition context; updated metadata; sources: 2→3.
- **Entities/SuperDARN.md** — added "HF Ray Tracing" section noting Coleman 1992 HASEL procedure for ray-path modeling; sources: 1→2.
- **Concepts/Radiation Belts.md** — added "Observational Constraints from Van Allen Probes" section (ULF diffusion, chorus acceleration, EMIC loss, hiss slot, plasma density); sources: 0→2.
- **Concepts/High-Speed Streams.md** — added "Solar Wind Origin" section connecting CH/HSS to Parker 1958 transonic solution; sources: 1→2.
- **Concepts/Polar Wind.md** — added Parker 1958 transonic lineage note in Classical Description section; added Parker 1958 to sources; sources: 1→2.
- **Concepts/Wave-Particle Interactions.md** — added Pierrard 2001 strahl/halo context note to Sources section.

Updated `index.md` with all 13 new entries (2 entities, 1 concept, 10 sources).

`overview.md` not updated — no source in this batch shifts the high-level ionospheric research synthesis (still anchored in [[Lundquist Varney 2026]]). All Read Papers are now ingested. Next priority: Need to Read Papers (30 papers); Varney 2023 PRISM Grant.docx (pending .docx handling); Decadal ITM appendix (pp. 424–502) for detailed ionosphere science priorities.

## [2026-05-19] ingest | Batch ingest of 16 Need-to-Read papers (Batches 1 & 2)

Sources processed from `Atlas/Papers/Need to Read Papers/`:

**Batch 1 (core polar cap / RISR-N):** Crowley 1993 (critical review patches/blobs), Bahcivan 2010 (initial RISR-N obs), Zou 2021 (polar cap density structure review), Gilles 2018 (RISR/SuperDARN velocity comparison), Larson 2023 (E-CHAIM vs RISR validation), Foster 2004 (multiradar TOI superstorm), Zhang 2016 (non-classic patch transport), Chartier 2017 (Swarm patch occurrence), Diaz Pena 2021 (auroral heating hot patches), Milan Grocott 2021 (high-latitude convection Dungey cycle review)

**Batch 2 (magnetosphere / instrumentation):** Albarran 2023 (N+ polar wind HIDRA/MAGE), Kennel 1966 (K-P limit), Perry 2021 (SuperDARN Poynting flux), Xiong 2020 (FACs + precipitation DMSP), Claudepierre 2022 (radiation belt electron loss L<4), Gerard 1980 (optical F-region processes)

**Out of scope:** David 2005 (weather forecast verification — Monthly Weather Review) | **Already ingested:** Laundal 2016

Created 16 new source pages:

- **Sources/** — `Crowley 1993 Critical Review Patches Blobs.md`, `Bahcivan 2010 Initial RISR-N Observations.md`, `Zou 2021 Polar Cap Density Structure Advances.md`, `Gilles 2018 RISR SuperDARN Velocity Comparison.md`, `Larson 2023 E-CHAIM vs RISR.md`, `Foster 2004 Multiradar TOI.md`, `Zhang 2016 Patch Transport Beyond Classic.md`, `Chartier 2017 Swarm Patch Occurrence.md`, `Diaz Pena 2021 Auroral Heating Patches.md`, `Milan Grocott 2021 High Latitude Convection.md`, `Albarran 2023 N+ Polar Wind MAGE.md`, `Kennel 1966 Limit Stably Trapped Fluxes.md`, `Perry 2021 SuperDARN Poynting Flux.md`, `Xiong 2020 FACs Precipitation DMSP.md`, `Claudepierre 2022 Radiation Belt Losses.md`, `Gerard 1980 Optical F-region Processes.md`

Updated 14 existing entity/concept pages:

- **Concepts/Polar Cap Patch.md** — added Zhang 2016 non-classic stagnation; Chartier 2017 December anomaly; Diaz Peña 2021 auroral heating mechanism; Zou 2021 statistical properties section; updated sources 4→11.
- **Entities/RISR-N.md** — added first science obs (Bahcivan 2010), velocity calibration (Gilles 2018), E-CHAIM comparison (Larson 2023); status stub→draft; sources 2→6.
- **Entities/E-CHAIM.md** — added RISR-N validation section (Larson 2023); sources 2→3.
- **Concepts/Tongue of Ionization.md** — added extreme TOI superstorm section (Foster 2004); sources 2→3.
- **Concepts/Dungey Cycle.md** — added ECPC model section (Milan Grocott 2021); status stub→draft; sources 1→2.
- **Concepts/Field-Aligned Currents.md** — added FAC–precipitation statistics section (Xiong 2020); sources 0→1.
- **Concepts/Airglow.md** — added excitation pathways section (Gerard 1980); sources 1→3.
- **Entities/IPWM.md** — added HIDRA section (Albarran 2023, N+ bug fix); sources 2→3.
- **Concepts/Polar Wind.md** — added N+ species section (Albarran 2023); sources 2→3.
- **Entities/MAGE.md** — added HIDRA component section (Albarran 2023); sources 1→2.
- **Entities/SuperDARN.md** — added velocity calibration section (Gilles 2018), Poynting flux section (Perry 2021); sources 2→4.
- **Entities/AMISR.md** — added sources (Bahcivan 2010, Gilles 2018); status stub→draft; sources 1→3.
- **Concepts/Radiation Belts.md** — added quantitative loss rates section (Claudepierre 2022); sources 2→3.
- **Concepts/Wave-Particle Interactions.md** — added Kennel 1966 source link (original K-P paper).

Updated `index.md` — added 16 new source entries (19 new entries counting Crowley, which is a Radio Science review chapter) plus 1 deferred Decadal Survey Blelly already present.

`overview.md` not updated — these sources consolidate and validate the existing polar-cap density structure synthesis; no new paradigm shift.

Remaining Need-to-Read Papers (deferred, lower priority — magnetosphere periphery topics): Agapitov 2011 (chorus chorus), Olifer 2023, Summers 2009, Treumann 2002, Artemyev 2008, Carlson 2001, Rietsch 1977, Sun 2020, Tsurutani 2021, Gallardo-Landcourt 2018. Still pending: Varney 2012 Thesis (very long), Varney 2023 PRISM Grant.docx (.docx), Decadal Survey 2024 Appendix D (pp. 424–502 ITM panel).

## [2026-05-19] ingest | Batch ingest of 10 deferred Need-to-Read papers (periphery topics)

Sources processed from `Atlas/Papers/Need to Read Papers/`:

Agapitov 2011 (THEMIS chorus waves), Olifer 2023 (K-P self-limiting precipitation), Summers 2009 (relativistic K-P limit), Treumann 2002 (auroral plasma physics Ch. 6: electrodynamics of auroral forms), Artemyev 2008 (Harris current sheet evolution), Carlson 2001 (FAST plasma instrument), Rietsch 1977 (maximum entropy inverse problems), Sun 2020 (TEC matrix completion VISTA), Tsurutani 2013 (PPEF comment — PDF filename incorrectly labeled 2021), Gallardo-Lacourt 2018 (STEVE statistics)

Created 10 new source pages (Sources/ only — no concept/entity page updates for this periphery batch):

- `Agapitov 2011 THEMIS Chorus Waves.md`
- `Olifer 2023 KP Self-Limiting Precipitation.md`
- `Summers 2009 Relativistic KP Limit.md`
- `Treumann 2002 Auroral Electrodynamics.md`
- `Artemyev 2008 Harris Current Sheet.md`
- `Carlson 2001 FAST Plasma Instrument.md`
- `Rietsch 1977 Maximum Entropy Inverse Problems.md`
- `Sun 2020 TEC Matrix Completion.md`
- `Tsurutani 2013 PPEF Ionosphere Comment.md`
- `Gallardo-Lacourt 2018 STEVE Statistics.md`

Updated `index.md` — added 10 new source entries.

Concept pages that could benefit from minor additions (deferred):
- `Wave-Particle Interactions.md` — Agapitov 2011 (reflected chorus), Olifer 2023 (K-P observational confirmation), Summers 2009 (relativistic K-P)
- `Radiation Belts.md` — Olifer 2023, Summers 2009
- `Aurora.md` — Treumann 2002 (auroral forms), Gallardo-Lacourt 2018 (STEVE)
- `Storm-Enhanced Density.md` / `Equatorial Ionosphere.md` — Tsurutani 2013 (PPEF superfountain)

All Need-to-Read Papers are now ingested. Remaining: Varney 2012 Thesis (very long, needs section-by-section), Varney 2023 PRISM Grant.docx (.docx not readable as PDF). Next step: Decadal Survey 2024 Appendix D pp. 424–502 (ITM panel — ionosphere/thermosphere/mesosphere science priorities).

## [2026-05-19] ingest | Decadal Survey 2024 — Appendix D ITM Panel (pp. 424–502)

Read PDF pages 440–502 (printed pp. 424–486) in full: D.1 Introduction, D.2 Current State of ITM Science, D.3 Priority Science Goals (PSGs 1–4), D.4 Long-Term Goal (other worlds), D.5 Emerging Opportunities, D.6 Implementation Strategy (spaceflight missions + ground facilities).

Updated 1 existing source page (major rewrite):

- **Sources/Decadal Survey 2024.md** — status draft→mature; expanded from high-level summary to full coverage of all four PSGs with objectives, five spaceflight mission concepts (BRAVO, Resolve, I-Circuit, LAITIR, SOURCE+), five ground-based facility concepts (DASHI, Meteor Radar Network, Subauroral IS Radar, Extended GNSS Network, existing AMISR network), key contextual findings (STEVE, O-O⁺ cross section resolution, Weddell Sea Anomaly, ICON/GOLD results, Antarctic infrastructure gap).

Updated 1 existing concept page:

- **Concepts/Joule Heating.md** — added "Observational constraints and forecast uncertainty" section noting 500% LAITIR motivation, AE-C heritage, and IS radar as uniquely suited for Joule heating constraints; sources: 2→3.

All Read Papers and all Need-to-Read Papers are now fully ingested (source pages created). Decadal Survey 2024 source page is now at mature status with complete ITM panel coverage.

Remaining work: Varney 2012 Thesis (very long, section-by-section), Varney 2023 PRISM Grant.docx (.docx not readable as PDF). Optional follow-on: deferred concept page additions for Aurora (Treumann/Gallardo-Lacourt), Wave-Particle Interactions (Agapitov/Olifer/Summers), Storm-Enhanced Density (Tsurutani).

## [2026-05-19] ingest | Varney 2012 Thesis — Photoelectron Transport and Energy Balance in the Low-Latitude Ionosphere

Source: `Atlas/Papers/Need to Read Papers/Varney 2012 - Thesis.pdf` (212 pp, Cornell PhD dissertation, 2012). Roger H. Varney; advisor: Prof. Michael Kelley. Read in 7 passes (PDF pp. 30–212): Chs. 1–2 (ISR theory, JRO modes, energetics history), Ch. 3 (SAMI2 fluid equations, sensitivity studies, JRO comparison), Ch. 4 (photoelectron physics: HEUVAC, cross sections, collision operators, guiding-center justification), Ch. 5 (finite volume numerics, energy grid, heating rate formula), Ch. 6 (SAMI2-PE results: fluxes, pitch-angle distributions, JRO comparison, N(²D) sensitivity, model parameter and driver sensitivity, day-to-day variability), Ch. 7 (conclusions, future work, code acceleration strategies).

Created 3 new pages:

- **Sources/** — `Varney 2012 Thesis.md`
- **Entities/** — `SAMI2.md` (SAMI2 + SAMI2-PE; NRL; low-latitude 2-D dipole grid; 7 species; 5-moment fluid; Boltzmann-Fokker-Planck photoelectron transport extension; energy grid; numerical methods; key scientific findings; relationship to FLIP, SAMI3, IPE, IPWM)
- **Entities/** — `Jicamarca Radio Observatory.md` (JRO; Lima Peru; dip equator; full-profile admittance mode; reference day March 25 2009; 6-day dataset July 8–13 2008)

Updated 4 existing pages:

- **Concepts/Ionospheric Energetics.md** — added "Photoelectron Transport and the Nonlocal Heating Problem" section: nonlocal heating mechanism, SAMI2 C_qe failure, T_e feedback loop, EIA arc shadows, N(²D) quenching, day-to-day variability; sources 0→1.
- **Entities/IPWM.md** — added "Relationship to SAMI2" section linking 8-moment heritage to SAMI2 fluid foundations; sources 3→4.
- **People/Roger Varney.md** — added Cornell PhD background (advisor Kelley), thesis topic, Jack Eddy Fellow, CEDAR CSSC; status stub→draft; sources 1→2.
- **index.md** — added SAMI2 and Jicamarca Radio Observatory entity entries; added Varney 2012 Thesis source entry.

No `overview.md` update — this is a focused low-latitude/equatorial energetics paper; the polar-cap research synthesis is unchanged.

Ingest queue fully cleared. Varney 2023 PRISM Grant.docx remains (.docx not readable). Next available: textbooks (Kelley - Earth's Ionosphere.pdf is highest priority).

## [2026-05-19] ingest | Schunk & Nagy 2009 — Ionospheres: Physics, Plasma Physics, and Chemistry (2nd ed.)

Source: `Atlas/Textbooks/Schunk and Nagy - Ionospheres.pdf` (~618 pp). Seminal graduate textbook; primary reference for polar wind physics, O⁺ chemistry, transport equations, and ionospheric energetics. Full-depth analysis across Chs. 3, 5, 8, 9, and 12.

Chapters analyzed:
- **Ch. 3 (pp 50–69):** Boltzmann equation (Eq 3.7); velocity moments (3.10–3.21); 13-moment closed system (3.57–3.63); bi-Maxwellian generalization (3.75); T_∥/T_⊥ temperatures (3.64–3.66).
- **Ch. 5 (pp 113–132):** Five-moment approximation (5.22); transport in weakly ionized plasma — Pedersen/Hall decomposition (5.35); ion frictional heating (5.36); T_i anisotropy from stress tensor (5.46–5.47); major ion ambipolar diffusion derivation (5.54–5.59); polarization electrostatic field and Boltzmann relation (5.61–5.63); minor ion diffusion (5.70–5.79) including light-ion upward force origin.
- **Ch. 8 (pp 231–250):** Chemical kinetics framework; Table 8.3 (53 ion-molecule reactions; key rates R47 O⁺+N₂, R48 O⁺+O₂, R51 O⁺+H); Tables 8.4–8.5 (dissociative recombination: NO⁺ α=4.0×10⁻⁷(300/Te)^0.5, O₂⁺ α=2.4×10⁻⁷(300/Te)^0.70); O(¹D) production channels (Eqs 8.57–8.74) including eight pathways from O₂⁺ dissociative recombination (dominant), photodissociation, and electron impact.
- **Ch. 9 (pp 254–287):** Solar EUV absorption (Chapman function, Eqs 9.1–9.26); EUVAC model (Eq 9.20); photoionization rates (Table 9.2); photoelectron transport (two-stream Eqs 9.31–9.43); electron heating rate (Eq 9.49); electron cooling rate catalog: N₂/O₂ rotation (9.50–9.51), N₂/O₂ vibration (9.58–9.61), O fine structure (9.65), O(¹D) excitation (9.67); altitude hierarchy in Fig. 9.17.
- **Ch. 12 (pp 398–477, from previous session):** Convection E-field models; ion frictional heating T_i formula (Eq 12.3); O⁺ chemistry rate enhancement (×16 for 2× E-field); patch/polar hole/TOI taxonomy (§§12.4–12.9); supersonic neutral winds (Mach 1–2, CPCP≥150 kV); geomagnetic storm positive/negative phases; substorms; SAID; polar wind kinetics (§12.16) — T_∥/T_⊥ anisotropy, H⁺ VDF evolution (Maxwellian→double-humped→kidney), 3D storm model results, H⁺ blowout; energetic ion outflow (§12.17) — cleft ion fountain, DE-1 statistics (O⁺ ×20 Kp 0→6, ×5 solar min→max; H⁺ ×2 decrease); neutral polar wind (§12.18) — IMAGE 1–4×10⁹ cm⁻² s⁻¹.

Created 2 new pages:
- **Sources/** — `Schunk Nagy 2009 Ionospheres.md`
- **Concepts/** — `Ion Frictional Heating.md`

Substantially updated 4 existing pages:
- **Concepts/Polar Wind.md** — added "Kinetic Structure and Storm Response (§12.16)" section with H⁺ VDF evolution table, H⁺ blowout mechanism, 7 storm model results; added "Energetic Ion Outflow — Cleft Ion Fountain (§12.17)" section with DE-1 statistics; added "Neutral Polar Wind (§12.18)" section with IMAGE measurements; status: draft→mature, sources: 3→5.
- **Concepts/Ionospheric Energetics.md** — added "Photoionization and Solar EUV" section (Chapman production function, EUVAC, photoelectron production rate); expanded "Heating Sources" with formal Q_e formula (Eq 9.49) and He II 30.4 nm context; replaced bullet-list "Cooling Processes" with quantitative rate expressions for N₂/O₂ rotation, N₂/O₂ vibration, O fine structure, O(¹D) excitation, Coulomb collisions, and Fig 9.17 altitude hierarchy; added ion cooling discussion; status: draft→mature, sources: 1→3.
- **Concepts/Airglow.md** — replaced single-sentence O(¹D) production description with eight-channel S&N taxonomy (Eqs 8.57–8.68), distinguishing nighttime-dominant (O₂⁺ DR), dayside (O₂ photodissociation), and auroral (electron impact) channels; sources: 3→4.
- **Concepts/Ambipolar Diffusion.md** — replaced heuristic derivation with full five-moment derivation from S&N Ch. 5 (Eqs 5.51–5.59, polarization field Eq 5.61, Boltzmann relation Eq 5.63); added "Minor Ion Diffusion (§5.7)" section explaining kinematic origin of polar wind (H⁺ mass < O⁺/2 → net upward force); sources: 0→1.

Updated `index.md` with new source entry (Schunk Nagy 2009) and new concept entry (Ion Frictional Heating).

`overview.md` not updated — this textbook adds theoretical depth and quantitative grounding to existing concepts but does not shift the polar-cap research synthesis. The two novel findings worth tracking are: (1) the eight O(¹D) production channels (more complete than current Airglow page had), and (2) the explicit kinematic origin of the polar wind from minor-ion force balance, now documented in Ambipolar Diffusion.

## [2026-05-20] ingest | Schunk & Nagy 2009 — Remaining Chapters (1, 2, 4, 5, 6, 7, 10, 11)

Continuation of the 2026-05-19 ingest. All remaining high-priority chapters read in full; wiki pages written to consolidate the material.

Chapters newly ingested in this session:
- **Ch. 1 (pp 1–10):** Historical overview — Marconi 1901, Kennelly-Heaviside hypothesis 1902, Breit-Tuve 1924 pulse sounding, Watson-Watt 1926 naming, IGY 1957, Sputnik 1 Oct 4 1957, Explorer 1 Jan 31 1958.
- **Ch. 2 §§2.1–2.6 (pp 11–40):** Space environment — Sun (corona ~10⁶ K, CMEs, solar constant 1370 W/m²); interplanetary medium (Parker spiral 43°, Table 2.3); Earth magnetosphere (bow shock 12 R_E, magnetopause 9 R_E, ring current, plasmasphere, two-cell convection); planetary ionospheres (Mercury, Venus ionopause, Mars Viking, Titan, Enceladus).
- **Ch. 4 §§4.6–4.10 (pp 106–125):** Collision frequency tables — resonant ion-neutral (O⁺–O), electron-neutral momentum transfer rates for e–O, e–N₂, e–O₂ (Table 4.4); full Coulomb collision tables (§4.3–4.4).
- **Ch. 5 §§5.12–5.18 (pp 146–158):** Electron field-aligned current and heat flux (Eqs 5.140–5.141); electron thermal conductivity (Eq 5.146); ion viscosity and stress (Eqs 5.148–5.149); higher-order ambipolar diffusion with thermal diffusion correction Δ_in (Eq 5.165); ion thermal conductivity (Eqs 5.168–5.169); transport coefficient accuracy summary.
- **Ch. 6 (from prior session — verified):** Full ionospheric wave taxonomy — electron plasma, ion acoustic, upper/lower hybrid, R/L modes, O/X waves, whistler, Alfvén/magnetosonic; two-stream instability; Rankine-Hugoniot shocks; double layers.
- **Ch. 7 (from prior session — verified):** MHD equations, generalized Ohm's law, frozen-in flux, plasma β, Parker spiral, CGL double-adiabatic invariants, firehose/mirror instability thresholds.
- **Ch. 10 §§10.10–10.11 (pp 323–342):** Escape velocity; Jeans escape flux (Eq 10.84); Liouville exospheric density (Eq 10.98); charge exchange hot-H production (Eqs 10.85–10.86); hot O corona at Venus/Earth/Mars; Monte Carlo methods.
- **Ch. 11 §§11.12–11.16 (pp 375–408):** Rayleigh-Taylor instability full derivation (Eqs 11.79–11.87); sporadic-E metallic ion wind-shear convergence; intermediate layers; F₃ layer and He⁺ layer; nonmigrating tides (wavenumber-4 TEC); ionospheric storms (positive/negative phase, SAPS-SED-TOI, PPEFs, composition changes).

Created 3 new concept pages:
- **Concepts/Ionospheric Storms.md** — positive/negative phase mechanisms; SAPS→SED→TOI→patch storm pathway; PPEF superfountain; composition changes; TID generation; observable quantities table.
- **Concepts/Sporadic E.md** — metallic ion wind-shear convergence mechanism; Fe⁺/Mg⁺ from meteor ablation; properties table; intermediate layers; auroral E-layer distinction.
- **Concepts/MHD.md** — MHD equations; generalized Ohm's law; frozen-in flux theorem; plasma β; Alfvén/fast/slow magnetosonic wave modes; CGL double-adiabatic; Parker spiral derivation.

Substantially updated 6 existing pages:
- **Concepts/Equatorial Ionosphere.md** — added Rayleigh-Taylor instability derivation (§11.12, Eqs 11.79–11.87); F₃ layer and He⁺ layer (§11.14); nonmigrating tides and wavenumber-4 TEC pattern (§11.15); updated sources: 1→2.
- **Concepts/Ionospheric Conductivity.md** — added formal §5.11 derivation of σ_P (Eq 5.119) and σ_H (Eq 5.120); added electron field-aligned current and thermal conductivity (§5.12, Eqs 5.140–5.146); updated sources: 0→1.
- **Concepts/F-Layer.md** — expanded stub→draft; added Chapman production function (Eq 9.21); chemistry-transport competition and βeff altitude dependence; plasma scale height in diffusive equilibrium; nighttime decay and conjugate photoelectron maintenance; topside/bottomside asymmetry; status: stub→draft, sources: 1→2.
- **Concepts/Atmospheric Escape.md** — replaced stub with formal Jeans escape flux (Eq 10.84); Liouville exospheric density (Eq 10.98); full taxonomy of non-thermal mechanisms; hot O corona; updated sources: 0→1.
- **Concepts/Plasma Waves.md** — added S&N Ch. 6 ionospheric wave taxonomy section: two-stream instability growth condition, Rankine-Hugoniot shock details, double layers; updated sources: 0→1.
- **Concepts/Traveling Atmospheric Disturbances.md** — added gravity wave theory foundation section: Brunt-Väisälä frequency, AGW dispersion relation (Eq 10.37), wind filtering/critical levels, TAD parameter table; updated sources: 1→2.
- **Sources/Schunk Nagy 2009 Ionospheres.md** — added Key Claims bullets for Chs. 1–2, 4, 5–7, 10–11; added connections to 9 more concept pages; Methods section now lists complete chapter coverage.

Updated `index.md` — added 3 new concept entries (Ionospheric Storms, Sporadic E, MHD); updated descriptions for Equatorial Ionosphere, F-Layer, Plasma Waves.

`overview.md` not updated — complete S&N coverage deepens theoretical foundations but does not shift the polar-cap research synthesis. All textbook chapters of primary relevance to Michael's research are now ingested.

**Schunk & Nagy ingest now complete.** All priority chapters (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12) covered. Remaining S&N chapters (13 equatorial, 14 planetary ionospheres) are lower priority; Ch. 2 §2.4–2.6 already provides comprehensive planetary coverage. Next textbook priority: Kelley - Earth's Ionosphere.pdf.

## [2026-05-20] lint | Math formatting pass — Unicode → LaTeX inline math

Converted all bare Unicode mathematical symbols (superscripts ⁺⁻²³⁰¹⁴–⁹, subscripts ₀–₉, Greek letters β λ μ Ω, and operators ≈ ≤ ≥ ≪ ≫ × ∇ ∂ ∫) to proper LaTeX `$…$` inline math in all Entity and Concept wiki pages.

Pages touched: all 14 Entity pages (GITM, E-CHAIM, RISR-N, SAMI2, SuperDARN, MAGE, Jicamarca Radio Observatory, Van Allen Probes, and others) and all 30 Concept pages (Airglow, Atmospheric Escape, Aurora, Equatorial Ionosphere, F-Layer, HF Radio Propagation, High-Speed Streams, Ion Frictional Heating, Ionosphere, Ionospheric Energetics, Ionospheric Storms, Joule Heating, Lifting, MHD, Plasma Waves, Polar Cap Patch, Polar Wind, Radiation Belts, Sporadic E, Storm-Enhanced Density, Subauroral Polarization Streams, Tongue of Ionization, Ambipolar Diffusion, Wave-Particle Interactions, Traveling Atmospheric Disturbances, and others).

## [2026-05-20] query | Analyzed wiki state and rewrote overview.md

Read `index.md`, `log.md`, and key concept pages (`Polar Cap Patch`, `Tongue of Ionization`, `Storm-Enhanced Density`, `Ion Frictional Heating`) to synthesize the current wiki state across 59 sources.

Rewrote `overview.md` from a 1-source stub (last updated 2026-05-12) to a full thesis-level synthesis covering:

- D/L/LD event taxonomy as the core finding
- Confirmed storm pathway: ring current → SAPS → SED → TOI → patches
- Patch formation mechanism taxonomy (4 classes + non-classic stagnation)
- UT/seasonal D-parameter framework + Chartier December anomaly complication
- Storm preconditioning and IT system memory (Themens 2024)
- Energy budget and TAD localization (Thayer & Pham)
- Upflow classification and density-as-rate-limiter (Zou 2021)
- Polar wind H⁺ jets and N⁺ contributions (Varney 2026 PatchesChapter, Albarran 2023)
- Modeling landscape table (IPWM/HIDRA, GITM, E-CHAIM, MAGE, SAMI2)
- Decadal Survey 2024 ITM priorities (PSG 1–4, DASHI, LAITIR)
- 7 prioritized open questions

Pages touched: `overview.md` (major rewrite, status stub→mature, sources 1→59).


## [2026-10-07] ingest | Strangeway Ch11 The Aurora + Sivadas 2020 Thesis (§2.6–2.7, §4.3) — kinetic Alfvén waves and auroral acceleration

Triggered by a query on how kinetic Alfvén waves accelerate electrons, how they differ from chorus, and how diffuse, monoenergetic and broadband aurora differ. The query also corrected a premise: KAWs drive **broadband** aurora, not diffuse or monoenergetic. The two-fluid KAW/IAW derivation from the query session was filed as durable content.

- **New sources:** `Sources/Strangeway Ch11 The Aurora.md`, `Sources/Sivadas 2020 Thesis Energetic Precipitation.md`
- **New concepts:** `Concepts/Alfvén Waves.md`, `Concepts/Auroral Acceleration.md`
- **Updated:** `Concepts/Aurora.md`, `Concepts/Plasma Waves.md`, `Concepts/Wave-Particle Interactions.md`, `Concepts/Field-Aligned Currents.md`, `Concepts/MHD.md`, `Entities/AMISR.md`, `Entities/THEMIS.md`, `index.md`
- **Scope note:** the 200C chapter sits in a course folder (out of scope by default) but was ingested at the user's explicit request, following the AOS 205B/250B course-seeding precedent.
- **Flagged for lint:**
  - (1) Three inconsistent Knight relation forms across `Aurora`, `Field-Aligned Currents` and the Strangeway source.
  - (2) `MHD` gives $v_A \approx 200$–$1000$ km/s "at 1 $R_E$", in tension with $v_A \sim 10^4$ km/s in the auroral cavity.
  - (3) Older source pages' `pdf:` links point to `Atlas/Textbooks/` and `Atlas/Papers/`, but the PDFs now live under `Atlas/Texts/`.
  - (4) Claims from memory on `Alfvén Waves` (Hasegawa & Chen ion-FLR term, Kletzing surfing, Newell 2009 taxonomy) need dedicated papers.


## [2026-10-07] ingest | KAW / auroral-acceleration reading list (9 papers)

All 9 PDFs were verified and renamed to the `Lastname YYYY - Title.pdf` convention in `Atlas/Texts/Research_Papers/`. Obsidian-illegal `?` and `:` were dropped; `Alfvén` is spelled with the accent. The Science PDF opens with an unrelated report; the Hasegawa copy is the PPPL-1286 scan.

- **New sources (9):** `Hasegawa Chen 1976 KAW Mode Conversion`, `Kletzing 1994 KAW Electron Acceleration`, `Lysak Lotko 1996 Kinetic Alfvén Dispersion`, `Chaston 2003 FAST Small-Scale Alfvén Waves`, `Keiling 2003 Alfvén Wave Poynting Flux`, `Chaston 2007 DAW Auroral Acceleration Fraction`, `Newell 2009 Global Precipitation Budget`, `Thorne 2010 Chorus Diffuse Aurora`, `Artemyev 2015 KAW Electron Trapping`
- **New entity:** `Entities/FAST.md`
- **Major revisions:** `Concepts/Alfvén Waves.md` (sources 3→11), `Concepts/Auroral Acceleration.md` (4→10)
- **Updated:** `Aurora`, `Wave-Particle Interactions`, `Plasma Waves`, `Field-Aligned Currents`, `MHD`, `Atmospheric Escape`, `Entities/DMSP`, `Sources/Sivadas 2020…`, `Sources/Strangeway Ch11…`, `index.md`

**Resolved from the 2026-10-07 flags:**
- The ion-FLR $\tfrac34\rho_i^2$ term is now sourced (Hasegawa & Chen; Lysak & Lotko).
- The inertial/kinetic transition at about 4–5 $R_E$ is sourced (Lysak & Carlson 1981 via Lysak & Lotko).
- The "Fermi to about $2v_A$" claim is sourced (Kletzing).
- The Newell taxonomy is now sourced.
- The `MHD` $v_A$ tension is resolved: 200–1000 km/s is equatorial; the auroral field line peaks at about $10^4$ km/s (Kletzing, Chaston 2003). A note was added to `MHD`.

**Corrections to my own earlier claims:**
- (a) Plasma-sheet KAWs do *not* generically Landau-damp on the bulk electrons; damping is weak unless $k_\perp\rho_s$ or $k_\perp\lambda_e \gtrsim 1$ (Lysak & Lotko).
- (b) Chorus is not purely pitch-angle scattering; upper-band chorus also scatters strongly in momentum at 1–10 keV (Thorne).
- (c) Broadband aurora is not confined to the poleward boundary; it occurs throughout the oval (Newell, Chaston 2003).
- (d) "About 100 eV typical" holds for the cusp; premidnight medians reach about 4 keV (Chaston 2003).

**New recorded disagreements (not resolved):**
- Diffuse electron scattering: ECH-type electrostatic waves (Newell 2009) vs. chorus (Thorne 2010).
- Alfvénic share of auroral energy: 6–13% (Newell, total including diffuse) vs. 25–39% (Chaston 2007, FAST electrons) vs. 30–35% (Keiling, luminosity). These are different denominators.

**Still open:**
- The Knight relation form mismatch.
- Stale `pdf:` paths on older source pages.
- Hasegawa 1976 *JGR* 81, 5083 (the magnetospheric KAW paper), which is not in the vault.

## [2026-10-07] derivations | Part I — Plasma foundations (6 derivation pages) + error audit

**New page type:** `type: derivation` in a new `Derivations/` folder (decision logged in MEMORY.md). Math is written in the KaTeX-safe subset so it renders in both Obsidian and Quartz.

**New derivation pages:** `Derivations Index`, `Debye Shielding and the Plasma Frequency`, `Guiding-Center Drifts`, `Adiabatic Invariants and Magnetic Mirrors`, `Moment Equations from the Vlasov Equation`, `Ideal MHD from Kinetic Theory`, `MHD Wave Modes`

**New source pages:** `Strangeway Ch3 Physics of Magnetized Plasmas`, `Bellan 2006 Fundamentals of Plasma Physics`, `Thorne 1993 AOS 250B Course Reader` (course reader; in scope by Michael's explicit request), `Siscoe 1983 Solar System MHD`

**Verification performed (scripts in session scratchpad):**
- SymPy: gyration and $\mathbf{E}\times\mathbf{B}$ solutions; gyro-averaged $\langle F\rangle=-\mu\nabla B$; $(\nabla\times\mathbf B)\times\mathbf B$ identity; Yukawa potential; energy-flux moment decomposition; $\mathsf P:\nabla\mathbf u$ identity; $\nabla_v\cdot(\mathbf v\times\mathbf B)=0$; $\nabla\times(\mathbf u\times\mathbf B)$ expansion; $D(\mathbf B/\rho)/Dt$; adiabatic law; MHD 3×3 matrix and eigenvalues; fast/slow pressure-phase ratio; dipole expansions.
- Numerical: test-particle orbits in a dipole (drift period to 0.15%, bounce period to 0.3%); polarization drift (exact); curl-free curvature identity; $F(\pi/2)=1.380$; Thorne Table 6.1 reproduced (bounce 17.59 vs 17.57 s; drift 6480 vs 6495 s; gyro 0.143 vs 0.139 s).

**Errors found and corrected (marked inline with "Corrected 2026-10-07"):**
- `MHD`: firehose and mirror conditions were swapped (now per Siscoe 1983 §IV.1); ionospheric β was given as ≫ 1 (actually about $4\times10^{-5}$); Gaussian $\beta$, $v_A$ and tension in an SI page converted; Parker spiral 43° → 45°; the slow-mode formula is now labelled as the near-perpendicular limit and the general dispersion relation added.
- `Ambipolar Diffusion`: sign of the temperature-gradient term in the diffusive-equilibrium profile (− → +).
- `Radiation Belts`: bounce period "~0.1–1 s" only applies to electrons (protons ~1–30 s); gyroperiod ranges tightened; dipole loss-cone formula added.
- `Plasma Waves`: Gaussian $v_A$ → SI; Bohm–Gross $v_{th}$ definition made explicit.

**Updated (Derivations links):** `MHD`, `Radiation Belts`, `Ring Current`, `Plasma Waves`, `Alfvén Waves`, `Field-Aligned Currents`, `index.md`

**Flagged, not changed:**
- `Blelly Schunk 1993 Moment Comparison`: the table lists the 13-moment variables as $T_\parallel, T_\perp, q_\parallel, q_\perp$, which looks like the 16-moment (bi-Maxwellian) set. Needs checking against the paper.
- `overview.md`: `Dst$_\min$` → `Dst$_{\min}$`, the only KaTeX parse failure across all 3,205 math blocks in the wiki (checked with KaTeX 0.16.11).

## [2026-10-07] lint | Blelly & Schunk 1993 source page re-checked against the PDF

Re-read §2–5 of the paper and corrected `Sources/Blelly Schunk 1993 Moment Comparison` (all marked inline):
- The 13-moment variables are $n, u, T_\parallel, T_\perp$ and a **single** $q$ (Eqs. 28–42). The table had listed the 16-moment $q_\parallel, q_\perp$.
- The 16-moment mean energy is $(E_\parallel + 2E_\perp)/2$; the factor 1/2 was missing. Thermoelectric/diffusion-thermal terms are present in 8/13/16, not only 16.
- The standard set peaks at a *higher altitude* with a *lower* scale height (was "higher scale height").
- The 13-moment instability is an *electron* blow-up when O$^+$ goes supersonic, which is why Mach 0.9 was imposed on all models. It had been misattributed to H$^+$ $T_\parallel\gg T_\perp$ via Eq. 52.
- The two H$^+$ fronts are the thermal response and the O$^+$-tied polarization field, not the $u\pm c_s$ edges.
- Electron oscillations occur in both the 13- and 16-moment sets (was 16 only).
- H$^+$ heating above 1000 km is frictional (was "from O$^+$ via charge exchange").
- $A\propto r^3$ (was $r^{-3}$).
- Stale `pdf:` path fixed.
- `Entities/IPWM`: the "8-moment is the optimum per Blelly" claim is now labeled as a wiki inference. Varney 2014 derives its 8-moment set as 13-moment with zero stress and does not cite Blelly for the choice.

## [2026-10-07] derivations | Five held derivations researched and written (Knight, Landau, QL, KP, ISR)

**New derivation pages:** `Knight Relation`, `Landau Damping`, `Quasilinear Diffusion`, `Kennel-Petschek Limit`, `Incoherent Scatter Spectrum`. Michael asked for web research plus a consensus or an explanation of disagreements; each page has a "why forms differ" section.

**Verification highlights:**
- **Knight:** quadrature and a $2\times10^6$-particle Monte Carlo reproduce the closed form. All published forms are limits of one relation.
- **Landau:** exact $Z$-function roots (e.g. $1.4157-0.1534i$ at $k\lambda_D=0.5$). The $e^{-3/2}$ form is 5–7× more accurate than the form without it.
- **QL:** bump-on-tail simulation forms a plateau, conserves particles, momentum and energy, and confirms the factor-2 Langmuir wave energy.
- **KP:** limit derived in SI and matched to Summers' Eq. B8 and B10 numbers. KP's lifetime formula 4.11 reproduced numerically to within 0.2%.
- **ISR:** Varney (2012) thesis spectrum verified (sum rules, Fig. 2.1 peaks, the free-electron limit). Discrepancy found: the closed-form total power is exact only for $T_e=T_i$ (+1%/+7% at $T_e/T_i=2/4$).

**Errors corrected (inline-marked):**
- `Field-Aligned Currents`: dimensionally wrong $\Phi^{1/2}$ Knight form replaced.
- `Aurora`: wrong-unit Knight $K$ fixed.
- `Auroral Acceleration`: flag resolved.
- `Wave-Particle Interactions`: a lifetime was called a rate; strong/weak-diffusion nature of the KP limit clarified; KP $L$-range was "$L\le12$", now "$L>4$".
- `Kennel 1966` source page: strong-diffusion claim ("flux cannot exceed") corrected; observational $L$-dependence was reversed.

**Housekeeping:** 53 stale `pdf:` links (`Atlas/Papers/...`) repointed to `Atlas/Texts/...` by unique filename match. Whole wiki passes KaTeX (3,786 blocks).

**Web sources used:** Gunell et al. 2013 (*Ann. Geophys.*, OA); Finn et al. 2023 (arXiv:2303.12620, abstract); ISRSpectrum code (Swoboda, GitHub); Kudeki & Milla 2011 and Fejer & Kohl 1980 (metadata/abstract only).

## [2026-10-07] derivations | Part II begun — Chapman Layer, Plasma Diffusion Along B

**New derivation pages:** `Chapman Layer`, `Plasma Diffusion Along B` (named to avoid colliding with the `Ambipolar Diffusion` concept page).
**Sources:** 200C textbook Ch. 2; AOS 205B Lectures 1.2 and 3.2 (course notes); Schunk & Nagy Ch. 5, 9, 11.
**Verification:**
- SymPy: Chapman $\tau(z_{\max})=1$, $P_{\max}$, universal form, near-peak expansion; collisional parallel flux including the wind term; minor-ion scale height ($H_{H^+}=-k_BT/7m_pg$).
- Numerical: production and α-layer FWHM (2.45H, 3.59H). A steady diffusion–chemistry BVP shows the F2 peak tracks $\beta=D/H_O^2$ within 4 km, while $\beta=D/H_p^2$ misses by about 22 km.

**Errors corrected (inline-marked):**
- `F-Layer`: the F2 peak was explained as "production = chemical loss"; it is actually where the chemical and diffusion times are equal (S&N §11.4). The F1 ledge was attributed to X-rays; it is at the 17–91 nm EUV production peak (200C Ch. 2). Diffusive-equilibrium sign error (as on `Ambipolar Diffusion`). sech² mislabelled as α-Chapman (it is the Epstein shape).
- `Ionospheric Energetics`: He II 30.4 nm photoelectron energy was given as ~41 eV, which is the photon energy; the O photoelectron gets about 27 eV.

**Course-note slip noted (not edited):** AOS 205B Lecture 1.2 writes the $X\ll-1$ Chapman limit as $\exp(e^{-X})$; it should be $\exp(-e^{-X})$.

## [2026-10-07] derivations | Part II — conductivity, heating, dynamo

**New derivation pages:** `Pedersen and Hall Conductivity`, `Frictional and Joule Heating`, `Electrostatic Dynamo Equation`.
**New source page:** `Kelley Earth's Ionosphere` (stub; Ch. 2 §2.2 read).
**Sources:** AOS 205B Lectures 6.1, 6.2 and 8.1 (course notes); Kelley §2.2; S&N §5.11, Eq. 5.36, §5.13.
**Verification (SymPy):**
- mobility tensor from force balance;
- σ_P and σ_H in κ form;
- Hall current opposite to E×B;
- F-region σ_P limit;
- steady T_i;
- neutral heating = σ_P|E'|²;
- J·E split;
- dynamo PDE identity in both hemispheres;
- Cowling conductivity;
- convection-cell rotation sense.

**Errors corrected (inline-marked):**
- `Ionospheric Dynamo`: master-equation overall sign (for downward J∥); dawn and dusk cell rotation senses were reversed.
- `Ionospheric Conductivity`: κ_i = 1 altitude refined (130 km per Kelley).

**Flagged, unresolved:** |κ_e| = 1 altitude is about 75 km in Kelley Fig. 2.5 (B = 0.25 G) vs about 90 km in the AOS 205B notes.

## [2026-10-08] derivations | Part II complete — instabilities, polar wind, Appleton–Hartree

**New derivation pages:** `Gradient-Drift and Rayleigh-Taylor Instabilities`, `Polar Wind Transonic Outflow`, `Appleton-Hartree Equation`.
**New source page:** `Davies 1966 Ionospheric Radio Propagation` (stub; §2.3 read).
**Verification:**
- SymPy: exact GDI dispersion relation; RT as GDI with effective field $(B/\nu_{in})\mathbf{g}\times\hat{\mathbf b}$ giving $g/\nu_{in}L$; Mach equation from momentum plus continuity; sonic radius $GM/pV_S^2$; exact integral of motion.
- Numerical: Appleton–Hartree vs Stix cold-plasma over 20,000 random cases (max relative difference $7.6\times10^{-12}$).

**Errors corrected (inline-marked):**
- `Ionospheric Instabilities`: GDI growth-rate expression had no $\hat{\mathbf b}$ (undefined sign); "equatorward gradient" at the trailing edge.
- `Polar Wind`: "flux tubes open above 2500 km" and a fixed sonic altitude; 13-moment instability misattributed (as on Blelly).
- `HF Radio Propagation`: $X$ coefficient $8.06\times10^{-6}$ → $8.06\times10^{-5}$ (factor 10).

**Links:** fixed 2 stale links to `Zou 2021 Polar Cap Density Structure Advances`. Six links to nonexistent pages (`Ion Upflow` ×5, `Magnetotail`) left for Michael.
**Unverified, labelled on page:** E-region loading factor $\Sigma_P^F/(\Sigma_P^F+\Sigma_P^E)$ (not found explicitly in Kelley).
**Whole wiki:** 4,737 math blocks pass KaTeX.

## [2026-10-08] derivations | Part III complete — solar wind, shocks, magnetopause, reconnection, DPS, cold-plasma waves, dipole

**New derivation pages (7):**
- `Parker Solar Wind and Spiral`
- `Rankine-Hugoniot Jump Conditions`
- `Chapman-Ferraro Standoff Distance`
- `Sweet-Parker Reconnection`
- `Dessler-Parker-Sckopke Relation`
- `Cold-Plasma Waves`
- `Dipole Field and L-Shells`

**New concept pages (2):** `Ion Upflow` and `Magnetotail`. This reverses the 2026-05 decision not to create an `Ion upflow` page; Michael approved it. It resolves 6 dangling links.

**New source page (1):** `Velli Basics of Plasma Astrophysics` (Chiuderi & Velli 2015).

**Updated:**
- `Derivations Index` (Part III table); `index.md`.
- `Siscoe 1983 Solar System MHD` (§§II–III read).
- Derivation backlinks on `MHD`, `Dungey Cycle`, `Ring Current`, `High-Speed Streams`, `Radiation Belts`, `Magnetic Coordinate Systems`, `Polar Wind`, `Wave-Particle Interactions`, `Field-Aligned Currents`.
- `next:` links on `Polar Wind Transonic Outflow`, `Appleton-Hartree Equation`, `MHD Wave Modes`.

**Corrections to existing pages (marked inline):**
- `Parker 1958 Solar Wind`: the ~500 cm⁻³ density was Biermann's input, not a confirmed prediction (measured ~5–10 cm⁻³).
- `Plasma Waves`:
  - lower-hybrid $\sqrt{\Omega_i\Omega_e}$ is only the dense limit (11% high at $L=4$ outside the plasmapause);
  - AKR "R-X cutoff below $f_{ce}$" needs the relativistic qualifier from Strangeway Ch. 11.
- `High-Speed Streams`: caveat that a hotter corona alone doesn't explain the fast wind.
- `Gerard 1980` source page: pdf link Unicode-normalized (NFD) to match the filename.

**Errors found in source texts (not edited; documented on derivation pages):**
- 200C Eq. 6.15 (RH quartic): $y^1$ and $y^0$ coefficients wrong by $2c(y-1)$. Verified against an independent SymPy derivation, the perpendicular limit and a brute-force solve.
- 200C errata sheet: "tangential velocity unchanged across a shock" is false for oblique MHD shocks.
- 200C Eq. 7.23b: Shue 1998 exponent written as −1/6; the published value is −1/6.6 (web-verified).
- 200C Eq. 5.8: text says $p = nkT$, but the equation needs $p = 2nkT$.
- 200C Eq. 7.19: $K(M=4.5) = 0.8945$ computed vs 0.897 quoted (0.3%, unexplained).

**External source used:** Vasyliūnas (2006), *Ann. Geophys.* 24, 1085, as the second source for DPS.

**Checks:** 5,612 math blocks pass KaTeX; 0 broken wiki-links.
