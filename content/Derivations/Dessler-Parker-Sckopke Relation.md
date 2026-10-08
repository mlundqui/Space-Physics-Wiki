---
type: derivation
status: draft
updated: 2026-10-08
sources: 3
tags: [derivations, ring-current, Dst, storms, magnetosphere, drifts]
prerequisites: "[[Guiding-Center Drifts]] (∇B drift, magnetic moment); [[Adiabatic Invariants and Magnetic Mirrors]] (dipole geometry)"
next: "[[Cold-Plasma Waves]]"
---

# Dessler-Parker-Sckopke Relation

**Part III, page 7** of the [[Derivations Index]] · Builds on: [[Guiding-Center Drifts]] · Concept pages: [[Ring Current]], [[Ionospheric Storms]] · Related: [[Chapman-Ferraro Standoff Distance]]

## Where we're going

During a geomagnetic storm, the horizontal field at low-latitude magnetometers drops by tens to hundreds of nT, and the **Dst** index records that drop. The cause is the **ring current**: hot ions (10–200 keV) drifting westward around the Earth ([[Ring Current]]). The Dessler–Parker–Sckopke (DPS) relation is the remarkable result that this depression measures **only the total kinetic energy** of the trapped particles:

$$\frac{\Delta B}{B_0} = -\frac23\frac{W_{\rm part}}{W_{\rm mag}}.$$

It is independent of how that energy is distributed in $L$, pitch angle or species. That's why Dst works as an energy meter for storms.

We'll derive it the way Dessler and Parker (1959) did, by adding up drift and gyration currents for particles at the equator. Then we'll discuss why it holds far more generally (Sckopke 1966, and the virial-theorem proofs). Sources: 200C textbook Ch. 9 (Eqs. 9.4–9.10) and Vasyliūnas (2006).

---

## 1. One particle, two currents

Take an ion with perpendicular energy $W_\perp$ mirroring at the equator, at radius $r$ in a dipole field $B(r) = B_0(R_E/r)^3$. It contributes **two** currents, and both produce a field at Earth's center.

**(a) The drift current.** From [[Guiding-Center Drifts]], the ∇B drift is $\mathbf v_D = W_\perp\,\mathbf B\times\nabla B/(qB^3)$ (200C Eq. 9.4). In the equatorial dipole, $|\nabla B|/B = 3/r$, so

$$v_D = \frac{3W_\perp}{qBr}.$$

The drift is **westward** for ions and eastward for electrons, so both carry westward current. One particle going around a circle of circumference $2\pi r$ is a current $I = qv_D/2\pi r$. A current loop of radius $r$ produces a field $\mu_0I/2r$ at its center:

$$\delta B_{\rm drift} = -\frac{\mu_0}{2r}\cdot\frac{q}{2\pi r}\cdot\frac{3W_\perp}{qBr} = -\frac{3\mu_0W_\perp}{4\pi Br^3} = -\frac{3\mu_0W_\perp}{4\pi B_0R_E^3}.$$

The minus sign means **southward**, opposing the dipole's equatorial field. Notice the last step: in a dipole, $Br^3 = B_0R_E^3$ is the same on every field line, so **the result doesn't depend on $r$**. That's the first hint of the magic.

**(b) The gyration current.** The particle's gyration is a tiny current loop with magnetic moment $\mu = W_\perp/B$. It is **diamagnetic**, pointing opposite to $\mathbf B$. A dipole $\mathbf m$ produces a field $-\mu_0\mathbf m/4\pi r^3$ in its own equatorial plane. With $\mathbf m$ pointing south, that field at Earth's center points **north**:

$$\delta B_{\rm gyro} = +\frac{\mu_0W_\perp}{4\pi Br^3} = +\frac{\mu_0W_\perp}{4\pi B_0R_E^3}.$$

The gyration partly *cancels* the drift. That's not a coincidence. In fluid language, the gyration loops add up to a **magnetization current** $\nabla\times\mathbf M$, which runs *eastward* on the inner edge of the ring current and westward on the outer edge ([[Strangeway Ch3 Physics of Magnetized Plasmas|Strangeway Ch. 3]] §3.7.2).

