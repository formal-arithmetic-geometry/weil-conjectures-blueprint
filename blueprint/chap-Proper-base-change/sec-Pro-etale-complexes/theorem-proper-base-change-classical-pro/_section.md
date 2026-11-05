+++
id = "theorem-proper-base-change-classical-pro"
kind = "theorem"
title = "Pro-étale proper base change"
order = 402
lean = ["AlgebraicGeometry.ProEtale.isIso_derivedBaseChangeMap_app_of_isProper", "AlgebraicGeometry.Etale.isIso_baseChange_of_isProper_of_torsionHomology"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "proposition-comparison-morphism-inverse-image", "definition-derived-base-change-map", "definition-pro-etale-base-change-map", "definition-torsion-sheaves"]
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
