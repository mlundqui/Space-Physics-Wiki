---
type: derivation
status: draft
updated: 2026-10-07
sources: 3
tags: [derivations, plasma-foundations, MHD, waves, alfven-waves]
prerequisites: "[[Ideal MHD from Kinetic Theory]]"
next: "Part II begins with [[Incoherent Scatter Spectrum]]"
---

# MHD Wave Modes

**Part I, page 6** of the [[Derivations Index]] · Previous: [[Ideal MHD from Kinetic Theory]]

## Where we're going

Ideal MHD has two restoring forces, pressure and magnetic tension/pressure, acting on one inertia, the mass density. Shake it and we should expect waves. We'll find exactly **three**:

- a **shear Alfvén** wave that bends field lines without compressing anything and carries its energy strictly along $\mathbf{B}$;
- a **fast** magnetosonic wave in which gas and magnetic pressure push together;
- a **slow** magnetosonic wave in which they fight each other.

These three modes are the vocabulary of everything that follows. The shear mode carries [[Field-Aligned Currents]] between the magnetosphere and ionosphere and becomes the kinetic/inertial wave of [[Alfvén Waves]]. The fast mode steepens into the bow shock. The slow mode is the seed of the mirror instability ([[MHD]] §CGL).

---

## 1. Linearize

Take a uniform, static equilibrium: density $\rho_0$, pressure $p_0$, field $\mathbf{B}_0 = B_0\hat{\mathbf{z}}$, no flow. Perturb it with small quantities ($\rho_1$, $p_1$, $\mathbf{u}$, $\mathbf{b}$), keep only first-order terms, and assume plane waves $\propto e^{i(\mathbf{k}\cdot\mathbf{r}-\omega t)}$, so $\partial_t\to-i\omega$ and $\nabla\to i\mathbf{k}$. Without loss of generality put $\mathbf{k}$ in the $x$–$z$ plane:

$$\mathbf{k} = (k_\perp, 0, k_\parallel) = k(\sin\theta, 0, \cos\theta).$$

The four ideal-MHD equations from [[Ideal MHD from Kinetic Theory]] §6 become:

$$
\begin{aligned}
\text{continuity:}&\quad \rho_1 = \rho_0\,\frac{\mathbf{k}\cdot\mathbf{u}}{\omega}\\
\text{adiabatic:}&\quad p_1 = c_s^2\,\rho_1, \qquad c_s^2 = \frac{\gamma p_0}{\rho_0}\\
\text{induction:}&\quad \mathbf{b} = -\frac{1}{\omega}\,\mathbf{k}\times(\mathbf{u}\times\mathbf{B}_0)\\
\text{momentum:}&\quad \omega\rho_0\,\mathbf{u} = \mathbf{k}\,p_1 - \frac{(\mathbf{k}\times\mathbf{b})\times\mathbf{B}_0}{\mu_0}
\end{aligned}
$$

The last line is $-i\omega\rho_0\mathbf{u} = -i\mathbf{k}p_1 + i(\mathbf{k}\times\mathbf{b})\times\mathbf{B}_0/\mu_0$ divided by $-i$. Linearization has thrown away $(\mathbf{u}\cdot\nabla)\mathbf{u}$ along with all other products of perturbations.

It helps to look at the field perturbation now. Working out the cross products,

$$\mathbf{b} = -\frac{B_0}{\omega}\left(k_\parallel u_x,\; k_\parallel u_y,\; -k_\perp u_x\right).$$

Only $u_x$ can change $b_z$, which is the field *strength*, since $\delta|B| = b_z$ to first order. A $u_y$ motion only *bends* the field.

---

## 2. One matrix, three waves

Substitute everything into the momentum equation and eliminate $\rho_1$, $p_1$ and $\mathbf{b}$ in favor of $\mathbf{u}$. Using the **Alfvén speed**

$$v_A = \frac{B_0}{\sqrt{\mu_0\rho_0}},$$

the result is an eigenvalue problem $\omega^2\mathbf{u} = \mathsf{M}\mathbf{u}$:

$$\omega^2\begin{pmatrix}u_x\\u_y\\u_z\end{pmatrix} = \begin{pmatrix} k^2v_A^2 + k_\perp^2c_s^2 & 0 & k_\perp k_\parallel c_s^2\\ 0 & k_\parallel^2v_A^2 & 0\\ k_\perp k_\parallel c_s^2 & 0 & k_\parallel^2c_s^2\end{pmatrix}\begin{pmatrix}u_x\\u_y\\u_z\end{pmatrix}$$

Before solving anything, look at the structure. **The $y$ row is all by itself.** Motion perpendicular to the plane containing $\mathbf{k}$ and $\mathbf{B}_0$ doesn't couple to anything else. The $x$ and $z$ motions are coupled through the gas pressure (the $c_s^2$ off-diagonal terms). So we expect one decoupled wave plus a pair.

### The shear Alfvén wave ($u_y$)