**(c) Total** (200C Eq. 9.7):

$$\Delta B_{\rm part} = -\frac{3\mu_0W_\perp}{4\pi B_0R_E^3} + \frac{\mu_0W_\perp}{4\pi B_0R_E^3} = -\frac{\mu_0W_\perp}{2\pi B_0R_E^3}.$$

Since each particle's contribution is independent of $r$, the contributions just **add**. For an equatorial population with total energy $W_{\rm part}$, replace $W_\perp$ with $W_{\rm part}$.

---

## 2. Comparing with the dipole's own energy

The magnetic energy of the dipole field outside the Earth is (200C Eq. 9.8; SymPy)

$$W_{\rm mag} = \int_{r>R_E}\frac{B_{\rm dip}^2}{2\mu_0}\,dV = \frac{4\pi B_0^2R_E^3}{3\mu_0}\approx8.3\times10^{17}\ \text{J}.$$

Divide $\Delta B$ by $B_0$ and use $\mu_0/B_0^2R_E^3 = 4\pi/(3W_{\rm mag})$:

$$\boxed{\frac{\Delta B}{B_0} = -\frac{2}{3}\,\frac{W_{\rm part}}{W_{\rm mag}}}\qquad\text{(DPS; 200C Eq. 9.9)}$$

This is the same as Vasyliūnas's (2006) Eq. 1, $\boldsymbol\mu\cdot\mathbf b(0) = 2U_K$, in Gaussian units with $\mu = B_0R_E^3$ and $W_{\rm mag} = B_0^2R_E^3/3$. That gives $b/B_0 = 2U_K/(3W_{\rm mag})$ in magnitude. The sign is set by $\boldsymbol\mu$ pointing south, so a depression gives $\boldsymbol\mu\cdot\mathbf b > 0$.

**In numbers** ($B_0 = 3.1\times10^4$ nT):

$$\Delta B\,[\text{nT}]\approx-\frac{W_{\rm part}}{4.0\times10^{13}\ \text{J}}.$$

So a Dst of $-100$ nT corresponds to about $4\times10^{15}$ J of ring-current energy.

---

## 3. Why it's so general, and why textbook numbers differ

**Arbitrary distributions.** Our derivation used equatorially mirroring particles. Particles with other pitch angles also have **curvature drift** (driven by $W_\parallel$) and a ∇B drift averaged over the bounce. Sckopke (1966) showed that when everything is summed in a dipole, $W_\perp$ is simply replaced by the **total** kinetic energy, $W_\perp + W_\parallel$. The later virial-theorem derivations (Olbert et al. 1968, and others, reviewed in Vasyliūnas 2006) drop even the assumptions of linearity and axial symmetry. A partial (asymmetric) ring current gives the same *globally averaged* depression.

The virial theorem is the deep reason the answer depends only on energy. For a plasma in force balance, $\mathbf J\times\mathbf B = \nabla\cdot\mathsf P$, and the moment $\int\mathbf r\cdot(\mathbf J\times\mathbf B)\,dV$ that controls $\mathbf b(0)$ equals $\int\mathrm{tr}\,\mathsf P\,dV = 2U_K$ after integrating by parts.

**Why "2.8×10¹³ J/nT" (200C Eq. 9.10) and not 4.0×10¹³.** The DPS field is the field at Earth's center, or equivalently the average over the surface. But Earth's interior **conducts**. A slowly varying external field induces currents inside the Earth whose field adds to the *horizontal* component at the surface. For a perfectly conducting sphere, the enhancement is exactly 3/2. The real Earth's conducting layers are deeper than the surface, so the factor is a bit smaller. The 200C coefficient implies $4.0/2.8 = 1.43$, which is in that range. Both numbers are "right": $4.0\times10^{13}$ J/nT is the DPS field from the ring current alone, and $2.8\times10^{13}$ J/nT is what a surface magnetometer sees. (The 3/2 for a superconducting sphere is my calculation; the 200C text just says shielding "enhances the surface effect.")

