+++
id = "def-weil-open-closed-recollement"
kind = "definition"
title = "Open--closed recollement"
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.derivedOpenImmersionLowerShriekUpperStarAdjunction", "AlgebraicGeometry.ProEtale.CondensedRing.derivedUpperStarLowerStarAdjunction"]
order = 1205
uses = ["def-weil-derived-direct-image", "def-weil-derived-pullback-tensor-hom", "def-weil-extension-by-zero", "def-weil-finite-torsion-constructibility", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "det-def-sfb-pulled-back-coefficients", "det-def-sfb-bounded-constructible"]
+++
Fix a prime $\ell$ and an admissible coefficient ring
$\Lambda\in\{A_{E,n},\mathcal O_E,E,\Qlb\}$, regarded as a condensed ring, with coefficient
sheaves $\Lambda_X=p_X^*\Lambda$ ([det-def-sfb-pulled-back-coefficients]). Let $Z,U,X$ be schemes on which $\ell$ is
invertible. Let $i:Z\hookrightarrow X$ be a closed immersion
[def-weil-scheme-morphism-properties] and let $j:U\hookrightarrow X$ be its
complementary open immersion. Write $i^*,j^*$ for the derived pullbacks
[def-weil-derived-pullback-tensor-hom], and use the exact
extension-by-zero functor [def-weil-extension-by-zero] $j_!$ and the derived
direct image [def-weil-derived-direct-image] $Ri_*$ on the small pro-etale
sites [def-weil-pbc-proetale-site]. For $K\in D(X_{\mathrm{proét}},\Lambda)$, in particular
for $K\in D^b_c(X,\Lambda)$ ([det-def-sfb-bounded-constructible]; for $\Lambda=A_{E,n}$ this is
the finite-torsion constructibility condition [def-weil-finite-torsion-constructibility]),
the canonical open--closed pair of maps is

$$
 j_!j^*K\longrightarrow K\longrightarrow Ri_*i^*K,
$$

given by the open counit and the closed unit. An *open--closed recollement
triangle* means a distinguished triangle extending this specified pair.
