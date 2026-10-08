---
type: derivation
status: draft
updated: 2026-10-07
sources: 3
tags: [derivations, ionosphere, photoionization, chapman-layer, F-region, E-region]
prerequisites: "Beer–Lambert absorption; hydrostatic (exponential) atmosphere; [[Moment Equations from the Vlasov Equation]] §4 (continuity)"
next: "[[Ambipolar Diffusion]] (concept page) · Part II continues in [[Derivations Index]]"
---

# Chapman Layer

**Part II (ionosphere), page 2** of the [[Derivations Index]] · Related: [[F-Layer]], [[Ionospheric Energetics]], [[Incoherent Scatter Spectrum]]

## Where we're going

Why does the ionosphere have *layers* at all? Sunlight gets stronger as you go up, and the gas it ionizes gets thinner. Multiply a rising function by a falling one and you get a peak. Sydney Chapman (1931) turned that observation into a closed-form production profile, and adding the simplest chemistry turns it into a density profile.

We'll derive:

1. the **Chapman production function** and its universal shape;
2. the **α-Chapman layer**, with recombination loss $\propto n_e^2$, which describes the E region and F1 ledge;
3. why the **β-type** (linear-loss) chemistry of the upper F region gives *no* peak on its own;
4. the **F2-peak condition**, where chemistry hands over to diffusion. This is the actual origin of the main ionospheric peak.

---

## 1. How sunlight is absorbed

Take monochromatic radiation with photon flux $\Phi$ (photons m$^{-2}$ s$^{-1}$) entering a plane-parallel atmosphere at solar zenith angle $\chi$. Along the ray, every absorber with cross-section $\sigma$ removes photons, giving the **Beer–Lambert law**:

$$\frac{d\Phi}{ds} = -\sigma n\,\Phi.$$

The ray travels downward, so a step $ds$ along it drops altitude by $dz = -ds\cos\chi$, i.e. $ds = -dz\sec\chi$. Integrating from the top of the atmosphere down to altitude $z$:

