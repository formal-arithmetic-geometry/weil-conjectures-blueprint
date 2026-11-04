+++
id = "lemma-finite-morphisms"
kind = "lemma"
title = "Finite morphisms"
order = 379
lean = ["AlgebraicGeometry.Etale.lowerStarSheafFiberIsoPi", "AlgebraicGeometry.Etale.preservesFiniteColimits_lowerStar_of_isFinite", "AlgebraicGeometry.Etale.isIso_baseChangeMap_of_isFinite", "AlgebraicGeometry.Etale.isBaseChangeIso_of_isFinite"]
uses = ["definition-underived-base-change-map", "definition-derived-base-change-map"]
+++
Let $u:V\to W$ be finite. For an abelian sheaf $F$ and a geometric point
$\bar w:\operatorname{Spec}(\Omega)\to W$, with $\Omega$ algebraically
closed, one has

$$
(u_*F)_{\bar w}
\simeq \prod_{\substack{\bar v:\operatorname{Spec}(\Omega)\to V\\
u\bar v=\bar w}}F_{\bar v}.
$$

The product is finite. The functor $u_*$ from abelian sheaves on
$V_{\acute{e}t}$ to abelian sheaves on $W_{\acute{e}t}$ is exact, and its formation
commutes with arbitrary base change. Consequently, for
every base change $W'\to W$ and every constant coefficient ring
$\Lambda$, the derived base change map
(4.3) is an isomorphism
for every $K\in D^+(V_{\acute{e}t},\Lambda)$.
