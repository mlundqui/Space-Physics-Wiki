---
type: concept
status: draft
updated: 2026-10-07
sources: 4
---

# Ion Frictional Heating

Elevation of ion temperature above the neutral temperature due to collisional friction when convection-driven ion flow has a large velocity relative to the neutral gas. The dominant ion heating mechanism at high latitudes in the E and lower F regions during strong convection. Closely related to — but distinct in framing from — [[Joule Heating]] (which describes the same energy transfer from the bulk-flow electromagnetic perspective).

## Physical Mechanism

When an applied electric field drives ion drift $\mathbf{u}_i$ through slower-moving neutrals (velocity $\mathbf{u}_n$), ion-neutral collisions convert the directed kinetic energy of the relative drift into random thermal motion of the ions. In the five-moment (drifting Maxwellian) approximation for a weakly ionized plasma, the steady-state energy equation (Schunk & Nagy Eq 5.32) yields:

$$T_i = T_n + \frac{m_n}{3k_B}|\mathbf{u}_i - \mathbf{u}_n|^2$$

For convection-driven drift in crossed electric and magnetic fields, the dominant relative velocity is the $E\times B$ drift minus the neutral wind:

$$|\mathbf{u}_i - \mathbf{u}_n| \approx \frac{|\mathbf{E}'|}{B}, \qquad \mathbf{E}' = \mathbf{E} + \mathbf{u}_n \times \mathbf{B}$$

so:

$$T_i \approx T_n + \frac{m_n}{3k_B}\left(\frac{E'}{B}\right)^2$$

For O$_2^+$ or NO$^+$ ($m_n \approx m_i \approx 30$ amu) in the E region at $B = 5\times10^4$ nT: a 50 mV/m convection field gives $\Delta T \approx 700$ K; 100 mV/m gives $\Delta T \approx 2800$ K. In strong SAID events or polar cap convection channels (E > 100 mV/m), ion temperatures can exceed 3000–4000 K.

## Effective Temperature for Chemical Reactions

Chemical reaction rates depend not on $T_i$ directly but on the *effective temperature* $T_{eff}$, which captures both the thermal energy of the colliding pair and the directed energy of the relative drift. For species $i$ (mass $m_i$) reacting with neutral $r$ (mass $m_r$):

$$T_{eff} = \frac{m_r T_i + m_i T_n}{m_r + m_i} + \frac{m_i m_r}{3k_B(m_i + m_r)}|\mathbf{u}_i - \mathbf{u}_n|^2$$

**O$^+$ + N$_2$** (rate $k_1$): strongly $T_{eff}$-dependent; a 2$\times$ increase in convection E-field elevates $T_{eff}$ enough to increase $k_1$ by a factor of ~16. This makes the O$^+$ + N$_2$ pathway the primary mechanism by which fast convection depletes polar-cap O$^+$ and creates density depletions.

**O$^+$ + O$_2$** (rate $k_2 \approx 2.1\times10^{-11}$ cm$^3$ s$^{-1}$): nearly temperature-independent over the relevant range; less sensitive to frictional heating than the N$_2$ channel.

Both rates from Table 8.3 in [[Schunk Nagy 2009 Ionospheres]].

## Polar Cap Patch Chemistry

Fast convection channels (E' ~ 50–100 mV/m) in the polar cap raise $T_{eff}$ enough to dramatically accelerate O$^+$ recombination. This creates chemical "gaps" in an otherwise continuous [[Tongue of Ionization]] — the *cutting mechanism* for [[Polar Cap Patch]] formation. Even without topological reconnection events or IMF variability, a stationary fast-flow channel can produce mesoscale density structures with 3–10$\times$ contrast within one convection timescale (~30–60 min).

## Temperature Anisotropy from Stress Tensor

In the weakly magnetized limit (strong $\nu_{in}$), the stress-tensor equations give an isotropic $T_i$ as above. In the low-collision limit ($\nu_{in}/\omega_{ci} \to 0$) relevant to F-region altitudes, the stress tensor produces anisotropy in the ion VDF when ions drift perpendicular to **B** (S&N Eqs 5.46–5.47):

$$T_{i\parallel} = T_i - \frac{1}{21}\frac{m_i}{k_B}|\mathbf{u}_i - \mathbf{u}_n|^2, \qquad T_{i\perp} = T_i + \frac{1}{42}\frac{m_i}{k_B}|\mathbf{u}_i - \mathbf{u}_n|^2$$

resulting in $T_{i\perp} > T_{i\parallel}$. ISRs that are not aligned with **B** measure an effective temperature that is a projection of $T_{i\parallel}$ and $T_{i\perp}$; this anisotropy is detectable in high-latitude radar measurements during fast convection events.

## Relationship to Joule Heating

The Joule heating rate $Q_J = \mathbf{J}\cdot\mathbf{E}'$ (Pedersen dissipation in the neutral frame) and the ion frictional heating $\Delta T_i$ are two framings of the same energy transfer: electromagnetic energy → ion thermal energy → neutral thermal energy via ion-neutral collisions. In the E region, nearly all Joule heating first passes through elevated $T_i$ before being re-distributed to neutrals via the thermal relaxation time $\tau_{in} \sim 1/\nu_{in}$.

## ISR Measurement

Incoherent scatter radars ([[RISR-N]], EISCAT, Poker Flat ISR) directly measure $T_i$ from the width of the ion-acoustic feature in the IS spectrum. During strong convection events, $T_i$ measurements map the convection electric field morphology and constrain ion-neutral collision frequency profiles. High-latitude RISR-N observations routinely detect frictional heating signatures in fast-flow polar-cap channels and SAID events.

## Related Concepts

- [[Joule Heating]] — bulk electromagnetic energy dissipation; same physical process as ion frictional heating from a different perspective
- [[Polar Cap Patch]] — frictional heating controls O$^+$ chemical loss rate; the $\times 16$ rate enhancement is a primary patch-cutting mechanism
- [[Polar Wind]] — elevated $T_i$ (and thus $T_p$) increases the plasma scale height and modifies the ambipolar electric field driving H$^+$ outflow
- [[Ionospheric Conductivity]] — ion-neutral collision frequency $\nu_{in}$ appears in Pedersen/Hall conductivity; $T_i$ elevation modifies effective $\nu_{in}$
- [[Ambipolar Diffusion]] — $T_i$ enters the plasma temperature $T_p = (T_e+T_i)/2$ and thus the ambipolar diffusion coefficient $D_a$
- [[RISR-N]] — primary observational constraint on ion frictional heating at polar latitudes

## Derivations

- [[Frictional and Joule Heating]] — derivation of $T_i = T_n + m_n|\Delta\mathbf{u}|^2/3k_B$ and $T_{\rm eff}$

## Sources

- [[Schunk Nagy 2009 Ionospheres]]
- [[Polar Cap Patch]]
- [[Blelly Schunk 1993 Moment Comparison]]
- AOS 205B course materials
