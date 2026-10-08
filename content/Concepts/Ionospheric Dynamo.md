---
type: concept
status: draft
updated: 2026-10-07
sources: 0
---

# Ionospheric Dynamo

The electrostatic framework that maps magnetospheric convection electric fields to the ionosphere and drives the two-cell polar convection pattern. In the electrostatic limit, the high-conductivity field lines act as equipotentials, so the magnetospheric convection electric field is transmitted along $\mathbf{B}$ into the ionosphere with little attenuation.

## Electrostatic Limit

For slow plasma flows ($\omega \ll \Omega_i$, scale sizes $\gg$ ion gyroradius):
- $\nabla \times \mathbf{E} = 0$, so $\mathbf{E} = -\nabla\Phi$
- $\mathbf{B}$ lines are equipotential: a potential $\Phi$ applied at the magnetopause maps directly to the ionosphere

The $\mathbf{E}\times\mathbf{B}$ drift pattern in the ionosphere is therefore a direct image of the magnetospheric convection pattern set by the [[Dungey Cycle]] (southward IMF drives a two-cell antisunward flow over the polar cap).

## Master Equation

Current continuity ($\nabla \cdot \mathbf{J} = 0$) with height-integrated Pedersen and Hall currents yields the ionospheric dynamo master equation:

$$\nabla_\perp \cdot (\Sigma_P \nabla_\perp\Phi) - \nabla_\perp\Sigma_H \cdot (\nabla_\perp\Phi \times \hat{\mathbf b}) = -j_{\rm in} + \nabla_\perp\cdot\mathbf{K}_0$$

where $j_{\rm in}$ is the [[Field-Aligned Currents|field-aligned current]] density flowing *into* the ionosphere from above, and $\mathbf{K}_0$ is the wind-driven sheet current. *(Corrected 2026-10-07: the equation previously read $\nabla\cdot(\Sigma_P\nabla\Phi) = J_\parallel - \nabla\Sigma_H\cdot(\nabla\Phi\times\hat B)$ with $J_\parallel$ downward, which has an overall sign error. A downward FAC with uniform $\Sigma_P$ requires $\Sigma_P\nabla^2\Phi = -J_{\rm down}$. Full derivation and SymPy check: [[Electrostatic Dynamo Equation]].)* and $\Sigma_P$, $\Sigma_H$ are the height-integrated [[Ionospheric Conductivity|conductances]]. This is an elliptic PDE for $\Phi$; given $J_\parallel$ and conductances, one solves for the electric potential pattern.

## Cross-Polar Cap Potential (CPCP)

$\text{CPCP} = \Phi_{max} - \Phi_{min}$ across the polar cap convection pattern. Scales with the dawn-to-dusk component of the interplanetary electric field ($\text{IEF}_y$):
CPCP ~ 20–100 kV under typical to active conditions; can exceed 200 kV during extreme events.

Saturation at high solar wind electric fields (Reiff & Luhmann 1986; more recent work shows $\text{CPCP} \propto E_{SW}^{1/2}$ rather than linear).

## Two-Cell Convection Pattern

Standard pattern (Heelis et al. 1982; Weimer model family):
- **Dawn cell**: counterclockwise viewed from above the north pole, around the dawn potential maximum. Flow is antisunward across the polar cap and returns sunward along the dawn flank.
- **Dusk cell**: clockwise, around the dusk potential minimum. Flow returns sunward along the dusk flank.
- *(Corrected 2026-10-07: the rotation senses were previously reversed. With $\mathbf{B}$ downward in the north, $\mathbf{E}\times\mathbf{B}$ circulates counterclockwise around a potential maximum; see [[Electrostatic Dynamo Equation]] §5.)*
- **Throat region**: antisunward flow across the noon polar cap where magnetopause reconnection injects open flux
- **Return flow**: sunward at sub-auroral latitudes (~60°–65° magnetic)

Cell pattern deforms with IMF $B_y$: $B_y > 0$ swells the dusk cell and contracts the dawn cell (NH); reverses for $B_y < 0$.

## E-Region Modification

When conductance gradients are large (e.g., near auroral arcs), $\nabla\Sigma_H$ terms in the master equation generate additional divergence of horizontal currents that must be balanced by $J_\parallel$. This is the essence of feedback instability mechanisms.

## Related Concepts

- [[Field-Aligned Currents]] — the source/sink currents that drive the dynamo potential
- [[Joule Heating]] — dissipative consequence of the driven Pedersen currents
- [[Ionospheric Conductivity]] — $\Sigma_P$ and $\Sigma_H$ enter the master equation
- [[Dungey Cycle]] — sets the global convection topology

## Derivations

- [[Electrostatic Dynamo Equation]] — current continuity → elliptic PDE for φ; slab dynamo; Cowling conductivity; equipotential reduction; conjugate coupling

## Sources

Seeded from AOS 205B course materials (Lecture 6.2).
