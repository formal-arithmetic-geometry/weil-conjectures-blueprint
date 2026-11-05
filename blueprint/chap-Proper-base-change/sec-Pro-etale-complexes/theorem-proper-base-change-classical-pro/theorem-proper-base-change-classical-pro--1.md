+++
id = "theorem-proper-base-change-classical-pro--1"
kind = "theorem"
title = "Étale proper base change with torsion cohomology"
name_showing = false
order = 402001
aliases = ["bp-r122-1"]
lean = ["AlgebraicGeometry.Etale.isIso_baseChange_of_isProper_of_torsionHomology", "AlgebraicGeometry.Etale.isIso_baseChange_of_isProper_of_isAddTorsion_ring"]
uses = ["definition-derived-base-change-map", "definition-torsion-sheaves"]
+++
Let $\Lambda$ be a commutative ring, let $f:X\to Y$ be a proper
morphism of schemes, and let $g:Y'\to Y$ be arbitrary. Set
$X'=X\times_YY'$, with projections $f':X'\to Y'$ and $g':X'\to X$.
Let $K\in D^+(X_{\acute{e}t},\Lambda)$ have torsion
cohomology sheaves (as abelian sheaves). Then the base change map
(4.3) of Definition [definition-derived-base-change-map]

$$
g^*Rf_*K\longrightarrow Rf'_*g'^*K
$$

is an isomorphism in $D^+(Y'_{\acute{e}t},\Lambda)$.

If the additive group of $\Lambda$ is torsion, this holds for every
$K\in D^+(X_{\acute{e}t},\Lambda)$, so the base change map is an
isomorphism of functors. In particular, this applies when $\Lambda$ is
finite.
