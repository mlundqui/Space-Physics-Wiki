---
type: derivation
status: draft
updated: 2026-10-08
sources: 4
tags: [derivations, solar-wind, heliosphere, transonic-flow, IMF, Parker-spiral]
prerequisites: "[[Polar Wind Transonic Outflow]] (the same Mach-equation mathematics); [[Ideal MHD from Kinetic Theory]] (frozen-in theorem)"
next: "[[Rankine-Hugoniot Jump Conditions]]"
---

# Parker Solar Wind and Spiral

**Part III (Sun, solar wind, magnetosphere), page 3** of the [[Derivations Index]] · Builds on: [[Polar Wind Transonic Outflow]] · Concept pages: [[High-Speed Streams]], [[MHD]] · Source: [[Parker 1958 Solar Wind]]

## Where we're going

In 1958 the corona was known to be hot ($\sim10^6$ K), and comet tails hinted at a steady outflow from the Sun. Parker asked a simple question: **can a million-degree corona sit in hydrostatic equilibrium?** The answer is no. The derivation of *why not* leads straight to a supersonic wind, and the frozen-in field then winds into a spiral. That spiral is the IMF geometry every magnetospheric coupling function assumes.

You've already seen the mathematics: [[Polar Wind Transonic Outflow]] derived a Mach equation with a critical point for an $A\propto r^3$ flux tube. The solar wind is the same equation with $A\propto r^2$. Here we follow [[Parker 1958 Solar Wind|Parker (1958)]] and the 200C textbook Ch. 5 §5.2 (Eqs. 5.1–5.13), cross-checked against S&N Ch. 2 and Ch. 7.

---

## 1. Why the corona can't be static

Take a spherically symmetric, fully ionized hydrogen corona with $T_e = T_p = T$, so $p = 2nk_BT$ (electrons and protons both contribute). Hydrostatic balance is

$$\frac{dp}{dr} = -\frac{GM_\odot m_pn}{r^2}.$$

For an **isothermal** corona this integrates to (200C Eq. 5.7, with $p = 2nk_BT$)

$$p(r) = p_0\exp\left[-\frac{GM_\odot m_p}{2k_BT}\left(\frac{1}{R}-\frac1r\right)\right]\xrightarrow{r\to\infty}p_0\exp\left(-\frac{GM_\odot m_p}{2k_BTR}\right).$$

Look at the limit. Because gravity weakens as $1/r^2$, the exponent saturates and **the pressure at infinity is finite**. For $T = 10^6$ K and $R = R_\odot$, the exponent is $GM_\odot m_p/(2k_BTR_\odot)\approx11.6$, so $p_\infty\approx10^{-5}p_0$. That is still vastly larger than any interstellar pressure that could hold it in. Parker made the argument even stronger: a corona heated only by conduction ($\kappa\propto T^{5/2}$) has $T\propto r^{-2/7}$, which falls too slowly to rescue the static solution.

So the corona can't be confined. It has to flow, and the question becomes *how*.

> **Compare the Earth.** For O$^+$ plasma with $T_e + T_i\approx2000$ K at 300 km, the equivalent exponent $GM_Em_O/[k_B(T_e+T_i)r]$ is about 60. That makes $p_\infty/p_0\sim e^{-60}$, effectively zero, so static (diffusive) equilibrium is fine. For the corona the exponent is only about 12. That ratio of gravitational binding to thermal energy is the whole difference, and it's why O$^+$ is bound ([[Polar Wind Transonic Outflow]] §3) while the corona escapes.

---

## 2. The Mach equation, again

Now allow a steady radial flow $u(r)$. Momentum and continuity are (Parker Eqs. 10–11; 200C Eqs. 5.1–5.6)

$$nm_pu\frac{du}{dr} = -\frac{d}{dr}(2nk_BT) - \frac{GM_\odot m_pn}{r^2},\qquad\frac{d}{dr}\left(r^2nu\right) = 0.$$

