---
type: concept
status: draft
updated: 2026-10-08
sources: 9
---

# Wave-Particle Interactions

Exchange of energy and momentum between plasma waves and individual particles. The two fundamental resonance mechanisms — Landau resonance and cyclotron resonance — govern both the growth/damping of waves and the diffusion of particles in energy and pitch angle.

## Landau Resonance

Occurs when a particle's parallel velocity matches the wave phase velocity:

$$v_\parallel = \frac{\omega}{k_\parallel} \quad (N = 0 \text{ resonance})$$

In the particle's rest frame, the wave frequency is Doppler-shifted to zero; the particle sees a static electric field and is continuously accelerated or decelerated. For a Maxwellian distribution:
- Particles slower than phase velocity gain energy on average (wave damping)
- Particles faster than phase velocity lose energy (Landau damping: $\gamma_L < 0$)
- Instability if $\partial f/\partial v > 0$ at $v = \omega/k$ (bump-on-tail, two-stream)

Landau damping rate for electron plasma waves:

$$\frac{\gamma_L}{\omega_{pe}} = -0.22 \sqrt{\frac{\pi}{8}} \left(\frac{k_D}{k}\right)^3 \exp\!\left(-\frac{k_D^2}{2k^2}\right)$$

**Landau resonance with Alfvén waves.** Dispersive (kinetic or inertial) [[Alfvén Waves]] carry $E_\parallel$, so electrons with $v_\parallel \approx \omega/k_\parallel \approx v_A$ are accelerated *along* $\mathbf{B}$. This is the mechanism of broadband auroral acceleration ([[Auroral Acceleration]]).
- **Landau damping** is weak ($\gamma/\omega \lesssim 0.1$) unless $k_\perp\rho_s$ or $k_\perp\lambda_e$ is about 1 or larger. Hot ions suppress it ([[Lysak Lotko 1996 Kinetic Alfvén Dispersion]]).
- **Fermi reflection** (inertial regime): electrons with $v_i \geq V - \sqrt{2e\phi/m_e}$ reflect off the moving $E_\parallel$ front to $v_f = 2V - v_i$ ([[Kletzing 1994 KAW Electron Acceleration]]).
- **Nonlinear trapping** (kinetic regime, equatorial inner magnetosphere): $E_\parallel$ plus the mirror force trap electrons up to about 100 eV and accelerate them to several keV, collapsing their pitch angles ([[Artemyev 2015 KAW Electron Trapping]]).

This contrasts with chorus, whose cyclotron resonance mainly scatters pitch angle (the diffuse aurora route), though it also scatters substantially in momentum at 1–10 keV (see below).

## Cyclotron Resonance

Occurs when the Doppler-shifted wave frequency matches a harmonic of the particle cyclotron frequency:

$$\omega - k_\parallel v_\parallel = \pm N \Omega_\alpha \quad (N = \pm 1, \pm 2, \ldots)$$

The $\pm$ selects resonance with the right-hand (R-mode/whistler) or left-hand (L-mode/EMIC) polarized component. At $N = 1$:
- Electrons resonate with R-mode (whistler-mode) waves: $\omega - k_\parallel v_R = \Omega_e$
- Protons resonate with L-mode (EMIC) waves: $\omega - k_\parallel v_R = -\Omega_i$

**Resonant energies:**
- Whistler R-mode (electrons): $E_{res} = \frac{B^2}{8\pi N}\frac{\Omega_e}{\omega}\left(1 - \frac{\omega}{\Omega_e}\right)^3$
- L-mode (protons): $E_{res} = \frac{B^2}{8\pi N}\left(\frac{\Omega_i}{\omega}\right)^2\left(1 - \frac{\omega}{\Omega_i}\right)^3$

## Pitch-Angle Diffusion

In the weak scattering limit, multiple random cyclotron resonances produce a random walk in pitch angle $\alpha$. The pitch-angle diffusion coefficient:

$$D_{\alpha\alpha} = \pi \Omega \left(\frac{b}{B_0}\right)^2 \quad [\text{rad}^2/\text{s}]$$

where $b$ is the wave magnetic fluctuation amplitude. This is the $N = 1$ result for parallel propagation; oblique waves add higher-harmonic contributions.

The Fokker-Planck equation governs the evolution of the distribution function $f(v,\alpha,t)$:

$$\frac{\partial f}{\partial t} = \frac{1}{\sin\alpha} \frac{\partial}{\partial \alpha}\!\left(D_{\alpha\alpha} \sin\alpha \frac{\partial f}{\partial \alpha}\right) + S - L$$

