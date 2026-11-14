+++
id = "definition-trace-map"
kind = "definition"
title = "Trace map"
order = 805
lean = ["AlgebraicGeometry.Etale.smoothPurityTrace"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "definition-tate-twists", "lemma-inverse-image-coefficient-sheaves", "definition-constructible-sheaves", "lemma-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "theorem-proper-base-change-classical-pro", "lemma-inverse-image-tensor-product", "proposition-composition-open-restriction-compactifications-f", "theorem-f-shriek-ell-adic-coefficients", "proposition-six-operations-dctf", "theorem-smooth-purity-all-admissible-coefficients", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "definition-relative-picard-functor", "lemma-finite-direct-images", "lemma-finite-morphisms-cohomology"]
+++
For $K\in D^b_{\mathrm{ctf}}(Y,\Lambda)$, the *trace map* is the composite

$$
\operatorname{Tr}_{f}(K):\quad
Rf_!\bigl(f^{*}K(d)[2d]\bigr)
\xrightarrow{\ Rf_!\gamma_{f}(K)\ }
Rf_!f^!K
\xrightarrow{\ \varepsilon_{f}(K)\ }K.
\tag{9.25}
$$
