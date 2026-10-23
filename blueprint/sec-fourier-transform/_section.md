+++
id = "sec-fourier-transform"
kind = "section"
title = "Fourier Transform"
order = 3922
uses = ["sec-abelian-varieties", "sec-curve-estimates", "sec-nagata-compactification", "sec-poincare-duality", "sec-proetale-coefficients", "sec-proper-base-change", "sec-purity-real-sheaves", "sec-six-functors", "sec-six-functors-basics", "sec-smooth-base-change", "sec-smooth-purity", "sec-trace-formula", "sk-prop-curve-affine-kummer"]
+++
The Fourier transform expresses the compactly supported cohomology of
a twisted sheaf on the affine line as a stalk of a sheaf on the dual
line. In this section we construct the transform, prove Fourier
inversion and compare squared trace sums by the Plancherel formula.
These results are used in the Deligne–Laumon section on the affine line
([sec-deligne-laumon-a1]) to prove the weight bound for $H^1_c$ of curves.

Let $k_0=\mathbf F_q$, of characteristic $p\ne\ell$, and fix
$\iota:\overline{\mathbf Q}_\ell\hookrightarrow\mathbf C$. Cohomology is
taken after base change to $k$, with the action of geometric Frobenius. We
use the six operations on the pro-étale site, first with coefficients in a
finite extension $E/\mathbf Q_\ell$ containing the values of the
characters, and then with coefficients in $\overline{\mathbf Q}_\ell$.

**Blocks** (tex §17, in order).

- [sk-lem-as-properties] — the Artin–Schreier character sheaf
  $\mathcal L_\psi$: lisse of rank one, trivialized at zero, multiplicative,
  with trace $\psi\circ\operatorname{Tr}$ and pure of weight zero.
- [sk-lem-wft-compact-kunneth] — compact-support Künneth, compatible with
  Weil structures and traces.
- [sk-lem-wft-character-integral] — the integral of a linear character over
  $\mathbf A^r$.
- [sk-thm-inversion] — the kernel $\mathcal K_\psi$ and the transform
  $\operatorname{FT}_\psi(K)=Rp_{2!}(p_1^*K\otimes\mathcal K_\psi)[r]$ on a
  vector bundle; base change, the stalk formula, Fourier inversion
  $\operatorname{FT}_{\psi^{-1}}\operatorname{FT}_\psi\simeq(-r)$, and
  $\operatorname{FT}_\psi(E)=\delta_0(-1)[-1]$,
  $\operatorname{FT}_\psi(\delta_0)=E[1]$ on a line, all compatible with
  Weil structures.
- [sk-cor-plancherel] — the trace formula (17.3) of the transform and the
  Plancherel identity, with the shift $\nu(\operatorname{FT}_\psi K)=\nu(K)+1$
  of the $L^2$ growth parameter on a line.

**References.**

- R. Kiehl and R. Weissauer, *Weil conjectures, perverse sheaves and
  $\ell$-adic Fourier transform* (statements of the section; the detail
  layer follows the Fourier–Deligne blueprint, with Laumon's normalization
  of the transform).
