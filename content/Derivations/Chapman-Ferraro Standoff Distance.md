---
type: derivation
status: draft
updated: 2026-10-08
sources: 3
tags: [derivations, magnetopause, magnetosphere, solar-wind, pressure-balance, bow-shock]
prerequisites: "[[Rankine-Hugoniot Jump Conditions]] (shock jumps); [[Ideal MHD from Kinetic Theory]] (magnetic pressure)"
next: "[[Sweet-Parker Reconnection]]"
---

# Chapman-Ferraro Standoff Distance

**Part III, page 5** of the [[Derivations Index]] · Builds on: [[Rankine-Hugoniot Jump Conditions]] · Concept pages: [[Dungey Cycle]], [[MHD]]

## Where we're going

How big is the magnetosphere? Chapman and Ferraro (1930) answered this before anyone knew the solar wind was continuous. A conducting plasma stream can't penetrate a magnetic field, so it carves out a cavity, and the cavity's edge sits where the plasma's push balances the field's pressure. We'll make that quantitative in three steps:

1. Find how much the boundary currents **compress** the dipole field.
2. Find how much of the solar wind's momentum flux actually **reaches** the boundary, once it has passed through the bow shock.
3. Balance the two.

The answer, $R_{mp}\propto(\rho u^2)^{-1/6}$, is one of the most robust scalings in magnetospheric physics. We follow 200C textbook Ch. 7 §§7.3–7.4 (Eqs. 7.11–7.22) and §7.6.1, check it against the Shue et al. (1998) empirical model, and use [[Siscoe 1983 Solar System MHD|Siscoe (1983)]] for the stagnation-point physics.

---

## 1. The image dipole: why the field doubles

Idealize the solar wind as a **perfect conductor** filling the half-space $x > L$ (sunward). A perfect conductor excludes magnetic field, so the normal component $B_x$ must vanish on the plane $x = L$. Surface currents on the boundary, the **Chapman–Ferraro currents**, arrange themselves to make that happen.

Rather than solving for the currents directly, use the method of images. Put a second, **identical** dipole (same orientation) at $x = 2L$. By symmetry, the normal components from the two dipoles cancel on the midplane. SymPy confirms that $B_x = 0$ everywhere on $x = L$. The field inside the cavity is the dipole plus its image.

At the subsolar point $x = L$, both dipoles contribute the same equatorial field, $B_0(R_E/L)^3$, pointing the same way:

$$B_{mp} = 2\,B_0\left(\frac{R_E}{L}\right)^3\qquad\text{(planar boundary: compression factor }a = 2\text{)}.$$

The real boundary is curved, and curvature compresses the field more. In the opposite limit of a **spherical** superconducting shell of radius $R$, the shielding currents produce a uniform internal field $-2m/R^3$ that cancels $B_r$ at the shell. At the equator this *adds* to the dipole's own $-m/R^3$, giving $a = 3$. The real magnetopause lies in between: Tsyganenko's model with the observed boundary shape gives about $2.4$ (200C §7.3).

**The Chapman–Ferraro current.** The jump in tangential $\mathbf B$ across the boundary is carried by a surface current $\mathbf K = \hat{\mathbf n}\times(\mathbf B_{\rm out} - \mathbf B_{\rm in})/\mu_0$. At the nose, $\hat{\mathbf n} = +\hat{\mathbf x}$ (sunward), $\mathbf B_{\rm in} = +B_{mp}\hat{\mathbf z}$ and $\mathbf B_{\rm out}\approx0$. That gives $\mathbf K = +(B_{mp}/\mu_0)\,\hat{\mathbf y}$: **dawn to dusk** across the dayside. For $B_{mp}\approx75$ nT, $K\approx0.06$ A/m.

> **Particle picture.** Solar-wind ions and electrons entering the field turn half a gyro-orbit and are reflected. Ions turn one way and electrons the other, so the net drift is a current. That current is the boundary layer, which is about an ion gyroradius thick for a Chapman–Ferraro sheet.

---

## 2. How hard does the solar wind push? The factor $K$

Upstream, almost all the solar wind's pressure is **dynamic**: $\rho_\infty u_\infty^2$. Thermal and magnetic pressures add only about 1% (200C §7.4.1). At the magnetopause the flow is tangential, so the dynamic pressure contributes nothing *directly*. The push comes from the thermal and magnetic pressure of the magnetosheath, which the decelerated flow has built up.

To relate the two, follow the stagnation streamline in two steps.

**Step 1: through the bow shock.** Use the normal-shock jumps from [[Rankine-Hugoniot Jump Conditions]] §2 (200C Eqs. 7.17–7.18):

$$\frac{p}{p_\infty} = 1 + \frac{2\gamma}{\gamma+1}\left(M_\infty^2 - 1\right),\qquad M^2 = \frac{2 + (\gamma-1)M_\infty^2}{2\gamma M_\infty^2 - (\gamma-1)}.$$

**Step 2: subsonic deceleration to rest.** The flow is adiabatic, so Bernoulli plus $p\rho^{-\gamma} = $ const gives the stagnation pressure (200C Eqs. 7.15–7.16):

