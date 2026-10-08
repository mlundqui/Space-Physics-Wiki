---
type: source
status: draft
updated: 2026-05-13
sources: 1
authors: David, Sojka, Schunk, Coster
year: 2016
tags: [patches, TOI, GPS-TEC, UT-dependence]
---

# David 2016 — Polar Cap Patches and the Tongue of Ionization: A Survey of GPS TEC Maps (2009–2015)

## Summary

Seven-year survey of Madrigal GPS TEC maps from the Northern Hemisphere polar cap (2009–2015) to test whether [[Polar Cap Patch|patches]] and the [[Tongue of Ionization]] (TOI) show the UT and seasonal dependence predicted by the Sojka et al. [1994] TDIM model. The answer is yes, and this confirmation has a critical implication: any patch source mechanism that lacks a UT/seasonal dependence (particle precipitation, FTEs, cusp electric field) is ruled out as the dominant plasma source. The surviving candidate is solar-illuminated dayside plasma transported antisunward by the convection electric field — the Sato [1959] / Sojka [1994] mechanism.

## Key claims

- GPS TEC maps from Madrigal (MIT Haystack) for 2009–2015 show a strong UT and seasonal dependence of the tongue-to-background ratio (TBR) consistent with the 1994 TDIM prediction: prime patch conditions are 1800–0300 UT in winter; a "hole" devoid of patches occurs at 0500–1200 UT in winter; equinox shows a broad band of patch availability at 0400–1400 UT.
- The winter hole (absence of patches at 0500–1200 UT) reflects the geometry of the solar terminator: at those times the dayside plasma is too far equatorward for the convection electric field to entrain it across the open–closed boundary. Since the hole recurs every year, any mechanism that does not depend on this geometry (precipitation, FTEs, cusp fields) is ruled out as the dominant source.
- TEC patches and TOIs are observationally equivalent: in the Madrigal data "patches are just a TOI that has been structured." Airglow patches may be a completely separate phenomenon.
- Geomagnetic activity level (Kp) has little effect on TOI/patch occurrence frequency, consistent with the solar-illumination source hypothesis — the source is not controlled by activity, only the structuring mechanism may be.
- The TBR reaches a maximum of ~2.0 in the Madrigal data vs ~3.0 in the 1994 model; the discrepancy is attributed to known patch location averaging, not a disagreement in physics.
- Solar cycle scaling is present: 2009–2010 (solar minimum) shows lower TBR than 2013 (moderate activity); this is expected from the solar-illumination mechanism where higher EUV produces more dayside plasma.

## Methods / data

- Source: Madrigal GPS TEC database, MIT Haystack Observatory. ~5000 GPS receivers processed by MAPGPS (Rideout and Coster, 2006). Data available from 2009 onward in NH polar cap coverage sufficient for this study.
- Cadence: 5-minute TEC maps in 1° × 1° geographic bins, recast to magnetic polar coordinates.
- Algorithm: for each of 288 daily strips, TBR = TEC in a 1200 km center segment / average of two flanking 1200 km background segments. TBR ≥ 1.5 constitutes a patch/TOI event.
- Coverage: 2009–2015 (7 years); figures shown for representative year 2013, other years in supporting information.

## Connections

- [[Polar Cap Patch]] — confirms solar-illumination transport as dominant plasma source; rules out local sources
- [[Tongue of Ionization]] — GPS TEC study confirms patches are structured TOI; same physical phenomenon
- [[Dungey Cycle]] — convection pattern determines whether dayside plasma can be entrained; the UT dependence arises from geographic vs geomagnetic pole offset
- [[OMNI]] — geomagnetic indices used to check Kp dependence

## Open questions

- The mechanisms responsible for structuring (chopping the TOI into patches) are explicitly left as a future study; the David et al. dataset of smooth-TOI vs patchy days would be an ideal basis.
- Does the UT/seasonal morphology change during extreme events (e.g., CH/HSS-driven storms without strong southward $B_z$)?