$$\boxed{\omega^2 = k_\parallel^2v_A^2 = k^2v_A^2\cos^2\theta}$$

Read off its personality:

- **Incompressible:** $\mathbf{k}\cdot\mathbf{u} = 0$, so $\rho_1 = p_1 = 0$. Gas pressure plays no role, which is why $c_s$ doesn't appear. The result holds for warm plasma too.
- **No change in $|B|$:** $b_z = 0$, and $\mathbf{b} = -(B_0k_\parallel/\omega)\,u_y\hat{\mathbf{y}}$ is purely transverse. The field is *sheared*, not squeezed. Using $\omega = \pm k_\parallel v_A$, this is the **Walén relation**, $\mathbf{b}/B_0 = \mp\mathbf{u}/v_A$.
- **Guided:** the group velocity is $\partial\omega/\partial\mathbf{k} = \pm v_A\hat{\mathbf{z}}$, exactly along $\mathbf{B}_0$ *whatever* $k_\perp$ is. Energy goes straight down the field line to the ionosphere and nowhere else.
- **Carries field-aligned current:** $\mu_0\mathbf{j} = i\mathbf{k}\times\mathbf{b}$, and with $\mathbf{b}\parallel\hat{\mathbf{y}}$ the $z$-component is $\propto k_\perp b_y$. *Any* shear wave with finite perpendicular structure carries $j_\parallel$. This is why the shear mode is the messenger of magnetosphere–ionosphere coupling.

The restoring force is pure tension $B_0^2\boldsymbol\kappa/\mu_0$, and the inertia is $\rho_0$. A wave speed of $\sqrt{\text{tension}/\text{mass density}}$ is exactly a guitar string with tension $B_0^2/\mu_0$, which is where $v_A$ comes from.

### The magnetosonic pair ($u_x$, $u_z$)

Set the determinant of the $x$–$z$ block to zero:

$$(\omega^2 - k^2v_A^2 - k_\perp^2c_s^2)(\omega^2 - k_\parallel^2c_s^2) - k_\perp^2k_\parallel^2c_s^4 = 0$$

$$\Longrightarrow\quad \omega^4 - \omega^2k^2(v_A^2+c_s^2) + k^2k_\parallel^2v_A^2c_s^2 = 0,$$

a quadratic in $\omega^2$:

$$\boxed{\frac{\omega^2}{k^2} = \frac12\left[(v_A^2+c_s^2) \pm\sqrt{(v_A^2+c_s^2)^2 - 4v_A^2c_s^2\cos^2\theta}\right]}$$

The $+$ root is the **fast** mode and the $-$ root the **slow** mode.

**Check the limits** (always do this):

- **Along $\mathbf{B}$** ($\theta=0$): the square root becomes $|v_A^2 - c_s^2|$, and the roots are $v_A^2$ and $c_s^2$. One is a transverse Alfvén-like wave and the other an ordinary sound wave sliding along the field, which the field ignores. Which one gets called "fast" depends on whether $v_A > c_s$.
- **Across $\mathbf{B}$** ($\theta = 90°$): fast gives $\omega^2 = k^2(v_A^2 + c_s^2)$. Gas and magnetic pressure add, since both are compressed together. The slow mode goes to $\omega\to0$ and stops propagating.
- **Cold plasma** ($c_s\to0$): fast gives $\omega = kv_A$ at every angle, and slow disappears.

**Ordering.** The product of the two roots is $v_A^2c_s^2\cos^2\theta$, and the fast root is at least $\max(v_A^2,c_s^2)$. A few lines of algebra then give

$$v_{\text{slow}} \le v_A|\cos\theta| \le v_{\text{fast}}.$$

The shear wave always sits *between* the other two. That's why it's also called the **intermediate** mode.

---

## 3. Fast vs. slow: in phase or fighting?

What really distinguishes the two compressional modes is how gas pressure and magnetic pressure vary together. From §1:

- gas pressure: $p_1 = c_s^2\rho_0(\mathbf{k}\cdot\mathbf{u})/\omega$;
- magnetic pressure: $B_0b_z/\mu_0 = \rho_0v_A^2k_\perp u_x/\omega$.

Eliminate $u_z$ using the $z$ row of the matrix. The ratio is

$$\frac{p_1}{B_0b_z/\mu_0} = \frac{c_s^2}{v_A^2}\,\frac{\omega^2}{\omega^2 - k_\parallel^2c_s^2}.$$

That's positive (in phase) when $\omega/k > c_s|\cos\theta|$ and negative otherwise:

- **Fast mode:** $\omega^2/k^2\ge c_s^2\ge c_s^2\cos^2\theta$, so it is **in phase**. Plasma and field are compressed together.
- **Slow mode:** the product rule gives $\omega^2/k^2\le\min(v_A^2,c_s^2)\cos^2\theta\le c_s^2\cos^2\theta$, so it is **anti-phase**. Where the plasma is dense, the field is weak. Total pressure stays nearly balanced and the wave moves slowly.