Define the isothermal sound speed $c_s^2 = 2k_BT/m_p$. Use continuity to eliminate $dn/dr$, exactly as on the polar-wind page:

$$\boxed{\left(u^2 - c_s^2\right)\frac1u\frac{du}{dr} = \frac{2c_s^2}{r} - \frac{GM_\odot}{r^2}}$$

This is 200C Eq. 5.8. It's the polar-wind equation with:

- area term $\frac{1}{A}\frac{dA}{dr} = 2/r$ (spherical expansion) instead of $3/r$;
- no friction.

The right-hand side is negative close to the Sun (gravity wins) and positive far away (expansion wins). It vanishes at the **critical radius**

$$r_c = \frac{GM_\odot}{2c_s^2} = \frac{GM_\odot m_p}{4k_BT}\qquad\text{(200C Eq. 5.9; Parker's }\xi = \lambda/2\text{)}.$$

The argument from the polar-wind page carries over unchanged. A solution that passes through $u = c_s$ anywhere *other than* $r_c$ has $du/dr\to\infty$. So the one solution that starts subsonic at the base and ends supersonic must cross $u = c_s$ exactly at $r = r_c$. That's the **solar wind**. The other branches are:

- **breezes**: subsonic everywhere, which take you back to a finite pressure at infinity (the problem we started with);
- solutions that are supersonic at the base, which are unphysical;
- double-valued curves.

**Integral of motion.** Multiply through and integrate (SymPy-verified):

$$\frac{u^2}{2} - c_s^2\ln u = 2c_s^2\ln r + \frac{GM_\odot}{r} + C.$$

This is Parker's Eq. 14 in his variables $\psi = u^2/c_s^2$, $\xi = r/a$, $\lambda = GM_\odot m_p/(2ak_BT)$: $\psi - \ln\psi = 4\ln\xi + 2\lambda/\xi + \text{const}$. Pinning $u = c_s$ at $r = r_c$ fixes $C$, and the transonic solution can be written in closed form using the Lambert $W$ function. With $x = r/r_c$ and $w = u^2/c_s^2$:

$$-we^{-w} = -x^{-4}\exp\left(3 - \frac{4}{x}\right),$$

using the principal branch $W_0$ for $x < 1$ and the branch $W_{-1}$ for $x > 1$.

> **Why geometry matters.** Parker himself repeated the calculation in $n$ dimensions. The coefficient of $\ln\xi$ becomes $2(n-1)$. In **one** dimension that term vanishes, the right-hand side only decreases, and the flow can never exceed the sound speed. The spherical divergence is what lets the wind keep accelerating, like the widening bell of a de Laval nozzle. This is the same role $3/r$ played for the polar wind.

---

## 3. Numbers

Transonic isothermal solutions with $m = m_p$ and $c_s^2 = 2k_BT/m_p$:

| $T$ | $c_s$ | $r_c$ | $u$ at 1 AU |
|---|---|---|---|
| $1.0\times10^6$ K | 128 km/s | 5.8 $R_\odot$ | 485 km/s |
| $1.5\times10^6$ K | 157 km/s | 3.9 $R_\odot$ | 628 km/s |
| $2.0\times10^6$ K | 182 km/s | 2.9 $R_\odot$ | 752 km/s |
| $3.0\times10^6$ K | 223 km/s | 1.9 $R_\odot$ | 966 km/s |

These are **solar-wind speeds**, which is the whole point. Thermal speeds of about 150 km/s, far below the 620 km/s surface escape speed, still produce a wind of several hundred km/s, because pressure keeps pushing all the way out. Parker's own check: 500 km/s is reached at $r = 5a$ for $3\times10^6$ K, $36a$ for $1.5\times10^6$ K and $200a$ for $10^6$ K ($a = 10^{11}$ cm). His integral reproduces these as 497, 500 and 507 km/s.

**Hotter corona, faster wind.** That's the textbook link between coronal holes and fast wind ([[High-Speed Streams]]), though see the caveats below.

---

## 4. The spiral

Beyond a few solar radii, the flow energy dominates the field energy ($\beta$ and the Alfvén Mach number are both large), so the field is carried by the plasma, which is the [[Ideal MHD from Kinetic Theory|frozen-in theorem]]. Each field line stays anchored at a footpoint on the rotating Sun, while the plasma on it moves out radially at $V$.

**Kinematics.** Go to the frame rotating with the Sun at $\Omega_\odot$. In that frame the footpoints are fixed and the flow is **steady**, so streamlines and field lines coincide (Parker's argument, also 200C Fig. 5.2). A parcel moves with $\dot r = V$ and $\dot\phi = -\Omega_\odot$, so

$$r - r_0 = -\frac{V}{\Omega_\odot}(\phi - \phi_0)\qquad\text{(Archimedean spiral; 200C Eq. 5.13)}.$$

**Field components.** The field is parallel to the rotating-frame velocity, which gives $B_\phi/B_r = v_\phi/v_r = -\Omega_\odot r\sin\theta/V$. Flux conservation ($\nabla\cdot\mathbf B = 0$) gives the radial part:

$$\boxed{B_r = B_0\left(\frac{r_0}{r}\right)^2,\qquad B_\theta = 0,\qquad B_\phi = -B_r\frac{\Omega_\odot r\sin\theta}{V}}$$

$$|B| = B_0\left(\frac{r_0}{r}\right)^2\sqrt{1 + \left(\frac{\Omega_\odot r\sin\theta}{V}\right)^2},\qquad\tan\psi = \frac{\Omega_\odot r\sin\theta}{V}.$$

The minus sign means the field **trails** the rotation, like the water from a lawn sprinkler.

**Check in the inertial frame.** In the inertial frame the pattern rotates, and the electric field is $\mathbf E = -\mathbf V\times\mathbf B$. SymPy confirms that this field, together with the rotating pattern, satisfies $\nabla\cdot\mathbf B = 0$ and Faraday's law $\partial_t\mathbf B = -\nabla\times\mathbf E$ exactly. The spiral is a genuine ideal-MHD solution, not just a cartoon.

**Two consequences.**

- **Scaling.** $B_r\propto r^{-2}$ but $B_\phi\propto r^{-1}$, so far from the Sun the field is almost purely azimuthal. $B_\phi = B_r$ on the cylinder $r\sin\theta = V/\Omega_\odot$. Parker computed 2.5 AU for $V = 1000$ km/s, and $V/\Omega_\odot$ gives 2.48 AU.
- **Angle at 1 AU.** This is the number everyone quotes, and it is the source of the 43° vs 45° vs 47° disagreements in the literature:

| $\Omega_\odot$ | $V = 400$ km/s | 450 km/s | 800 km/s |
|---|---|---|---|
| $2.7\times10^{-6}$ s$^{-1}$ (27-day synodic, Parker's value) | 45.3° | 41.9° | 26.8° |
| $2.87\times10^{-6}$ s$^{-1}$ (25.4-day sidereal) | 47.0° | 43.7° | 28.2° |

The spiral is set by the Sun's rotation in an inertial frame, so the **sidereal** rate is the physically right one. The commonly quoted "45° at 1 AU" is a round number from either choice. S&N's "43°" corresponds to their mean speed of about 470 km/s. None of these values is wrong; they are different inputs. The physics point is that **slow wind is more tightly wound**.

> **Why Parker's formula has $(r - b)$.** Parker 1958 Eq. 26 writes $B_\phi\propto(r - b)\sin\theta$ rather than $r\sin\theta$. He assumes the gas corotates with the Sun out to a radius $b$. That gives it an inertial azimuthal speed $\Omega b\sin\theta$, and the field line picks up a logarithmic term (his Eq. 25). SymPy confirms that his version also satisfies Faraday's law, *provided* you include that azimuthal velocity in $\mathbf E = -\mathbf v\times\mathbf B$. For $r\gg b$ (1 AU vs. a few $R_\odot$), the two forms agree to better than 1%.

---

## What we assumed, and where it breaks

- **Isothermal all the way out.** The isothermal integral gives $u\propto\sqrt{\ln r}$ growing forever, which requires unlimited heating. Parker cut off the heating at $r = b$. Polytropic and two-fluid models instead give a finite asymptotic speed. The real solar wind has $T_p\neq T_e$ and non-Maxwellian electrons ([[Pierrard 2001 Solar Wind Electrons]]).
- **Speed–temperature link.** Simple Parker models can't produce 750 km/s fast wind with realistic coronal-hole temperatures, which are actually *cooler* than in streamers. Extra momentum and heat must be deposited above the critical point, for example by Alfvén waves (200C Ch. 5 discussion of post-critical-point heating). The table above shows the mechanism, not a quantitative model of the fast wind.
- **No magnetic torque.** The Weber–Davis model adds the azimuthal momentum equation, which gives a second (Alfvén) critical point and the solar angular-momentum loss ("magnetic braking", 200C §5.2). Corotation out to the Alfvén radius is the physical version of Parker's radius $b$.
- **Uniform, radial flow.** The real wind is structured into fast and slow streams, which interact as **corotating interaction regions** (CIRs) and form shocks ([[Rankine-Hugoniot Jump Conditions]], [[High-Speed Streams]]).

---

## Verification

- **Sources agree.**
  - Static-corona argument, momentum and continuity, transonic integral, critical point, $n$-dimension remark, spiral, $B_\phi = B_r$ cylinder at 2.5 AU: [[Parker 1958 Solar Wind|Parker 1958]] Eqs. 10–27.
  - The same equations: 200C textbook Ch. 5 §5.2, Eqs. 5.1–5.13.
  - The spiral formula and 43° at 1 AU: [[Schunk Nagy 2009 Ionospheres|S&N]] Ch. 2 and Ch. 7.
  - The same critical-point structure: [[Polar Wind Transonic Outflow]] (S&N §5.8).
- **SymPy.**
  - Mach equation from momentum plus continuity.
  - Exact conservation of the integral of motion.
  - $r_c = GM/2c_s^2$.
  - $\nabla\cdot\mathbf B = 0$ and Faraday's law for the Archimedean spiral (rotating pattern with $\mathbf E = -\mathbf V\times\mathbf B$).
  - The same for Parker's $(r - b)$ version when $v_\phi = \Omega b\sin\theta$ is included; without that term Faraday's law fails, which is how the reason for the difference was found.
- **Numerical.**
  - Lambert-$W$ solution vs. direct ODE integration: agreement to $7\times10^{-10}$.
  - The speed table.
  - Parker's Fig. 1 claims (497, 500 and 507 km/s against his stated 500 km/s).
  - The spiral-angle table and the 2.48 AU cylinder.
- **Note on the 200C text.** Eq. 5.8 uses $2k_BT/m$ for the sound speed, which needs $p = 2nk_BT$ (electrons plus protons). The line above it says "$p = nkT$". The equations are self-consistent with $p = 2nk_BT$, which is what Parker uses, so it's a wording slip in the text.

## Sources

- [[Parker 1958 Solar Wind]] — the original derivation (§§III–V)
- 200C textbook Ch. 5 §5.2, *Solar wind and heliosphere* (`Atlas/Texts/Textbooks/200C Textbook/Ch5_SolarWindHeliosphereJLfinal2015v2.pdf`)
- [[Schunk Nagy 2009 Ionospheres]] — Ch. 2 (interplanetary medium), Ch. 7 (Parker spiral)
- [[Polar Wind Transonic Outflow]] — the $A\propto r^3$ version of the same mathematics
