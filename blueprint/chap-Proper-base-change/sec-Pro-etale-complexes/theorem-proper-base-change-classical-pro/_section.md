+++
id = "theorem-proper-base-change-classical-pro"
kind = "theorem"
title = "Pro-étale proper base change"
order = 402
lean = ["AlgebraicGeometry.Etale.isIso_baseChange_of_isProper_of_torsionHomology"]
uses = ["definition-derived-base-change-map", "definition-torsion-sheaves"]
+++
Let $\Lambda$ be a commutative ring, let $f:X\to Y$ be a proper
morphism of schemes, and let $g:Y'\to Y$ be arbitrary. Set
$X'=X\times_YY'$, with projections $f':X'\to Y'$ and $g':X'\to X$.
Let $K\in D^+_{\mathrm{class}}(\href{@definition-small-pro-etale-site}{X_{\mathrm{pro}\acute{e}t}},\Lambda)$ have [torsion](@definition-torsion-sheaves)
cohomology sheaves (as abelian sheaves). Then the base change map
(4.5) of Definition [definition-pro-etale-base-change-map]

$$
g^*Rf_*K\longrightarrow Rf'_*g'^*K
$$

is an isomorphism in $D^+_{\mathrm{class}}(\href{@definition-small-pro-etale-site}{Y'_{\mathrm{pro}\acute{e}t}},\Lambda)$.
