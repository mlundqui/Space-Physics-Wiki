---
type: concept
status: draft
updated: 2026-10-07
sources: 1
---

# Ionospheric Conductivity

The response of the ionospheric plasma to applied electric fields. Three distinct conductivity components arise because ions and electrons gyrate in different directions around $\mathbf{B}$ and experience different collision rates with neutrals.

## Formal Derivation (Schunk & Nagy §5.11)

The momentum equations for ions and electrons in the E region, retaining the $\mathbf{E}\times\mathbf{B}$, $\mathbf{v}\times\mathbf{B}$, and collision terms, yield the general current density in the frame moving with the neutral gas. For a species with gyrofrequency $\omega_{cs} = eB/m_s$ and collision frequency $\nu_s$, the partial conductivity tensor diagonal components are:

$$\sigma_{1s} = \frac{n_s e^2}{m_s}\frac{\nu_s}{\nu_s^2 + \omega_{cs}^2} \qquad \text{(Pedersen contribution)}$$
$$\sigma_{2s} = \frac{n_s e^2}{m_s}\frac{\omega_{cs}}{\nu_s^2 + \omega_{cs}^2} \qquad \text{(Hall contribution)}$$

Summing over ions (sign $+$) and electrons (sign $-$, since $\omega_{ce} < 0$ by convention):

**Pedersen conductivity** (S&N Eq 5.119):
$$\sigma_P = \sum_i \frac{n_i e^2}{m_i}\frac{\nu_i}{\nu_i^2 + \omega_{ci}^2} + \frac{n_e e^2}{m_e}\frac{\nu_e}{\nu_e^2 + \omega_{ce}^2}$$

In practice the electron term is small compared to ions in the E region, so $\sigma_P \approx \sum_i \sigma_{1i}$.

**Hall conductivity** (S&N Eq 5.120):
$$\sigma_H = \sum_i \frac{n_i e^2}{m_i}\frac{\omega_{ci}}{\nu_i^2 + \omega_{ci}^2} - \frac{n_e e^2}{m_e}\frac{\omega_{ce}}{\nu_e^2 + \omega_{ce}^2}$$

The electron term dominates $\sigma_H$ in the E region (electrons are magnetized while ions are not): $\sigma_H \approx n_e e / B$ when $\nu_e \ll \omega_{ce}$ and $\nu_i \gg \omega_{ci}$.

**Parallel conductivity** (along $\mathbf{B}$):
$$\sigma_0 = \frac{n_e e^2}{m_e \nu_{ei}}$$

## Electron Field-Aligned Current and Thermal Conductivity (§5.12)

The electron field-aligned current density and heat flux including the electron pressure gradient (Eqs 5.140–5.141):
$$J_\parallel = \sigma'_e\!\left(E_\parallel + \frac{kT_e}{e n_e}\nabla_\parallel n_e\right) + \bar{\varepsilon}'_e \nabla_\parallel T_e$$
$$q_{e\parallel} = -\lambda_e \nabla_\parallel T_e - \beta_e J_\parallel$$

where the electron thermal conductivity (Eq 5.146):
$$\lambda_e = \frac{7.7\times10^5 T_e^{5/2}}{1 + 3.22\times10^4 T_e^2 n_e^{-1}\sum_n n_n Q^{(1)}_{en}} \quad [\text{eV cm}^{-1}\text{s}^{-1}\text{K}^{-1}]$$

The denominator accounts for electron-neutral quenching of the thermal conductivity; at F-region altitudes where neutral density is low, $\lambda_e \propto T_e^{5/2}$.

## The Three Conductivities

For a plasma with electron/ion gyrofrequency $\Omega$ and momentum-transfer collision frequency $\nu$:

**Parallel ($\sigma_0$):** along $\mathbf{B}$; essentially unlimited (large, limited only by collisions and field-aligned resistance)

$$\sigma_0 = \frac{n_e e^2}{m_e \nu_e}$$