Steady-state solutions (Kennel & Petschek 1966) give the **strong** vs. **weak diffusion** regimes:

**Strong diffusion** ($D_{\alpha\alpha} > D_c = \alpha_L^2/2\tau_{1/4B}$): loss cone is full; precipitation proceeds at its maximum rate, giving the minimum lifetime $\tau_{\min} = 2\tau_{1/4B}/\alpha_L^2\approx4\tau_{1/4B}L^3$. *(Corrected 2026-10-07: this expression is a lifetime, not a rate.)*

**Weak diffusion** ($D_{\alpha\alpha} < D_c$): loss cone essentially empty; precipitation rate $\propto D_{\alpha\alpha}$

The Kennel-Petschek theory predicts the maximum stably trapped flux, $J^*\propto B_0/(LR_E)\propto L^{-4}$, set by the balance between whistler growth and wave loss. It is a **weak-diffusion** limit: a strong enough source can push trapped flux above it once scattering reaches the strong-diffusion rate. Derivation and the reasons published values differ: [[Kennel-Petschek Limit]].

## Wave Growth Rates

For whistler R-mode driven by anisotropic electrons ($T_\perp > T_\parallel$):

$$\gamma_\text{whistler} = \pi \Omega_e \left(1 - \frac{\omega}{\Omega_e}\right)^2 \eta_{res}(v_{res}) \left[A(v_{res}) - A_c\right]$$

where $A = T_\perp/T_\parallel - 1$ is the pitch-angle anisotropy and $A_c = 1/(\Omega_e/\omega - 1)$ is the critical anisotropy for marginal stability.

For EMIC L-mode (proton anisotropy):

$$\gamma_\text{EMIC} \propto \Omega_i \cdot \eta_{res} \cdot [A_p - A_{c,p}]$$

**Chorus** emission in the outer radiation belt: driven by freshly injected electrons with $A \gtrsim 1$ (substorm injection); occurs at $(0.2$–$0.6)\,\Omega_e$, outside the plasmapause.

## Diffuse Aurora: Chorus vs. ECH Scattering

[[Thorne 2010 Chorus Diffuse Aurora]] computed bounce-averaged diffusion rates from CRRES wave statistics at L = 5 and ran Fokker–Planck simulations:
- **ECH waves** scatter only within about 15° of the loss cone.
- **Upper-band chorus** scatters 0.1 to a few keV over broad pitch angles, producing **pancake distributions**. It also stochastically accelerates electrons above 10 keV.
- **Lower-band chorus** removes electrons above about 7 keV.
- Combined, they cause momentum diffusion at 1–10 keV and loss of the whole injected 0.1–50 keV population in about 1 hour.

**Chorus, not ECH, is the dominant driver of diffuse aurora** (for L below about 8). [[Newell 2009 Global Precipitation Budget]] attributed it to electrostatic waves; that disagreement is recorded on [[Auroral Acceleration]].

## Energy vs. Pitch-Angle Diffusion

The ratio of energy diffusion to pitch-angle diffusion:

$$\frac{\Delta E_\perp}{\Delta E_\parallel} = 1 - \frac{\Omega_e}{\omega}$$

For low-frequency waves ($\omega/\Omega \ll 1$): nearly all energy goes into perpendicular momentum (pitch-angle scattering toward the loss cone). For higher-frequency whistlers ($\omega \sim 0.3\,\Omega_e$): substantial energy diffusion → particle acceleration.

## Radial Diffusion

Violation of the third invariant $\Phi$ by long-period (ULF) magnetic and electric field fluctuations drives radial transport across $L$ shells. The radial diffusion equation:

$$\frac{\partial f}{\partial t} = L^2 \frac{\partial}{\partial L}\!\left(\frac{D_{LL}}{L^2} \frac{\partial f}{\partial L}\right) - \frac{f}{\tau}$$

$D_{LL}$ driven by: magnetic fluctuations at drift frequency ($B_w \sim 10$ m$\gamma$ typical); electric field fluctuations from ionospheric disturbances.

Lyons & Thorne (1973): at $L > 2$, whistler-mode diffusion lifetime dominates over Coulomb losses for electrons $\mu > 30$ MeV/G; these electrons can diffuse inward from outer belt without loss.

## Bohm Diffusion (Upper Limit)

When wave turbulence is very strong ($\tau_{eff} \sim \Omega^{-1}$):

