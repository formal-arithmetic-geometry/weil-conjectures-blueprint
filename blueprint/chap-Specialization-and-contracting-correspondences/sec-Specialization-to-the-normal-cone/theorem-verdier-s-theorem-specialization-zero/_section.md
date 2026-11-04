+++
id = "theorem-verdier-s-theorem-specialization-zero"
kind = "theorem"
title = "Verdier's theorem on specialization to the zero section"
order = 1639
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isIso_zeroSectionMap", "AlgebraicGeometry.ProEtale.CondensedRing.isZero_specializationDefect", "AlgebraicGeometry.ProEtale.CondensedRing.isZero_upperStar_zeroSection_specialization"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "lemma-inverse-image-coefficient-sheaves", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-proper-direct-image-unbounded-complexes"]
+++
For every separated $k$-scheme $X$ of finite type, every closed subscheme
$Z\subset X$, and $K\in D^b_{\mathrm{ctf}}(X,A)$, the
map (E.1)

$$
\tau_{X,Z}(K):z^*\operatorname{Sp}_{X,Z}(K)\longrightarrow i^*K
$$

is an isomorphism.  In particular, $i^*K=0$ implies
$z^*\operatorname{Sp}_{X,Z}(K)=0$.
