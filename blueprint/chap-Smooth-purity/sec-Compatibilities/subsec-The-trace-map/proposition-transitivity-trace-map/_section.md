+++
id = "proposition-transitivity-trace-map"
kind = "proposition"
title = "Transitivity of the trace map"
order = 808
lean = ["AlgebraicGeometry.Etale.smoothPurityTrace_comp"]
uses = ["lemma-stability", "proposition-comparison-morphism-inverse-image", "definition-derived-base-change-map", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "theorem-proper-base-change-classical-pro", "proposition-composition-open-restriction-compactifications-f", "definition-trace-map", "lemma-schematic-closure-uniqueness", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
Let $X\xrightarrow{f}Y\xrightarrow{g}Z$ be smooth of pure relative
dimensions $d$ and $e$, and $K\in D^b_{\mathrm{ctf}}(Z,\Lambda)$ for any admissible
$\Lambda$. Then
$\operatorname{Tr}_{g\circ f}(K)$ is the composite

$$
\begin{gathered}
R(g\circ f)_!
\bigl((g\circ f)^{*}K(d+e)[2d+2e]\bigr)
\simeq Rg_!Rf_!
\bigl(f^{*}
(g^{*}K(e)[2e])(d)[2d]\bigr)\\
\xrightarrow{\ Rg_!
(\operatorname{Tr}_{f}(g^{*}K(e)[2e]))\ }
Rg_!\bigl(g^{*}K(e)[2e]\bigr)
\xrightarrow{\ \operatorname{Tr}_{g}(K)\ }K.
\end{gathered}
$$