$$D_{LL,max} = \frac{v_\perp^2}{4\Omega}$$

This is the Bohm diffusion limit, representing the maximum possible cross-field transport. Relevant at the magnetopause boundary where strong waves allow solar wind particle injection into the magnetosphere even without field-line reconnection.

## Related Concepts

- [[Plasma Waves]] — whistler, chorus, EMIC, hiss — the waves involved
- [[Radiation Belts]] — wave-particle interaction is the primary source and loss mechanism
- [[Aurora]] — diffuse aurora from wave-induced precipitation into loss cone
- [[Alfvén Waves]] — Landau-resonant electron acceleration by kinetic and inertial Alfvén waves
- [[Auroral Acceleration]] — scattering (diffuse) vs. acceleration (inverted-V, broadband)

## Derivations

- [[Landau Damping]] — the $N=0$ resonance from linearized Vlasov–Poisson
- [[Quasilinear Diffusion]] — velocity-space and pitch-angle diffusion; weak vs strong diffusion lifetimes
- [[Kennel-Petschek Limit]] — self-limiting trapped flux
- [[Cold-Plasma Waves]] — dispersion relations of the resonating wave modes

## Sources

Seeded from AOS 250B course materials (Thorne 1993 course reader, Chapters 6–7); Lyons et al. 1972 (JGR 77, 3455); Spjeldvik & Thorne 1975 (JATP 37, 777); Kindel & Kennel 1971 (JGR 76, 3055).
- [[Kennel 1966 Limit Stably Trapped Fluxes]] — original K-P paper; self-regulating wave-particle feedback; strong vs weak diffusion; electrons >40 keV near the limit for $L > 4$ and well below it for $L < 4$ (KP p. 19). *(Corrected 2026-10-07 from "$L \leq 12$".)*
- [[Summers 2009 Relativistic KP Limit]] — fully relativistic extension of K-P theory; marginal stability (convective gain over growth length) replaces the wave-reflection criterion of Kennel 1966; relativistic effects lower the allowable trapped flux for E > 100 keV; K-P limit confirmed at Earth (L=5–10), Jupiter, and Uranus.
- [[Olifer 2023 KP Self-Limiting Precipitation]] — observational confirmation of K-P self-regulation using 70 storms (Van Allen Probes + POES): dawn-side substorm injections briefly drive 54 keV electron flux above the K-P limit, exciting chorus waves that return fluxes to the asymptotic K-P level (~$5\times10^3$ cm$^{-2}$ s$^{-1}$ sr$^{-1}$ keV$^{-1}$ at $L\approx 4.5$); intense precipitation seen at LEO is caused by this self-limiting process, not independent injection dynamics.
- [[Sivadas 2020 Thesis Energetic Precipitation]] — diffuse aurora from chorus pitch-angle scattering (isotropic below about 5 keV); pulsating aurora from lower-band chorus; EMIC scattering of >100 keV electrons in substorm expansion; KAW trapping in the plasma sheet.
- [[Agapitov 2011 THEMIS Chorus Waves]] — THEMIS observations of both forward and reflected chorus at $L\geq8$; reflected waves are attenuated $10$–$30\times$ and ~10% higher frequency than co-located forward waves; ray tracing reproduces both properties as geometric consequences of non-ducted poleward propagation (reflected waves originate at lower L where f_ce is larger); reflected chorus may scatter radiation belt electrons at off-equatorial latitudes.

**Strahl/halo electrons in the solar wind:** [[Pierrard 2001 Solar Wind Electrons]] demonstrates that solar wind electron VDFs have three components — thermal core (collisionally trapped in the ambipolar potential), isotropic suprathermal halo, and field-aligned strahl (focused by magnetic moment conservation). The halo isotropy requires wave scattering (whistler-mode or other) en route from Sun to 1 AU; the strahl carries observable information about the wave-particle interaction environment in the solar wind. Analogous processes (strahl-like suprathermal tails, ambipolar-potential-driven escape) apply to electrons in the polar wind.
- [[Thorne 2010 Chorus Diffuse Aurora]] — chorus (not ECH) dominates diffuse-aurora scattering; pitch-angle and momentum diffusion coefficients; pancake distributions.
- [[Lysak Lotko 1996 Kinetic Alfvén Dispersion]] — Landau damping of kinetic Alfvén waves.
- [[Kletzing 1994 KAW Electron Acceleration]] — Fermi reflection off Alfvén wave fronts.
- [[Artemyev 2015 KAW Electron Trapping]] — nonlinear KAW trapping.
