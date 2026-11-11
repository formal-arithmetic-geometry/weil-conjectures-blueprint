+++
id = "corollary-dualizing-complex-smooth-scheme"
kind = "corollary"
title = "The dualizing complex of a smooth scheme"
order = 818
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.smoothPurityIso", "AlgebraicGeometry.Etale.exists_counit_eq_smoothPurityTrace"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "definition-tate-twists", "definition-constructible-sheaves", "lemma-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "theorem-proper-base-change-classical-pro", "proposition-composition-open-restriction-compactifications-f", "theorem-f-shriek-ell-adic-coefficients", "proposition-six-operations-dctf", "definition-trace-map", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "definition-relative-picard-functor", "lemma-finite-direct-images", "lemma-finite-morphisms-cohomology"]
+++
Let $a:X\to\operatorname{Spec}k$ be smooth of pure dimension $d$, and let
$\Lambda$ be any admissible coefficient ring. There is a natural isomorphism
$a^!\Lambda_{\operatorname{Spec}k}\simeq\Lambda_X(d)[2d]$ in
$D^b_{\mathrm{ctf}}(X,\Lambda)$.