**Dst isn't only the ring current.** Other contributions:

- **Magnetopause (Chapman–Ferraro) currents** give a *positive* contribution that grows with $\sqrt{\rho u^2}$. That's the storm sudden commencement ([[Chapman-Ferraro Standoff Distance]]). Pressure-corrected indices ("Dst*") remove it empirically.
- **Tail currents** add a negative contribution.
- **Boundary and ionospheric terms** in the virial theorem (Vasyliūnas 2006) are generally small compared with the plasma energy term.
- **Non-dipole fields.** Near the outer edge (beyond about 5–6 $R_E$) the field isn't dipolar.

**200C's worked example.** A Dst drop of 200 nT over about 9000 s, during a storm with IMF $B_z\approx-10$ nT and 1000 km/s solar wind, gives $5.6\times10^{15}$ J, delivered at $6.2\times10^{11}$ W. That's comparable to the energy reconnection loads into the tail ([[Sweet-Parker Reconnection]] §4 context; 200C Ch. 9).

---

## What we assumed, and where it breaks

- **Linear.** The ring-current field is treated as a small perturbation of the dipole. During superstorms ($|{\rm Dst}|\sim500$ nT), the ring current inflates the field and the drift paths themselves change. The virial form survives better than the drift-sum form.
- **Dipole geometry.** The $r$-independence used $Br^3 = $ const, which is exact only for a dipole.
- **Trapped particles only.** Particles on open or reconnecting field lines, and plasma near the magnetopause, contribute boundary terms.

---

## Verification

- **Sources agree.**
  - Drift field $-3\mu_0W_\perp/4\pi B_0R_E^3$, gyration field $+\mu_0W_\perp/4\pi B_0R_E^3$, dipole energy, DPS ratio, 2.8×10¹³ J/nT with shielding, worked storm example: 200C textbook Ch. 9 §9.7, Eqs. 9.4–9.10.
  - The general form $\boldsymbol\mu\cdot\mathbf b(0) = 2U_K$, its history (Dessler & Parker 1959; Sckopke 1966; virial derivations) and boundary/ionospheric corrections: Vasyliūnas, V. M. (2006), *Ann. Geophys.* 24, 1085–1097 ([link](https://angeo.copernicus.org/articles/24/1085/2006/)), Eqs. 1–2. Converted from Gaussian units, this matches the 2/3 factor.
  - The magnetization current partly cancelling the drift current: [[Strangeway Ch3 Physics of Magnetized Plasmas|Strangeway Ch. 3]] §3.7.2.
- **SymPy.**
  - Continuous equatorial distribution with a generic radial profile: drift currents give exactly $-3$ and magnetization currents $+1$ (in units of $\mu_0W/4\pi B_0R_E^3$), confirming that the $r$-independence holds for a distributed ring current and not just a single particle.
  - $W_{\rm mag} = 4\pi B_0^2R_E^3/3\mu_0$ by direct integration of $B_{\rm dip}^2/2\mu_0$.
- **Numerical.**
  - $W_{\rm mag} = 8.28\times10^{17}$ J.
  - $4.01\times10^{13}$ J/nT unshielded, and the ratio 1.43 to 200C's value.
  - The 200C worked example ($200\times2.8\times10^{13} = 5.6\times10^{15}$ J).
- **Not verified here:** Sckopke's arbitrary-pitch-angle generalization (cited from Vasyliūnas 2006's summary, not re-derived), and the Earth-conductivity factor for the real Earth.

## Sources

- 200C textbook Ch. 9 §9.7, *Solar wind–magnetosphere coupling* (`Atlas/Texts/Textbooks/200C Textbook/Ch9_SolarWindMagnetosphereCoupling.pdf`)
- Vasyliūnas, V. M. (2006), Ionospheric and boundary contributions to the Dessler–Parker–Sckopke formula for Dst, *Ann. Geophys.*, 24, 1085–1097 (external; open access)
- [[Strangeway Ch3 Physics of Magnetized Plasmas]] — §3.7.2 (drift vs. magnetization currents)
- [[Guiding-Center Drifts]] — the ∇B drift