**Pedersen ($\sigma_P$):** along $\mathbf{E}$ projected perpendicular to $\mathbf{B}$; current in the direction of $\mathbf{E}_\perp$

$$\sigma_P = n_e e \left(\frac{\nu_e \Omega_e}{\Omega_e^2 + \nu_e^2} + \frac{\nu_i \Omega_i}{\Omega_i^2 + \nu_i^2}\right) \frac{1}{B}$$

**Hall ($\sigma_H$):** perpendicular to both $\mathbf{E}$ and $\mathbf{B}$; arises from the drift of differently colliding species

$$\sigma_H = n_e e \left(\frac{\Omega_e^2}{\Omega_e^2 + \nu_e^2} - \frac{\Omega_i^2}{\Omega_i^2 + \nu_i^2}\right) \frac{1}{B}$$

## The $\kappa_i$ Parameter

$\kappa_i = \Omega_i / \nu_{in}$ is the ratio of ion gyrofrequency to ion-neutral collision frequency. It governs which component dominates:

- $\kappa_i \ll 1$ (low altitude, E-region and below): ions are collision-dominated, move with neutrals; electrons are magnetized; large Hall conductivity
- $\kappa_i \gg 1$ (F-region): ions are magnetized like electrons; Pedersen current dominates; Hall conductivity decreases
- $\kappa_i \sim 1$ (~120–130 km): maximum ion Pedersen mobility. Kelley Fig. 2.5 puts $\kappa_i = 1$ near 130 km; AOS 205B gives 120–140 km. *(Refined 2026-10-07 from "~100–130 km".)*

## Height-Integrated Conductances

Because the magnetospheric circuit "sees" the whole ionospheric column, the relevant quantities are the height-integrated Pedersen and Hall conductances:

$$\Sigma_P = \int \sigma_P \, dz \quad \text{[Siemens]}$$

$$\Sigma_H = \int \sigma_H \, dz$$

- $\Sigma_P \sim$ 5–20 S dayside; $\ll 1$ S on nightside (absent solar EUV)
- $\Sigma_H / \Sigma_P \sim$ 1.5–2 under typical conditions
- During aurora, local enhancements driven by particle precipitation can raise $\Sigma_P$ to 50–100 S (Robinson et al. 1987 parameterization: $\Sigma_P \propto \sqrt{\Phi_E} \cdot E_0$)

## Altitude Structure

- **D region** (60–90 km): $\sigma_P$ and $\sigma_H$ are small (low $n_e$)
- **E region** (90–150 km): dominant contribution to both $\Sigma_P$ and $\Sigma_H$; peak near 110–130 km
- **F region** (150–1000 km): low $\sigma_H$ (large $\kappa_i$); some Pedersen current

## Applications

$\Sigma_P$ and $\Sigma_H$ enter the ionospheric dynamo equation (see [[Ionospheric Dynamo]]) and the Joule heating rate. Conductance asymmetries between conjugate hemispheres affect how field-aligned currents close and drive Pedersen currents.

## Related Concepts

- [[Ionospheric Dynamo]] — conductivity is the key parameter in the dynamo master equation
- [[Joule Heating]] — $Q_J = \Sigma_P |\mathbf{E} + \mathbf{u}_n \times \mathbf{B}|^2$
- [[Aurora]] — Robinson parameterization links precipitation energy flux to $\Sigma_P$, $\Sigma_H$
- [[Field-Aligned Currents]] — close through Pedersen currents; $\nabla \cdot \mathbf{J} = 0$ requires $\Sigma_P \nabla\Phi = J_\parallel$

## Derivations

- [[Pedersen and Hall Conductivity]] — full derivation of the mobility and conductivity tensors, with SymPy checks

## Sources

- [[Schunk Nagy 2009 Ionospheres]] (§5.11: Pedersen and Hall conductivity formal derivation, Eqs 5.119–5.120; §5.12: electron conductivity and thermal conductivity, Eqs 5.140–5.146)
- AOS 205B course materials
