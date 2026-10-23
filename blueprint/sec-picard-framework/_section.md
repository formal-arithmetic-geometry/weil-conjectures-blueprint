+++
id = "sec-picard-framework"
kind = "section"
title = "Picard Framework"
order = 617
uses = ["sec-nagata-compactification", "sec-abelian-varieties", "sk-def-av-jacobian", "sk-def-av-pic"]
+++
**Content.** This section constructs the Jacobian of a smooth projective
curve as the identity component of its Picard scheme, along two strands.
Strand A is the cohomological machinery: the Čech-to-derived and
Grothendieck/Leray spectral sequences ([det-thm-picard-cech],
[det-thm-groth-ss]), affine vanishing, the cohomology of $\mathbf P^n$,
Serre's theorems A and B, coherence of higher direct images
([det-thm-picard-coherence]), semicontinuity and base change
([det-thm-picard-semicon]), Serre duality and Riemann–Roch for curves, and
the twist lemma [sk-thm-picard-twist]. Strand B is descent and
representability: the Hilbert functor of points on a curve is representable
([sk-thm-picard-hilb-curves]), the Picard functor is an fppf sheaf split by
a rational point ([sk-prop-picard-pic-split]), and the open subfunctor $F$
of line bundles $\mathcal L$ with $Rf_*\mathcal L$ an invertible module in degree $0$ is representable over any field, given a rational point
([sk-thm-picard-f-representable]). Translates of $F$ cover the normalized
Picard functor by the twist lemma, which needs $k$ separably closed, so the criterion [det-thm-picard-criterion]
gives representability over a separably closed field ([sk-thm-picard-main]).
The degree decomposition and the tangent space $H^1(C,\mathcal O_C)$ then
show that $\underline{\mathrm{Pic}}^0_{C/k}$ is an abelian variety of
dimension $g$, which descends to any base field.

**Key theorem.**

- Prop [sk-thm-picard-main] (the Jacobian is an abelian variety): for a
  smooth projective curve $C$ of genus $g$ over algebraically closed $k$,
  $J(C)=\underline{\mathrm{Pic}}^0_{C/k}$ is an abelian variety of
  dimension $g$ with $T_eJ(C)\cong H^1(C,\mathcal O_C)$ and
  $J(C)(k)\cong\mathrm{Pic}^0(C)$. Used in §[sec-curve-estimates],
  §[sec-purity-real-sheaves].
- Prop [sk-prop-jacobian-descent] (Jacobian over a general field): for a
  proper smooth geometrically connected curve $C_0/k_0$ the Jacobian descends
  to $J_0/k_0$ with $J_0[\ell^n](\bar k_0)\cong\mathrm{Pic}^0(C)[\ell^n]$
  Galois-equivariantly. Used in §[sec-purity-real-sheaves].
- Thm [det-thm-picard-semicon] (semicontinuity and base change): for $f$
  proper and $\mathcal F$ flat of finite presentation,
  $t\mapsto\dim H^q(X_t,\mathcal F_t)$ is upper semicontinuous, and over a
  reduced base local constancy makes $R^qf_*\mathcal F$ finite locally free;
  over a reduced locally Noetherian base the base-change maps
  $R^qf_*\mathcal F\otimes\kappa(t)\to H^q(X_t,\mathcal F_t)$ are then
  isomorphisms. Used in §[sec-proper-base-change],
  §[sec-smooth-base-change], §[sec-smooth-purity], §[sec-six-functors],
  §[sec-trace-formula], §[sec-poincare-duality],
  §[sec-algebraic-groups-lie-algebras], §[sec-zeta-weil].
- Thm [det-thm-picard-duality] (Serre duality): for a smooth proper curve
  and $\mathcal F$ locally free, the trace pairing
  $H^q(X,\mathcal F)\otimes H^{1-q}(X,\mathcal F^\vee\otimes\omega_X)\to k$
  is perfect; with Riemann–Roch [sk-thm-picard-rr]. Used in
  §[sec-curve-estimates], §[sec-proper-base-change], §[sec-smooth-purity],
  §[sec-algebraic-groups-lie-algebras], §[sec-purity-real-sheaves],
  §[sec-deligne-laumon-a1].

**References.**

- Stacks Project, cohomology: `03F6`, `03AW`, `03AZ` (Čech-to-derived
  spectral sequence); `0732`, `0733`, `01F2`, `01F6` (Grothendieck/Leray
  spectral sequence); `01EO`, `01XD` (affine vanishing, Čech cohomology of
  quasi-coherent sheaves); `02O5` (coherence of higher direct images).
- Stacks Project, descent and representability: `05VF`, `023T`, `03I0`,
  `02VO` (fpqc descent); `01JJ` (representability by an open cover);
  `056U` (dense separable points); `0CCJ`, `01ZM` (effective descent,
  limits); `03GN` (properness of images).
- Stacks Project, Picard schemes of curves: `0B95`, `0B9K`, `0B9L`, `0B9N`,
  `0B9Z` (Hilbert and Picard functors, representability of
  $\mathrm{Pic}_{X/k}$); `0BA0` (the Jacobian).
- J. Tate, *Residues of differentials on curves*, Ann. Sci. ÉNS 1968; J.-P.
  Serre, *Groupes algébriques et corps de classes*, Ch. II (residues, Serre
  duality).
- R. Hartshorne, *Algebraic Geometry*, II.5.17 (Serre's theorem A);
  EGA IV$_3$ 8.5.2 (finite-presentation limits).
- D. Mumford, *Abelian Varieties*; J. S. Milne, *Abelian Varieties* (the Jacobian).
