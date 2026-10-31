+++
id = "sk-thm-properbasechange"
kind = "theorem"
title = "Proper base change on classical pro-étale complexes"
order = 220
lean = ["AlgebraicGeometry.Etale.isIso_baseChange_of_isProper_of_torsionHomology", "AlgebraicGeometry.Etale.hasTorsionBaseChange_of_isProper", "AlgebraicGeometry.Etale.hasTorsionBaseChange_of_projectiveLine_of_isProper", "AlgebraicGeometry.Etale.hasTorsionBaseChange_of_forall_prime", "AlgebraicGeometry.ProEtale.comparison_derivedBaseChangeMap", "AlgebraicGeometry.ProEtale.isIso_derivedBaseChangeMap_app_of_isProper"]
uses = ["sk-def-conv", "sk-def-exchange", "sk-def-pbc", "sk-def-pbc-conventions", "sk-thm-p1", "sk-thm-iff", "sk-thm-reduction", "sk-cor-pe-classical-derived", "sk-thm-pe-direct-image-comparison"]
tags = ["sketch"]
+++
Let $\Lambda$ be a commutative ring, let $f:X\to Y$ be a proper
morphism of schemes, and let $g:Y'\to Y$ be arbitrary. Set
$X'=X\times_YY'$, with projections $f':X'\to Y'$ and $g':X'\to X$.
Let $K\in D^+_{\mathrm{class}}(X_{\mathrm{pro}\acute{e}t},\Lambda)$ have torsion
cohomology sheaves (as abelian sheaves). Then the base change map,
defined as in Definition [sk-def-exchange] from the pro-étale
inverse images $g^*,g'^*$ and direct images $Rf_*,Rf'_*$,

$$
g^*Rf_*K\longrightarrow Rf'_*g'^*K
$$

is an isomorphism in $D^+_{\mathrm{class}}(Y'_{\mathrm{pro}\acute{e}t},\Lambda)$.
If $\Lambda$ is killed by a positive integer, for instance if $\Lambda$ is a
finite ring, every complex of $\Lambda_X$-modules has torsion cohomology
sheaves, so the theorem applies to every
$K\in D^+_{\mathrm{class}}(X_{\mathrm{pro}\acute{e}t},\Lambda)$.
