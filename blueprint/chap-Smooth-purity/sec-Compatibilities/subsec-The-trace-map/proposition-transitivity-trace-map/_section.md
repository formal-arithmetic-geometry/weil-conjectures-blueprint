+++
id = "proposition-transitivity-trace-map"
kind = "proposition"
title = "Transitivity of the trace map"
order = 808
lean = ["AlgebraicGeometry.Etale.smoothPurityTrace_comp"]
uses = ["definition-small-pro-etale-site", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "theorem-proper-base-change-classical-pro", "proposition-composition-open-restriction-compactifications-f", "definition-trace-map", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "definition-relative-picard-functor", "lemma-finite-direct-images", "lemma-finite-morphisms-cohomology"]
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
