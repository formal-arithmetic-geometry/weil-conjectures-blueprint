+++
id = "sk-lem-pbc-finite"
kind = "lemma"
title = "Finite morphisms"
order = 1415
lean = ["AlgebraicGeometry.Etale.lowerStarSheafFiberIsoPi", "AlgebraicGeometry.Etale.preservesFiniteColimits_lowerStar_of_isFinite", "AlgebraicGeometry.Etale.isIso_baseChangeMap_of_isFinite", "AlgebraicGeometry.Etale.isBaseChangeIso_of_isFinite"]
uses = ["sk-def-exchange", "sk-def-conv", "sec-abelian-varieties", "sec-picard-framework"]
tags = ["sketch"]
+++
Let $u:V\to W$ be finite. For an abelian sheaf $F$ and a geometric point
$\bar w:\operatorname{Spec}(\Omega)\to W$, with $\Omega$ algebraically
closed, one has

$$
(u_*F)_{\bar w}\simeq
\prod_{\substack{\bar v:\operatorname{Spec}(\Omega)\to V\\ u\bar v=\bar w}}F_{\bar v}.
$$

The product is finite. The functor $u_*$ on abelian sheaves is exact, and its
formation commutes with arbitrary base change. Consequently, for every base
change $W'\to W$ and every constant coefficient ring $\Lambda$, the derived
exchange [sk-def-exchange] is an isomorphism in $D^+(W'_{\Et},\Lambda)$ for
every $K\in D^+(V_{\Et},\Lambda)$.
