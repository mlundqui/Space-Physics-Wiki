---
type: entity
status: draft
updated: 2026-05-19
sources: 1
tags: [instrument, radar, ISR, equatorial]
---

# Jicamarca Radio Observatory (JRO)

The world's largest incoherent scatter radar (ISR), located near Lima, Peru, at geographic latitude −11.95°N, longitude −76.87°E — effectively at the magnetic dip equator. JRO operates at 49.92 MHz on a 300 m $\times$ 300 m fixed phased array and has been continuously providing equatorial ionospheric measurements since 1961. It is the canonical observing platform for equatorial ionospheric electrodynamics, electron and ion temperature profiles, plasma drifts, and instability phenomena (equatorial spread-F, NEIALs).

## Location and Geometry

JRO sits directly on the magnetic dip equator, making it uniquely positioned to observe equatorial phenomena: the equatorial electrojet (EEJ), equatorial plasma bubbles, the fountain effect shaping the equatorial ionization anomaly (EIA), and the vertical $E\times B$ drifts that drive all of these. The nearly horizontal magnetic field (~1° dip angle at JRO) also means the antenna beam can be directed perpendicular to B for incoherent scatter or nearly parallel to B for coherent scatter and plasma drift measurements.

## Operating Modes

**Standard (perpendicular-to-B) mode:** Measures electron density profiles. When the beam is perpendicular to B the ISR power spectrum is dominated by the ion acoustic peak, enabling clean electron density profiles.

**Oblique / Faraday mode:** Used for electron and ion temperature measurements. The oblique mode simultaneously measures two orthogonal polarizations; the difference in their power spectra is sensitive to T_e and T_i through the Faraday rotation admittance.

**Full profile mode (Hysell et al. 2008):** A high-accuracy technique based on the Swartz-Farley admittance matrix formalism. Jointly inverts for T_e, T_i, and N_e across the full altitude profile (~150–1600 km), including the challenging region below the F-peak where E-region contributions complicate the spectrum. This mode provides the electron and ion temperature data used in [[Varney 2012 Thesis]] for [[SAMI2]] validation.

## Reference Observations Used in SAMI2-PE

The key JRO datasets in [[Varney 2012 Thesis]]:

- **Reference day:** March 25, 2009 — F10.7 = 68.2, Ap = 4.0 nT; geomagnetically quiet solar minimum. Used for all primary SAMI2-PE comparisons. The full-profile analysis provides T_e and T_i from ~150 to 1600 km as functions of local time.
- **Day-to-day variability dataset:** July 8–13, 2008 — 6 consecutive days; F10.7 = 67.7, Ap = 3.0 nT; one of the longest continuous full-profile-mode experiments run at JRO. Reveals ~500 K day-to-day T_e variability at 1370 km that SAMI2-PE with climatological drivers cannot reproduce.

Key observational features of equatorial topside T_e from JRO (Hysell et al. 2008; Aponte et al. 1999):
- T_e rises rapidly at dawn to ~3500 K when N_e is lowest and neutral densities are smallest
- T_e decreases during midday as N_e increases and the thermosphere expands
- T_e rises again slightly in the late afternoon as the thermosphere begins to retract
- T_e at 250 km exhibits a local maximum driven by N($^2$D) quenching, with high sensitivity to neutral NO density

## Electrodynamic Monitoring

Because SAMI2-PE requires $E\times B$ drift inputs and JRO was not in beam-steering mode during the reference observations, vertical drifts are estimated from magnetometer data. The JRO staff operate magnetometers at Jicamarca (on the dip equator) and Piura (a few degrees off-equator). Their horizontal-component difference ΔH is primarily controlled by the equatorial electrojet current, which is in turn proportional to the zonal electric field responsible for vertical $E\times B$ drifts. A neutral network converts ΔH into vertical drift estimates (Anderson et al. 2004). Planned upgrades to a phased-array beam-steerable antenna will permit simultaneous T_e and $E\times B$ drift measurements.

## Connections

- [[Equatorial Ionosphere]] — EEJ, EIA, equatorial plasma bubbles, PRE: all observed at JRO
- [[Ionospheric Energetics]] — T_e, T_i measurements that motivated SAMI2-PE development
- [[SAMI2]] — primary model validated against JRO full-profile data
- [[AMISR]] — represents the family of modern phased-array ISRs that complement JRO at high latitudes
- [[NEIALs]] — coherent scatter analog of ISR instability physics; also observed at JRO during active conditions

## Sources

- [[Varney 2012 Thesis]]
