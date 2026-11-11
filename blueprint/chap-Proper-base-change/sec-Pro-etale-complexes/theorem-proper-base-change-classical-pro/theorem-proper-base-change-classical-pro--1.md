+++
id = "theorem-proper-base-change-classical-pro--1"
kind = "theorem"
title = "Pro-étale proper base change (1)"
name_showing = false
order = 402001
aliases = ["bp-r122-1"]
lean = ["AlgebraicGeometry.Etale.isIso_baseChange_of_isProper_of_torsionHomology"]
uses = ["definition-derived-base-change-map", "definition-torsion-sheaves--1"]
+++
Let $\Lambda$ be a commutative ring, let $f:X\to Y$ be a proper
morphism of schemes, and let $g:Y'\to Y$ be arbitrary. Set
$X'=X\times_YY'$, with projections $f':X'\to Y'$ and $g':X'\to X$.
Let $K\in D^+_{\mathrm{class}}(X_{\mathrm{pro}\acute{e}t},\Lambda)$ have torsion
cohomology sheaves (as abelian sheaves). Then the base change map
(4.5) of Definition [definition-pro-etale-base-change-map]

$$
g^*Rf_*K\longrightarrow Rf'_*g'^*K
$$

is an isomorphism in $D^+_{\mathrm{class}}(Y'_{\mathrm{pro}\acute{e}t},\Lambda)$.
