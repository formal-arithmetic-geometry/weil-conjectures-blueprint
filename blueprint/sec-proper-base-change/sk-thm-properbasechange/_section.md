+++
id = "sk-thm-properbasechange"
kind = "theorem"
title = "Proper base change on classical pro-étale complexes"
order = 2073
lean = ["AlgebraicGeometry.Etale.isIso_baseChange_of_isProper_of_torsionHomology", "AlgebraicGeometry.Etale.hasTorsionBaseChange_of_isProper", "AlgebraicGeometry.Etale.hasTorsionBaseChange_of_projectiveLine_of_isProper", "AlgebraicGeometry.Etale.hasTorsionBaseChange_of_forall_prime", "AlgebraicGeometry.ProEtale.comparison_derivedBaseChangeMap", "AlgebraicGeometry.ProEtale.isIso_derivedBaseChangeMap_app_of_isProper"]
uses = ["sk-def-conv", "sk-def-exchange", "sk-def-pbc", "sk-def-pbc-conventions", "sk-thm-p1", "sk-thm-iff", "sk-thm-reduction", "sk-cor-pe-classical-derived", "sk-thm-pe-direct-image-comparison"]
tags = ["sketch"]
+++
Let $\Lambda$ be a commutative ring, let $f:X\to Y$ be a proper morphism of
schemes, and let $g:Y'\to Y$ be arbitrary. Set $X'=X\times_YY'$, with
projections $f':X'\to Y'$ and $g':X'\to X$. If
$K\in D^+_{\mathrm{class}}(X_{\mathrm{proét}},\Lambda)$ has torsion underlying
abelian cohomology sheaves, the canonical exchange, defined as in
[sk-def-exchange] from the pro-étale inverse and direct images $g^*,g'^*$ and
$Rf_*,Rf'_*$ on $D^+(\,\cdot_{\mathrm{proét}},\Lambda)$,

$$
g^*Rf_*K\longrightarrow Rf'_*g'^*K
$$

is an isomorphism in $D^+_{\mathrm{class}}(Y'_{\mathrm{proét}},\Lambda)$.
If $\Lambda$ is killed by a positive integer, for instance if $\Lambda$ is a
finite ring, every complex of $\Lambda_X$-modules has torsion cohomology
sheaves, so the theorem applies to every
$K\in D^+_{\mathrm{class}}(X_{\mathrm{proét}},\Lambda)$.
