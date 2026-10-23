+++
id = "lem-weil-pbc-comparison-pullback"
kind = "lemma"
title = "Comparison inverse image commutes with scheme pullback"
lean = ["AlgebraicGeometry.ProEtale.comparisonUpperStarCompUpperStarIso", "AlgebraicGeometry.ProEtale.mapDerivedCategoryComparisonUpperStarCompUpperStarIso", "AlgebraicGeometry.ProEtale.leftDerivedUpperStarComparisonIso"]
order = 1044
uses = ["def-weil-pbc-derived-categories", "def-weil-pbc-direct-image", "def-weil-pbc-inverse-image", "def-weil-pbc-site-comparison-morphism", "prop-weil-pbc-inverse-image-exact", "lem-sfb-finite-upper-star-exact"]
+++
For a morphism $u:U\to V$ there is a natural isomorphism

$$
 \nu_U^*u_{\Et}^{-1}\xrightarrow{\sim}
 u_{\Proet}^{-1}\nu_V^*
$$

of functors from etale sheaves on $V$ to pro-etale sheaves on $U$, with values
in any Grothendieck abelian category, for instance $\Lambda$-modules. Since all
four functors are exact, it induces natural isomorphisms
$\nu_U^*u_{\Et}^{-1}\simeq u_{\Proet}^{-1}\nu_V^*$ of functors
$D(V_{\Et},\Lambda)\to D(U_{\Proet},\Lambda)$, and
$\nu_U^*u_{\Et}^{-1}\simeq Lu_{\Proet}^*\nu_V^*$ of functors
$\Dplus(V_{\Et},\Lambda)\to D(U_{\Proet},\Lambda)$.
