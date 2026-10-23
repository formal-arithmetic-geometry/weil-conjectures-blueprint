+++
id = "lemma-weil-pbc-prime-proper-base-change"
kind = "lemma"
title = "Proper base change with torsion coefficient rings"
order = 1983
lean = ["AlgebraicGeometry.Etale.isIso_baseChange_of_isProper_of_isAddTorsion_ring", "AlgebraicGeometry.Etale.hasTorsionBaseChange_of_projectiveLine_of_isProper_of_isAddTorsion", "AlgebraicGeometry.Etale.hasTorsionBaseChange_projectiveLine"]
uses = ["def-weil-pbc-cartesian-square", "def-weil-pbc-derived-exchange", "def-weil-pbc-property", "def-weil-pbc-scheme-conventions", "prop-weil-pbc-projective-line", "prop-weil-pbc-reduction-to-projective-line"]
+++
Let $\Lambda$ be a commutative ring which is torsion as an additive group
(for instance $\Lambda=\mathbf F_r$ for a prime $r$). For every proper
$f:X\to Y$ (no finite-presentation hypothesis) and every cartesian square
[def-weil-pbc-cartesian-square] with base change $g:Y'\to Y$, the derived
exchange morphism [def-weil-pbc-derived-exchange]

$$
 \Ex_\square:g^{-1}Rf_*\xrightarrow{\sim}Rf'_*g'^{-1}
$$

is an isomorphism of functors $\Dplus(X_{\Et},\Lambda)\to
\Dplus(Y'_{\Et},\Lambda)$. In particular, for every prime $r$ and every sheaf
$F$ of $\mathbf F_r$-modules on $X_{\Et}$, the map
$g^{-1}Rf_*F\to Rf'_*g'^{-1}F$ is an isomorphism.
