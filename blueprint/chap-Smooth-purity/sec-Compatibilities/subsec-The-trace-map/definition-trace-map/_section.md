+++
id = "definition-trace-map"
kind = "definition"
title = "Trace map"
order = 805
lean = ["AlgebraicGeometry.Etale.smoothPurityTrace"]
uses = ["lemma-stability", "proposition-comparison-morphism-inverse-image", "definition-derived-base-change-map", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "theorem-proper-base-change-classical-pro", "proposition-composition-open-restriction-compactifications-f", "lemma-schematic-closure-uniqueness", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
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
