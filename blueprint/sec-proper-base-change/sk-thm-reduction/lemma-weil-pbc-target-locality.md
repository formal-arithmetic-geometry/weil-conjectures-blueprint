+++
id = "lemma-weil-pbc-target-locality"
kind = "lemma"
title = "Target locality"
lean = ["AlgebraicGeometry.Etale.hasTorsionBaseChange_of_affineOpens"]
order = 1965
uses = ["def-weil-pbc-cartesian-square", "def-weil-pbc-derived-exchange", "def-weil-pbc-scheme-conventions", "def-weil-pbc-torsion-etale-sheaf"]
+++
Let $\Lambda$ be a commutative ring and $f:X\to Y$ a morphism of schemes. Say
that $f$ has *torsion base change* over $\Lambda$ if for every cartesian square
[def-weil-pbc-cartesian-square] with $f$ on the right and an arbitrary $g:Y'\to Y$
at the bottom, the derived exchange morphism [def-weil-pbc-derived-exchange]
$g^{-1}Rf_*K\to Rf'_*g'^{-1}K$ is an isomorphism for every
$K\in\Dplus(X_{\Et},\Lambda)$ with torsion cohomology sheaves
[def-weil-pbc-torsion-etale-sheaf]. If for every affine open $U\subseteq Y$ the
restriction $f|_U:f^{-1}(U)\to U$ has torsion base change over $\Lambda$, then $f$
has torsion base change over $\Lambda$.