$$p_s = p\left[1 + \frac{\gamma-1}{2}M^2\right]^{\gamma/(\gamma-1)}.$$

Combine the two and divide by $\rho_\infty u_\infty^2$ (200C Eq. 7.19):

$$K\equiv\frac{p_s}{\rho_\infty u_\infty^2}\xrightarrow{M_\infty\to\infty}\frac{2}{\gamma+1}\left[1 + \frac{(\gamma-1)^2}{4\gamma}\right]^{\gamma/(\gamma-1)}.$$

This is Rayleigh's pitot formula from aerodynamics. Numerically:

| $\gamma$ | $M_\infty$ | $K$ |
|---|---|---|
| 5/3 | ∞ | 0.881 |
| 5/3 | 8 | 0.886 |
| 5/3 | 6 | 0.889 |
| 5/3 | 4.5 | 0.895 (200C quotes 0.897) |
| 2 | ∞ | 0.844 |

So the magnetopause feels about **88%** of the incident momentum flux. $K$ barely depends on the Mach number, which is why the standoff distance is controlled by $\rho u^2$ and almost nothing else.

> **Why textbooks disagree on the factor in front of $\rho u^2$.** Chapman and Ferraro's original picture had particles *specularly reflecting* off the boundary. Reflection reverses the momentum, which gives $2\rho u^2$. The fluid picture, where the wind is shocked and diverted *around* the obstacle rather than bounced back, gives $K\rho u^2\approx0.88\rho u^2$. The real magnetosphere has a bow shock, so the fluid value is the physically appropriate one. Because $R_{mp}\propto(\text{prefactor})^{-1/6}$, the choice changes $R_{mp}$ by only $(2/0.88)^{1/6} = 1.15$, about 15%.

---

## 3. Pressure balance and the 1/6 power

Inside the magnetopause, take the pressure to be purely magnetic. That's a good approximation at Earth's nose, but not at Jupiter or Saturn (200C §7.4.2). Write the field there as $aB_0(R_E/R_{mp})^3$ and balance:

$$K\rho_\infty u_\infty^2 = \frac{\left(aB_0\right)^2}{2\mu_0}\left(\frac{R_E}{R_{mp}}\right)^6\qquad\text{(200C Eq. 7.20)},$$

$$\boxed{\frac{R_{mp}}{R_E} = \left(\frac{a^2B_0^2}{2\mu_0K\rho_\infty u_\infty^2}\right)^{1/6}}$$

The **sixth root** comes from squaring the field (pressure) and the dipole's $r^{-3}$ falloff. It makes the magnetopause remarkably stiff: doubling the solar-wind pressure moves it inward by only $2^{-1/6}$, about 11%.

**Numbers for Earth.** With $B_0 = 31{,}000$ nT, the constant $(B_0^2/2\mu_0)^{1/6}$ evaluates to 8.53 when pressure is in nPa. That gives (200C Eq. 7.21)

$$\frac{R_{mp}}{R_E} = 8.53\,a^{1/3}\left(K\rho u^2\right)^{-1/6}.$$

Observed: $R_{mp}\approx10\,R_E$ for $\rho u^2 = 2.6$ nPa. Solving for the compression factor gives $a = 2.44$, between the planar value of 2 and the spherical value of 3, as it should be. In practical units, this is

$$R_{mp}\approx107.6\,(n\,u^2)^{-1/6}\,R_E,$$

with $n$ in cm$^{-3}$ and $u$ in km/s. 200C writes 107.4, and the difference is rounding.

**Comparison with an empirical model.** The Shue et al. (1998) fit to magnetopause crossings has $R_0 = \{10.22 + 1.29\tanh[0.184(B_z + 8.14)]\}\,D_p^{-1/6.6}$. With $B_z = 0$:

| $D_p$ (nPa) | Pressure balance, $a = 2.44$ | Shue 1998 |
|---|---|---|
| 1 | 11.7 | 11.4 |
| 2.6 | 10.0 | 9.9 |
| 5 | 9.0 | 8.9 |
| 10 | 8.0 | 8.0 |
| 20 | 7.1 | 7.2 |

These agree to within 0.3 $R_E$. The fitted exponent 1/6.6 is slightly *weaker* than the theoretical 1/6. That's expected: under compression the magnetospheric currents (ring current, tail, field-aligned currents) change too, which effectively changes $a$ (200C §7.4.2). The **IMF $B_z$ term** has no counterpart in pressure balance at all. Southward IMF reconnects at the nose and erodes dayside flux ([[Dungey Cycle]], [[Sweet-Parker Reconnection]]).

> **Exponent discrepancy in 200C.** Eq. 7.23b quotes the Shue model with $D_p^{-1/6}$. The published Shue et al. (1998) exponent is $-1/6.6$, confirmed from the literature (see the Verification section). The table uses 1/6.6.

