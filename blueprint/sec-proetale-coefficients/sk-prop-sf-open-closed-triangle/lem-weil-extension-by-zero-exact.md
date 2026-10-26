+++
id = "lem-weil-extension-by-zero-exact"
kind = "lemma"
title = "Exactness of extension by zero"
lean = ["AlgebraicGeometry.ProEtale.shortExact_map_openImmersionLowerShriek", "AlgebraicGeometry.ProEtale.preservesFiniteLimits_and_preservesFiniteColimits_openImmersionLowerShriek"]
order = 1083
uses = ["def-weil-extension-by-zero", "def-weil-finite-torsion-constructibility", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "lem-weil-extension-by-zero-adjunction"]
+++
Let $\mathcal A$ be a Grothendieck abelian category, for instance modules
over a finite commutative ring such as the finite-torsion coefficient rings
$A_{E,n}$ [def-weil-finite-torsion-constructibility]. Let
$j:U\hookrightarrow\overline X$ be an open immersion
[def-weil-scheme-morphism-properties] of schemes and use $\mathcal A$-valued
sheaves on the small pro-etale sites [def-weil-pbc-proetale-site]. Then the
extension-by-zero functor [def-weil-extension-by-zero] $j_!$ is exact: it
preserves finite limits and finite colimits, and so carries short exact
sequences to short exact sequences.