$$\Phi(z) = \Phi_\infty\,e^{-\tau(z)},\qquad \tau(z) = \sec\chi\int_z^\infty\sigma\,n(z')\,dz'.$$

$\tau$ is the **optical depth**: the number of e-folds of attenuation between you and the Sun.

For an isothermal atmosphere, $n(z) = n_0e^{-(z-z_0)/H}$ with scale height $H = k_BT/mg$, and the integral is immediate:

$$\tau(z) = \sigma n(z)H\sec\chi.$$

The optical depth is just the cross-section times the **column of gas above you along the slant path**, and in an exponential atmosphere that column is $n(z)H$ vertically.

---

## 2. The production function

Each absorbed photon produces ions with some efficiency $\eta$. The production rate is (absorbers) × (cross-section) × (local flux):

$$P(z) = \eta\,\sigma\,n(z)\,\Phi_\infty\,e^{-\tau(z)}.$$

That's the rising-times-falling product. To find the peak, note that $\ln P = \text{const} - (z-z_0)/H - \tau(z)$, and $d\tau/dz = -\tau/H$:

$$\frac{d\ln P}{dz} = -\frac1H + \frac{\tau}{H} = 0\quad\Longrightarrow\quad\boxed{\tau(z_{\max}) = 1}$$

**Production peaks where the optical depth is one.** Above that level there isn't enough gas to absorb much. Below it, the light has already been used up. Different wavelengths have different $\sigma$, so they reach $\tau = 1$ at different heights. That's why different parts of the solar spectrum build different layers (200C textbook Ch. 2, Fig. 2.14).

At the peak, $\sigma n(z_{\max})H\sec\chi = 1$ and $e^{-\tau} = e^{-1}$, so

$$P_{\max} = \frac{\eta\,\Phi_\infty\cos\chi}{e\,H}.$$

**Where's the cross-section?** It cancels. A bigger $\sigma$ moves the peak *up*, but the peak production depends only on how many photons arrive and how thick the atmosphere is. Every photon is eventually absorbed somewhere; $\sigma$ just decides where.

Now measure height from the peak in scale heights, $X = (z - z_{\max})/H$. Then $\tau = e^{-X}$ and $n\propto e^{-X}$, and the whole profile collapses onto one universal curve:

$$\boxed{P(X) = P_{\max}\exp\!\left(1 - X - e^{-X}\right)}$$

Look at its three regions:

| Region | Behavior | Why |
|---|---|---|
| Far above ($X\gg1$) | $P\propto e^{-X}$ | no attenuation; $P$ simply follows the neutral density |
| Near the peak ($|X|\ll1$) | $P\approx P_{\max}e^{-X^2/2}$ | Gaussian, with full width at half maximum ≈ $2.45H$ |
| Far below ($X\ll-1$) | $P\propto\exp(-e^{-X})$ | double-exponential cutoff as the light runs out |

The profile is **asymmetric**: a gentle exponential top and a sharp bottom.

> **Note on the AOS 205B notes (Lecture 1.2, "Asymptotic forms of Chapman layer").** There the $X\ll-1$ limit is written $\exp(e^{-X})$; it should be $\exp(-e^{-X})$, a double-exponential *decay*, as the sketch beside it shows. This is a sign slip in transcription only. The notes themselves are left unchanged.

### Solar zenith angle

Fix the reference height $z_0$ at the overhead-Sun ($\chi = 0$) peak and measure $y = (z-z_0)/H$ from there. A slant path just multiplies the optical depth by $\sec\chi$:

$$P(y,\chi) = P_{0}\exp\!\left(1 - y - \sec\chi\,e^{-y}\right),$$

so the peak rises and weakens:

$$z_{\max}(\chi) = z_0 + H\ln\sec\chi,\qquad P_{\max}(\chi) = P_0\cos\chi.$$

The low Sun at high latitudes, or near dawn and dusk, ionizes higher and more weakly. (The plane-stratified $\sec\chi$ is "good for $\chi$ less than about 75°." At larger angles, Earth's curvature matters and the column is described by the **Chapman function** $\mathrm{Ch}(z_0,\chi_0)$, or simply computed exactly by ray integration; [[Schunk Nagy 2009 Ionospheres|Schunk & Nagy]] §9.1, Eqs. 9.17–9.18.)

---

## 3. Adding chemistry: the α-Chapman layer

Production alone isn't a density. The continuity equation from [[Moment Equations from the Vlasov Equation]] §4, with no transport, is

$$\frac{\partial n_e}{\partial t} = P - L.$$

In the **E region** the dominant ions are molecular (O$_2^+$, NO$^+$), and they disappear by **dissociative recombination** with electrons, e.g. NO$^+ + e\to$ N + O. That loss requires one ion and one electron, so $L = \alpha n_in_e = \alpha n_e^2$ by quasi-neutrality. This is "α-type" loss. In photochemical equilibrium ($\partial_t\to0$):

$$n_e = \sqrt{P/\alpha}\quad\Longrightarrow\quad\boxed{n_e(y,\chi) = \sqrt{\frac{P_0}{\alpha}}\exp\!\left[\tfrac12\left(1 - y - \sec\chi\,e^{-y}\right)\right]}$$

This matches [[Schunk Nagy 2009 Ionospheres|Schunk & Nagy]] Eq. 11.57. Taking the square root halves the exponent, so the density layer is **wider** than the production layer: full width at half maximum ≈ $3.59H$ versus $2.45H$. Near the peak it's parabolic, $n_e\approx n_m(1 - y^2/4)$ (S&N Eq. 11.58).

Two classic consequences:

- **The $\cos^{1/2}\chi$ law.** The peak density goes as $n_m\propto(\cos\chi)^{1/2}$. The ionosonde critical frequency $f_oE\propto\sqrt{n_m}$ therefore goes as $(\cos\chi)^{1/4}$. The E layer obeys this well, which is the observational evidence that it's a near-Chapman layer (200C Ch. 2: "the E and F1 layers are often thought to be fair approximations to Chapman layers").
- **Fast response.** The relaxation time is $\tau_\alpha = 1/(2\alpha n_e)$. With $\alpha\sim3\times10^{-13}$ m³ s$^{-1}$ and $n_e\sim10^{11}$ m$^{-3}$, that's tens of seconds. The E region switches on and off with the Sun (and with solar flares) almost instantly.

**The F1 ledge** sits at about 170 km, near the production peak of 17–91 nm EUV photons (200C Ch. 2). It's a ledge rather than a separate peak because it merges into the much larger F2 layer above.

---

## 4. β-type loss: why chemistry alone can't make the F2 peak

Above about 200 km the dominant ion is O$^+$. Atomic ions recombine with electrons directly only very slowly (radiatively). Instead O$^+$ is lost in two steps:

$$\text{O}^+ + \text{N}_2\to\text{NO}^+ + \text{N},\qquad \text{O}^+ + \text{O}_2\to\text{O}_2^+ + \text{O},$$

followed by fast dissociative recombination of the molecular ion. The slow first step is rate-limiting, and its rate doesn't depend on $n_e$:

$$L = \beta\,n(\text{O}^+),\qquad \beta = k_1[\text{N}_2] + k_2[\text{O}_2],$$

with $k_1\approx1.2\times10^{-12}$ and $k_2\approx2.1\times10^{-11}$ cm³ s$^{-1}$ (S&N Eq. 11.60, from their Table 8.3).

Here's the punchline. In chemical equilibrium, $n(\text{O}^+) = P/\beta$:

- $P\propto[\text{O}]$ falls with scale height $H_{\text{O}}$;
- $\beta\propto[\text{N}_2]$ falls *faster*, with $H_{\text{N}_2} = H_{\text{O}}\times16/28$.

So

$$n(\text{O}^+)\propto\frac{e^{-z/H_{\text{O}}}}{e^{-z/H_{\text{N}_2}}}\quad\text{increases with altitude.}$$

**Pure β-chemistry gives an ionosphere that keeps getting denser as you go up.** Something else has to turn it over.

---

## 5. The F2 peak: chemistry meets diffusion

That something is [[Ambipolar Diffusion]]. At high altitude, plasma drains downward along $\mathbf{B}$ toward diffusive equilibrium, which falls off with the plasma scale height. Compare the two timescales:

$$\tau_{\text{chem}} = \frac1\beta\quad(\text{increases rapidly with height}),\qquad \tau_{\text{diff}}\sim\frac{H^2}{D}\quad(\text{decreases with height, since }D\propto1/n_{\text{neutral}}).$$

- **Below the peak**, chemistry is fast, and the density sits at the rising chemical-equilibrium curve $P/\beta$.
- **Above it**, diffusion is fast, and the density follows the falling diffusive-equilibrium curve.
- The **peak** forms where the two are comparable. [[Schunk Nagy 2009 Ionospheres|Schunk & Nagy]] put it exactly this way (§11.4): "The F region peak density occurs at the altitude where the diffusion and chemical processes are of equal importance, i.e., where the chemical and diffusion time constants are equal."

$$\boxed{\beta(h_mF_2)\approx\frac{D(h_mF_2)}{H^2}}$$

**Which $H$?** I tested this numerically. I solved the steady 1-D continuity–diffusion equation, with production $\propto[\text{O}]$, $\beta\propto[\text{N}_2]$, $D\propto1/[\text{O}]$, and a vertical field. The F2 peak landed within about 4 km of where $\beta = D/H_{\text{O}}^2$, using the **neutral atomic-oxygen scale height**. Using the plasma scale height $H_p = 2H_{\text{O}}$ (for $T_e = T_i = T_n$) missed by about 22 km. The condition is a scaling law, not an identity, but with $H = H_{\text{O}}$ it is accurate.

**Consequences for the research topics in this wiki:**

- Push plasma **up** (equatorward wind, eastward $E$, upflow) and it moves to where $\beta$ is smaller. Both $N_mF_2$ and $h_mF_2$ rise, and the plasma lives longer. This is [[Lifting]], the long life of [[Polar Cap Patch|patches]], and part of [[Storm-Enhanced Density]] (S&N Fig. 11.9).
- Push it **down**, or raise $[\text{N}_2]$ (storm-time composition change, frictional heating raising $k_1$), and the F region erodes. See [[Ionospheric Storms]] and [[Polar Holes]].
- The **field inclination** matters. Only the field-aligned part of diffusion counts, so the vertical diffusion rate scales as $\sin^2I$ (S&N Eq. 11.59). Near the dip equator, vertical diffusion is suppressed and $\mathbf{E}\times\mathbf{B}$ drifts take over ([[Equatorial Ionosphere]]).

---

## What we assumed, and where it breaks

- **Monochromatic light, one absorber, isothermal atmosphere.** The real ionosphere superposes many Chapman-like contributions across the EUV spectrum (EUVAC, 37 bins; [[Ionospheric Energetics]]). Real temperature gradients make $H$ vary with height.
- **Flat Earth.** For $\chi\gtrsim75°$, use the Chapman function or exact ray integration (S&N §9.1). This is essential at polar latitudes in winter.
- **Photochemical equilibrium** (§3) holds in the daytime E region. It fails at sunrise and sunset, and for the F region (§5).
- **Photoionization only.** Particle precipitation (aurora) and photoelectrons from the conjugate hemisphere add production with completely different altitude profiles. This dominates the winter polar ionosphere where [[RISR-N]] operates.

---

## Verification

- **Sources agree.**
  - Production function, $\tau = 1$ peak, $P_{\max}$, universal form and zenith-angle scaling: 200C textbook Ch. 2 §2.7.1 (Eqs. 2.48–2.63); AOS 205B Lecture 1.2 (course notes); [[Schunk Nagy 2009 Ionospheres|S&N]] Eqs. 9.21, 11.52–11.57.
  - α-Chapman layer: S&N Eq. 11.57–11.58 and Lecture 1.2.
  - β-type chemistry and the F2-peak criterion: S&N §11.4 (Eq. 11.60, Fig. 11.8, and the quote above) and 200C Ch. 2 (E/F1 as Chapman layers; F1 at the 17–91 nm production peak).
- **SymPy.**
  - $\tau(z) = \sigma nH\sec\chi$.
  - $z_{\max}$ with $\tau(z_{\max}) = 1$, and $P_{\max} = \Phi_\infty\cos\chi/(eH)$.
  - The universal form $P/P_{\max} = e^{1-X-e^{-X}}$ exactly.
  - Near-peak expansion $e^{(1-X-e^{-X})/2} = 1 - X^2/4 + \dots$.
- **Numerical.**
  - FWHM of 2.45$H$ (production) and 3.59$H$ (α-layer).
  - The steady diffusion–chemistry BVP over three decades of $D$. The F2 peak tracks $\beta = D/H_{\text{O}}^2$ to within 4 km in every case, and $\beta = D/H_p^2$ is off by about 22 km.
  - The model parameters are illustrative ($H_{\text{O}} = 50$ km, $H_{\text{N}_2} = 30$ km), not a fit to data.

## Sources

- 200C textbook Ch. 2, *Upper Atmosphere and Ionosphere* (`Atlas/Texts/Textbooks/200C Textbook/Ch2_UpperAtmosphereIonosphere.pdf`) — §2.7.1 Chapman theory; §2.11 layers
- AOS 205B Lecture 1.2, *Absorption of Radiation* (`Atlas/Courses/AOS 205B/Lecture1_2_AbsorptionOfRadiation.pdf`) — course notes; production, optical depth and α-Chapman derivation
- [[Schunk Nagy 2009 Ionospheres]] — Ch. 9 (§9.1 absorption, optical depth, Chapman function; Eq. 9.21 production), §11.4 (Chapman layer, chemical vs diffusive equilibrium, F2 peak, induced drifts)