The slow mode's anti-phase structure is exactly the "magnetic bottle" geometry of the mirror instability. Particle pressure peaks where the field is weakest (Siscoe 1983 Fig. IV.2).

---

## Sanity check: numbers

| Region | $v_A$ | $c_s$ | Regime |
|---|---|---|---|
| F region, O$^+$, $10^{12}$ m$^{-3}$, $B=5\times10^{-5}$ T | about 270 km/s | about 1.6 km/s | $v_A\gg c_s$: fast ≈ isotropic at $v_A$, slow ≈ sound along $\mathbf{B}$ |
| Solar wind, 1 AU ($n = 5$ cm$^{-3}$, 5 nT) | about 50 km/s | about 50 km/s | $\beta\sim1$: all three modes comparable |
| Auroral acceleration region (~7000 km) | about $3.7\times10^4$ km/s | — | see [[Alfvén Waves]] |

*($c_s$ is computed with $\gamma=5/3$ and $p = nk_B(T_e+T_i)$, using $T_e + T_i = 3000$ K in the F region and $2\times10^5$ K in the solar wind, both illustrative. The auroral $v_A$ is from [[Kletzing 1994 KAW Electron Acceleration]].)*

The solar wind's speed of about 400 km/s is several times every MHD wave speed. That is why a fast-mode **bow shock** must stand in front of the magnetosphere ([[Strangeway Ch3 Physics of Magnetized Plasmas|Strangeway]] §3.7.4: the bow shock is a standing fast-mode wave).

---

## A naming warning

Sources disagree on what "slow" means.

- [[Strangeway Ch3 Physics of Magnetized Plasmas|Strangeway]] (and most space-physics usage) calls the shear wave the **intermediate** mode and reserves "slow" for the compressional $-$ root.
- [[Bellan 2006 Fundamentals of Plasma Physics|Bellan]] §4.3.7 titles the shear wave the "**MHD shear (slow) mode**," because in a low-β, zero-pressure picture it is the slower of the two surviving modes.

Same physics, different labels. When a paper says "slow mode," check whether it means compressional or shear.

---

## What we assumed, and where it breaks

- **Ideal, isotropic, uniform.** Gradients in $v_A$ cause reflection and mode conversion (the ionospheric Alfvén resonator; Hasegawa's KAW mode conversion on [[Alfvén Waves]]). Pressure anisotropy modifies the modes and can make them unstable: firehose (shear branch) and mirror (slow branch), on [[MHD]].
- **$\omega\ll\Omega_i$ and $k\rho_i, kd_i\ll1$.** At small perpendicular scales the shear wave becomes dispersive, $\omega^2 = k_\parallel^2v_A^2(1+k_\perp^2\rho_s^2)/(1+k_\perp^2\lambda_e^2)$, and acquires $E_\parallel$. This is the kinetic/inertial Alfvén wave of [[Alfvén Waves]]. At $\omega\to\Omega_i$ it becomes the ion-cyclotron wave, and the fast mode becomes the whistler.
- **Collisionless damping is invisible here.** Landau and transit-time damping, which strongly damp the slow mode in hot plasmas, need kinetic theory.

---

## Verification

- **Sources agree.**
  - Dispersion relations: [[Strangeway Ch3 Physics of Magnetized Plasmas|Strangeway]] Eqs. 3.163–3.188 (triad construction, then the full warm-plasma relation 3.187).
  - [[Bellan 2006 Fundamentals of Plasma Physics|Bellan]] Eqs. 4.65–4.87 (fast/slow quartic 4.84–4.85).
  - [[Siscoe 1983 Solar System MHD]] §III.1 and §IV.1 (same modes, plus anisotropic extensions).
  - [[Schunk Nagy 2009 Ionospheres]] Ch. 7.
  - Pressure-phase result: Strangeway Eq. 3.188.
- **SymPy.**
  - Built the linearized system from the four equations above and derived the $3\times3$ matrix shown.
  - Its eigenvalues are exactly $k_\parallel^2v_A^2$ and the fast/slow pair.
  - Derived the pressure ratio $p_1/(B_0b_z/\mu_0) = c_s^2\omega^2/[v_A^2(\omega^2-k_\parallel^2c_s^2)]$ independently.
- **By hand:** limits, the root ordering via the product of roots, and the shear-mode $j_\parallel\propto k_\perp$.

## Sources

- [[Strangeway Ch3 Physics of Magnetized Plasmas]] — §3.7.1 (MHD waves, Table 3-1), §3.7.3 (field-aligned currents and the shear mode)
- [[Bellan 2006 Fundamentals of Plasma Physics]] — §4.3 (MHD waves, finite pressure, fast and shear modes)
- [[Siscoe 1983 Solar System MHD]] — §III.1 (small-amplitude MHD waves), §IV.1 (anisotropic modes)
- [[Kletzing 1994 KAW Electron Acceleration]] — $v_A$ above the auroral zone
