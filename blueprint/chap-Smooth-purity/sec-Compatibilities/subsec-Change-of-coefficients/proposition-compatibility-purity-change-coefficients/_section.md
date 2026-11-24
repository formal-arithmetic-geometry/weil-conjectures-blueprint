+++
id = "proposition-compatibility-purity-change-coefficients"
kind = "proposition"
title = "Compatibility of purity with change of coefficients"
order = 812
lean = ["AlgebraicGeometry.Etale.map_smoothPurityIso_hom_comp", "AlgebraicGeometry.Etale.map_smoothPurityTrace"]
uses = ["definition-small-pro-etale-site", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "theorem-proper-base-change-classical-pro", "proposition-composition-open-restriction-compactifications-f", "proposition-exceptional-inverse-image-smooth-morphism", "proposition-smooth-purity-finite-coefficients", "definition-trace-map", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "definition-relative-picard-functor", "lemma-finite-direct-images", "lemma-finite-morphisms-cohomology"]
+++
Let $f:X\to Y$ be smooth of pure relative dimension $d$, let
$\Lambda\to\Lambda'$ be a coefficient map of
Proposition [proposition-six-operations-change-coefficients] and let
$K\in \href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(Y,\Lambda)}$. Then the change-of-coefficients isomorphism
$(\href{@theorem-existence-exceptional-inverse-image}{f^!K})_{\Lambda'}\to \href{@theorem-existence-exceptional-inverse-image}{f^!(K_{\Lambda'})}$ carries
$(\href{@theorem-smooth-purity-all-admissible-coefficients}{\gamma_{f,\Lambda}(K)})_{\Lambda'}$ to $\gamma_{f,\Lambda'}(K_{\Lambda'})$, the
sources being identified by the [change-of-coefficients isomorphism](@definition-change-of-coefficients-maps) for $f^*$.
The same holds for the [trace maps](@definition-trace-map): the [change-of-coefficients isomorphism](@definition-change-of-coefficients-maps) for
[$Rf_!$](@proposition-construction-independence-rf-shriek) carries $(\href{@definition-trace-map}{\operatorname{Tr}_{f,\Lambda}(K)})_{\Lambda'}$ to
$\operatorname{Tr}_{f,\Lambda'}(K_{\Lambda'})$.
