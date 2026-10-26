+++
id = "lem-cbc-proetale-extension-zero-comparison"
kind = "lemma"
title = "Comparison of extension by zero with the site morphism"
lean = ["AlgebraicGeometry.ProEtale.openImmersionLowerShriekComparisonUpperStarIso", "AlgebraicGeometry.ProEtale.plusEtaleOrigin_mapDerivedCategory_openImmersionLowerShriek"]
order = 1017
uses = ["def-weil-extension-by-zero", "def-weil-pbc-extension-by-zero", "def-weil-pbc-proetale-site", "def-weil-pbc-site-comparison-morphism", "lem-cbc-proetale-extension-zero"]
+++
Let $\nu_X:X_{\Proet}\to X_{\Et}$ be the comparison morphism of
[def-weil-pbc-site-comparison-morphism]. For an open immersion
$j:U\hookrightarrow X$ and a finite commutative ring $\Lambda$ the
canonical comparison

$$
\nu_X^*j^{\mathrm{et}}_!F\xrightarrow{\ \sim\ }j^{\mathrm{proet}}_!\nu_U^*F
$$

is an isomorphism for every sheaf $F$ of $\Lambda$-modules on
$U_{\Et}$, naturally in $F$; here the two $j_!$ are those of
[def-weil-pbc-extension-by-zero] and
[def-weil-extension-by-zero]. Since all four functors are exact, it
follows that $j^{\mathrm{proet}}_!$ carries a bounded-below complex
$\nu_U^*L$ of etale origin to the complex $\nu_X^*j^{\mathrm{et}}_!L$ of
etale origin.
