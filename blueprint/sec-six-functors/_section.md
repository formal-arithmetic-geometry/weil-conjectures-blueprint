+++
id = "sec-six-functors"
kind = "section"
title = "Six Functors"
order = 2383
uses = ["sec-curve-estimates", "sec-nagata-compactification", "sec-proetale-coefficients", "sec-proper-base-change", "sec-six-functors-basics", "sec-smooth-base-change", "sec-smooth-purity"]
+++
**Content.** For separated finite-type morphisms of finite-type schemes over
$k=\overline{\mathbf F}_q$ and every admissible coefficient ring ($A_{E,n}$,
$\mathcal O_E$, $E$, $\Qlb$), this section assembles the six operations
$Lf^*,Rf_*,Rf_!,Rf^!,\otimes^L,\RHom$ into one package. The operations are
defined only on ambient derived categories, and their descent to $\Dctf$ is
proved, not assumed ([sk-rem-sf-typing]). Proper and smooth base change,
Nagata compactification and smooth purity come from the earlier sections.
This section then proves the projection formula at every stage
([sk-prop-sf-pf-coherence]) and the stability of $\Dctf$ under all six
operations ([sk-thm-sf-ctf-stability]). Duality comes next: the dualizing
complex $\omega_X=Ra_X^!\Lambda$ gives biduality
([sk-prop-sf-biduality-general]), the tensor–Hom exchange
([sk-thm-sf-tensor-hom]) gives the Verdier exchange
$\mathbb D_Y Rf_!\cong Rf_*\mathbb D_X$ ([sk-thm-sf-verdier-exchange]),
and global duality follows ([sk-thm-sf-global-duality]). Last comes the
Künneth–Verdier isomorphism ([sk-thm-sf-kunneth-verdier]). All of this is
gathered into [sk-thm-sf-package].

**Key theorem.**

- Thm [sk-thm-sf-package] (six-operations package): the six operations exist
  on $\Dctf$ with the adjunctions $Lf^*\dashv Rf_*$ and $Rf_!\dashv Rf^!$.
  They satisfy base change, the projection formula, $Rf_!\cong Rf_*$ for
  proper $f$, the orientation $Rf^!\cong Lf^*(d)[2d]$ for smooth $f$, and
  Verdier duality. Used in §[sec-trace-formula], §[sec-poincare-duality],
  §[sec-purity-real-sheaves], §[sec-fourier-transform],
  §[sec-deligne-laumon-a1], §[sec-deligne-laumon-general], §[sec-zeta-weil].
- Thm [sk-thm-sf-ctf-stability] (stability of $\Dctf$): $Lf^*$, $\otimes^L$,
  $\RHom$, $Rf_*$, $Rf_!$, $Rf^!$ and $\mathbb D_X$ all preserve the
  constructible finite-Tor categories, with explicit Tor-amplitude bounds.
  Used in §[sec-trace-formula], §[sec-poincare-duality],
  §[sec-deligne-laumon-a1], §[sec-deligne-laumon-general].
- Prop [sk-prop-sf-biduality-general] (general Verdier biduality):
  $\mathbb D_Y=\RHom(-,Ra_Y^!\Lambda)$ is an anti-equivalence of
  $\Dctf(Y,\Lambda)$ with $\mathbb D_Y\mathbb D_Y\cong\mathrm{id}$. Used in
  §[sec-trace-formula], §[sec-poincare-duality], §[sec-purity-real-sheaves],
  §[sec-deligne-laumon-a1], §[sec-zeta-weil].
- Thm [sk-thm-sf-kunneth-verdier] (Künneth–Verdier):
  $M\boxtimes\mathbb D_YN\xrightarrow{\sim}\RHom(p_Y^*N,Rp_X^!M)$ for
  $M\in\Dctf(X,\Lambda)$, $N\in\Dctf(Y,\Lambda)$. Used in
  §[sec-trace-formula], §[sec-deligne-laumon-a1].

**References.**

- Stacks Project: `0F1N`, `0F1J`, `0F1P` (Künneth formula); `09AK`, `0990`,
  `0991` (pro-étale site, étale-origin complexes); `095M` (constructible
  sheaves as quotients of $j_{V!}\Lambda_V$); `0656`, `07VI` (perfect
  complexes over a regular ring); `03Q7`, `03PK` (strictly henselian stalks,
  Kummer classes); `0BFH`, `0BF9` (multiplication covers of an elliptic
  curve, used in a counterexample).
- SGA 4, XVII, §5.2 (projection formula and base change).
- P. Deligne, *SGA 4½*, Ch. 5 (Dualité) 1.1–1.2 and Ch. 7 (Théorèmes de
  finitude) 4.1–4.6 (biduality).
- SGA 5, III, 1.1 and 1.6.4 (Künneth formula); the Künneth–Verdier
  isomorphism follows the SGA 5 route.
- Varshavsky / SGA 5: normal-cone inputs to fixed-point localization, which
  the trace layer takes as explicit hypotheses.
