+++
id = "proposition-transitivity-trace-map"
kind = "proposition"
title = "Transitivity of the trace map"
order = 807
lean = ["AlgebraicGeometry.Etale.smoothPurityTrace_comp"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "theorem-proper-base-change-classical-pro", "definition-trace-map", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "lemma-symmetric-ample-sheaf", "proposition-pullback-multiplication-n", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "corollary-serre-duality-field-extension", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic"]
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