**Mercury as a check.** S&N Table 2.4 gives a Mercury moment of $(3.5\text{–}4.4)\times10^{12}$ T m$^3$. At 0.39 AU, the solar-wind pressure scales up to about 17 nPa. The formula then gives $R_{mp}\approx1.35\text{–}1.56\,R_M$, a stand-off altitude of about 850–1350 km. S&N quote about 1460 km. Given the uncertainty in the moment and the unknown $a$ for such a small, conductive-core magnetosphere, that's reasonable order-of-magnitude agreement, but no more than that.

---

## 4. Where's the bow shock?

The bow shock has to stand far enough upstream that all the shocked plasma can flow around the obstacle. The gas-dynamic simulations of Spreiter et al. (1966) give a simple empirical rule (200C §7.6.1):

$$\frac{\Delta}{R_{mp}} \approx 1.1\,\frac{\rho_1}{\rho_2} = 1.1\,\frac{(\gamma-1)M_1^2 + 2}{(\gamma+1)M_1^2}.$$

The density ratio is the [[Rankine-Hugoniot Jump Conditions|RH compression]]. For $M_1 = 8$ and $\gamma = 5/3$, $\Delta/R_{mp} = 0.29$, so the shock sits about 29% farther out than the magnetopause: roughly 13 $R_E$ for a 10 $R_E$ magnetopause.

This rule fails as $M_1\to1$, where the shock should retreat to infinity. The Farris & Russell (1994) form, 200C Eq. 7.27, fixes that by including the obstacle's radius of curvature.

---

## What we assumed, and where it breaks

- **Vacuum magnetosphere.** Plasma pressure inside the magnetopause is neglected. That fails at Jupiter and Saturn, where centrifugally loaded plasma inflates the magnetosphere (200C §7.4.2).
- **Stagnation point.** In MHD, a true stagnation point with $\mathbf B\neq0$ forces the density to vanish there (Siscoe Eq. II.65). The real subsolar magnetosheath develops a **plasma depletion layer**: magnetic pressure takes over from thermal pressure as plasma is squeezed out along the draped field. The total pressure balance still holds, which is all §3 needs.
- **No reconnection.** A closed, impenetrable boundary is the $B_z > 0$ idealization. For $B_z < 0$, flux erosion moves the magnetopause inward at the same pressure (the Shue $\tanh$ term).
- **Newtonian shape.** Away from the nose, the normal pressure falls roughly as $\cos^2\psi$ (Newtonian approximation, 200C §7.4.3). That gives the blunt dayside and flaring tail fitted by the Shue form $r = R_0[2/(1 + \cos\theta)]^\alpha$.

---

## Verification

- **Sources agree.**
  - Image dipole, factor-2 doubling, Tsyganenko factor of about 2.4, $K$ derivation and values, pressure-balance equation, 8.53 and 107.4 constants, $a = 2.44$, bow-shock rule: 200C textbook Ch. 7 §§7.3–7.4 and §7.6.1, Eqs. 7.11–7.27.
  - Stagnation-point density depletion: [[Siscoe 1983 Solar System MHD|Siscoe]] §II, Eq. II.65.
  - Magnetopause at about 9–10 $R_E$, Mercury standoff about 1460 km, planetary moments: [[Schunk Nagy 2009 Ionospheres|S&N]] Ch. 2, Table 2.4.
  - Empirical model: Shue et al. (1998), *JGR* 103, 17691. Exponent $-1/6.6$ confirmed in the Shue 1998 formula as reproduced in [*Ann. Geophys.* 43, 835 (2025)](https://angeo.copernicus.org/articles/43/835/2025/) and in other papers that cite $N = 6.6$ for Shue 1998. That differs from 200C Eq. 7.23b's $-1/6$.
- **SymPy.**
  - Image-dipole $B_x = 0$ on the midplane, with compression factor 2.
  - Spherical-shell factor 3 (uniform shielding field $-2m/R^3$).
- **Numerical.**
  - $K$ table: 0.881 and 0.844 match 200C exactly. At $M = 4.5$ I get 0.8945 against the quoted 0.897, a 0.3% difference I can't attribute; the cause is not identified.
  - 8.53 constant, $a = 2.44$, 107.6 vs 107.4.
  - Comparison with Shue 1998.
  - Mercury estimate.
  - Spreiter bow-shock ratio 0.29 at $M = 8$.
- **Interpretive (mine):** the dawn-to-dusk current magnitude (0.06 A/m) and the particle-reflection vs. fluid explanation of the $2\rho u^2$ vs. $0.88\rho u^2$ prefactor.

## Sources

- 200C textbook Ch. 7, *Solar-wind interaction with magnetized obstacles* (`Atlas/Texts/Textbooks/200C Textbook/Ch7_Solar-Wind_Interaction_with_Magnetized_ObstaclesJLcomm_CTR.pdf`)
- [[Siscoe 1983 Solar System MHD]] — §II, Eqs. II.62–65 (stagnation points in MHD flow)
- [[Schunk Nagy 2009 Ionospheres]] — Ch. 2 (magnetosphere dimensions, planetary moments)
- [[Rankine-Hugoniot Jump Conditions]] — the shock jumps used for $K$
