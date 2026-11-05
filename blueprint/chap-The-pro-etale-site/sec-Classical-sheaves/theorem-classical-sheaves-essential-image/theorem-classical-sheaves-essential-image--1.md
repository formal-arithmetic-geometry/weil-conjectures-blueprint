+++
id = "theorem-classical-sheaves-essential-image--1"
kind = "theorem"
title = "Classical sheaves as the essential image (1)"
name_showing = false
order = 115001
aliases = ["bp-r032-1"]
lean = ["AlgebraicGeometry.ProEtale.full_comparisonUpperStar", "AlgebraicGeometry.ProEtale.faithful_comparisonUpperStar", "AlgebraicGeometry.Scheme.proEtaleComparisonUnitSets_isIso", "AlgebraicGeometry.Scheme.proEtaleClassicalSheavesImage", "AlgebraicGeometry.ProEtale.coefficientClassicalModule_origin"]
uses = ["definition-small-pro-etale-site", "definition-classical-pro-etale-sheaves", "proposition-comparison-morphism-inverse-image"]
+++
Let $X$ be a scheme and $A$ a Grothendieck abelian category. The comparison
functor

$$
\nu_X^*:\Sh(X_{\acute{e}t},A)\longrightarrow
\Sh(X_{\mathrm{pro}\acute{e}t},A)
$$

is fully faithful.

For sheaves of sets, the unit $F\to\nu_{X,*}\nu_X^*F$ is an isomorphism.
For a sheaf of sets $G$ on $X_{\mathrm{pro}\acute{e}t}$, the following
conditions are equivalent:

1. There is an étale sheaf $F$ and an isomorphism $G\simeq\nu_X^*F$.
2. $G$ is classical in the sense of Definition
   [definition-classical-pro-etale-sheaves].
3. The counit $\nu_X^*\nu_{X,*}G\to G$ is an isomorphism.

Let $\Lambda$ be a discrete commutative ring and $G$ a sheaf of
$\Lambda_X$-modules. If, for every affine étale presentation
$U=\varprojlim_iU_i$, the restriction maps induce an isomorphism

$$
\varinjlim_i G(U_i)\xrightarrow{\ \sim\ }G(U)
$$

of $\Lambda$-modules, then there is an étale $\Lambda$-module sheaf $F$
and an isomorphism $\nu_X^*F\simeq G$.
