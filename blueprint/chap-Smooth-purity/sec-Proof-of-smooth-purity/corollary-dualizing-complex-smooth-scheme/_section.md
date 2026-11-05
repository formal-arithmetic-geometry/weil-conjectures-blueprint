+++
id = "corollary-dualizing-complex-smooth-scheme"
kind = "corollary"
title = "The dualizing complex of a smooth scheme"
order = 818
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.smoothPurityIso", "AlgebraicGeometry.Etale.exists_counit_eq_smoothPurityTrace"]
uses = ["proposition-etale-implications", "lemma-stability", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-comparison-morphism-inverse-image", "proposition-pro-etale-site-separably-closed", "definition-tate-twists", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "definition-derived-base-change-map", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "theorem-proper-base-change-classical-pro", "proposition-composition-open-restriction-compactifications-f", "proposition-six-operations-change-coefficients", "definition-trace-map", "lemma-schematic-closure-uniqueness", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
Let $a:X\to\operatorname{Spec}k$ be smooth of pure dimension $d$, and let
$\Lambda$ be any admissible coefficient ring. There is a natural isomorphism
$a^!\Lambda_{\operatorname{Spec}k}\simeq\Lambda_X(d)[2d]$ in
$D^b_{\mathrm{ctf}}(X,\Lambda)$.
